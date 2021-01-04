.source MCClass.java
.class public MCClass
.super java.lang.Object

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
.var 1 is x [[I from Label0 to Label1
	iconst_2
	iconst_2
	multianewarray [[I 2
	astore_1
	aload_1
	iconst_0
	aaload
	iconst_0
	iconst_1
	iastore
	aload_1
	iconst_0
	aaload
	iconst_1
	iconst_2
	iastore
	aload_1
	iconst_1
	aaload
	iconst_0
	iconst_3
	iastore
	aload_1
	iconst_1
	aaload
	iconst_1
	iconst_4
	iastore
Label0:
	aload_1
	iconst_0
	iconst_1
	iconst_5
	aastore
	aload_1
	iconst_0
	aaload
	iconst_1
	iaload
	invokestatic io/string_of_int(I)Ljava/lang/String;
	invokestatic io/print(Ljava/lang/String;)V
Label1:
	return
.limit stack 12
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
