.source MCClass.java
.class public MCClass
.super java.lang.Object

.method public static foo()[I
.var 0 is x [I from Label0 to Label1
	iconst_3
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
Label0:
	aload_0
	areturn
Label1:
.limit stack 7
.limit locals 1
.end method

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
	invokestatic MCClass/foo()[I
	iconst_2
	sipush 1234
	iastore
	invokestatic MCClass/foo()[I
	iconst_2
	iaload
	invokestatic io/string_of_int(I)Ljava/lang/String;
	invokestatic io/print(Ljava/lang/String;)V
Label1:
	return
.limit stack 5
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