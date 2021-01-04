.source MCClass.java
.class public MCClass
.super java.lang.Object

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
.var 1 is a [[I from Label0 to Label1
	iconst_3
	iconst_2
	multianewarray [[I 2
	astore_1
	aload_1
	iconst_0
	aaload
	iconst_0
	iconst_1
	iastore
	aload_1
	iconst_0
	aaload
	iconst_1
	iconst_2
	iastore
	aload_1
	iconst_1
	aaload
	iconst_0
	iconst_3
	iastore
	aload_1
	iconst_1
	aaload
	iconst_1
	iconst_4
	iastore
	aload_1
	iconst_2
	aaload
	iconst_0
	iconst_5
	iastore
	aload_1
	iconst_2
	aaload
	iconst_1
	bipush 6
	iastore
.var 2 is i I from Label0 to Label1
	iconst_0
	istore_2
Label0:
Label6:
	iload_2
	iconst_3
	if_icmpge Label4
	iconst_1
	goto Label5
Label4:
	iconst_0
Label5:
	ifle Label7
.var 3 is j I from Label0 to Label1
	iconst_0
	istore_3
	iload_2
	iload_3
	if_icmpge Label14
	iconst_1
	goto Label15
Label14:
	iconst_0
Label15:
	ifle Label10
	goto Label8
	goto Label11
Label10:
Label11:
Label20:
	iload_3
	iconst_2
	if_icmpge Label18
	iconst_1
	goto Label19
Label18:
	iconst_0
Label19:
	ifle Label21
	aload_1
	iload_2
	aaload
	iload_3
	iaload
	invokestatic io/string_of_int(I)Ljava/lang/String;
	invokestatic io/print(Ljava/lang/String;)V
	iload_3
	iconst_1
	iadd
	istore_3
	iload_3
	iconst_3
	if_icmpne Label28
	iconst_1
	goto Label29
Label28:
	iconst_0
Label29:
	ifle Label24
	goto Label22
	goto Label25
Label24:
Label25:
Label22:
	goto Label20
Label21:
Label23:
	iload_2
	iconst_1
	iadd
	istore_2
Label8:
	goto Label6
Label7:
Label9:
	return
Label1:
.limit stack 21
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
