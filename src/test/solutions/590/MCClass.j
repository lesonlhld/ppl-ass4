.source MCClass.java
.class public MCClass
.super java.lang.Object

.method public static func2(I)I
.var 0 is n I from Label0 to Label1
Label0:
	iload_0
	iconst_0
	if_icmpne Label4
	iconst_1
	goto Label5
Label4:
	iconst_0
Label5:
	ifle Label2
	iconst_1
	ireturn
Label2:
	iload_0
	iload_0
	iconst_1
	isub
	invokestatic MCClass/func2(I)I
	imul
	ireturn
Label3:
Label1:
	return
.limit stack 6
.limit locals 1
.end method

.method public static goo(I)I
.var 0 is n I from Label0 to Label1
.var 1 is string Ljava/lang/String; from Label0 to Label1
	ldc "Xin chao"
	astore_1
Label0:
	aload_1
	invokestatic io/print(Ljava/lang/String;)V
	bipush 108
	iload_0
	imul
	ireturn
Label1:
.limit stack 4
.limit locals 2
.end method

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
.var 1 is a I from Label0 to Label1
	bipush 123
	istore_1
Label0:
	iconst_3
	invokestatic MCClass/func2(I)I
	invokestatic MCClass/func1(I)I
	bipush 23
	iadd
	iload_1
	invokestatic MCClass/func1(I)I
	invokestatic MCClass/goo(I)I
	invokestatic MCClass/foo(I)I
	isub
	istore_1
	iload_1
	invokestatic io/string_of_int(I)Ljava/lang/String;
	invokestatic io/print(Ljava/lang/String;)V
Label1:
	return
.limit stack 4
.limit locals 2
.end method

.method public static func1(I)I
.var 0 is x I from Label0 to Label1
.var 1 is a I from Label0 to Label1
	iconst_0
	istore_1
.var 2 is b I from Label0 to Label1
	sipush 4324
	istore_2
.var 3 is c I from Label0 to Label1
	sipush 8235
	istore_3
Label0:
	iload_2
	bipush 15
	irem
	bipush 7
	if_icmplt Label4
	iconst_1
	goto Label5
Label4:
	iconst_0
Label5:
	iload_3
	bipush 30
	irem
	bipush 15
	if_icmpgt Label6
	iconst_1
	goto Label7
Label6:
	iconst_0
Label7:
	iand
	ifle Label2
	iload_2
	iload_3
	isub
	istore_1
	goto Label3
Label2:
	iload_2
	iload_3
	iadd
	istore_1
Label3:
	iload_0
	iload_1
	isub
	istore_0
	iload_0
	ireturn
Label1:
.limit stack 12
.limit locals 4
.end method

.method public static foo(I)I
.var 0 is n I from Label0 to Label1
Label0:
Label2:
	iconst_1
	ifle Label3
	iload_0
	iconst_2
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
	iload_0
	iconst_2
	idiv
	istore_0
Label7:
Label4:
	goto Label2
Label3:
Label5:
	iload_0
	ireturn
Label1:
.limit stack 5
.limit locals 1
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
