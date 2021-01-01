.source MCClass.java
.class public MCClass
.super java.lang.Object

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
.var 1 is x I from Label0 to Label1
	bipush 100
	istore_1
Label0:
Label4:
	iload_1
	iconst_1
	if_icmple Label2
	iconst_1
	goto Label3
Label2:
	iconst_0
Label3:
	ifle Label5
.var 2 is i I from Label0 to Label1
	iconst_0
	istore_2
.var 3 is a I from Label0 to Label1
	bipush 10
	istore_3
	bipush 100
	istore_2
Label8:
	iconst_1
	ifle Label9
	iload_3
	ineg
	iconst_3
	ineg
	if_icmple Label14
	iconst_1
	goto Label15
Label14:
	iconst_0
Label15:
	ifle Label12
	goto Label11
	goto Label13
Label12:
Label13:
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
Label10:
	iload_2
	iload_2
	bipush 6
	isub
	ineg
	iadd
	istore_2
	goto Label8
Label9:
Label11:
Label6:
	goto Label4
Label5:
Label7:
	iload_1
	invokestatic io/string_of_int(I)Ljava/lang/String;
	invokestatic io/print(Ljava/lang/String;)V
Label1:
	return
.limit stack 13
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
