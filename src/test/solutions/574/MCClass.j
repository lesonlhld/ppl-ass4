.source MCClass.java
.class public MCClass
.super java.lang.Object

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
.var 1 is i I from Label0 to Label1
	iconst_0
	istore_1
.var 2 is result I from Label0 to Label1
	iconst_0
	istore_2
.var 3 is x I from Label0 to Label1
	bipush 9
	istore_3
Label0:
	iconst_1
	istore_1
Label2:
	iload_1
	iload_3
	iload_3
	imul
	iload_3
	imul
	if_icmpgt Label6
	iconst_1
	goto Label7
Label6:
	iconst_0
Label7:
	ifle Label3
	iload_1
	iload_1
	imul
	iload_1
	iconst_1
	ineg
	ineg
	idiv
	iload_1
	irem
	iadd
	iload_1
	ineg
	isub
	istore_2
Label4:
	iload_1
	iload_1
	iload_3
	iadd
	iadd
	istore_1
	goto Label2
Label3:
Label5:
	iload_2
	invokestatic io/string_of_int(I)Ljava/lang/String;
	invokestatic io/print(Ljava/lang/String;)V
Label1:
	return
.limit stack 9
.limit locals 4
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
