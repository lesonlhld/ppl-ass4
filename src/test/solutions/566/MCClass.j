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
	iconst_2
	newarray int
	dup
	iconst_0
	sipush 212
	iastore
	dup
	iconst_1
	sipush 529
	iastore
	aastore
	dup
	iconst_1
	iconst_2
	newarray int
	dup
	iconst_0
	sipush 272
	iastore
	dup
	iconst_1
	sipush 398
	iastore
	aastore
	dup
	iconst_2
	iconst_2
	newarray int
	dup
	iconst_0
	sipush 247
	iastore
	dup
	iconst_1
	sipush 954
	iastore
	aastore
	astore_1
.var 2 is y [[I from Label0 to Label1
	iconst_3
	anewarray [I
	dup
	iconst_0
	iconst_2
	newarray int
	dup
	iconst_0
	sipush 652
	iastore
	dup
	iconst_1
	sipush 654
	iastore
	aastore
	dup
	iconst_1
	iconst_2
	newarray int
	dup
	iconst_0
	sipush 256
	iastore
	dup
	iconst_1
	sipush 214
	iastore
	aastore
	dup
	iconst_2
	iconst_2
	newarray int
	dup
	iconst_0
	sipush 158
	iastore
	dup
	iconst_1
	sipush 765
	iastore
	aastore
	astore_2
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
.limit stack 29
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
