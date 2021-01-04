.source MCClass.java
.class public MCClass
.super java.lang.Object

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
.var 1 is x [[I from Label0 to Label1
	iconst_3
	iconst_2
	multianewarray [[I 2
	astore_1
	aload_1
	iconst_0
	aaload
	iconst_0
	sipush 212
	iastore
	aload_1
	iconst_0
	aaload
	iconst_1
	sipush 529
	iastore
	aload_1
	iconst_1
	aaload
	iconst_0
	sipush 272
	iastore
	aload_1
	iconst_1
	aaload
	iconst_1
	sipush 398
	iastore
	aload_1
	iconst_2
	aaload
	iconst_0
	sipush 247
	iastore
	aload_1
	iconst_2
	aaload
	iconst_1
	sipush 954
	iastore
.var 2 is y [[I from Label0 to Label1
	iconst_3
	iconst_2
	multianewarray [[I 2
	astore_2
	aload_2
	iconst_0
	aaload
	iconst_0
	sipush 652
	iastore
	aload_2
	iconst_0
	aaload
	iconst_1
	sipush 654
	iastore
	aload_2
	iconst_1
	aaload
	iconst_0
	sipush 256
	iastore
	aload_2
	iconst_1
	aaload
	iconst_1
	sipush 214
	iastore
	aload_2
	iconst_2
	aaload
	iconst_0
	sipush 158
	iastore
	aload_2
	iconst_2
	aaload
	iconst_1
	sipush 765
	iastore
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
	iconst_3
	if_icmpge Label8
	iconst_1
	goto Label9
Label8:
	iconst_0
Label9:
	ifle Label3
	iconst_0
	istore 4
Label10:
	iload 4
	iconst_2
	if_icmpge Label16
	iconst_1
	goto Label17
Label16:
	iconst_0
Label17:
	ifle Label11
	aload_1
	iload_3
	aaload
	iload 4
	iaload
	aload_2
	iload_3
	aaload
	iload 4
	iaload
	iadd
	invokestatic io/string_of_int(I)Ljava/lang/String;
	invokestatic io/print(Ljava/lang/String;)V
	ldc " "
	invokestatic io/print(Ljava/lang/String;)V
Label12:
	iload 4
	iconst_1
	iadd
	istore 4
	goto Label10
Label11:
Label13:
	invokestatic io/printLn()V
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
