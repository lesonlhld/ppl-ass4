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
	if_icmpge Label6
	iconst_1
	goto Label7
Label6:
	iconst_0
Label7:
	ifle Label3
	invokestatic io/printLn()V
	iload_2
	iconst_2
	idiv
	iload_3
	if_icmpge Label10
	iconst_1
	goto Label11
Label10:
	iconst_0
Label11:
	ifle Label8
	iconst_0
	istore 4
Label12:
	iload 4
	iload_2
	iconst_2
	idiv
	if_icmpge Label16
	iconst_1
	goto Label17
Label16:
	iconst_0
Label17:
	ifle Label13
	ldc " "
	invokestatic io/print(Ljava/lang/String;)V
Label14:
	iload 4
	iconst_1
	iadd
	istore 4
	goto Label12
Label13:
Label15:
	aload_1
	invokestatic io/print(Ljava/lang/String;)V
	goto Label9
Label8:
	iconst_0
	istore 4
Label18:
	iload 4
	iload_2
	iconst_2
	idiv
	iload_3
	isub
	if_icmpge Label22
	iconst_1
	goto Label23
Label22:
	iconst_0
Label23:
	ifle Label19
	ldc " "
	invokestatic io/print(Ljava/lang/String;)V
Label20:
	iload 4
	iconst_1
	iadd
	istore 4
	goto Label18
Label19:
Label21:
	iconst_0
	istore 4
Label24:
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
	if_icmpge Label28
	iconst_1
	goto Label29
Label28:
	iconst_0
Label29:
	ifle Label25
	aload_1
	invokestatic io/print(Ljava/lang/String;)V
Label26:
	iload 4
	iconst_1
	iadd
	istore 4
	goto Label24
Label25:
Label27:
Label9:
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
