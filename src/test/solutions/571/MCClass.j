.source MCClass.java
.class public MCClass
.super java.lang.Object

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
.var 1 is i I from Label0 to Label1
	iconst_0
	istore_1
.var 2 is c Z from Label0 to Label1
	iconst_1
	istore_2
Label0:
Label6:
	iload_1
	sipush 423
	if_icmpgt Label4
	iconst_1
	goto Label5
Label4:
	iconst_0
Label5:
	ifle Label7
.var 3 is b Z from Label0 to Label1
	iconst_1
	istore_3
.var 4 is a Z from Label0 to Label1
	iconst_0
	istore 4
	iload_1
	bipush 100
	if_icmpge Label12
	iconst_1
	goto Label13
Label12:
	iconst_0
Label13:
	istore_3
	iload_3
	ifle Label14
	iconst_1
	iload_2
	iand
	goto Label15
Label14:
	iconst_0
Label15:
	ifgt Label16
	iconst_1
	goto Label17
Label16:
	iconst_0
Label17:
	ifgt Label22
	iconst_0
	iload 4
	ifle Label18
	iconst_1
	iload_3
	iand
	goto Label19
Label18:
	iconst_0
Label19:
	ifgt Label20
	iconst_1
	goto Label21
Label20:
	iconst_0
Label21:
	ior
	goto Label23
Label22:
	iconst_1
Label23:
	ifle Label28
	iconst_1
	iload_1
	iconst_1
	iadd
	sipush 234
	if_icmpne Label26
	iconst_1
	goto Label27
Label26:
	iconst_0
Label27:
	iand
	goto Label29
Label28:
	iconst_0
Label29:
	istore 4
	iload_1
	iconst_3
	iadd
	istore_1
	iload_1
	sipush 212
	if_icmpne Label34
	iconst_1
	goto Label35
Label34:
	iconst_0
Label35:
	ifle Label30
	goto Label9
	goto Label31
Label30:
Label31:
	iload 4
	istore_2
Label8:
	goto Label6
Label7:
Label9:
	iload_2
	invokestatic io/string_of_bool(Z)Ljava/lang/String;
	invokestatic io/print(Ljava/lang/String;)V
Label1:
	return
.limit stack 27
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
