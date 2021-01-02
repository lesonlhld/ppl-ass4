.source MCClass.java
.class public MCClass
.super java.lang.Object

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
.var 1 is octalNumber I from Label0 to Label1
	sipush 23313
	istore_1
.var 2 is decimalNumber I from Label0 to Label1
	iconst_0
	istore_2
.var 3 is i I from Label0 to Label1
	iconst_0
	istore_3
.var 4 is rem I from Label0 to Label1
	iconst_0
	istore 4
Label0:
Label4:
	iload_1
	iconst_0
	if_icmpeq Label2
	iconst_1
	goto Label3
Label2:
	iconst_0
Label3:
	ifle Label5
	iload_1
	bipush 10
	irem
	istore 4
	iload_1
	bipush 10
	idiv
	istore_1
	iload_2
	iload 4
	bipush 8
	iload_3
	invokestatic MCClass/pow(II)I
	imul
	iadd
	istore_2
	iload_3
	iconst_1
	iadd
	istore_3
Label6:
	goto Label4
Label5:
Label7:
	iload_2
	invokestatic io/string_of_int(I)Ljava/lang/String;
	invokestatic io/print(Ljava/lang/String;)V
Label1:
	return
.limit stack 13
.limit locals 5
.end method

.method public static pow(II)I
.var 0 is x I from Label0 to Label1
.var 1 is y I from Label0 to Label1
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
Label3:
	iload_0
	iload_0
	iconst_1
	isub
	iload_1
	invokestatic MCClass/pow(II)I
	imul
	ireturn
Label1:
.limit stack 6
.limit locals 2
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
