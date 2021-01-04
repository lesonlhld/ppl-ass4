.source MCClass.java
.class public MCClass
.super java.lang.Object

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
.var 1 is x I from Label0 to Label1
	bipush 100
	istore_1
Label0:
Label6:
	iload_1
	iconst_1
	if_icmple Label4
	iconst_1
	goto Label5
Label4:
	iconst_0
Label5:
	ifle Label7
.var 2 is i I from Label0 to Label1
	iconst_0
	istore_2
.var 3 is a I from Label0 to Label1
	bipush 10
	istore_3
	bipush 100
	istore_2
Label10:
	iconst_1
	ifle Label11
	iload_3
	ineg
	iconst_3
	ineg
	if_icmple Label18
	iconst_1
	goto Label19
Label18:
	iconst_0
Label19:
	ifle Label14
	goto Label13
	goto Label15
Label14:
Label15:
	iload_3
	iconst_3
	isub
	istore_3
	iload_1
	iload_3
	bipush 10
	imul
	isub
	istore_1
Label12:
	iload_2
	iload_2
	bipush 6
	isub
	ineg
	iadd
	istore_2
	goto Label10
Label11:
Label13:
Label8:
	goto Label6
Label7:
Label9:
	iload_1
	invokestatic io/string_of_int(I)Ljava/lang/String;
	invokestatic io/print(Ljava/lang/String;)V
Label1:
	return
.limit stack 11
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
