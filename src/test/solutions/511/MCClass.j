.source MCClass.java
.class public MCClass
.super java.lang.Object

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
.var 1 is x [F from Label0 to Label1
	iconst_3
	newarray float
	dup
	iconst_0
	ldc 1.2
	fastore
	dup
	iconst_1
	ldc 2.3
	fastore
	dup
	iconst_2
	ldc 3.4
	fastore
	astore_1
Label0:
Label1:
	return
.limit stack 8
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
