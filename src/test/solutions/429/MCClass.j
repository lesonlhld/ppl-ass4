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
	iconst_2
	iastore
	aload_1
	iconst_1
	iconst_3
	iastore
	aload_1
	iconst_2
	iconst_5
	iastore
	aload_1
	iconst_3
	bipush 7
	iastore
	aload_1
	iconst_4
	bipush 8
	iastore
.var 2 is x I from Label0 to Label1
	iconst_0
	istore_2
Label0:
	bipush 15
	ineg
	bipush 45
	iconst_2
	imul
	bipush 35
	bipush 108
	iadd
	aload_1
	iconst_4
	iaload
	iadd
	imul
	iadd
	ineg
	ldc "21"
	invokestatic io/int_of_string(Ljava/lang/String;)I
	imul
	istore_2
	invokestatic io/printLn()V
	iload_2
	invokestatic io/string_of_int(I)Ljava/lang/String;
	invokestatic io/printStrLn(Ljava/lang/String;)V
Label1:
	return
.limit stack 7
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
