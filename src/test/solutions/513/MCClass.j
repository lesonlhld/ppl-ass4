.source MCClass.java
.class public MCClass
.super java.lang.Object

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
.var 1 is a [[Ljava/lang/String; from Label0 to Label1
	iconst_2
	anewarray [Ljava/lang/String;
	dup
	iconst_0
	iconst_2
	anewarray java/lang/String
	dup
	iconst_0
	ldc "a"
	aastore
	dup
	iconst_1
	ldc "b"
	aastore
	aastore
	dup
	iconst_1
	iconst_2
	anewarray java/lang/String
	dup
	iconst_0
	ldc "c"
	aastore
	dup
	iconst_1
	ldc "d"
	aastore
	aastore
	astore_1
.var 2 is c [[F from Label0 to Label1
	iconst_2
	anewarray [F
	dup
	iconst_0
	iconst_3
	newarray float
	dup
	iconst_0
	ldc 0.01
	fastore
	dup
	iconst_1
	ldc 3.5
	fastore
	dup
	iconst_2
	ldc 5.0
	fastore
	aastore
	dup
	iconst_1
	iconst_3
	newarray float
	dup
	iconst_0
	ldc 3.1
	fastore
	dup
	iconst_1
	ldc 500.0
	fastore
	dup
	iconst_2
	ldc 0.007
	fastore
	aastore
	astore_2
Label0:
Label1:
	return
.limit stack 20
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
