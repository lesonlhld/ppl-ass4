.source MCClass.java
.class public MCClass
.super java.lang.Object

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
.var 1 is x [[I from Label0 to Label1
	iconst_3
	iconst_3
	multianewarray [[I 2
	astore_1
	aload_1
	iconst_0
	aaload
	iconst_0
	bipush 114
	iastore
	aload_1
	iconst_0
	aaload
	iconst_1
	sipush 834
	iastore
	aload_1
	iconst_0
	aaload
	iconst_2
	sipush 217
	iastore
	aload_1
	iconst_1
	aaload
	iconst_0
	sipush 568
	iastore
	aload_1
	iconst_1
	aaload
	iconst_1
	sipush 471
	iastore
	aload_1
	iconst_1
	aaload
	iconst_2
	sipush 651
	iastore
	aload_1
	iconst_2
	aaload
	iconst_0
	sipush 831
	iastore
	aload_1
	iconst_2
	aaload
	iconst_1
	sipush 246
	iastore
	aload_1
	iconst_2
	aaload
	iconst_2
	bipush 123
	iastore
.var 2 is i I from Label0 to Label1
	iconst_0
	istore_2
Label0:
Label4:
	iload_2
	iconst_3
	if_icmpge Label2
	iconst_1
	goto Label3
Label2:
	iconst_0
Label3:
	ifle Label5
.var 3 is j I from Label0 to Label1
	iconst_0
	istore_3
Label8:
	aload_1
	iload_2
	aaload
	iload_3
	iaload
	invokestatic io/string_of_int(I)Ljava/lang/String;
	invokestatic io/print(Ljava/lang/String;)V
	ldc " "
	invokestatic io/print(Ljava/lang/String;)V
	iload_3
	iconst_1
	iadd
	istore_3
	iload_3
	iconst_3
	if_icmpge Label12
	iconst_1
	goto Label13
Label12:
	iconst_0
Label13:
	ifle Label9
	goto Label8
Label9:
Label11:
	invokestatic io/printLn()V
	iload_2
	iconst_1
	iadd
	istore_2
Label6:
	goto Label4
Label5:
Label7:
Label1:
	return
.limit stack 20
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
