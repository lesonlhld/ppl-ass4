'''
 *   @author Nguyen Hua Phung
 *   @version 1.0
 *   23/10/2015
 *   This file provides a simple version of code generator
 *
'''
from Visitor import BaseVisitor
from Emitter import Emitter
from Frame import Frame
from abc import ABC, abstractmethod
from AST import *

class MethodEnv():
    def __init__(self, frame, sym, isGlobal=False):
        # frame: Frame
        # sym: List[Symbol]

        self.frame = frame
        self.sym = sym
        self.isGlobal = isGlobal
class Symbol:
    def __init__(self,name,mtype,value = None):
        self.name = name
        self.mtype = mtype
        self.value = value
    def __str__(self):
        return "Symbol(" + (self.name.name if type(self.name) == Id else self.name) + ',' + str(self.mtype) + ',' + (str(self.value) if self.value != None else "") + ')'
class CName:
    def __init__(self,n):
        self.value = n
class Index:
    def __init__(self,n):
        self.value = n
class Type(ABC): pass
class IntType(Type): pass
class FloatType(Type): pass
class VoidType(Type): pass
class ClassType(Type):
    def __init__(self,n):
        self.cname = n
class StringType(Type):pass
class BoolType(Type): pass
class MType(Type):
    def __init__(self,i,o):
        self.partype = i #List[Type]
        self.rettype = o #Type	
class ArrayType(Type):
    def __init__(self,et,*s):
        self.eleType = et #Type
        self.dimen = s   #List[int]  

class Access():
    def __init__(self, frame, sym, isLeft, isFirst):
        # frame: Frame
        # sym: List[Symbol]
        # isLeft: Boolean
        # isFirst: Boolean

        self.frame = frame
        self.sym = sym
        self.isLeft = isLeft
        self.isFirst = isFirst

class CodeGenerator():
    def __init__(self):
        self.libName = "io"

    def init(self):
        return [
Symbol("int_of_float",MType([FloatType()],IntType()), CName(self.libName)),
Symbol("float_to_int",MType([IntType()],FloatType()), CName(self.libName)),
Symbol("int_of_string",MType([StringType()],IntType()), CName(self.libName)),
Symbol("string_of_int",MType([IntType()],StringType()), CName(self.libName)),
Symbol("float_of_string",MType([StringType()],FloatType()), CName(self.libName)),
Symbol("string_of_float",MType([FloatType()],StringType()), CName(self.libName)),
Symbol("bool_of_string",MType([StringType()],BoolType()), CName(self.libName)),
Symbol("string_of_bool",MType([BoolType()],StringType()), CName(self.libName)),
Symbol("read",MType([],StringType()), CName(self.libName)),
Symbol("printLn",MType([],VoidType()), CName(self.libName)),
Symbol("print",MType([StringType()],VoidType()), CName(self.libName)),
Symbol("printStrLn",MType([StringType()],VoidType()), CName(self.libName))]

    def gen(self, ast, dir_):
        #ast: AST
        #dir_: String

        gl = self.init()
        gc = CodeGenVisitor(ast, gl, dir_)
        gc.visit(ast, None)


class CodeGenVisitor(BaseVisitor):
    def __init__(self, astTree, env, dir_):
        #astTree: AST
        #env: List[Symbol]
        #dir_: File

        self.astTree = astTree
        self.env = env
        self.className = "MCClass"
        self.path = dir_
        self.emit = Emitter(self.path + "/" + self.className + ".j")

    def getType(self, var):
        if IntLiteral == type(var):
            return IntType()        
        elif FloatLiteral == type(var):
            return FloatType()        
        elif BooleanLiteral == type(var):
            return BoolType()        
        elif StringLiteral == type(var):
            return StringType()
        else:
            return ArrayType()

    def visitProgram(self, ast, c):
        #ast: Program
        #c: Any

        self.emit.printout(self.emit.emitPROLOG(self.className, "java.lang.Object"))

        staticDecl = self.env

        for x in ast.decl:
            if type(x) == VarDecl:
                newSym = self.visit(x, MethodEnv(None, None, True))
                staticDecl = [newSym] + staticDecl
            else:
                paramType = [self.getType(y, c) for y in x.param]
                staticDecl = [Symbol(x.name.name, MType(paramType, IntType()), CName(self.className))] + staticDecl

        e = MethodEnv(None, staticDecl)

        [self.visit(x, e) for x in ast.decl if type(x) is FuncDecl]
        #self.genMain(e)
        # generate default constructor
        self.genInit()
        # generate class init if necessary
        self.emit.emitEPILOG()
        return c

    def genInit(self):
        methodName,methodType = "<init>",MType([],VoidType())
        frame = Frame(methodName, methodType.rettype)
        self.emit.printout(self.emit.emitMETHOD(methodName,methodType,False,frame))
        frame.enterScope(True)
        varname,vartype,varindex = "this",ClassType(self.className),frame.getNewIndex()
        startLabel, endLabel = frame.getStartLabel(), frame.getEndLabel()
        self.emit.printout(self.emit.emitVAR(varindex, varname, vartype, startLabel, endLabel,frame ))
        self.emit.printout(self.emit.emitLABEL(startLabel,frame))
        self.emit.printout(self.emit.emitREADVAR(varname, vartype, varindex, frame))
        self.emit.printout(self.emit.emitINVOKESPECIAL(frame))
        self.emit.printout(self.emit.emitLABEL(endLabel, frame))
        self.emit.printout(self.emit.emitRETURN(methodType.rettype, frame))
        self.emit.printout(self.emit.emitENDMETHOD(frame))

    # The following code is just for initial, students should remove it and write your visitor from here
    def genMethod(self, funcDecl: FuncDecl, sym, frame: Frame):
        methodName = funcDecl.name.name
        paramType = [self.getType(x, sym) for x in funcDecl.param] + [ArrayType(StringType())] if methodName == "main" else []
        isMain = methodName == "main" and len(funcDecl.param) == 0 and type(frame.returnType) is VoidType
        methodType = MType(paramType, frame.returnType)
        self.emit.printout(self.emit.emitMETHOD(methodName, methodType, True, frame))

        frame.enterScope(True)

        varname, varindex = "args", frame.getNewIndex()
        startLabel, endLabel = frame.getStartLabel(), frame.getEndLabel()
        if isMain:
            self.emit.printout(self.emit.emitVAR(varindex, varname, methodType.partype[0], startLabel, endLabel, frame ))
        
        varList = MethodEnv(frame, sym)
        for x in funcDecl.param:
            varList = self.visit(x, varList)
        for x in funcDecl.body[0]:
            varList = self.visit(x, varList)

        self.emit.printout(self.emit.emitLABEL(startLabel,frame))

        list(map(lambda x: self.visit(x, varList), funcDecl.body[1]))

        self.emit.printout(self.emit.emitLABEL(endLabel, frame))
        self.emit.printout(self.emit.emitRETURN(methodType.rettype, frame))
        self.emit.printout(self.emit.emitENDMETHOD(frame))
        frame.exitScope()

    def visitVarDecl(self, var, o):
        varName = var.variable.name
        frame = o.frame
        isGlobal = o.isGlobal
        if len(var.varDimen) > 0:
            init = self.visit(var.varInit, o)
            val, varType = ArrayType(var.varDimen, init.eletype)
        else:
            val, varType = self.visit(var.varInit, o)
        
        # if isGlobal or frame == None:
        if isGlobal:
            self.emit.printout(self.emit.emitATTRIBUTE(varName, varType, False, ""))
            return Symbol(varName, varType)
        else:
            value = var.varInit.value if var.varInit else None
            idx = frame.getNewIndex()
            self.emit.printout(self.emit.emitVAR(idx, varName, varType, frame.getStartLabel(), frame.getEndLabel(), frame))
            o.sym = [Symbol(varName, varType, Index(idx))] + o.sym
            rightCode, rightType = self.visit(var.varInit, Access(frame, o.sym, False, True))
            leftCode, leftType = self.visit(var.variable, Access(frame, o.sym, True, True))
            self.emit.printout(rightCode + leftCode)
            return MethodEnv(frame, o.sym)

    def visitFuncDecl(self, func, o):
        name = func.name.name
        frame = Frame(name, VoidType())
        self.genMethod(func, o.sym, frame)

    def visitBinaryOp(self, ast, o):
        left, leftType = self.visit(ast.left,o)
        right, rightType = self.visit(ast.right,o)

        if ast.op in ['==', '!=', '<', '>', '<=', '>=', '=/=', '<.', '>.', '<=.', '>=.', '&&', '||']:
            mType = BoolType()
        elif FloatType in [type(leftType), type(rightType)] or ast.op == '\\':
            mType = FloatType()
        else:
            mType = IntType()

        if type(leftType) == IntType and type(mType) == FloatType:
            left = left + self.emit.emitI2F(o.frame)
        if type(rightType) == IntType and type(mType) == FloatType:
            right = right + self.emit.emitI2F(o.frame)

        if ast.op in ['+', '-', '+.', '-.']:
            w = left + right + self.emit.emitADDOP(ast.op[0], mType, o.frame)
        elif ast.op in ['*', '\\', '*.', '\\.']:
            w = left + right + self.emit.emitMULOP(ast.op[0], mType, o.frame)
        elif ast.op in ['%']:
            w = left + right + self.emit.emitMOD(o.frame)
        elif ast.op in ['&&']:
            w = left + right + self.emit.emitANDOP(o.frame)
        elif ast.op in ['||']:
            w = left + right + self.emit.emitOROP(o.frame)
        elif ast.op in ['==', '!=', '<', '>', '<=', '>=']:
            w = left + right + self.emit.emitREOP(ast.op, mType, o.frame)
        elif ast.op in ['=/=', '<.', '>.', '<=.', '>=.']:
            if ast.op == '=/=':
                ast.op = '!=.'
            w = left + right + self.emit.emitREOP(ast.op[:-1], mType, o.frame)
        return w, mType

    def visitUnaryOp(self, ast: UnaryOp, o):
        body, bodyType = self.visit(ast.body, o)

        if ast.op == '-':
            return body + self.emit.emitNEGOP(IntType(), o.frame), IntType()
        elif ast.op == '-.':
            if type(bodyType) == IntType:
                body = body + self.emit.emitI2F(o.frame)
            return body + self.emit.emitNEGOP(FloatType(), o.frame), FloatType()
        elif ast.op == '!':
            return body + self.emit.emitNOT(BoolType(), o.frame), BoolType()

    def visitCallStmt(self, ast, o):
        self.handleCall(ast, o)

    def visitCallExpr(self, ast, o):
        return self.handleCall(ast, o)

    def handleCall(self, ast, o):
        frame, symbols = o.frame, o.sym

        sym = next(filter(lambda x: x.name == ast.method.name,symbols))

        paramTypes = sym.mtype.partype
        returnType = sym.mtype.rettype

        paramsCode = ""
        idx = 0
        for x in ast.param:
            pCode, pType = self.visit(x, Access(frame, symbols, False, True))
            if type(paramTypes[idx]) is FloatType and type(pType) is IntType:
                pCode = pCode + self.emit.emitI2F(frame)
            paramsCode = paramsCode + pCode
            idx = idx + 1
        
        code = paramsCode + self.emit.emitINVOKESTATIC(sym.value.value+"/"+sym.name,sym.mtype,frame)

        if type(ast) == CallExpr:
            return code, returnType
        else:
            self.emit.printout(code)

    def visitId(self, ast, o: Access):
        sym = next(filter(lambda x: x.name == ast.name, o.sym))
        # recover status of stack in frame
        if o.isLeft: o.frame.push()
        elif not o.isLeft: o.frame.pop()

        if type(sym.value) == CName:
            a = self.emit.emitPUTSTATIC(self.className + "/" + sym.name, sym.mtype, o.frame) if o.isLeft else self.emit.emitGETSTATIC(self.className + "/" + sym.name, sym.mtype, o.frame)
        else:
            index = sym.value.value
            a = self.emit.emitWRITEVAR(sym.name, sym.mtype, index, o.frame) if o.isLeft else self.emit.emitREADVAR(sym.name, sym.mtype, index, o.frame)
        return a, sym.mtype

    def visitAssign(self,ast,o):
        right, rightType = self.visit(ast.rhs, Access(o.frame, o.sym, False, False))
        left, leftType = self.visit(ast.lhs, Access(o.frame, o.sym, True, False))
        self.emit.printout(right + left)

    def visitIf(self, ast, o):
        label = [o.frame.getNewLabel() for x in range(len(ast.ifthenStmt))]
        labelE = o.frame.getNewLabel()
        for x in range(len(ast.ifthenStmt)):
            exp, expType = self.visit(ast.ifthenStmt[x][0], Access(o.frame, o.sym, False, False))
            self.emit.printout(exp)
        
            self.emit.printout(self.emit.emitIFFALSE(label[x], o.frame))
        
            varList = MethodEnv(o.frame, o.sym)
            for x in ast.ifthenStmt[x][1]:
                varList = self.visit(x, varList)

            list(map(lambda x: self.visit(x, varList), ast.ifthenStmt[x][2]))
            self.emit.printout(self.emit.emitGOTO(labelE, o.frame))
        
            self.emit.printout(self.emit.emitLABEL(label[x], o.frame))

        if len(ast.elseStmt[1]) > 0:
            varList = MethodEnv(o.frame, o.sym)
            for x in ast.elseStmt[0]:
                varList = self.visit(x, varList)

            list(map(lambda x: self.visit(x, varList), ast.elseStmt[1]))
        
        self.emit.printout(self.emit.emitLABEL(labelE, o.frame))

    def visitWhile(self, ast, o):
        expCode, expType = self.visit(ast.exp, Access(o.frame, o.sym, False, False))
        
        labelS = o.frame.getNewLabel() # label start
        labelE = o.frame.getNewLabel() # label end
        o.frame.enterLoop()
        self.emit.printout(self.emit.emitLABEL(labelS, o.frame))
        self.emit.printout(expCode)
        self.emit.printout(self.emit.emitIFFALSE(labelE, o.frame))
    
        varList = MethodEnv(o.frame, o.sym)
        for x in ast.sl[0]:
            varList = self.visit(x, varList)

        hasReturnStmt = True in [self.visit(x, varList) for x in ast.sl[1]]
        
        self.emit.printout(self.emit.emitLABEL(o.frame.getContinueLabel(), o.frame))
        if not hasReturnStmt:
            self.emit.printout(self.emit.emitGOTO(labelS, o.frame)) # loop
        self.emit.printout(self.emit.emitLABEL(labelE, o.frame))
        self.emit.printout(self.emit.emitLABEL(o.frame.getBreakLabel(), o.frame))
        o.frame.exitLoop()

    def visitDowhile(self, ast, o):        
        labelS = o.frame.getNewLabel() # label start
        labelE = o.frame.getNewLabel() # label end
        o.frame.enterLoop()
        self.emit.printout(self.emit.emitLABEL(labelS, o.frame))
            
        varList = MethodEnv(o.frame, o.sym)
        for x in ast.sl[0]:
            varList = self.visit(x, varList)

        hasReturnStmt = True in [self.visit(x, varList) for x in ast.sl[1]]
        
        expCode, expType = self.visit(ast.exp, Access(o.frame, o.sym, False, False))
        self.emit.printout(expCode)
        self.emit.printout(self.emit.emitIFFALSE(labelE, o.frame))

        self.emit.printout(self.emit.emitLABEL(o.frame.getContinueLabel(), o.frame))
        if not hasReturnStmt:
            self.emit.printout(self.emit.emitGOTO(labelS, o.frame)) # loop
        self.emit.printout(self.emit.emitLABEL(labelE, o.frame))
        self.emit.printout(self.emit.emitLABEL(o.frame.getBreakLabel(), o.frame))
        o.frame.exitLoop()

    def visitFor(self, ast, o):
        lhsWCode, _ = self.visit(ast.idx1, Access(o.frame, o.sym, True, True)) # Write code
        lhsRCode, _ = self.visit(ast.idx1, Access(o.frame, o.sym, False, False)) # Read code
        exp1Code, _ = self.visit(ast.expr1, Access(o.frame, o.sym, False, True))
        exp2Code, _ = self.visit(ast.expr2, Access(o.frame, o.sym, False, True))
        exp3Code, exp3Type = self.visit(ast.expr3, Access(o.frame, o.sym, False, True))

        labelS = o.frame.getNewLabel() # label start
        labelE = o.frame.getNewLabel() # label end

        # Init value
        self.emit.printout(exp1Code)
        self.emit.printout(lhsWCode)
        o.frame.enterLoop()
        # Loop
        self.emit.printout(self.emit.emitLABEL(labelS, o.frame))
        # 1. Condition
        self.emit.printout(exp2Code)
        self.emit.printout(self.emit.emitIFFALSE(labelE, o.frame))
        # 2. Statements
        varList = MethodEnv(o.frame, o.sym)
        for x in ast.loop[0]:
            varList = self.visit(x, varList)

        hasReturnStmt = True in [self.visit(x, varList) for x in ast.loop[1]]
        self.emit.printout(self.emit.emitLABEL(varList.frame.getContinueLabel(), varList.frame))
        # 3. Update index
        self.emit.printout(lhsRCode)
        self.emit.printout(exp3Code)
        self.emit.printout(self.emit.emitADDOP('+', exp3Type, o.frame))
        self.emit.printout(lhsWCode)

        if not hasReturnStmt:
            self.emit.printout(self.emit.emitGOTO(labelS, o.frame)) # loop
        self.emit.printout(self.emit.emitLABEL(labelE, o.frame))
        self.emit.printout(self.emit.emitLABEL(o.frame.getBreakLabel(), o.frame))
        o.frame.exitLoop()

    def visitReturn(self, ast: Return, o):
        retType = o.frame.returnType
        if o.frame.name != "main":
            expCode, expType = self.visit(ast.expr, Access(o.frame, o.sym, False, True))
            if type(retType) is FloatType and type(expType) is IntType:
                expCode = expCode + self.emit.emitI2F(o.frame)
                expType = FloatType()
            self.emit.printout(expCode)
            retType = o.frame.returnType = expType
        self.emit.printout(self.emit.emitRETURN(retType, o.frame))
        return True

    def visitBreak(self, ast, o):
        self.emit.printout(self.emit.emitGOTO(o.frame.getBreakLabel(), o.frame))

    def visitContinue(self, ast, o):
        self.emit.printout(self.emit.emitGOTO(o.frame.getContinueLabel(), o.frame))

    def visitIntLiteral(self, ast: IntLiteral, o: Access):
        return self.emit.emitPUSHICONST(ast.value, o.frame), IntType()

    def visitFloatLiteral(self, ast: FloatLiteral, o: Access):
        return self.emit.emitPUSHFCONST(str(float(ast.value)), o.frame), FloatType()

    def visitBooleanLiteral(self, ast: BooleanLiteral, o: Access):
        return self.emit.emitPUSHICONST(str(ast.value).lower(), o.frame), BoolType()

    def visitStringLiteral(self, ast: StringLiteral, o: Access):
        return self.emit.emitPUSHCONST("\"" + ast.value + "\"", StringType(), o.frame), StringType()

    def visitArrayLiteral(self, ast, param):
        valueType = [self.visit(x, param) for x in ast.value]

        dimen1 = len(valueType)
        dimen2 = 0
        dimen3 = 0
        for x in ast.value:
            varType = varTypleft = self.visit(x, param)
            if type(varTypleft) == ArrayType:
                dimen2 = len(x.value) if dimen2 < len(x.value) else dimen2
                for y in x.value:
                    varType = varTypright = self.visit(y, param)
                    if type(varTypright) == ArrayType:
                        dimen3 = len(y.value) if dimen3 < len(y.value) else dimen3
        dimen = [dimen1, dimen2, dimen3] if dimen3 > 0 else [dimen1, dimen2] if dimen2 > 0 else [dimen1]
        return ArrayType(dimen, varType)