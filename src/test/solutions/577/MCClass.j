.source MCClass.java
.class public MCClass
.super java.lang.Object

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
.var 1 is x I from Label0 to Label1
	iconst_0
	istore_1
.var 2 is y I from Label0 to Label1
	iconst_1
	istore_2
.var 3 is j I from Label0 to Label1
	iconst_0
	istore_3
.var 4 is i I from Label0 to Label1
	iconst_0
	istore 4
Label0:
	iconst_0
	istore 4
Label2:
	iconst_1
	ifle Label3
	iload_2
	iload 4
	iadd
	istore_1
	iload_2
	iconst_1
	iadd
	istore_2
	iload 4
	iconst_1
	iadd
	iconst_3
	irem
	iconst_0
	if_icmpne Label8
	iconst_1
	goto Label9
Label8:
	iconst_0
Label9:
	ifle Label6
	goto Label5
	goto Label7
Label6:
Label7:
Label4:
	iload 4
	bipush 123
	iadd
	istore 4
	goto Label2
Label3:
Label5:
	iload_1
	iload_2
	iadd
	invokestatic io/string_of_int(I)Ljava/lang/String;
	invokestatic io/printStrLn(Ljava/lang/String;)V
Label1:
	return
.limit stack 13
.limit locals 5
.end method

.method public <init>()V
.var 0 is this LMCClass; from Label0 to Label1
Label0:
	aload_0
	invokespecial java/lang/Object/<init>()V
Label1:
	return
.limit stack 1
.limit locals 1
.end method
