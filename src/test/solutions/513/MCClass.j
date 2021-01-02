.source MCClass.java
.class public MCClass
.super java.lang.Object

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
.var 1 is a [[Ljava/lang/String; from Label0 to Label1
	iconst_2
	iconst_2
	multianewarray [[Ljava/lang/String; 2
	astore_1
	aload_1
	iconst_0
	aaload
	iconst_0
	ldc "a"
	aastore
	aload_1
	iconst_0
	aaload
	iconst_1
	ldc "b"
	aastore
	aload_1
	iconst_1
	aaload
	iconst_0
	ldc "c"
	aastore
	aload_1
	iconst_1
	aaload
	iconst_1
	ldc "d"
	aastore
.var 2 is c [[F from Label0 to Label1
	iconst_2
	iconst_3
	multianewarray [[F 2
	astore_2
	aload_2
	iconst_0
	aaload
	iconst_0
	ldc 0.01
	fastore
	aload_2
	iconst_0
	aaload
	iconst_1
	ldc 3.5
	fastore
	aload_2
	iconst_0
	aaload
	iconst_2
	ldc 5.0
	fastore
	aload_2
	iconst_1
	aaload
	iconst_0
	ldc 3.1
	fastore
	aload_2
	iconst_1
	aaload
	iconst_1
	ldc 500.0
	fastore
	aload_2
	iconst_1
	aaload
	iconst_2
	ldc 0.007
	fastore
Label0:
Label1:
	return
.limit stack 16
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
