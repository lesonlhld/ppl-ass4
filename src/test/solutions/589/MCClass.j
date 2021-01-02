.source MCClass.java
.class public MCClass
.super java.lang.Object
.field static arr [I

.method public static func1(I)I
.var 0 is x I from Label0 to Label1
Label0:
	iload_0
	iload_0
	imul
	iconst_2
	irem
	ireturn
Label1:
.limit stack 3
.limit locals 1
.end method

.method public static main([Ljava/lang/String;)V
	iconst_5
	newarray int
	putstatic MCClass/arr [I
	getstatic MCClass/arr [I
	iconst_0
	iconst_1
	iastore
	getstatic MCClass/arr [I
	iconst_1
	iconst_2
	iastore
	getstatic MCClass/arr [I
	iconst_2
	iconst_3
	iastore
	getstatic MCClass/arr [I
	iconst_3
	iconst_4
	iastore
	getstatic MCClass/arr [I
	iconst_4
	iconst_5
	iastore
.var 0 is args [Ljava/lang/String; from Label0 to Label1
.var 1 is a F from Label0 to Label1
	ldc 1343.74
	fstore_1
.var 2 is arr [I from Label0 to Label1
	iconst_5
	newarray int
	astore_2
	aload_2
	iconst_0
	sipush 2761
	iastore
	aload_2
	iconst_1
	sipush 5832
	iastore
	aload_2
	iconst_2
	sipush 8533
	iastore
	aload_2
	iconst_3
	sipush 6834
	iastore
	aload_2
	iconst_4
	sipush 556
	iastore
Label0:
	bipush 46
	invokestatic MCClass/func1(I)I
	bipush 23
	iadd
	ineg
	fload_1
	invokestatic MCClass/func2(F)I
	ineg
	imul
	aload_2
	iconst_3
	iaload
	iadd
	ineg
	invokestatic io/float_to_int(I)F
	ldc 0.75
	fdiv
	fstore_1
	fload_1
	invokestatic io/string_of_float(F)Ljava/lang/String;
	invokestatic io/print(Ljava/lang/String;)V
Label1:
	return
.limit stack 10
.limit locals 3
.end method

.method public static func2(F)I
.var 0 is y F from Label0 to Label1
.var 1 is z F from Label0 to Label1
	ldc 1543.0
	fstore_1
.var 2 is i I from Label0 to Label1
	iconst_0
	istore_2
Label0:
Label4:
	iload_2
	iconst_5
	if_icmpge Label2
	iconst_1
	goto Label3
Label2:
	iconst_0
Label3:
	ifle Label5
	fload_1
	fload_0
	fadd
	fstore_1
	iload_2
	iconst_1
	iadd
	istore_2
Label6:
	goto Label4
Label5:
Label7:
	fload_1
	invokestatic io/int_of_float(F)I
	ireturn
Label1:
.limit stack 8
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
