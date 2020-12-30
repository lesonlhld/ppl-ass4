import unittest
from TestUtils import TestCodeGen
from AST import *


class CheckCodeGenSuite(unittest.TestCase):
    def test_501(self):
        """Created automatically"""
        input = r"""Function: main
                   Body: 
                        print(string_of_int(120));
                   EndBody."""
        expect = r"""120"""
        self.assertTrue(TestCodeGen.test(input,expect,501))
        
    def test_502(self):
        """Created automatically"""
        input = r"""Function: main
                   Body:
                   Var: str = 123;
                   print(string_of_int(str));
                   EndBody."""
        expect = r"""123"""
        self.assertTrue(TestCodeGen.test(input,expect,502))
        
    def test_503(self):
        """Created automatically"""
        input = r"""Function: main
                   Body:
                   Var: x = "120";
                   print(x);
                   EndBody."""
        expect = r"""120"""
        self.assertTrue(TestCodeGen.test(input,expect,503))
        
    def test_504(self):
        """Created automatically"""
        input = r"""Function: main
                   Body:
                   Var: str = 123.2e-1;
                   print(string_of_float(str));
                   EndBody."""
        expect = r"""12.32"""
        self.assertTrue(TestCodeGen.test(input,expect,504))
        
    def test_505(self):
        """Created automatically"""
        input = r"""Function: main
                   Body:
                   Var: str = 123.2e-1;
                   str = 15.6;
                   print(string_of_float(str));
                   EndBody."""
        expect = r"""15.6"""
        self.assertTrue(TestCodeGen.test(input,expect,505))
        
    def test_506(self):
        """Created automatically"""
        input = r"""Function: main
                   Body:
                   print(string_of_int(1+2));
                   EndBody."""
        expect = r"""3"""
        self.assertTrue(TestCodeGen.test(input,expect,506))
        
    def test_507(self):
        """Created automatically"""
        input = r"""Function: main
                   Body:
                   print(string_of_int(1*2));
                   EndBody."""
        expect = r"""2"""
        self.assertTrue(TestCodeGen.test(input,expect,507))
        
    def test_508(self):
        """Created automatically"""
        input = r"""Function: main
                   Body:
                   print(string_of_float(3\2));
                   EndBody."""
        expect = r"""1.5"""
        self.assertTrue(TestCodeGen.test(input,expect,508))
        
    def test_509(self):
        """Created automatically"""
        input = r"""Function: main
                   Body:
                   print(string_of_bool(1<2));
                   EndBody."""
        expect = r"""true"""
        self.assertTrue(TestCodeGen.test(input,expect,509))
        
    def test_510(self):
        """Created automatically"""
        input = r"""Function: main
                   Body:
                   print(string_of_bool(True));
                   EndBody."""
        expect = r"""true"""
        self.assertTrue(TestCodeGen.test(input,expect,510))
        
    def test_511(self):
        """Created automatically"""
        input = r"""Function: main
                   Body:
                   print(string_of_bool(False));
                   EndBody."""
        expect = r"""false"""
        self.assertTrue(TestCodeGen.test(input,expect,511))
        
    def test_512(self):
        """Created automatically"""
        input = r"""Function: main
                    Body:
                    Var: n = 1;
                    If n < 0 Then
                        print("n < 0");
                    Else
                        print("n >= 0");
                    EndIf.
                    EndBody."""
        expect = r"""n >= 0"""
        self.assertTrue(TestCodeGen.test(input,expect,512))
        
    def test_513(self):
        """Created automatically"""
        input = r"""Function: main
                    Body:
                    Var: n = -1;
                    If n < 0 Then
                        print("n < 0");
                    Else
                        print("n >= 0");
                    EndIf.
                    EndBody."""
        expect = r"""n < 0"""
        self.assertTrue(TestCodeGen.test(input,expect,513))
        
    def test_514(self):
        """Created automatically"""
        input = r"""Function: main
                    Body:
                    Var: n = -1;
                    If n == 0 Then
                        print("n < 0");
                    ElseIf (n>0) Then
                        print("n > 0");
                    Else
                        print("n = 0");
                    EndIf.
                    EndBody."""
        expect = r"""n = 0"""
        self.assertTrue(TestCodeGen.test(input,expect,514))
        
    def test_515(self):
        """Created automatically"""
        input = r"""Function: main
                    Body:
                    Var: i = 0;
                        While (i<5) Do
                            print(string_of_int(i));
                            i = i + 1;
                        EndWhile.
                    EndBody."""
        expect = r"""01234"""
        self.assertTrue(TestCodeGen.test(input,expect,515))
        
    def test_516(self):
        """Created automatically"""
        input = r"""Function: main
                    Body:
                    Var: i = 0;
                        While (True) Do
                            print(string_of_int(i));
                            i = i + 1;
                            If i == 5 Then
                                Break;
                            EndIf.   
                        EndWhile.
                    EndBody."""
        expect = r"""01234"""
        self.assertTrue(TestCodeGen.test(input,expect,516))
        
    def test_517(self):
        """Created automatically"""
        input = r"""Function: main
                    Body:
                    Var: i = 0;
                    Do
                        print(string_of_int(i));
                        i = i + 1;
                    While (i<2) EndDo.
                    EndBody."""
        expect = r"""01"""
        self.assertTrue(TestCodeGen.test(input,expect,517))
        
    def test_518(self):
        """Created automatically"""
        input = r"""Function: main
                    Body:
                    Var: i = 0;
                    Do
                        print(string_of_int(i));
                        i = i + 1;
                    While (i<0) EndDo.
                    EndBody."""
        expect = r"""0"""
        self.assertTrue(TestCodeGen.test(input,expect,518))
        
    def test_519(self):
        """Created automatically"""
        input = r"""Function: main
                    Body:
                    Var: i = 0;
                    For (i = 0, i < 10, 2) Do
                        print(string_of_int(i));
                    EndFor.
                    EndBody."""
        expect = r"""IllegalRuntimeException("Pop empty stack")"""
        self.assertTrue(TestCodeGen.test(input,expect,519))
        
    def test_520(self):
        """Created automatically"""
        input = r"""Function: main
                    Body:
                    Var: n = -1;
                    If n < 0 Then
                        Return;
                    Else
                        print("n >= 0");
                    EndIf.
                    EndBody."""
        expect = r""""""
        self.assertTrue(TestCodeGen.test(input,expect,520))
        
    def test_521(self):
        """Created automatically"""
        input = r"""
        Function: sum
        Body:
            Return 0;
        EndBody.
        Function: main
        Body:
            Var: y=0;
            y = sum();
            printStrLn(string_of_int(y+1));
            Return;
        EndBody."""
        expect = r"""1
"""
        self.assertTrue(TestCodeGen.test(input,expect,521))
        
    def test_522(self):
        """Created automatically"""
        input = r"""
        Function: sum
        Parameter: x
        Body:
            Var: i=0;
            For (i = 0 , i < 5, 1) Do
                x = x + i;
            EndFor.
            Return x;
        EndBody.
        Function: main
        Body:
            Var: y=0;
            y = sum(0);
            print(string_of_int(y));
        EndBody."""
        expect = r"""IllegalRuntimeException("Pop empty stack")"""
        self.assertTrue(TestCodeGen.test(input,expect,522))
        
    def test_523(self):
        """Created automatically"""
        input = r""" 
        Function: main
        Body:
        Var: a[3] = {1,2,3};
            Var: i = 0;
            While (i < 3) Do
                print(string_of_int(a[i]));
                i = i + 1;
            EndWhile.
        EndBody.
        """
        expect = r"""123"""
        self.assertTrue(TestCodeGen.test(input,expect,523))
        