.source MCClass.java
.class public MCClass
.super java.lang.Object

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
.var 1 is x [Ljava/lang/String; from Label0 to Label1
	iconst_3
	anewarray java/lang/String
	astore_1
	aload_1
	iconst_0
	ldc "1"
	aastore
	aload_1
	iconst_1
	ldc "2"
	aastore
	aload_1
	iconst_2
	ldc "3"
	aastore
Label0:
	aload_1
	iconst_1
	aaload
	invokestatic io/print(Ljava/lang/String;)V
Label1:
	return
.limit stack 7
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
