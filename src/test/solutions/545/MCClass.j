.source MCClass.java
.class public MCClass
.super java.lang.Object

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
.var 1 is n I from Label0 to Label1
	bipush 120
	istore_1
.var 2 is array [[I from Label0 to Label1
	iconst_2
	iconst_3
	multianewarray [[I 2
	astore_2
	aload_2
	iconst_0
	aaload
	iconst_0
	sipush 867
	iastore
	aload_2
	iconst_0
	aaload
	iconst_1
	sipush 345
	iastore
	aload_2
	iconst_0
	aaload
	iconst_2
	sipush 987
	iastore
	aload_2
	iconst_1
	aaload
	iconst_0
	bipush 76
	iastore
	aload_2
	iconst_1
	aaload
	iconst_1
	bipush 12
	iastore
	aload_2
	iconst_1
	aaload
	iconst_2
	sipush 744
	iastore
Label0:
	iload_1
	bipush 10
	if_icmple Label4
	iconst_1
	goto Label5
Label4:
	iconst_0
Label5:
	ifle Label2
	iload_1
	bipush 11
	irem
	bipush 10
	if_icmpge Label8
	iconst_1
	goto Label9
Label8:
	iconst_0
Label9:
	ifle Label6
	iload_1
	iload_1
	imul
	bipush 9
	irem
	istore_1
	goto Label7
Label6:
Label7:
	iload_1
	invokestatic io/string_of_int(I)Ljava/lang/String;
	invokestatic io/printStrLn(Ljava/lang/String;)V
	goto Label3
Label2:
Label3:
Label1:
	return
.limit stack 15
.limit locals 3
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
