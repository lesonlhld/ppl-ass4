.source MCClass.java
.class public MCClass
.super java.lang.Object

.method public static foo()[I
.var 0 is a [I from Label0 to Label1
	iconst_4
	newarray int
	astore_0
	aload_0
	iconst_0
	iconst_1
	iastore
	aload_0
	iconst_1
	iconst_2
	iastore
	aload_0
	iconst_2
	iconst_3
	iastore
	aload_0
	iconst_3
	iconst_4
	iastore
Label0:
	aload_0
	areturn
Label1:
.limit stack 8
.limit locals 1
.end method

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
.var 1 is a [I from Label0 to Label1
	iconst_4
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
Label0:
	invokestatic MCClass/foo()[I
	iconst_2
	aload_1
	iconst_1
	iaload
	iastore
	invokestatic MCClass/foo()[I
	iconst_2
	iaload
	invokestatic io/string_of_int(I)Ljava/lang/String;
	invokestatic io/print(Ljava/lang/String;)V
Label1:
	return
.limit stack 9
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
