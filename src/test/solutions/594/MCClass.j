.source MCClass.java
.class public MCClass
.super java.lang.Object

.method public static foo([I)I
.var 0 is a [I from Label0 to Label1
.var 1 is x [I from Label0 to Label1
	bipush 6
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
	aload_1
	iconst_5
	bipush 6
	iastore
.var 2 is y I from Label0 to Label1
	iconst_1
	istore_2
Label0:
	aload_0
	iload_2
	aload_1
	aload_0
	aload_1
	aload_0
	aload_1
	iload_2
	iaload
	iaload
	iaload
	iaload
	iaload
	iastore
	aload_0
	iload_2
	iaload
	iload_2
	iadd
	ireturn
Label1:
.limit stack 14
.limit locals 3
.end method

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
	iconst_1
	iconst_2
	iconst_3
	iconst_4
	iconst_5
	invokestatic MCClass/foo([I)I
	invokestatic io/string_of_int(I)Ljava/lang/String;
	invokestatic io/print(Ljava/lang/String;)V
	return
Label1:
.limit stack 6
.limit locals 1
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
