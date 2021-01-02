import unittest
from TestUtils import TestCodeGen
from AST import *


class CheckCodeGenSuite(unittest.TestCase):
    # Variable Decleration
    def test_600(self):
        """Created automatically"""
        input = r"""
        Var:x="hello";
        Function: main 
        Body:
        print(x);
        EndBody."""
        expect = "hello"
        self.assertTrue(TestCodeGen.test(input,expect,600))

    def test_601(self):
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
        self.assertTrue(TestCodeGen.test(input,expect,601))

    def test_602(self):
        """Created automatically"""
        input = r"""Function: main
                   Body:
                   Var: x = 0x123ABC;
                   Var: y = 0o1234;
                    print(string_of_int(x));
                    print(string_of_int(y));
                   EndBody."""
        expect = r"""1194684668"""
        self.assertTrue(TestCodeGen.test(input,expect,602))

    def test_603(self):
        """Created automatically"""
        input = r"""
        Var:x="hello";
        Function: main 
        Body:
        x="Hello World";
        print(x);
        EndBody."""
        expect = "Hello World"
        self.assertTrue(TestCodeGen.test(input,expect,603))

    def test_604(self):
        """Created automatically"""
        input = r"""Function: main
                   Body:
                   Var: x = 1.234;
                   EndBody."""
        expect = r""""""
        self.assertTrue(TestCodeGen.test(input,expect,604))

    def test_605(self):
        """Created automatically"""
        input = r"""Function: main
                   Body:
                   Var: x = 32.4e-1;
                   EndBody."""
        expect = r""""""
        self.assertTrue(TestCodeGen.test(input,expect,605))

    def test_606(self):
        """Created automatically"""
        input = r"""Function: main
                   Body:
                   Var: x = True;
                   EndBody."""
        expect = r""""""
        self.assertTrue(TestCodeGen.test(input,expect,606))

    def test_607(self):
        """Created automatically"""
        input = r"""Function: main
                   Body:
                   Var: x = "Chung Xon";
                   EndBody."""
        expect = r""""""
        self.assertTrue(TestCodeGen.test(input,expect,607))

    def test_608(self):
        """Created automatically"""
        input = r"""Function: main
                   Body:
                   Var: x = "\tHello moi nguoi @@~!@#$%^&***** \n";
                   EndBody."""
        expect = r""""""
        self.assertTrue(TestCodeGen.test(input,expect,608))

    def test_609(self):
        """Created automatically"""
        input = r"""Function: main
                   Body:
                   Var: x[3] = {1,2,3};
                   EndBody."""
        expect = r""""""
        self.assertTrue(TestCodeGen.test(input,expect,609))

    def test_610(self):
        """Created automatically"""
        input = r"""Function: main
                   Body:
                   Var: x[3] = {1.2,2.3,3.4};
                   EndBody."""
        expect = r""""""
        self.assertTrue(TestCodeGen.test(input,expect,610))

    def test_611(self):
        """Created automatically"""
        input = r"""Function: main
        Body:
            Var: a[3] = {1,2,3}, c[2][3] = {{1,3,5},{3,5,7}};
        EndBody."""
        expect = ""
        self.assertTrue(TestCodeGen.test(input,expect,611))

    def test_612(self):
        """Created automatically"""
        input = r"""Function: main
        Body:
            Var: a[2][2] = {{"a","b"},{"c","d"}}, c[2][3] = {{1e-2,3.5,5.0},{3.1,5e2,7.0e-3}};
        EndBody."""
        expect = ""
        self.assertTrue(TestCodeGen.test(input,expect,612))

    # Built-in functions
    def test_613(self):
        """Created automatically"""
        input = r"""Function: main
                   Body: 
                        print("120");
                   EndBody."""
        expect = r"""120"""
        self.assertTrue(TestCodeGen.test(input,expect,613))

    def test_614(self):
        """Created automatically"""
        input = r"""Function: main
                   Body: 
                        print(string_of_int(120));
                   EndBody."""
        expect = r"""120"""
        self.assertTrue(TestCodeGen.test(input,expect,614))

    def test_615(self):
        """Created automatically"""
        input = r"""Function: main
                   Body:
                   Var: str = 123;
                   print(string_of_int(str));
                   EndBody."""
        expect = r"""123"""
        self.assertTrue(TestCodeGen.test(input,expect,615))
        
    def test_616(self):
        """Created automatically"""
        input = r"""Function: main
                   Body:
                   Var: x = "120";
                   print(x);
                   EndBody."""
        expect = r"""120"""
        self.assertTrue(TestCodeGen.test(input,expect,616))

    def test_617(self):
        """Created automatically"""
        input = r"""Function: main
                   Body:
                   Var: str = 123.2e-1;
                   print(string_of_float(str));
                   EndBody."""
        expect = r"""12.32"""
        self.assertTrue(TestCodeGen.test(input,expect,617))

    def test_618(self):
        """Created automatically"""
        input = r"""Function: main
                   Body:
                   print(string_of_bool(True));
                   EndBody."""
        expect = r"""true"""
        self.assertTrue(TestCodeGen.test(input,expect,618))

    def test_619(self):
        """Created automatically"""
        input = r"""Function: main
                   Body:
                   print("False");
                   EndBody."""
        expect = r"""False"""
        self.assertTrue(TestCodeGen.test(input,expect,619))
        
    def test_620(self):
        """Created automatically"""
        input = r"""Function: main
        Body:
            Var: a[3] = {1,2,3}, c[2][3] = {{1,3,5},{3,5,7}};
            print(string_of_int(c[1][2]));
        EndBody."""
        expect = """7"""
        self.assertTrue(TestCodeGen.test(input,expect,620))
        
    def test_621(self):
        """Created automatically"""
        input = r"""Function: main
                   Body:
                   printStrLn(string_of_int(int_of_float(float_of_string("12.2"))));
                   printLn();
                   print(string_of_float(float_to_int(int_of_float(float_of_string("12.8")))));
                   EndBody."""
        expect = r"""12

12.0"""
        self.assertTrue(TestCodeGen.test(input,expect,621))

    def test_622(self):
        """Created automatically"""
        input = r"""Function: main
        Body:
            print(string_of_bool(!bool_of_string("False")));
        EndBody."""
        expect = "true"
        self.assertTrue(TestCodeGen.test(input,expect,622))
        

    # Assignment and expression
    def test_623(self):
        """Created automatically"""
        input = r"""Function: main
                   Body:
                   Var: str = 123.2e-1;
                   str = 15.6;
                   print(string_of_float(str));
                   EndBody."""
        expect = r"""15.6"""
        self.assertTrue(TestCodeGen.test(input,expect,623))

    def test_624(self):
        """Created automatically"""
        input = r"""Function: main
                   Body:
                   print(string_of_int(1+2));
                   EndBody."""
        expect = r"""3"""
        self.assertTrue(TestCodeGen.test(input,expect,624))
        
    def test_625(self):
        """Created automatically"""
        input = r"""
        Function: main 
        Body:
        Var:x[3]={"1","2","3"};
        print(x[1]);
        EndBody."""
        expect = r"""2"""
        self.assertTrue(TestCodeGen.test(input,expect,625))
        
    def test_626(self):
        """Created automatically"""
        input = r"""Function: main
                   Body:
                   print(string_of_float(3.0\.2.0));
                   EndBody."""
        expect = r"""1.5"""
        self.assertTrue(TestCodeGen.test(input,expect,626))
        
    def test_627(self):
        """Created automatically"""
        input = r"""Function: main
                   Body:
                   print(string_of_bool(1<2));
                   EndBody."""
        expect = r"""true"""
        self.assertTrue(TestCodeGen.test(input,expect,627))
        
    def test_628(self):
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
        expect = "true"
        self.assertTrue(TestCodeGen.test(input,expect,628))
        
    def test_629(self):
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
        self.assertTrue(TestCodeGen.test(input,expect,629))

    def test_630(self):
        """Created automatically"""
        input = r"""Function: main
        Body:
        Var: x = False, a = 1.e-2, b = 20; 
            x = ((a <=. 2.3e-13) || (b == 21) || (b != 235));
            print(string_of_bool(x));
        EndBody."""
        expect = "true"
        self.assertTrue(TestCodeGen.test(input,expect,630))
        
    def test_631(self):
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
        expect = "2623"
        self.assertTrue(TestCodeGen.test(input,expect,631))

    def test_632(self):
        """Created automatically"""
        input = r"""Function: main
                   Body:
                   print(string_of_int(2*2));
                   EndBody."""
        expect = r"""4"""
        self.assertTrue(TestCodeGen.test(input,expect,632))
        
    # If stmt
    def test_633(self):
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
        self.assertTrue(TestCodeGen.test(input,expect,633))
        
    def test_634(self):
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
        self.assertTrue(TestCodeGen.test(input,expect,634))
        
    def test_635(self):
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
        self.assertTrue(TestCodeGen.test(input,expect,635))

    def test_636(self):
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
        self.assertTrue(TestCodeGen.test(input,expect,636))
        

    def test_637(self):
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
        expect = "19.056602"
        self.assertTrue(TestCodeGen.test(input,expect,637))

    def test_638(self):
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
        expect = "3.3"
        self.assertTrue(TestCodeGen.test(input,expect,638))
        

    def test_639(self):
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
        expect = "100.0"
        self.assertTrue(TestCodeGen.test(input,expect,639))
        
    def test_640(self):
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
        expect = "23.207546"
        self.assertTrue(TestCodeGen.test(input,expect,640))
        
    def test_641(self):
        """Created automatically"""
        input = r"""Function: main 
        Body:
        Var: k=0,i=0,j=False,f=11;
            If ((k<1)&&(i!=0))||(k>5)||!j Then
                f=f%3;
            EndIf.
            print(string_of_int(f));
        EndBody."""
        expect = "2"
        self.assertTrue(TestCodeGen.test(input,expect,641))

    def test_642(self):
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
        self.assertTrue(TestCodeGen.test(input,expect,642))
        

    def test_643(self):
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
        expect = "4"
        self.assertTrue(TestCodeGen.test(input,expect,643))
        
    def test_644(self):
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
        self.assertTrue(TestCodeGen.test(input,expect,644))

    def test_645(self):
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
        self.assertTrue(TestCodeGen.test(input,expect,645))
        
    # While Stmt
    def test_646(self):
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
        expect = "12131415283032344851"
        self.assertTrue(TestCodeGen.test(input,expect,646))

    def test_647(self):
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
        expect = ""
        self.assertTrue(TestCodeGen.test(input,expect,647))

    def test_648(self):
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
        self.assertTrue(TestCodeGen.test(input,expect,648))
        
    def test_649(self):
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
        expect = "-1.0"
        self.assertTrue(TestCodeGen.test(input,expect,649))
        
    def test_650(self):
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
        self.assertTrue(TestCodeGen.test(input,expect,650))

    def test_651(self):
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
        self.assertTrue(TestCodeGen.test(input,expect,651))
        
    def test_652(self):
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
        self.assertTrue(TestCodeGen.test(input,expect,652))
        
    def test_653(self):
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
        expect = "123"
        self.assertTrue(TestCodeGen.test(input,expect,652))

    def test_654(self):
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
        expect = "1162.7"
        self.assertTrue(TestCodeGen.test(input,expect,654))
        
    # DoWhile Stmt
    def test_655(self):
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
        self.assertTrue(TestCodeGen.test(input,expect,655))
        
    def test_656(self):
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
        self.assertTrue(TestCodeGen.test(input,expect,656))
        

    def test_657(self):
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
        self.assertTrue(TestCodeGen.test(input,expect,657))
        
    def test_658(self):
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
        expect = "0012043210"
        self.assertTrue(TestCodeGen.test(input,expect,658))

    # For Stmt
    def test_659(self):
        """Created automatically"""
        input = r"""Function: main
                    Body:
                    Var: i = 0;
                    For (i = 0, i < 10, 2) Do
                        print(string_of_int(i));
                    EndFor.
                    EndBody."""
        expect = r"""02468"""
        self.assertTrue(TestCodeGen.test(input,expect,659))
         
    def test_660(self):
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
        self.assertTrue(TestCodeGen.test(input,expect,660))
        
    def test_661(self):
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
        expect = "1234"
        self.assertTrue(TestCodeGen.test(input,expect,661))
        
    def test_662(self):
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
        self.assertTrue(TestCodeGen.test(input,expect,662))

    def test_663(self):
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
        expect = "21"
        self.assertTrue(TestCodeGen.test(input,expect,663))

    def test_664(self):
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
        self.assertTrue(TestCodeGen.test(input,expect,664))
        
    def test_665(self):
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
        self.assertTrue(TestCodeGen.test(input,expect,665))

    def test_666(self):
        """Simple program: main"""
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
        self.assertTrue(TestCodeGen.test(input,expect,666))

    # Multi Stmt
    def test_667(self):
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
        self.assertTrue(TestCodeGen.test(input,expect,667))

    def test_668(self):
        """Created automatically"""
        input = r"""Function: main
        Body:
        Var:i=0;
            For (i=1, i%15!=9, (i*20)) Do
            EndFor.
            print(string_of_int(i));
        EndBody."""
        expect = r"""547383789"""
        self.assertTrue(TestCodeGen.test(input,expect,668))
          
    def test_669(self):
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
        expect = "10"
        self.assertTrue(TestCodeGen.test(input,expect,669))

    def test_670(self):
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
        expect = "false"
        self.assertTrue(TestCodeGen.test(input,expect,670))

    def test_671(self):
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
        self.assertTrue(TestCodeGen.test(input,expect,671))

    def test_672(self):
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
        self.assertTrue(TestCodeGen.test(input,expect,672))

    def test_673(self):
        """Created automatically"""
        input = r"""Function: main
                    Body:
                    Var: i=0, result=0,x=9;
                        For (i = 1, i <= x*x*x,i + x ) Do
                            result = i * i + i \ --1 % i--i;
                        EndFor.
                        print(string_of_int(result));
                    EndBody."""
        expect = "398792"
        self.assertTrue(TestCodeGen.test(input,expect,673))

    def test_674(self):
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
        expect = "-20"
        self.assertTrue(TestCodeGen.test(input,expect,674))

    def test_675(self):
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
        expect = "15"
        self.assertTrue(TestCodeGen.test(input,expect,675))

    def test_676(self):
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
        self.assertTrue(TestCodeGen.test(input,expect,676))
        
    def test_677(self):
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
        expect = "97531"
        self.assertTrue(TestCodeGen.test(input,expect,677))

    # Multi Function
    def test_678(self):
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
        self.assertTrue(TestCodeGen.test(input,expect,678))
        
    def test_679(self):
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
        expect = "3628800"
        self.assertTrue(TestCodeGen.test(input,expect,679))
        
    def test_680(self):
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
        self.assertTrue(TestCodeGen.test(input,expect,680))
    
    def test_681(self):
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
        expect = "-8933-10820001082000"
        self.assertTrue(TestCodeGen.test(input,expect,681))
        
    def test_682(self):
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
        expect = "false"
        self.assertTrue(TestCodeGen.test(input,expect,682))
        
    def test_683(self):
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
        expect = "3293"
        self.assertTrue(TestCodeGen.test(input,expect,683))
        
    def test_684(self):
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
        expect = "3"
        self.assertTrue(TestCodeGen.test(input,expect,684))
        
    def test_685(self):
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
        self.assertTrue(TestCodeGen.test(input,expect,685))
        
    def test_686(self):
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
        expect = "1"
        self.assertTrue(TestCodeGen.test(input,expect,686))
        
    def test_687(self):
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
        expect = "3"
        self.assertTrue(TestCodeGen.test(input,expect,687))
          
    def test_688(self):
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
        expect = "-262449.34"
        self.assertTrue(TestCodeGen.test(input,expect,688))
        
        
    def test_689(self):
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
        expect = "Xin chao1330558"
        self.assertTrue(TestCodeGen.test(input,expect,689))
        
    def test_690(self):
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
        expect = "483840"
        self.assertTrue(TestCodeGen.test(input,expect,690))

    def test_691(self):
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
        expect = "5"
        self.assertTrue(TestCodeGen.test(input,expect,691))

    def test_692(self):
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
        self.assertTrue(TestCodeGen.test(input,expect,692))
        
    def test_693(self):
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
        expect = "3"
        self.assertTrue(TestCodeGen.test(input,expect,693))
        
    def test_694(self):
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
        expect = "3"
        self.assertTrue(TestCodeGen.test(input,expect,694))
      
    def test_695(self):
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
        self.assertTrue(TestCodeGen.test(input,expect,695))

    def test_696(self):
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
        expect = "-17731.988"
        self.assertTrue(TestCodeGen.test(input,expect,696))
        
    def test_697(self):
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
        self.assertTrue(TestCodeGen.test(input,expect,697))
        
    def test_698(self):
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
        self.assertTrue(TestCodeGen.test(input,expect,698))
           
    def test_699(self):
        """Simple program: main"""
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
        self.assertTrue(TestCodeGen.test(input,expect,699))