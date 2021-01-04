.source MCClass.java
.class public MCClass
.super java.lang.Object

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
.var 1 is char Ljava/lang/String; from Label0 to Label1
	ldc "*"
	astore_1
.var 2 is n I from Label0 to Label1
	bipush 11
	istore_2
.var 3 is i I from Label0 to Label1
	iconst_0
	istore_3
.var 4 is j I from Label0 to Label1
	iconst_0
	istore 4
Label0:
	iconst_0
	istore_3
Label2:
	iload_3
	iload_2
	if_icmpge Label8
	iconst_1
	goto Label9
Label8:
	iconst_0
Label9:
	ifle Label3
	invokestatic io/printLn()V
	iload_2
	iconst_2
	idiv
	iload_3
	if_icmpge Label14
	iconst_1
	goto Label15
Label14:
	iconst_0
Label15:
	ifle Label10
	iconst_0
	istore 4
Label16:
	iload 4
	iload_2
	iconst_2
	idiv
	if_icmpge Label22
	iconst_1
	goto Label23
Label22:
	iconst_0
Label23:
	ifle Label17
	ldc " "
	invokestatic io/print(Ljava/lang/String;)V
Label18:
	iload 4
	iconst_1
	iadd
	istore 4
	goto Label16
Label17:
Label19:
	aload_1
	invokestatic io/print(Ljava/lang/String;)V
	goto Label11
Label10:
	iconst_0
	istore 4
Label24:
	iload 4
	iload_2
	iconst_2
	idiv
	iload_3
	isub
	if_icmpge Label30
	iconst_1
	goto Label31
Label30:
	iconst_0
Label31:
	ifle Label25
	ldc " "
	invokestatic io/print(Ljava/lang/String;)V
Label26:
	iload 4
	iconst_1
	iadd
	istore 4
	goto Label24
Label25:
Label27:
	iconst_0
	istore 4
Label32:
	iload 4
	iload_2
	iload_2
	iconst_2
	idiv
	iload_3
	isub
	iconst_2
	imul
	isub
	if_icmpge Label38
	iconst_1
	goto Label39
Label38:
	iconst_0
Label39:
	ifle Label33
	aload_1
	invokestatic io/print(Ljava/lang/String;)V
Label34:
	iload 4
	iconst_1
	iadd
	istore 4
	goto Label32
Label33:
Label35:
Label11:
Label4:
	iload_3
	iconst_1
	iadd
	istore_3
	goto Label2
Label3:
Label5:
Label1:
	return
.limit stack 21
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
