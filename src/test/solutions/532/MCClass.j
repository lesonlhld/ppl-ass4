.source MCClass.java
.class public MCClass
.super java.lang.Object

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
.var 1 is a [I from Label0 to Label1
	iconst_5
	newarray int
	astore_1
	aload_1
	iconst_0
	iconst_1
	iastore
	aload_1
	iconst_1
	iconst_2
	iastore
	aload_1
	iconst_2
	iconst_3
	iastore
	aload_1
	iconst_3
	iconst_4
	iastore
	aload_1
	iconst_4
	iconst_5
	iastore
.var 2 is i I from Label0 to Label1
	iconst_0
	istore_2
Label0:
	aload_1
	iconst_1
	iconst_2
	iconst_1
	invokestatic MCClass/foo(II)I
	iadd
	iaload
	iconst_1
	isub
	istore_2
	aload_1
	iload_2
	sipush 873
	iconst_3
	imul
	iconst_4
	iadd
	iastore
	aload_1
	iload_2
	iaload
	invokestatic io/string_of_int(I)Ljava/lang/String;
	invokestatic io/print(Ljava/lang/String;)V
Label1:
	return
.limit stack 12
.limit locals 3
.end method

.method public static foo(II)I
.var 0 is a I from Label0 to Label1
.var 1 is b I from Label0 to Label1
Label0:
	iload_0
	iload_1
	iadd
	ireturn
Label1:
.limit stack 2
.limit locals 2
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
