.source MCClass.java
.class public MCClass
.super java.lang.Object

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
.var 1 is x [[I from Label0 to Label1
	iconst_3
	anewarray [I
	dup
	iconst_0
	iconst_3
	newarray int
	dup
	iconst_0
	bipush 114
	iastore
	dup
	iconst_1
	sipush 834
	iastore
	dup
	iconst_2
	sipush 217
	iastore
	aastore
	dup
	iconst_1
	iconst_3
	newarray int
	dup
	iconst_0
	sipush 568
	iastore
	dup
	iconst_1
	sipush 471
	iastore
	dup
	iconst_2
	sipush 651
	iastore
	aastore
	dup
	iconst_2
	iconst_3
	newarray int
	dup
	iconst_0
	sipush 831
	iastore
	dup
	iconst_1
	sipush 246
	iastore
	dup
	iconst_2
	bipush 123
	iastore
	aastore
	astore_1
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
Label10:
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
	if_icmpge Label16
	iconst_1
	goto Label17
Label16:
	iconst_0
Label17:
	ifle Label11
	goto Label10
Label11:
Label13:
	invokestatic io/printLn()V
	iload_2
	iconst_1
	iadd
	istore_2
Label8:
	goto Label6
Label7:
Label9:
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
