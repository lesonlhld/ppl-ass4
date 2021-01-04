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
from functools import *
import copy

class MethodEnv():
    def __init__(self, frame, sym, isGlobal=False):
        # frame: Frame
        # sym: List[Symbol]

        self.frame = frame
        self.sym = sym
        self.isGlobal = isGlobal

class CName:
    def __init__(self,n):
        self.value = n
    def __str__(self):
        return "CName(" + str(self.value) + ")"
class Index:
    def __init__(self,n):
        self.value = n
class Type(ABC): 
    __metaclass__ = ABCMeta
    @staticmethod
    def getTypeFromLiteral(literal):
        if type(literal) == IntLiteral:
            return IntType()
        elif type(literal) == FloatLiteral:
            return FloatType()
        elif type(literal) == StringLiteral:
            return StringType()
        elif type(literal) == BooleanLiteral:
            return BoolType()
        elif type(literal) == ArrayLiteral:
            dimen1 = len(literal.value)
            dimen2 = 0
            dimen3 = 0
            if dimen1 == 0:
                return ArrayType(Unknown(), [0])
            for x in literal.value:
                varType = varType1 = Type.getTypeFromLiteral(x)
                if type(varType1) == ArrayType:
                    dimen2 = len(x.value) if dimen2 < len(x.value) else dimen2
                    for y in x.value:
                        varType = varType2 = Type.getTypeFromLiteral(y)
                        if type(varType2) == ArrayType:
                            varType = Type.getTypeFromLiteral(y.value)
                            dimen3 = len(y.value) if dimen3 < len(y.value) else dimen3
                            varType = ArrayType(varType)
                    varType = ArrayType(varType)
            dimen = [dimen1, dimen2, dimen3] if dimen3 > 0 else [dimen1, dimen2] if dimen2 > 0 else [dimen1]
            return ArrayType(varType, dimen)
        else:
            return Unknown()
            
class IntType(Type):
    def __str__(self):
        return "IntType"
class FloatType(Type):
    def __str__(self):
        return "FloatType"
class StringType(Type):
    def __str__(self):
        return "StringType"
class BoolType(Type):
    def __str__(self):
        return "BoolType"
class VoidType(Type):
    def __str__(self):
        return "VoidType"
class Unknown(Type):
    def __str__(self):
        return "Unknown"
class ClassType(Type):
    def __init__(self,n):
        self.cname = n
class MType(Type):
    def __init__(self,i,o):
        self.partype = i #List[Type]
        self.rettype = o #Type	
    def __str__(self):
        return "MType(" + printlist(self.partype) + ',' + str(self.rettype) + ')'
class ArrayType(Type):
    def __init__(self,et,*s):
        self.eleType = et #Type
        self.dimen = s   #List[int]  
    def __str__(self):
        return "ArrayType(" + str(self.eleType) +"," + printlist(self.dimen) + ")"
def printlist(lst,f=str,start="[",sepa=",",ending="]"):
	return start + sepa.join(f(i) for i in lst) + ending
class Kind(ABC):
    __metaclass__ = ABCMeta
    pass
class Variable(Kind):
    def __str__(self):
        return "Variable"
class Function(Kind):
    def __str__(self):
        return "Function"
class Parameter(Kind):
    def __str__(self):
        return "Parameter"
class Identifier(Kind):
    def __str__(self):
        return "Identifier"
     
class Symbol:
    def __init__(self,name,mtype,value = None, kind = Function(), isGlobal = False, visited = False, inHere = False):
        self.name = name
        self.mtype = mtype
        self.value = value
        self.kind = kind
        self.isGlobal = isGlobal
        self.visited = visited
        self.inHere = inHere

    def __str__(self):
        return "Symbol(" + (self.name.name if type(self.name) == Id else self.name) + ',' + str(self.mtype) + ',' + ("no value" if self.value == None else str(self.value)) + ("" if self.kind == None else ("," + str(self.kind))) + (",global" if self.isGlobal == True else ",local") + (",visited" if self.visited == True else ",not visited") + (",in here" if self.inHere == True else ",not here") + ')'
    def toGlobal(self):
        self.isGlobal = True
        return self

    def makeHere(self):
        self.inHere = True
        return self

    def makeVisit(self):
        self.visited = True
        return self

    def toParam(self):
        self.kind = Parameter()
        return self

    def toVar(self):
        self.kind = Variable()
        return self
    
    def updateMember(self, mtype = None, value = None, kind = None, isGlobal = None, visited = None, inHere = None):
        if mtype != None:
            self.mtype = mtype
        if value != None:
            self.value = value
        if kind != None:
            self.kind = kind
        if isGlobal != None:
            self.isGlobal = isGlobal
        if visited != None:
            self.visited = visited
        if inHere != None:
            self.inHere = inHere
        return self

    def update(self, newSymbol):
        self.updateMember(mtype = newSymbol.mtype, value = newSymbol.value, kind = newSymbol.kind, isGlobal = newSymbol.isGlobal, visited = newSymbol.visited, inHere= newSymbol.inHere)
        return self

    @staticmethod
    def fromVarDecl(var, envi):
        name = var.variable.name
        if len(var.varDimen) > 0:
            init = Type.getTypeFromLiteral(var.varInit)
            if type(init) == ArrayType:
                varType = ArrayType(init.eleType, var.varDimen)
            elif type(init) == Unknown:
                varType = ArrayType(init, var.varDimen)
        else:
            varType = Type.getTypeFromLiteral(var.varInit)
        kind = Variable()
        return Symbol(name, varType, None, kind)

    @staticmethod
    def fromFuncDecl(func, envi):
        name = func.name.name
        kind = Function()

        param = [Symbol.fromVarDecl(x, envi).toParam() for x in func.param]
        listParams = Checker.checkRedeclared([], param)
        paramType = [x.mtype for x in listParams]
        varType = MType(paramType, Unknown())

        return Symbol(name, varType, None, kind)

    @staticmethod
    def fromDecl(decl, envi):
        return Symbol.fromVarDecl(decl, envi).makeVisit() if type(decl) is VarDecl else Symbol.fromFuncDecl(decl, envi)

    @staticmethod
    def getSymbol(name, listSymbol):
        for x in listSymbol:
            if name == x.name:
                return x

    @staticmethod
    def getNowSymbol(listSymbol):
        for x in listSymbol:
            if x.inHere == True:
                return x
        
    @staticmethod
    def updateParamType(envi, ast):
        symbol = Symbol.getNowSymbol(envi)

        actualParam = [x for x in envi if type(x.kind) == Parameter]
        actualParamType = [x.mtype for x in actualParam]

        formaParamType = symbol.mtype.partype
        
        paramType = []
        if len(formaParamType) == len(actualParamType):
            for i in range(len(formaParamType)):
                if type(formaParamType[i]) == Unknown and type(actualParamType[i]) != Unknown and type(actualParamType[i]) != ArrayType:
                    paramType.append(actualParamType[i])
                elif type(formaParamType[i]) == Unknown and type(actualParamType[i]) == ArrayType and type(actualParamType[i].eleType) != Unknown:
                    paramType.append(actualParamType[i].eleType)
                elif type(formaParamType[i]) != Unknown and type(formaParamType[i]) != ArrayType and type(actualParamType[i]) == Unknown:
                    paramType.append(formaParamType[i])
                    actualParam[i].updateMember(mtype = formaParamType[i])
                elif type(formaParamType[i]) == ArrayType and type(formaParamType[i].eleType) != Unknown and type(actualParamType[i]) == Unknown:
                    paramType.append(formaParamType[i].eleType)
                    actualParam[i].updateMember(mtype = formaParamType[i].eleType)
                elif type(formaParamType[i]) == ArrayType and type(formaParamType[i].eleType) != Unknown and type(actualParamType[i]) == ArrayType and type(actualParamType[i].eleType) == Unknown:
                    paramType.append(formaParamType[i].eleType)
                    actualParam[i].updateMember(mtype = formaParamType[i])
                elif type(formaParamType[i]) == ArrayType and type(formaParamType[i].eleType) == Unknown and type(actualParamType[i]) == ArrayType and type(actualParamType[i].eleType) != Unknown:
                    paramType.append(actualParamType[i])
                else:
                    paramType.append(formaParamType[i])
                    actualParam[i].updateMember(mtype = formaParamType[i])
        else:
            paramType = formaParamType
        typeReturn = symbol.mtype.rettype

        varType = MType(paramType, typeReturn)
        symbol.updateMember(mtype = varType)

    @staticmethod
    def updateReturnType(listReturn, envi, ast):
        symbol = Symbol.getNowSymbol(envi)

        actualParamType = [x.mtype for x in envi if type(x.kind) == Parameter]
        formaParamType = symbol.mtype.partype
        paramType = formaParamType if len(formaParamType) != len(actualParamType) or Unknown not in [type(x) for x in formaParamType] else actualParamType

        if len(listReturn) > 0:
            if type(symbol.mtype.rettype) == Unknown or type(symbol.mtype.rettype) in [type(x) for x in listReturn]:
                typeReturn = listReturn[0]
        else:
            typeReturn = symbol.mtype.rettype

        varType = MType(paramType, typeReturn)

        symbol.updateMember(mtype = varType, visited = True)
        return typeReturn

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
        globalEnvi = StaticChecker(ast,gl).check()
        gc = CodeGenVisitor(ast, globalEnvi, dir_)
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
        self.initGlobalVardecl = []

    def visitProgram(self, ast, c):
        #ast: Program
        #c: Any

        self.emit.printout(self.emit.emitPROLOG(self.className, "java.lang.Object"))

        staticDecl = self.env

        for x in ast.decl:
            if type(x) == VarDecl:
                symbol = Symbol.getSymbol(x.variable.name, staticDecl)
                symbol.updateMember(value = CName(self.className))
                newSym = self.visit(x, MethodEnv(Frame(symbol.name, symbol.mtype), staticDecl, True))
            else:
                symbol = Symbol.getSymbol(x.name.name, staticDecl)
                symbol.updateMember(value = CName(self.className))

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
        symbol = Symbol.getSymbol(methodName, sym).makeHere()
        paramType = symbol.mtype.partype + ([ArrayType(StringType())] if methodName == "main" else [])
        isMain = methodName == "main" and len(funcDecl.param) == 0 and type(frame.returnType) is VoidType
        methodType = MType(paramType, frame.returnType if type(frame.returnType) != Unknown else VoidType())
        self.emit.printout(self.emit.emitMETHOD(methodName, methodType, True, frame))
        if isMain and self.initGlobalVardecl != []:
            for x in self.initGlobalVardecl:
                self.emit.printout(x)

        frame.enterScope(True)

        frame.push()
        startLabel, endLabel = frame.getStartLabel(), frame.getEndLabel()
        if isMain:
            varname, varindex = "args", frame.getNewIndex()
            self.emit.printout(self.emit.emitVAR(varindex, varname, methodType.partype[0], startLabel, endLabel, frame ))
        varList = MethodEnv(frame, sym)
        for x in range(len(funcDecl.param)):
            idx = frame.getNewIndex()
            name = funcDecl.param[x].variable.name
            self.emit.printout(self.emit.emitVAR(idx, name, paramType[x], frame.getStartLabel(), frame.getEndLabel(), frame))
            varList.sym = [Symbol(name, paramType[x], Index(idx))] + varList.sym
        for x in funcDecl.body[0]:
            varList = self.visit(x, varList)

        self.emit.printout(self.emit.emitLABEL(startLabel,frame))

        hasReturnStmt = True in list(map(lambda x: self.visit(x, varList), funcDecl.body[1]))
        self.emit.printout(self.emit.emitLABEL(endLabel, frame))
        if not hasReturnStmt:
            self.emit.printout(self.emit.emitRETURN(VoidType(), frame))
        self.emit.printout(self.emit.emitENDMETHOD(frame))
        frame.exitScope()
        symbol.updateMember(inHere = False)

    def visitVarDecl(self, var, o):
        varName = var.variable.name
        frame = o.frame
        isGlobal = o.isGlobal
        init, initType = self.visit(var.varInit, Access(frame, o.sym, False, True))
        
        # if isGlobal or frame == None:
        if isGlobal:
            self.emit.printout(self.emit.emitATTRIBUTE(varName, initType, False, ""))
            varCode, varType = self.visit(var.variable, Access(frame, o.sym, True, True))
            if type(initType) == ArrayType:
                if type(initType.eleType) == ArrayType:
                    for x in range(len(var.varDimen)):
                        self.initGlobalVardecl.append(self.visit(IntLiteral(var.varDimen[x]), Access(frame, o.sym, False, True))[0])
                    self.initGlobalVardecl.append(self.emit.emitWRITEVAR2(initType))
                    self.initGlobalVardecl.append(varCode)
                    varCode2, varType = self.visit(var.variable, Access(frame, o.sym, False, False))
                    for x in range(var.varDimen[0]):
                        for y in range(var.varDimen[1]):
                            frame.push()
                            self.initGlobalVardecl.append(varCode2)
                            self.initGlobalVardecl.append(self.visit(IntLiteral(x), Access(frame, o.sym, False, True))[0])
                            self.initGlobalVardecl.append(self.emit.emitALOAD(initType.eleType, frame))
                            self.initGlobalVardecl.append(self.visit(IntLiteral(y), Access(frame, o.sym, False, True))[0])
                            self.initGlobalVardecl.append(init[x][0][y][0])
                            self.initGlobalVardecl.append(self.emit.emitASTORE(init[x][0][y][1], frame))

                else:
                    self.initGlobalVardecl.append(self.visit(IntLiteral(len(init)), Access(frame, o.sym, False, True))[0])
                    self.initGlobalVardecl.append(self.emit.emitWRITEVAR2(init[0][1]))
                    self.initGlobalVardecl.append(varCode)
                    varCode2, varType = self.visit(var.variable, Access(frame, o.sym, False, False))
                    for x in range(len(init)):
                        frame.push()
                        self.initGlobalVardecl.append(varCode2)
                        self.initGlobalVardecl.append(self.visit(IntLiteral(x), Access(frame, o.sym, False, True))[0])
                        self.initGlobalVardecl.append(init[x][0])
                        self.initGlobalVardecl.append(self.emit.emitASTORE(init[x][1], frame))
            else:
                self.initGlobalVardecl.append(init + varCode)
                
            return Symbol(varName, initType)
        else:
            idx = frame.getNewIndex()
            self.emit.printout(self.emit.emitVAR(idx, varName, initType, frame.getStartLabel(), frame.getEndLabel(), frame))
            o.sym = [Symbol(varName, initType, Index(idx))] + o.sym
            if type(initType) == ArrayType:
                if type(initType.eleType) == ArrayType:
                    for x in range(len(var.varDimen)):
                        self.emit.printout(self.visit(IntLiteral(var.varDimen[x]), Access(frame, o.sym, False, True))[0])
                    self.emit.printout(self.emit.emitWRITEVAR2(initType))
                    self.emit.printout(self.emit.emitWRITEVAR(varName, initType, idx, frame))
                    for x in range(var.varDimen[0]):
                        for y in range(var.varDimen[1]):
                            frame.push()
                            self.emit.printout(self.emit.emitREADVAR(varName, initType, idx, frame))
                            self.emit.printout(self.visit(IntLiteral(x), Access(frame, o.sym, False, True))[0])
                            self.emit.printout(self.emit.emitALOAD(initType.eleType, frame))
                            self.emit.printout(self.visit(IntLiteral(y), Access(frame, o.sym, False, True))[0])
                            self.emit.printout(init[x][0][y][0])
                            self.emit.printout(self.emit.emitASTORE(initType.eleType.eleType, frame))

                else:
                    self.emit.printout(self.visit(IntLiteral(len(init)), Access(frame, o.sym, False, True))[0])
                    self.emit.printout(self.emit.emitWRITEVAR2(init[0][1]))
                    self.emit.printout(self.emit.emitWRITEVAR(varName, initType, idx, frame))
                    for x in range(len(init)):
                        frame.push()
                        self.emit.printout(self.emit.emitREADVAR(varName, initType, idx, frame))
                        self.emit.printout(self.visit(IntLiteral(x), Access(frame, o.sym, False, True))[0])
                        self.emit.printout(init[x][0])
                        self.emit.printout(self.emit.emitASTORE(init[x][1], frame))
            else:
                varCode2, varType = self.visit(var.variable, Access(frame, o.sym, True, False))
                self.emit.printout(init + varCode2)
            return MethodEnv(frame, o.sym)

    def visitFuncDecl(self, func, o):
        name = func.name.name
        symbol = Symbol.getSymbol(name, o.sym)
        returnType = symbol.mtype.rettype
        frame = Frame(name, returnType)
        self.genMethod(func, o.sym, frame)

    def visitBinaryOp(self, ast, o):
        left, leftType = self.visit(ast.left, Access(o.frame, o.sym, False, False))
        right, rightType = self.visit(ast.right, Access(o.frame, o.sym, False, False))
        if ast.op in ['==', '!=', '<', '>', '<=', '>=', '=/=', '<.', '>.', '<=.', '>=.', '&&', '||']:
            mType = BoolType()
        if FloatType in [type(leftType), type(rightType)]:
            mType = FloatType()
        else:
            mType = IntType()

        if ast.op in ['+', '-', '+.', '-.', '*', '\\', '*.', '\\.', '%']:
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
        elif ast.op in ['==', '!=', '<', '>', '<=', '>=', '=/=', '<.', '>.', '<=.', '>=.', '&&', '||']:
            label1 = o.frame.getNewLabel()
            label2 = o.frame.getNewLabel()
            if ast.op in ['&&']:
                w = left + self.emit.emitIFFALSE(label1, o.frame) + self.emit.emitPUSHICONST(1, o.frame) + right + self.emit.emitANDOP(o.frame) + self.emit.emitGOTO(label2, o.frame) + self.emit.emitLABEL(label1, o.frame) + self.emit.emitPUSHICONST(0, o.frame) + self.emit.emitLABEL(label2, o.frame)
            elif ast.op in ['||']:
                w = left + self.emit.emitIFTRUE(label1, o.frame) + self.emit.emitPUSHICONST(0, o.frame) + right + self.emit.emitOROP(o.frame) + self.emit.emitGOTO(label2, o.frame) + self.emit.emitLABEL(label1, o.frame) + self.emit.emitPUSHICONST(1, o.frame) + self.emit.emitLABEL(label2, o.frame)
            elif ast.op in ['==', '!=', '<', '>', '<=', '>=']:
                w = left + right + self.emit.emitREOP(ast.op, mType, o.frame)
            elif ast.op in ['=/=', '<.', '>.', '<=.', '>=.']:
                if ast.op == '=/=':
                    ast.op = '!=.'
                w = left + right + self.emit.emitREOP(ast.op, mType, o.frame)
        return w, mType

    def visitUnaryOp(self, ast: UnaryOp, o):
        body, bodyType = self.visit(ast.body, Access(o.frame, o.sym, False, False))

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

    def visitArrayCell(self, ast, o):
        arr, arrType = self.visit(ast.arr, o)
        listIdx = [self.visit(x, Access(o.frame, o.sym, False, True)) for x in ast.idx]
        if not o.isFirst and o.isLeft: o.frame.push()
        code = arr
        for x in range(len(listIdx) - 1):
            code += listIdx[x][0]
            if not o.isLeft:
                code += self.emit.emitALOAD(arrType, o.frame)
        code += listIdx[len(listIdx) - 1][0]
        if not o.isLeft:
            if type(arrType.eleType) == ArrayType:
                code += self.emit.emitALOAD(arrType.eleType.eleType, o.frame)
                return code, arrType.eleType.eleType
            else:
                code += self.emit.emitALOAD(arrType.eleType, o.frame)
                return code, arrType.eleType
        else:
            return code, arrType


    def visitId(self, ast, o: Access):
        sym = next(filter(lambda x: x.name == ast.name, o.sym))
        # recover status of stack in frame
        if not o.isFirst and o.isLeft: o.frame.push()
        #elif not o.isFirst and not o.isLeft: o.frame.pop()
        
        if type(sym.value) == CName:
            a = self.emit.emitPUTSTATIC(self.className + "/" + sym.name, sym.mtype, o.frame) if ((o.isFirst and o.isLeft) or (o.isLeft and type(sym.mtype) != ArrayType)) else self.emit.emitGETSTATIC(self.className + "/" + sym.name, sym.mtype, o.frame)
        else:
            index = sym.value.value
            a = self.emit.emitWRITEVAR(sym.name, sym.mtype, index, o.frame) if (o.isLeft and type(sym.mtype) != ArrayType) else self.emit.emitREADVAR(sym.name, sym.mtype, index, o.frame)
        return a, sym.mtype

    def visitAssign(self,ast,o):
        right, rightType = self.visit(ast.rhs, Access(o.frame, o.sym, False, True))
        left, leftType = self.visit(ast.lhs, Access(o.frame, o.sym, True, False))
        if type(ast.lhs) == ArrayCell:
            code = self.emit.emitASTORE(leftType.eleType, o.frame)
            self.emit.printout(left + right + code)
        else:
            self.emit.printout(right + left)

    def visitIf(self, ast, o):
        label = [o.frame.getNewLabel() for x in range(len(ast.ifthenStmt))]
        labelE = o.frame.getNewLabel()
        for x in range(len(ast.ifthenStmt)):
            exp, expType = self.visit(ast.ifthenStmt[x][0], Access(o.frame, o.sym, False, False))
            self.emit.printout(exp)
        
            self.emit.printout(self.emit.emitIFFALSE(label[x], o.frame))
        
            varList = MethodEnv(o.frame, o.sym)
            for y in ast.ifthenStmt[x][1]:
                varList = self.visit(y, varList)
                
            hasReturnStmt = True in [self.visit(y, varList) for y in ast.ifthenStmt[x][2]]
            
            if not hasReturnStmt:
                self.emit.printout(self.emit.emitGOTO(labelE, o.frame))
            self.emit.printout(self.emit.emitLABEL(label[x], o.frame))

        if len(ast.elseStmt[1]) > 0:
            varList = MethodEnv(o.frame, o.sym)
            for x in ast.elseStmt[0]:
                varList = self.visit(x, varList)

            list(map(lambda x: self.visit(x, varList), ast.elseStmt[1]))
        
        self.emit.printout(self.emit.emitLABEL(labelE, o.frame))

    def visitWhile(self, ast, o):
        expCode, expType = self.visit(ast.exp, Access(o.frame, o.sym, False, True))
        
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
        
        expCode, expType = self.visit(ast.exp, Access(o.frame, o.sym, False, True))
        self.emit.printout(expCode)
        self.emit.printout(self.emit.emitIFFALSE(labelE, o.frame))

        #self.emit.printout(self.emit.emitLABEL(o.frame.getContinueLabel(), o.frame))
        if not hasReturnStmt:
            self.emit.printout(self.emit.emitGOTO(labelS, o.frame)) # loop
        self.emit.printout(self.emit.emitLABEL(labelE, o.frame))
        self.emit.printout(self.emit.emitLABEL(o.frame.getBreakLabel(), o.frame))
        o.frame.exitLoop()

    def visitFor(self, ast, o):
        lhsWCode, _ = self.visit(ast.idx1, Access(o.frame, o.sym, True, True)) # Write code
        lhsRCode, _ = self.visit(ast.idx1, Access(o.frame, o.sym, False, False)) # Read code
        exp1Code, _ = self.visit(ast.expr1, Access(o.frame, o.sym, False, True))

        labelS = o.frame.getNewLabel() # label start
        labelE = o.frame.getNewLabel() # label end

        # Init value
        self.emit.printout(exp1Code)
        self.emit.printout(lhsWCode)
        o.frame.enterLoop()
        # Loop
        self.emit.printout(self.emit.emitLABEL(labelS, o.frame))
        # 1. Condition
        exp2Code, _ = self.visit(ast.expr2, Access(o.frame, o.sym, False, True))
        self.emit.printout(exp2Code)
        self.emit.printout(self.emit.emitIFFALSE(labelE, o.frame))
        # 2. Statements
        varList = MethodEnv(o.frame, o.sym)
        for x in ast.loop[0]:
            varList = self.visit(x, varList)

        hasReturnStmt = True in [self.visit(x, varList) for x in ast.loop[1]]
        self.emit.printout(self.emit.emitLABEL(varList.frame.getContinueLabel(), varList.frame))
        # 3. Update index
        exp3Code, exp3Type = self.visit(ast.expr3, Access(o.frame, o.sym, False, True))
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

    def visitArrayLiteral(self, ast, o):
        array = Type.getTypeFromLiteral(ast)
        valueType = [self.visit(x, o) for x in ast.value]
        return valueType, array

class Checker:
    @staticmethod
    def mergedEnvi(globalEnvi, localEnvi):
        curFunction = Symbol.getNowSymbol(globalEnvi)
        redeclareFunctionName = False
        newEnvi = copy.deepcopy(globalEnvi)
        envi = [x.name for x in newEnvi]
        for x in localEnvi:
            if x.name in envi:
                symbol = Symbol.getSymbol(x.name, newEnvi)
                symbol.update(x)
            else:
                envi.append(x.name)
                newEnvi.append(x)
            if x.name == curFunction.name and type(x.kind) != Function:
                redeclareFunctionName = True
        if redeclareFunctionName == True:
            newEnvi.append(curFunction)
        return newEnvi

    @staticmethod
    def updateEnvi(globalEnvi, localEnvi, exceptList = None):
        if exceptList == None:
            envi = [x for x in localEnvi if x.isGlobal == True]
            for x in envi:
                symbol = Symbol.getSymbol(x.name, globalEnvi)
                symbol.update(x)
        else:
            curFunction = Symbol.getNowSymbol(globalEnvi)
            envi = [x for x in localEnvi]
            noUpdateList = [x.name for x in exceptList]
            
            for x in localEnvi:
                if x.name not in noUpdateList:
                    if x.name == curFunction.name:
                        if type(x.kind) == Function:
                            symbol = curFunction.update(x)
                    else:
                        symbol = Symbol.getSymbol(x.name, globalEnvi).update(x)

    # Check Redeclared Variable/Function/Parameter and return merged two environment
    @staticmethod
    def checkRedeclared(currentEnvi, listNewSymbols):
        newEnvi = copy.deepcopy(currentEnvi)
        envi = [x.name for x in newEnvi]
        for x in listNewSymbols:
            envi.append(x.name)
            newEnvi.append(x)
        return newEnvi

    @staticmethod
    def checkUndeclared(currentEnvi, name, kind):
        checkRedeclareFunction = Symbol.getSymbol(currentEnvi[-1].name, currentEnvi)
        if type(checkRedeclareFunction.kind) != type(currentEnvi[-1].kind):
            newCurrentEnvi = copy.deepcopy(currentEnvi[:-1])
        else:
            newCurrentEnvi = currentEnvi
        envi = {x.name: Identifier() if type(x.kind) in [Variable, Parameter] else x.kind for x in newCurrentEnvi}
        
        return Symbol.getSymbol(name, newCurrentEnvi)
        
    @staticmethod
    def updateSideType(side, sideType, ast, envi):
        if type(ast) == ArrayCell:
            name = ast.arr.name
        elif type(ast) == CallExpr:
            name = ast.method.name
        elif type(ast) == Id:
            name = ast.name
        elif type(ast) == BinaryOp:
            name = ast.left.name if side == "left" else ast.right.name
        else:
            name = ast.lhs.name if side == "left" else ast.rhs.name

        symbol = Symbol.getSymbol(name, envi)
        
        if type(symbol.kind) == Function:
            if (type(symbol.mtype.rettype) == Unknown or type(symbol.mtype.rettype) == type(sideType)) and side == "right":
                varType = MType(symbol.mtype.partype, sideType)
                symbol.updateMember(mtype = varType)
        elif type(symbol.mtype) == ArrayType:
            if type(symbol.mtype.eleType) == Unknown or type(symbol.mtype.eleType) == type(sideType):
                varType = ArrayType(sideType, symbol.mtype.dimen)
                symbol.updateMember(mtype = varType)
        else:
            varType = sideType
            symbol.updateMember(mtype = varType)
        return sideType

    @staticmethod
    def checkTwoSideType(left, right, ast, envi, opType = None, targetType = None, final = None):
        if type(ast) == Assign:
            if type(left) == Unknown and type(right) != Unknown and type(right) != ArrayType:
                left = right
                typeReturn = Checker.updateSideType("left", right, ast.lhs, envi)
            elif type(left) != Unknown and type(left) != ArrayType and type(right) == Unknown:
                right = left
                typeReturn = Checker.updateSideType("right", left, ast.rhs, envi)
            else:
                typeReturn = left
        elif type(ast) in [CallExpr, CallStmt]:
            for i in range(len(right)):
                if type(left[i]) == Unknown and type(right[i]) != Unknown and type(right[i]) != ArrayType:
                    left[i] = right[i]
                elif type(left[i]) == Unknown and type(right[i]) == ArrayType and type(right[i].eleType) != Unknown:
                    left[i] = right[i].eleType
                elif type(left[i]) != Unknown and type(left[i]) != ArrayType and type(right[i]) == Unknown:
                    right[i] = left[i]
                    typeReturn = Checker.updateSideType("right", left[i], ast.param[i], envi)
                elif type(left[i]) == ArrayType and type(left[i].eleType) == Unknown and type(right[i]) == ArrayType and type(right[i].eleType) != Unknown:
                    left[i].eleType = right[i].eleType
                elif type(left[i]) == ArrayType and type(left[i].eleType) != Unknown and type(right[i]) == ArrayType and type(right[i].eleType) == Unknown:
                    right[i].eleType = left[i].eleType
            typeReturn = Checker.updateSideType("left", left, ast.method, envi)
            return left, right
        return typeReturn

    @staticmethod
    def checkOneSideType(body, ast, envi, opType, targetType):
        if type(body) == Unknown:
            body = Checker.updateSideType("right", opType, ast, envi)
        elif type(body) == ArrayType and type(body.eleType) == Unknown:
            body = Checker.updateSideType("right", opType, ast, envi)
        elif type(body) == ArrayType and type(body.eleType) != Unknown:
            body = body.eleType
        typeReturn = targetType

        Symbol.updateParamType(envi, ast)
        return typeReturn

    @staticmethod
    def checkMatchType(left, right, ast, envi):
        # Handle Array Type
        if type(left) == ArrayType and type(right) == ArrayType:
            lhs = left.eleType
            rhs = right.eleType
            typeReturn = Checker.checkTwoSideType(lhs, rhs, ast, envi)
        elif ArrayType in [type(left), type(right)]:
            lhs = left.eleType if type(left) == ArrayType else left
            rhs = right.eleType if type(right) == ArrayType else right
            typeReturn = Checker.checkTwoSideType(lhs, rhs, ast, envi)
        else:
            typeReturn = Checker.checkTwoSideType(left, right, ast, envi)
            
        return typeReturn
    
    @staticmethod
    def checkParamType(actualParameters, formaParameters, ast, envi, final):
        if len(formaParameters) < len(actualParameters):
            return False        
            
        formaParameters, actualParameters = Checker.checkTwoSideType(formaParameters, actualParameters, ast, envi, final = final)
        if len(formaParameters) > len(actualParameters) and final == True:
            return False        

        for a, b in zip(formaParameters, actualParameters):
            if VoidType in [type(a), type(b)]:
                return False
            if Unknown not in [type(a), type(b)] and type(a) != type(b) and type(a) != ArrayType and type(b) == ArrayType and type(b.eleType) != Unknown and type(a) != type(b.eleType):
                return False
            
        return True

    @staticmethod
    def checkCall(ast, envi, actualParameters, final = False):
        symbol = Checker.checkUndeclared(envi, ast.method.name, Function())

        formaParameters = symbol.mtype.partype
        
        checkParam = Checker.checkParamType(actualParameters, formaParameters, ast, envi, final)
        if type(ast) == CallStmt:
            if type(symbol.mtype.rettype) in [Unknown, VoidType]:
                typeReturn = VoidType()
        else:
            typeReturn = symbol.mtype.rettype
        varType = MType(formaParameters, typeReturn)
        symbol.updateMember(mtype = varType)
        
        return typeReturn

class StaticChecker(BaseVisitor):
    def checkUnOp(self, ast, param, partype, outType):
        bodyType = self.visit(ast.body, param)
        typeReturn = Checker.checkOneSideType(bodyType, ast.body, param, partype, outType)
        return typeReturn

    def checkLeftBinOp(self, ast, param, partype, outType):
        leftType = self.visit(ast.left, param)
        typeReturn = Checker.checkOneSideType(leftType, ast.left, param, partype, outType)

    def checkRightBinOp(self, ast, param, partype, outType):
        rightType = self.visit(ast.right, param)
        typeReturn = Checker.checkOneSideType(rightType, ast.right, param, partype, outType)

    def __init__(self,ast,envi):
        self.ast = ast
        # global_envi: built-in function names
        self.global_envi = envi
   
    def check(self):
        return self.visit(self.ast,self.global_envi)

    # globalEnvi: global variables, built-in function names and other function names
    def visitProgram(self, ast: Program, globalEnvi):
        for x in globalEnvi:
            x.toGlobal()
            x.makeVisit()

        # Visit all global variables, function names from input
        symbols = [Symbol.fromDecl(x, globalEnvi).toGlobal() for x in ast.decl]
        
        # Check Redeclared Variable/Function and update globalEnvi
        globalEnvi = Checker.checkRedeclared(globalEnvi, symbols)

        # Visit all function
        [self.visit(x, globalEnvi) for x in ast.decl if type(x) == FuncDecl]
        return globalEnvi

    # Visit declaration
    def visitVarDecl(self, ast, c):
        return Symbol.fromVarDecl(ast, c)

    def visitFuncDecl(self, ast: FuncDecl, globalEnvi):
        symbol = Symbol.getSymbol(ast.name.name, globalEnvi).makeHere()
        formaParameters = symbol.mtype.partype

        # Visit all local variables, parameter of function from input
        listParams = [self.visit(x, globalEnvi).toParam() for x in ast.param]
        
        # Check Redeclared Parameter and update localEnvi
        localEnvi = Checker.checkRedeclared([], listParams)
        for a, b in zip(localEnvi, formaParameters):
            a.updateMember(mtype = b)

        for x in ast.body[0]:
            t = self.visit(x, globalEnvi).toVar()
            localEnvi = Checker.checkRedeclared(localEnvi, [t])

        # Merge local with global environment
        localEnvi = Checker.mergedEnvi(globalEnvi, localEnvi)

        # Visit statements
        listReturn = []
        for y in ast.body[1]:
            z = self.visit(y, localEnvi)
            if type(y) == Return:
                listReturn.append(z)
        # Update global environment
        Checker.updateEnvi(globalEnvi, localEnvi)
        Symbol.updateReturnType(listReturn, globalEnvi, ast)

        if type(symbol.mtype.rettype) == Unknown:
            symbol.updateMember(mtype = MType(symbol.mtype.partype, VoidType()))
        symbol.updateMember(inHere = False)

    # Visit expression
    # Return Type of expression
    def visitBinaryOp(self, ast: BinaryOp, param):
        if ast.op in ['+', '-', '*', '\\', '%']:
            self.checkLeftBinOp(ast, param, IntType(), IntType())
            self.checkRightBinOp(ast, param, IntType(), IntType())

            typeReturn = IntType()
        elif ast.op in ['+.', '-.', '*.', '\\.']:
            self.checkLeftBinOp(ast, param, FloatType(), FloatType())
            self.checkRightBinOp(ast, param, FloatType(), FloatType())

            typeReturn = FloatType()
        elif ast.op in ['==', '!=', '<', '>', '<=', '>=']:
            self.checkLeftBinOp(ast, param, IntType(), BoolType())
            self.checkRightBinOp(ast, param, IntType(), BoolType())

            typeReturn = BoolType()
        elif ast.op in ['=/=', '<.', '>.', '<=.', '>=.']:
            self.checkLeftBinOp(ast, param, FloatType(), BoolType())
            self.checkRightBinOp(ast, param, FloatType(), BoolType())

            typeReturn = BoolType()
        elif ast.op in ['&&', '||']:
            self.checkLeftBinOp(ast, param, BoolType(), BoolType())
            self.checkRightBinOp(ast, param, BoolType(), BoolType())

            typeReturn = BoolType()
        return typeReturn
    
    def visitUnaryOp(self, ast: UnaryOp, param):
        if ast.op == '-':
            typeReturn = self.checkUnOp(ast, param, IntType(), IntType())
        elif ast.op == '-.':
            typeReturn = self.checkUnOp(ast, param, FloatType(), FloatType())
        elif ast.op == '!':
            typeReturn = self.checkUnOp(ast, param, BoolType(), BoolType())
        return typeReturn
    
    def visitId(self, ast: Id, envi):
        symbol = Checker.checkUndeclared(envi, ast.name, Identifier())
        return symbol.mtype
    
    # Function call, no semi
    def visitCallExpr(self, ast: CallExpr, globalEnvi):
        typeReturn = self.visitCall(ast, globalEnvi)
        
        return typeReturn

    def visitArrayCell(self, ast: ArrayCell, envi):
        arrType = self.visit(ast.arr, envi)
        idxType = []
        for i in ast.idx:
            y = self.visit(i, envi)
            if type(y) == Unknown:
                y = Checker.updateSideType("left", IntType(), i, envi)
            Symbol.updateParamType(envi, ast)
            idxType.append(y)

        Symbol.updateParamType(envi, ast)
        return self.visit(ast.arr, envi).eleType
    

    # Visit statement
    def visitAssign(self, ast: Assign, envi):
        lhsType = self.visit(ast.lhs, envi)
        rhsType = self.visit(ast.rhs, envi)
        if type(lhsType) == Unknown:
            lhsType = self.visit(ast.lhs, envi)
        
        typeReturn = Checker.checkMatchType(lhsType, rhsType, ast, envi)
        Symbol.updateParamType(envi, ast)
        return typeReturn

    def visitIf(self, ast: If, envi):
        listReturn = []
        for x in ast.ifthenStmt:
            conditionalExprIf = self.visit(x[0], envi)
            if type(conditionalExprIf) == Unknown:
                Checker.checkOneSideType(conditionalExprIf, x[0], envi, BoolType(), BoolType())
            varDeclIf = [self.visit(y, envi) for y in x[1]]
            localEnvi = Checker.checkRedeclared([], varDeclIf)
            localEnvi = Checker.mergedEnvi(envi, localEnvi)
            for y in x[2]:
                z = self.visit(y, localEnvi)
                if type(y) == Return:
                    listReturn.append(z)
            listReturn.append(Symbol.updateReturnType(listReturn, localEnvi, ast))
                
            Checker.updateEnvi(envi, localEnvi, varDeclIf)
            
        varDeclElse = [self.visit(y, envi) for y in ast.elseStmt[0]]
        localEnvi = Checker.checkRedeclared([], varDeclElse)
        localEnvi = Checker.mergedEnvi(envi, localEnvi)
        for y in ast.elseStmt[1]:
            z = self.visit(y, localEnvi)
            if type(y) == Return:
                listReturn.append(z)
        typeReturn = Symbol.updateReturnType(listReturn, localEnvi, ast)

        Checker.updateEnvi(envi, localEnvi, varDeclElse)
        
        Symbol.updateParamType(envi, ast)
        return typeReturn
    
    def visitFor(self, ast: For, envi):
        indexVar = self.visit(ast.idx1, envi)
        if type(indexVar) != IntType:
            if type(indexVar) == Unknown:
                Checker.checkOneSideType(indexVar, ast.idx1, envi, IntType(), IntType())
        expr1 = self.visit(ast.expr1, envi)
        if type(expr1) != IntType:
            if type(expr1) == Unknown:
                Checker.checkOneSideType(expr1, ast.expr1, envi, IntType(), IntType())
        expr2 = self.visit(ast.expr2, envi)
        if type(expr2) != BoolType:
            if type(expr2) == Unknown:
                Checker.checkOneSideType(indexVar, ast.expr2, envi, BoolType(), BoolType())
        expr3 = self.visit(ast.expr3, envi)
        if type(expr3) != IntType:
            if type(expr3) == Unknown:
                Checker.checkOneSideType(indexVar, ast.expr3, envi, IntType(), IntType())

        varDecl = [self.visit(y, envi) for y in ast.loop[0]]
        localEnvi = Checker.checkRedeclared([], varDecl)
        localEnvi = Checker.mergedEnvi(envi, localEnvi)
        
        listReturn = []
        for y in ast.loop[1]:
            z = self.visit(y, localEnvi)
            if type(y) == Return:
                listReturn.append(z)

        typeReturn = Symbol.updateReturnType(listReturn, localEnvi, ast)

        Checker.updateEnvi(envi, localEnvi, varDecl)
        
        Symbol.updateParamType(envi, ast)
        return typeReturn
    
    def visitContinue(self, ast, param):
        return None
    
    def visitBreak(self, ast, param):
        return None
    
    def visitReturn(self, ast: Return, envi):
        symbol = Symbol.getNowSymbol(envi)
        if ast.expr == None:
            typeReturn = VoidType()
        else:
            typeReturn = self.visit(ast.expr, envi)
        return typeReturn
    
    def visitDowhile(self, ast: Dowhile, envi):        
        varDecl = [self.visit(y, envi) for y in ast.sl[0]]
        localEnvi = Checker.checkRedeclared([], varDecl)
        localEnvi = Checker.mergedEnvi(envi, localEnvi)
        
        listReturn = []
        for y in ast.sl[1]:
            z = self.visit(y, localEnvi)
            if type(y) == Return:
                listReturn.append(z)

        Checker.updateEnvi(envi, localEnvi, varDecl)
    
        exp = self.visit(ast.exp, envi)
        if type(exp) == Unknown:
            Checker.checkOneSideType(exp, ast.exp, envi, BoolType(), BoolType())
        
        typeReturn = Symbol.updateReturnType(listReturn, envi, ast)
        Symbol.updateParamType(envi, ast)
        return typeReturn

    def visitWhile(self, ast: While, envi):
        exp = self.visit(ast.exp, envi)
        if type(exp) == Unknown:
            Checker.checkOneSideType(exp, ast.exp, envi, BoolType(), BoolType())
        
        varDecl = [self.visit(y, envi) for y in ast.sl[0]]
        localEnvi = Checker.checkRedeclared([], varDecl)
        localEnvi = Checker.mergedEnvi(envi, localEnvi)
        listReturn = []
        for y in ast.sl[1]:
            z = self.visit(y, localEnvi)
            if type(y) == Return:
                listReturn.append(z)

        typeReturn = Symbol.updateReturnType(listReturn, localEnvi, ast)
        Checker.updateEnvi(envi, localEnvi, varDecl)
        Symbol.updateParamType(envi, ast)
        return typeReturn

    def visitCall(self, ast, globalEnvi):
        symbol = Symbol.getSymbol(ast.method.name, globalEnvi)

        paramType = []
        for i in ast.param:
            y = self.visit(i, globalEnvi)
            paramType.append(y)
            Checker.checkCall(ast, globalEnvi, paramType)
            Symbol.updateParamType(globalEnvi, ast)

        typeReturn = Checker.checkCall(ast, globalEnvi, paramType, True)
        Symbol.updateParamType(globalEnvi, ast)
        return typeReturn
        
    # Call stmt return VoidType, have semi
    def visitCallStmt(self, ast: CallStmt, globalEnvi):
        typeReturn = self.visitCall(ast, globalEnvi)
        
        return typeReturn

    # Visit literal
    # Return type
    def visitIntLiteral(self, ast, param):
        return IntType()
    
    def visitFloatLiteral(self, ast, param):
        return FloatType()
    
    def visitBooleanLiteral(self, ast, param):
        return BoolType()
    
    def visitStringLiteral(self, ast, param):
        return StringType()
        
    def visitArrayLiteral(self, ast, param):
        valueType = [self.visit(x, param) for x in ast.value]

        dimen1 = len(valueType)
        dimen2 = 0
        dimen3 = 0
        for x in ast.value:
            varType = varType1 = self.visit(x, param)
            if type(varType1) == ArrayType:
                dimen2 = len(x.value) if dimen2 < len(x.value) else dimen2
                for y in x.value:
                    varType = varType2 = self.visit(y, param)
                    if type(varType2) == ArrayType:
                        dimen3 = len(y.value) if dimen3 < len(y.value) else dimen3
        dimen = [dimen1, dimen2, dimen3] if dimen3 > 0 else [dimen1, dimen2] if dimen2 > 0 else [dimen1]
        return ArrayType(varType, dimen)