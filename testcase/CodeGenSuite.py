import unittest
from TestUtils import TestCodeGen
from AST import *


class CheckCodeGenSuite(unittest.TestCase):
    def test_501(self):
        """Created automatically"""
        input = r"""
        Var:x="hello";
        Function: main 
        Body:
        print(x);
        EndBody."""
        expect = r"""hello"""
        self.assertTrue(TestCodeGen.test(input,expect,501))
        
    def test_502(self):
        """Created automatically"""
        input = r"""
        Var:x[3]={"1","2","3"};
        Var:y[3]={1,2,3};
        Function: main 
        Body:
        print(x[1]);
        print(string_of_int(y[1]));
        EndBody."""
        expect = r"""22"""
        self.assertTrue(TestCodeGen.test(input,expect,502))
        
    def test_503(self):
        """Created automatically"""
        input = r"""Function: main
                   Body:
                   Var: x = 0x123ABC;
                   Var: y = 0o1234;
                    print(string_of_int(x));
                    print(string_of_int(y));
                   EndBody."""
        expect = r"""1194684668"""
        self.assertTrue(TestCodeGen.test(input,expect,503))
        
    def test_504(self):
        """Created automatically"""
        input = r"""
        Var:x="hello";
        Function: main 
        Body:
        x="Hello World";
        print(x);
        EndBody."""
        expect = r"""Hello World"""
        self.assertTrue(TestCodeGen.test(input,expect,504))
        
    def test_505(self):
        """Created automatically"""
        input = r"""Function: main
                   Body:
                   Var: x = 1.234;
                   EndBody."""
        expect = r""""""
        self.assertTrue(TestCodeGen.test(input,expect,505))
        
    def test_506(self):
        """Created automatically"""
        input = r"""Function: main
                   Body:
                   Var: x = 32.4e-1;
                   EndBody."""
        expect = r""""""
        self.assertTrue(TestCodeGen.test(input,expect,506))
        
    def test_507(self):
        """Created automatically"""
        input = r"""Function: main
                   Body:
                   Var: x = True;
                   EndBody."""
        expect = r""""""
        self.assertTrue(TestCodeGen.test(input,expect,507))
        
    def test_508(self):
        """Created automatically"""
        input = r"""Function: main
                   Body:
                   Var: x = "Chung Xon";
                   EndBody."""
        expect = r""""""
        self.assertTrue(TestCodeGen.test(input,expect,508))
        
    def test_509(self):
        """Created automatically"""
        input = r"""Function: main
                   Body:
                   Var: x = "\tHello moi nguoi @@~!@#$%^&***** \n";
                   EndBody."""
        expect = r""""""
        self.assertTrue(TestCodeGen.test(input,expect,509))
        
    def test_510(self):
        """Created automatically"""
        input = r"""Function: main
                   Body:
                   Var: x[3] = {1,2,3};
                   EndBody."""
        expect = r""""""
        self.assertTrue(TestCodeGen.test(input,expect,510))
        
    def test_511(self):
        """Created automatically"""
        input = r"""Function: main
                   Body:
                   Var: x[3] = {1.2,2.3,3.4};
                   EndBody."""
        expect = r""""""
        self.assertTrue(TestCodeGen.test(input,expect,511))
        
    def test_512(self):
        """Created automatically"""
        input = r"""Function: main
        Body:
            Var: a[3] = {1,2,3}, c[2][3] = {{1,3,5},{3,5,7}};
        EndBody."""
        expect = r""""""
        self.assertTrue(TestCodeGen.test(input,expect,512))
        
    def test_513(self):
        """Created automatically"""
        input = r"""Function: main
        Body:
            Var: a[2][2] = {{"a","b"},{"c","d"}}, c[2][3] = {{1e-2,3.5,5.0},{3.1,5e2,7.0e-3}};
        EndBody."""
        expect = r""""""
        self.assertTrue(TestCodeGen.test(input,expect,513))
        
    def test_514(self):
        """Created automatically"""
        input = r"""Function: main
                   Body: 
                        print("120");
                   EndBody."""
        expect = r"""120"""
        self.assertTrue(TestCodeGen.test(input,expect,514))
        
    def test_515(self):
        """Created automatically"""
        input = r"""Function: main
                   Body: 
                        print(string_of_int(120));
                   EndBody."""
        expect = r"""120"""
        self.assertTrue(TestCodeGen.test(input,expect,515))
        
    def test_516(self):
        """Created automatically"""
        input = r"""Function: main
                   Body:
                   Var: str = 123;
                   print(string_of_int(str));
                   EndBody."""
        expect = r"""123"""
        self.assertTrue(TestCodeGen.test(input,expect,516))
        
    def test_517(self):
        """Created automatically"""
        input = r"""Function: main
                   Body:
                   Var: x = "120";
                   print(x);
                   EndBody."""
        expect = r"""120"""
        self.assertTrue(TestCodeGen.test(input,expect,517))
        
    def test_518(self):
        """Created automatically"""
        input = r"""Function: main
                   Body:
                   Var: str = 123.2e-1;
                   print(string_of_float(str));
                   EndBody."""
        expect = r"""12.32"""
        self.assertTrue(TestCodeGen.test(input,expect,518))
        
    def test_519(self):
        """Created automatically"""
        input = r"""Function: main
                   Body:
                   print(string_of_bool(True));
                   EndBody."""
        expect = r"""true"""
        self.assertTrue(TestCodeGen.test(input,expect,519))
        
    def test_520(self):
        """Created automatically"""
        input = r"""Function: main
                   Body:
                   print("False");
                   EndBody."""
        expect = r"""False"""
        self.assertTrue(TestCodeGen.test(input,expect,520))
        
    def test_521(self):
        """Created automatically"""
        input = r"""Function: main
        Body:
            Var: a[3] = {1,2,3}, c[2][3] = {{1,3,5},{3,5,7}};
            print(string_of_int(c[1][2]));
        EndBody."""
        expect = r"""7"""
        self.assertTrue(TestCodeGen.test(input,expect,521))
        
    def test_522(self):
        """Created automatically"""
        input = r"""Function: main
                   Body:
                   printStrLn(string_of_int(int_of_float(float_of_string("12.2"))));
                   printLn();
                   print(string_of_float(float_to_int(int_of_float(float_of_string("12.8")))));
                   EndBody."""
        expect = r"""12

12.0"""
        self.assertTrue(TestCodeGen.test(input,expect,522))
        
    def test_523(self):
        """Created automatically"""
        input = r"""Function: main
        Body:
            print(string_of_bool(!bool_of_string("False")));
        EndBody."""
        expect = r"""true"""
        self.assertTrue(TestCodeGen.test(input,expect,523))
        
    def test_524(self):
        """Created automatically"""
        input = r"""Function: main
                   Body:
                   Var: str = 123.2e-1;
                   str = 15.6;
                   print(string_of_float(str));
                   EndBody."""
        expect = r"""15.6"""
        self.assertTrue(TestCodeGen.test(input,expect,524))
        
    def test_525(self):
        """Created automatically"""
        input = r"""Function: main
                   Body:
                   print(string_of_int(1+2));
                   EndBody."""
        expect = r"""3"""
        self.assertTrue(TestCodeGen.test(input,expect,525))
        
    def test_526(self):
        """Created automatically"""
        input = r"""
        Function: main 
        Body:
        Var:x[3]={"1","2","3"};
        print(x[1]);
        EndBody."""
        expect = r"""2"""
        self.assertTrue(TestCodeGen.test(input,expect,526))
        
    def test_527(self):
        """Created automatically"""
        input = r"""Function: main
                   Body:
                   print(string_of_float(3.0\.2.0));
                   EndBody."""
        expect = r"""1.5"""
        self.assertTrue(TestCodeGen.test(input,expect,527))
        
    def test_528(self):
        """Created automatically"""
        input = r"""Function: main
                   Body:
                   print(string_of_bool(1<2));
                   EndBody."""
        expect = r"""true"""
        self.assertTrue(TestCodeGen.test(input,expect,528))
        
    def test_529(self):
        """Created automatically"""
        input = r"""
        Function: main 
        Body:
            Var: var=True,x=False;
            Var: ilv=4e3, nvh=2.3;
            var = (nvh=/=123.45);
            x = var && (ilv <. nvh);
            print(string_of_bool(x));
        EndBody."""
        expect = r"""false"""
        self.assertTrue(TestCodeGen.test(input,expect,529))
        
    def test_530(self):
        """Created automatically"""
        input = r"""
        Function: main
        Body:
            Var: a[5]={2,3,5,7,8},x=0;
            x = -(-15+(45*2)*(35+108+a[4]))*int_of_string("21");
            printLn();
            printStrLn(string_of_int(x));
        EndBody."""
        expect = r"""
-285075
"""
        self.assertTrue(TestCodeGen.test(input,expect,530))
        
    def test_531(self):
        """Created automatically"""
        input = r"""Function: main
        Body:
        Var: x = False, a = 1.e-2, b = 20; 
            x = ((a <=. 2.3e-13) || (b == 21) || (b != 235));
            print(string_of_bool(x));
        EndBody."""
        expect = r"""true"""
        self.assertTrue(TestCodeGen.test(input,expect,531))
        
    def test_532(self):
        """Created automatically"""
        input = r"""
        Function: main
        Body:
            Var: a[5]={1,2,3,4,5};
            Var: i = 0;
            i = a[1 + foo(2,1)]-1;
            a[i] = 0x369*3 + 4;
            print(string_of_int(a[i]));
        EndBody.
        Function: foo
        Parameter: a,b
        Body:
            Return a+b;
        EndBody."""
        expect = r"""2623"""
        self.assertTrue(TestCodeGen.test(input,expect,532))
        
    def test_533(self):
        """Created automatically"""
        input = r"""Function: main
                   Body:
                   print(string_of_int(2*2));
                   EndBody."""
        expect = r"""4"""
        self.assertTrue(TestCodeGen.test(input,expect,533))
        
    def test_534(self):
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
        self.assertTrue(TestCodeGen.test(input,expect,534))
        
    def test_535(self):
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
        self.assertTrue(TestCodeGen.test(input,expect,535))
        
    def test_536(self):
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
        self.assertTrue(TestCodeGen.test(input,expect,536))
        
    def test_537(self):
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
        self.assertTrue(TestCodeGen.test(input,expect,537))
        
    def test_538(self):
        """Created automatically"""
        input = r"""Function: main 
        Body:
        Var: n=101.0;
            If n <. 100.0 Then
            n=n*.3.3;
            ElseIf n>=.101.0 Then
            n=n\.5.3;
            EndIf.
            print(string_of_float(n));
        EndBody.
        """
        expect = r"""19.056602"""
        self.assertTrue(TestCodeGen.test(input,expect,538))
        
    def test_539(self):
        """Created automatically"""
        input = r"""Function: main 
        Body:
        Var: n=1.0;
            If n <. 3.0 Then
            n=n*.3.3;
            ElseIf n>.100.2 Then
            n=n\.5.3;
            EndIf.
            print(string_of_float(n));
        EndBody.
        """
        expect = r"""3.3"""
        self.assertTrue(TestCodeGen.test(input,expect,539))
        
    def test_540(self):
        """Created automatically"""
        input = r"""Function: main 
        Body:
        Var: n=100.0;
            If n <. 3.0 Then
            n=n*.3.3;
            ElseIf n>.100.2 Then
            n=n\.5.3;
            EndIf.
            print(string_of_float(n));
        EndBody.
        """
        expect = r"""100.0"""
        self.assertTrue(TestCodeGen.test(input,expect,540))
        
    def test_541(self):
        """Created automatically"""
        input = r"""Function: main 
        Body:
        Var: n=123.0;
            If n <. 3.0 Then
            n=n*.3.3;
            ElseIf n>.100.2 Then
            n=n\.5.3;
            EndIf.
            print(string_of_float(n));
        EndBody.
        """
        expect = r"""23.207546"""
        self.assertTrue(TestCodeGen.test(input,expect,541))
        
    def test_542(self):
        """Created automatically"""
        input = r"""Function: main 
        Body:
        Var: k=0,i=0,j=False,f=11;
            If ((k<1)&&(i!=0))||(k>5)||!j Then
                f=f%3;
            EndIf.
            print(string_of_int(f));
        EndBody."""
        expect = r"""2"""
        self.assertTrue(TestCodeGen.test(input,expect,542))
        
    def test_543(self):
        """Created automatically"""
        input = r"""Function: main 
        Body:
            Var: a=0;
                If bool_of_string("True") Then
                    Var: b="hello";
                    printStrLn(string_of_float(float_to_int(a) +. 2.0));
                EndIf.
                print(string_of_float(float_to_int(a) +. 2.0));
        EndBody."""
        expect = r"""2.0
2.0"""
        self.assertTrue(TestCodeGen.test(input,expect,543))
        
    def test_544(self):
        """Created automatically"""
        input = r"""
        Function: main
        Body:
        Var: n=1, i=5.5;
            If i <. 4.5 Then
                printStrLn(string_of_float(i));
            ElseIf n > 10 Then 
                print("Else If");
            Else
                n=int_of_float(i)-1;
                print(string_of_int(n));
            EndIf.
            EndBody."""
        expect = r"""4"""
        self.assertTrue(TestCodeGen.test(input,expect,544))
        
    def test_545(self):
        """Created automatically"""
        input = r"""Function: main
        Body:
        Var: n = 120,  array[2][3] = {{867,345,987},{76,12,744}};
            If n > 10 Then
                If n%11 < 10 Then 
                n = n * n % 9;
                EndIf.
                printStrLn(string_of_int(n));
            EndIf.
        EndBody."""
        expect = r"""120
"""
        self.assertTrue(TestCodeGen.test(input,expect,545))
        
    def test_546(self):
        """Created automatically"""
        input = r"""Function: main
        Body:
        Var: n = 120,  array[2][3] = {{867,345,987},{76,12,744}};
            If n > 10 Then
                If n%11 <= 10 Then 
                n = n * n % 9;
                EndIf.
                printStrLn(string_of_int(n));
            EndIf.
        EndBody."""
        expect = r"""0
"""
        self.assertTrue(TestCodeGen.test(input,expect,546))
        
    def test_547(self):
        """Created automatically"""
        input = r"""Function: main
        Body:
            Var: i = 0,k=10;
            Var:a[5]={0,0,0,0,0}, c = "12";
            While i !=k Do
                a[i%4] = a[i%4] + i + int_of_string(c);
                print(string_of_int(a[i%4]));
                i = i + 1;
            EndWhile.
        EndBody."""
        expect = r"""12131415283032344851"""
        self.assertTrue(TestCodeGen.test(input,expect,547))
        
    def test_548(self):
        """Created automatically"""
        input = r"""Function: main 
        Body:
            Var: x=6452342;
            While True Do
                If x<0 Then Break;
                ElseIf x > 1 Then
                    x=x-3;
                Else 
                printStrLn("Error");
                Break;
                EndIf.
            EndWhile.
        EndBody."""
        expect = r""""""
        self.assertTrue(TestCodeGen.test(input,expect,548))
        
    def test_549(self):
        """Created automatically"""
        input = r"""Function: main 
        Body:
            Var: x=20;
            While True Do
                If (x>0) && (x<3) Then 
                printStrLn("oke");
                Break;
                Else printStrLn("Error");
                EndIf.
                x=x-3;
            EndWhile.
        EndBody."""
        expect = r"""Error
Error
Error
Error
Error
Error
oke
"""
        self.assertTrue(TestCodeGen.test(input,expect,549))
        
    def test_550(self):
        """Created automatically"""
        input = r"""Function: main
        Body:
        Var: x = 5;
            While (True) Do
                While (x>=0) Do
                    x = x+-2;
                EndWhile.
                If ((x<0)) Then
                Break;
                EndIf.
            EndWhile.
            print(string_of_float(float_to_int(x)));
        EndBody."""
        expect = r"""-1.0"""
        self.assertTrue(TestCodeGen.test(input,expect,550))
        
    def test_551(self):
        """Created automatically"""
        input = r"""
        Function: main
        Body:
            While True Do 
            printStrLn("Hello World");
            Break;
            EndWhile.
        EndBody."""
        expect = r"""Hello World
"""
        self.assertTrue(TestCodeGen.test(input,expect,551))
        
    def test_552(self):
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
        self.assertTrue(TestCodeGen.test(input,expect,552))
        
    def test_553(self):
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
        self.assertTrue(TestCodeGen.test(input,expect,553))
        
    def test_554(self):
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
        self.assertTrue(TestCodeGen.test(input,expect,554))
        
    def test_555(self):
        """Created automatically"""
        input = r"""Function: main
        Body:
            Var: x = 1.2, a =2.e2, b = 32.3;
            Do 
            x = a +. b +. x;
            While(x<.1000.1)
            EndDo.
            print(string_of_float(x));
        EndBody."""
        expect = r"""1162.7"""
        self.assertTrue(TestCodeGen.test(input,expect,555))
        
    def test_556(self):
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
        self.assertTrue(TestCodeGen.test(input,expect,556))
        
    def test_557(self):
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
        self.assertTrue(TestCodeGen.test(input,expect,557))
        
    def test_558(self):
        """Created automatically"""
        input = r"""Function: main 
        Body:
            Var: x =1;
            Do
                Var: x =1.5;
                x= x+.1.5;
                printStrLn(string_of_float(x));
            While x>1 
            EndDo.
        EndBody."""
        expect = r"""3.0
"""
        self.assertTrue(TestCodeGen.test(input,expect,558))
        
    def test_559(self):
        """Created automatically"""
        input = r"""Function: main
        Body:
            Var: i = 0;
            Do
                Var: k = 10;
                If i>0 Then
                    print(string_of_int(k%i));
                EndIf.
                i = i + 1;
            While i <= 10 
            EndDo.
        EndBody."""
        expect = r"""0012043210"""
        self.assertTrue(TestCodeGen.test(input,expect,559))
        
    def test_560(self):
        """Created automatically"""
        input = r"""Function: main
                    Body:
                    Var: i = 0;
                    For (i = 0, i < 10, 2) Do
                        print(string_of_int(i));
                    EndFor.
                    EndBody."""
        expect = r"""02468"""
        self.assertTrue(TestCodeGen.test(input,expect,560))
        
    def test_561(self):
        """Created automatically"""
        input = r"""
        Function: main 
        Body:
        Var: n[5]={3.34,6.67,8.03,32.57,54.108},i=0,k=10,j=1;
            For (i = 0, i < k, j*j) Do
                n[i%5]=n[i%5]+.float_to_int(i);
                print(string_of_float(n[i%5]));
            EndFor.
        EndBody."""
        expect = r"""3.347.6710.0335.5758.1088.3413.6717.02999943.5767.108"""
        self.assertTrue(TestCodeGen.test(input,expect,561))
        
    def test_562(self):
        """Created automatically"""
        input = r"""
        Var:x[2][2]={{"1","2"},{"3","4"}};
        Function: main 
        Body:
        Var: i=0, j=0;
        For( i=0,i<2,1) Do
            For(j=0,j<2,1) Do
                print(x[i][j]);
            EndFor.
        EndFor.
        EndBody."""
        expect = r"""1234"""
        self.assertTrue(TestCodeGen.test(input,expect,562))
        
    def test_563(self):
        """Created automatically"""
        input = r"""
        Function: main
        Body:
        Var: i =0, x=15;
            For (i = 1, i <= x*x,i*i+1)
            Do x=x+1;
            print(string_of_int(i));
            print(", ");
            print(string_of_int(x));
            printLn();
            EndFor.
        EndBody."""
        expect = r"""1, 16
3, 17
13, 18
183, 19
"""
        self.assertTrue(TestCodeGen.test(input,expect,563))
        
    def test_564(self):
        """Created automatically"""
        input = r"""
        Function: main
        Body:
        Var: row=2,col=3,arr[2][3]={{1,2,3},{4,5,6}};
            Var: sum=0;
            Var: i=0, j=0;
            For( i=0,i<row,1) Do
                For(j=0,j<col,1) Do
                    sum=sum+arr[i][j];
                EndFor.
            EndFor.
            print(string_of_int(sum));
        EndBody."""
        expect = r"""21"""
        self.assertTrue(TestCodeGen.test(input,expect,564))
        
    def test_565(self):
        """Created automatically"""
        input = r"""Function: main
        Body:
        Var:factorial=1,n=0,i=0;
        print("Enter integer: ");
        n=3;
        printStrLn(string_of_int(n));
        For (i=1, i<n, 1) Do
            factorial=factorial*i;
        EndFor.
        print(string_of_int(factorial));
        EndBody."""
        expect = r"""Enter integer: 3
2"""
        self.assertTrue(TestCodeGen.test(input,expect,565))
        
    def test_566(self):
        """Created automatically"""
        input = r"""
        Function: main
            Body:
                Var: x[3][2] = { {212,529}, {272,398}, {247,954} };
                Var: y[3][2] = { {652,654}, {256,214}, {158,765} };
                Var: i=0,j=0;
                For( i=0,i<3,1) Do
                    For(j=0,j<2,1) Do
                        print(string_of_int(x[i][j]+y[i][j]));
                        print(" ");
                    EndFor.
                    printLn();
                EndFor.
            EndBody."""
        expect = r"""864 1183 
528 612 
405 1719 
"""
        self.assertTrue(TestCodeGen.test(input,expect,566))
        
    def test_567(self):
        """Created automatically"""
        input = r"""
        Function: main
            Body:
                Var: char = "*";
                Var: n = 11;
                Var: i=0,j=0;
                For(i=0,i<n,1) Do
                    printLn();
                    If n\2 < i Then
                        For(j=0,j<n\2,1) Do
                            print(" ");
                        EndFor.
                        print(char);
                    Else
                        For(j=0,j<(n\2-i),1) Do
                            print(" ");
                        EndFor.
                        For(j=0,j<(n-(n\2-i)*2),1) Do
                            print(char);
                        EndFor.
                    EndIf.
                EndFor.
            EndBody."""
        expect = r"""
     *
    ***
   *****
  *******
 *********
***********
     *
     *
     *
     *
     *"""
        self.assertTrue(TestCodeGen.test(input,expect,567))
        
    def test_568(self):
        """Created automatically"""
        input = r"""Function:main
        Body:
        Var: a =True,b=0;
        If!a Then
        b=5; 
        Else
        While(b<3) Do
        b=b+1;
        EndWhile.
        EndIf.
        printLn();
        print(string_of_int(b));
        EndBody."""
        expect = r"""
3"""
        self.assertTrue(TestCodeGen.test(input,expect,568))
        
    def test_569(self):
        """Created automatically"""
        input = r"""Function: main
        Body:
        Var:i=0;
            For (i=1, i%15!=9, (i*20)) Do
            EndFor.
            print(string_of_int(i));
        EndBody."""
        expect = r"""547383789"""
        self.assertTrue(TestCodeGen.test(input,expect,569))
        
    def test_570(self):
        """Created automatically"""
        input = r"""
        Function: main
            Body:
                Var: x=0,i=0;
                For (i=1,i<=1,i) Do
                    Var:x=1;
                    print(string_of_int(x));
                    x = x + 1;
                EndFor.
                print(string_of_int(x));
            EndBody."""
        expect = r"""10"""
        self.assertTrue(TestCodeGen.test(input,expect,570))
        
    def test_571(self):
        """Created automatically"""
        input = r"""Function: main 
        Body:
            Var: i = 0,c=True;
            While i<=423 Do
                Var: b =True, a=False;
                b=i<100;
                a = (!(b && c)||!(a&&b)&&((i+1)==234)); 
                i = i + 3; **cmt**
                If i==212 Then Break;
                EndIf.
                c=a;
            EndWhile.
            print(string_of_bool(c));
        EndBody.
        """
        expect = r"""false"""
        self.assertTrue(TestCodeGen.test(input,expect,571))
        
    def test_572(self):
        """Created automatically"""
        input = r"""Function: main
        Body:
        Var: x[3][3] = {{114,834,217},{568,471,651},{831,246,123}};
        Var: i = 0;
        While (i < 3) Do
            Var: j = 0;
            Do
                print(string_of_int(x[i][j]));
                print(" ");
                j = j + 1;
            While (j<3)
            EndDo.
            printLn();
            i = i + 1;
        EndWhile.
        EndBody."""
        expect = r"""114 834 217 
568 471 651 
831 246 123 
"""
        self.assertTrue(TestCodeGen.test(input,expect,572))
        
    def test_573(self):
        """Created automatically"""
        input = r"""Function: main
        Body:
        Var: n = 0;
            Var: t1 = 0, t2 = 1, nextTerm = 0, i = 0;
            print("Enter the number of terms: ");
            n = 15;
            print("Fibonacci Series: ");
            printStrLn(string_of_int(n));
            For (i = 0, i < n, 1) Do
                If(i == 0) Then
                    print(string_of_int(t1));
                    Continue;
                EndIf.
                If(i == 1) Then
                    print(string_of_int(t2));
                    Continue;
                EndIf.
                nextTerm = t1 + t2;
                t1 = t2;
                t2 = nextTerm;
                
                print(string_of_int(nextTerm));
            EndFor.
        EndBody."""
        expect = r"""Enter the number of terms: Fibonacci Series: 15
01123581321345589144233377"""
        self.assertTrue(TestCodeGen.test(input,expect,573))
        
    def test_574(self):
        """Created automatically"""
        input = r"""Function: main
                    Body:
                    Var: i=0, result=0,x=9;
                        For (i = 1, i <= x*x*x,i + x ) Do
                            result = i * i + i \ --1 % i--i;
                        EndFor.
                        print(string_of_int(result));
                    EndBody."""
        expect = r"""398792"""
        self.assertTrue(TestCodeGen.test(input,expect,574))
        
    def test_575(self):
        """Created automatically"""
        input = r"""Function: main 
        Body:
        Var:x=100;
            While x>1 Do
            Var: i=0,a = 10;
                For (i = 100,True, -(i-6)) Do
                    If -a>-3 Then
                        Break;
                    EndIf.
                    a = a -3;
                    x=x-a*10;
                EndFor.
            EndWhile.
            print(string_of_int(x));
        EndBody."""
        expect = r"""-20"""
        self.assertTrue(TestCodeGen.test(input,expect,575))
        
    def test_576(self):
        """Created automatically"""
        input = r""" 
                Function: main
                Body:
                    Var: a = 5,b=4.5;
                    a = a + foo(b);
                    print(string_of_int(a));
                EndBody.

                Function: foo
                Parameter: a
                Body:
                    Var: c = 5.5;
                    Return int_of_float(c+a);
                EndBody.
            """
        expect = r"""15"""
        self.assertTrue(TestCodeGen.test(input,expect,576))
        
    def test_577(self):
        """Created automatically"""
        input = r"""
        Function: main
            Body:
            Var:x=0,y=1,j=0,i=0;
                For (i=0, True, 123) Do
                    x = y + i;
                    y = y + 1;
                    If (i+1)%3 == 0 Then
                        Break;
                    EndIf.
                EndFor.
                printStrLn(string_of_int(x+y));
            EndBody.
            """
        expect = r"""-2112565168
"""
        self.assertTrue(TestCodeGen.test(input,expect,577))
        
    def test_578(self):
        """Created automatically"""
        input = r"""Function: main
        Body:
        Var:i = 10;
            While !False Do
                If i< 0 Then
                    Break;
                ElseIf i%2 == 0 Then
                    i=i-1;
                    Continue;
                Else
                    print(string_of_int(i));
                EndIf.
                i=i-1;
            EndWhile.
        EndBody."""
        expect = r"""97531"""
        self.assertTrue(TestCodeGen.test(input,expect,578))
        
    def test_579(self):
        """Created automatically"""
        input = r"""
        Function: sum
            Parameter: x[5]
                Body:
                    Var: sum = 0, i=0;
                    For (i = 0 , i < 5, 1) Do
                        sum = sum + x[i];
                    EndFor.
                    Return sum;
                EndBody.
        Function: main
            Body:
                Var: x[5] = {1,2,3,4,5};
                Var: y=0;
                y = sum(x);
                printStrLn(string_of_int(y));
                Return;
            EndBody."""
        expect = r"""15
"""
        self.assertTrue(TestCodeGen.test(input,expect,579))
        
    def test_580(self):
        """Created automatically"""
        input = r"""
Function: fact
Parameter: n
Body:
If n == 0 Then
Return 1;
Else
Return n * fact (n - 1);
EndIf.
EndBody.
Function: main
Body:
Var:x = 10;
x = fact(x);
print(string_of_int(x));
EndBody."""
        expect = r"""3628800"""
        self.assertTrue(TestCodeGen.test(input,expect,580))
        
    def test_581(self):
        """Created automatically"""
        input = r"""
        Function: fact
        Parameter: n
        Body:
            If n == 0 Then
                Return 1;
            ElseIf (n>0) Then
                Return n * fact (n - 1);
            Else
                Return n;
            EndIf.
        EndBody.
        Function: main
        Body:
        printStrLn(string_of_int(fact(3)));
        print(string_of_int(fact(-5)));
        EndBody."""
        expect = r"""6
-5"""
        self.assertTrue(TestCodeGen.test(input,expect,581))
        
    def test_582(self):
        """Created automatically"""
        input = r"""
        Function: main
        Body:
        Var: a=0,b=0,c=0,d=0;
            a = -1082000;
            b = -0X123BCD;
            c = -0o21345;
            d = -a;
            print(string_of_int(c));
            c = -call(a);
            print(string_of_int(c));
        EndBody.
        Function: call
            Parameter: s
            Body:
                print(string_of_int(s));
                Return s;
            EndBody.
                """
        expect = r"""-8933-10820001082000"""
        self.assertTrue(TestCodeGen.test(input,expect,582))
        
    def test_583(self):
        """Created automatically"""
        input = r"""
        Function: foo
        Parameter: x
        Body:
            Return string_of_bool(!x);
        EndBody.
        Function: main 
        Body:
            print(foo(True));
        EndBody."""
        expect = r"""false"""
        self.assertTrue(TestCodeGen.test(input,expect,583))
        
    def test_584(self):
        """Created automatically"""
        input = r"""
        Function: call
        Parameter: a, b, c, d, e, f, g
        Body:
            Return string_of_int(a+b+int_of_float(c)+d+int_of_string(g));
        EndBody.
        Function: main
        Body:
        Var: a=6, var=214.45, arr[5]={1,67,32,65,23};
            print(call(a,876,var*.65e-1,arr[3],True,"chuoi~~\n","953"));
        EndBody."""
        expect = r"""3293"""
        self.assertTrue(TestCodeGen.test(input,expect,584))
        
    def test_585(self):
        """Created automatically"""
        input = r"""
        Var:x = 0, y=0;
        Function: main
        Body:
            x=1;
            y=2;
            print(string_of_int(foo()));
        EndBody.
        Function: foo
        Body:
            Return x+y;
        EndBody."""
        expect = r"""3"""
        self.assertTrue(TestCodeGen.test(input,expect,585))
        
    def test_586(self):
        """Created automatically"""
        input = r"""
        Function: foo
            Parameter: x[3]
            Body:
            Var: i =0;
                For(i=0,i<3,1) Do
                    Var: y = 2;
                    printStrLn(string_of_float(x[i]));
                EndFor.
            EndBody.
        Function: main
            Body:
            Var: x[3] = {1.1,2.2,3.3};
                foo(x);
            EndBody."""
        expect = r"""1.1
2.2
3.3
"""
        self.assertTrue(TestCodeGen.test(input,expect,586))
        
    def test_587(self):
        """Created automatically"""
        input = r"""
        Function: foo
        Body:
        Var: x[3]={1,2,3};
        Return x;
        EndBody.
        Function: main
        Body:
            print(string_of_int(foo()[0]));
        EndBody.
"""
        expect = r"""1"""
        self.assertTrue(TestCodeGen.test(input,expect,587))
        
    def test_588(self):
        """Created automatically"""
        input = r"""
        Function: foo
        Body:
        Var: x[3]={1,2,3};
        Return x;
        EndBody.
        Function: main
        Body:
            foo()[2] = 1234;
            print(string_of_int(foo()[2]));
        EndBody.
"""
        expect = r"""3"""
        self.assertTrue(TestCodeGen.test(input,expect,588))
        
    def test_589(self):
        """Created automatically"""
        input = r"""
        Var: arr[5]={1,2,3,4,5};
        Function: func1
        Parameter: x
        Body:
        Return x *x%2;
        EndBody.
        Function: main
        Body:
        Var: a = 1343.74;
        Var: arr[5]={2761,5832,8533,6834,556};
            a =float_to_int(-(-(func1(46)+23) * -func2(a)+arr[3]))\. 0.75;
            print(string_of_float(a));
        EndBody.
        Function: func2
        Parameter: y
        Body:
        Var: z=1543.0;
        Var: i = 0;
        While (i < 5) Do
            z = z +. y;
            i = i + 1;
        EndWhile.
        Return int_of_float(z);
        EndBody."""
        expect = r"""-262449.34"""
        self.assertTrue(TestCodeGen.test(input,expect,589))
        
    def test_590(self):
        """Created automatically"""
        input = r"""
        Function: func2 
        Parameter: n
        Body: 
            If n == 0 Then
                Return 1;
            Else
                Return n * func2 (n - 1);
            EndIf.
        EndBody.
        Function: goo 
        Parameter: n
        Body: ** Xin chao**
        Var: string = "Xin chao";
        print(string);
        Return 108*n;
        EndBody.
        Function: main
        Body:
        Var: a=123;
            a =func1(func2(3))+23 - foo(goo(func1(a)));
            print(string_of_int(a));
        EndBody.
        Function: func1
        Parameter: x
        Body:
        Var: a=0, b=4324, c=8235;
            If((b%15>=7)&&(c%30<=15)) Then
                a = b - c;
            Else
                a = b + c;
            EndIf.
            x = x -a;
            Return x;
        EndBody.
        Function: foo 
        Parameter: n
        Body: 
            While(1) Do
                If n%2==0 Then
                    Break;
                Else
                    n=n\2;
                EndIf.
            EndWhile.
            Return n;
        EndBody.
        """
        expect = r"""Xin chao1330558"""
        self.assertTrue(TestCodeGen.test(input,expect,590))
        
    def test_591(self):
        """Created automatically"""
        input = r"""Function: main
        Body:
            Var: octalNumber = 0o55421;
            Var: decimalNumber = 0, i = 0, rem=0;
            While (octalNumber != 0) Do
                rem = octalNumber % 10;
                octalNumber =octalNumber \ 10;
                decimalNumber =decimalNumber  + rem * pow(8,i);
                i=i+1;
            EndWhile.
            print(string_of_int(decimalNumber));
        EndBody.
        Function: pow
        Parameter: x,y
        Body:
        If x == 0 Then
        Return 1;
        EndIf.
        Return x * pow(x-1,y);
        EndBody."""
        expect = r"""483840"""
        self.assertTrue(TestCodeGen.test(input,expect,591))
        
    def test_592(self):
        """Created automatically"""
        input = r"""
            Function: sqrt
            Parameter: x
            Body:
                Var: i=0;
                While (i*i) < x Do
                    i = i - -1;
                EndWhile.
                Return i-1;
            EndBody.
            Function: main
            Body:
            Var: n=5,x=0;
                Var: i=0;
                For (i = 0, i < sqrt(n), 2) Do
                    x = i + n;
                EndFor.
                print(string_of_int(x));
            EndBody."""
        expect = r"""5"""
        self.assertTrue(TestCodeGen.test(input,expect,592))
        
    def test_593(self):
        """Created automatically"""
        input = r"""
        Var: m =0,i=0;
        Function: main
        Body:
        Var:a=1,b=5645;
            i=1;
            m = test2(a,b);
            i=2;
            m = test2(a,m);
            printStrLn(string_of_int(m));
        EndBody.
        Function: test2
        Parameter: x,y
        Body:
            Do
                If((y%11)%6>=4) Then
                    y=y*x;
                EndIf.
                x=x+1;
            While x<10
            EndDo.
            print("Lap lan ");
            printStrLn(string_of_int(i));
            Return y;
        EndBody."""
        expect = r"""Lap lan 1
Lap lan 2
5645
"""
        self.assertTrue(TestCodeGen.test(input,expect,593))
        
    def test_594(self):
        """Created automatically"""
        input = r"""
        Function: foo
        Body:
            Var: a[4]={1,2,3,4};
            Return a;
        EndBody.
        Function: main
        Body:
            Var: a[4]={1,2,3,4};
            foo()[2] = a[1];
            print(string_of_int(foo()[2]));
        EndBody.
        """
        expect = r"""3"""
        self.assertTrue(TestCodeGen.test(input,expect,594))
        
    def test_595(self):
        """Created automatically"""
        input = r"""
        Function: foo
        Body:
            Var: a[4]={1,2,3,4};
            Return a;
        EndBody.
        Function: main
        Body:
            print(string_of_int(foo()[2]));
        EndBody.
        """
        expect = r"""3"""
        self.assertTrue(TestCodeGen.test(input,expect,595))
        
    def test_596(self):
        """Created automatically"""
        input = r"""** this is a comment **
        Function: foo
        Parameter: a[5], b
        Body:
            Var: i = 0;
            While (i < 5) Do
                a[i] = b +. a[i]*.74.431;
                printStrLn(string_of_float(a[i]));
                i = i + 1;
            EndWhile.
        EndBody.
        Function: main
        Body:
        Var:c[5]={13.4,52.63,25e2,1.3543e-2,5823.35};
        Var: temp = 2344.2;
        foo(c,temp);
        EndBody."""
        expect = r"""3341.5752
6261.504
188421.7
2345.208
435781.97
"""
        self.assertTrue(TestCodeGen.test(input,expect,596))
        
    def test_597(self):
        """Created automatically"""
        input = r"""
        Var: a=1.0;
        Function: main 
        Body:
            a=4325.43674;
            a = a +. 432.57523 -. float_to_int(foo(int_of_float(a)));
            print(string_of_float(a));
        EndBody.
        Function: foo
        Parameter: x
        Body:
        Return x*(x%12)+x\(x%12);
        EndBody."""
        expect = r"""-17731.988"""
        self.assertTrue(TestCodeGen.test(input,expect,597))
        
    def test_598(self):
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
        self.assertTrue(TestCodeGen.test(input,expect,598))
        
    def test_599(self):
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
        expect = r"""10"""
        self.assertTrue(TestCodeGen.test(input,expect,599))
        
    def test_600(self):
        """Created automatically"""
        input = r"""
Function: abs
Parameter: x
Body:
If x>=0 Then
Return x;
Else
Return -x;
EndIf.
EndBody.

Function: ok
Parameter: x2,y2,a[20]
Body:
    Var: i =0;
    For(i = 1, i < x2, 1) Do
        If((a[i] == y2) || (abs(i-x2) == abs(a[i] - y2))) Then
            Return False;
        EndIf.
    EndFor.
    Return True;
EndBody.
 
Function: xuat
Parameter: n,a[20]
Body:
    Var: i=0;
    For(i=1, i<=n, 1) Do
        print(" ");
        print(string_of_int(a[i]));
    EndFor.
    printLn();
EndBody.
 
Function: try
Parameter: i, n,a[20]
Body:
Var: j=0;
    For(j = 1,j<=n,1) Do
        If (ok(i,j,a)) Then
            a[i] = j; 
            If (i==n) Then
                xuat(n,a);
            EndIf.
            try(i+1,n,a);
        EndIf.
    EndFor.
EndBody.
 
    Function: main
    Body:
        Var: a[20]={0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0};
        Var: n=5; 
        try(1,n,a);
    EndBody.
    """
        expect = r""" 1 3 5 2 4
 1 4 2 5 3
 2 4 1 3 5
 2 5 3 1 4
 3 1 4 2 5
 3 5 2 4 1
 4 1 3 5 2
 4 2 5 3 1
 5 2 4 1 3
 5 3 1 4 2
"""
        self.assertTrue(TestCodeGen.test(input,expect,600))
        