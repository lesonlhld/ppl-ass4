.source MCClass.java
.class public MCClass
.super java.lang.Object
.field static x [Ljava/lang/String;
.field static y [I

.method public static main([Ljava/lang/String;)V
	iconst_3
	anewarray java/lang/String
	putstatic MCClass/x [Ljava/lang/String;
	getstatic MCClass/x [Ljava/lang/String;
	iconst_0
	ldc "1"
	aastore
	getstatic MCClass/x [Ljava/lang/String;
	iconst_1
	ldc "2"
	aastore
	getstatic MCClass/x [Ljava/lang/String;
	iconst_2
	ldc "3"
	aastore
	iconst_3
	newarray int
	putstatic MCClass/y [I
	getstatic MCClass/y [I
	iconst_0
	iconst_1
	iastore
	getstatic MCClass/y [I
	iconst_1
	iconst_2
	iastore
	getstatic MCClass/y [I
	iconst_2
	iconst_3
	iastore
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
	getstatic MCClass/x [Ljava/lang/String;
	iconst_1
	aaload
	invokestatic io/print(Ljava/lang/String;)V
	getstatic MCClass/y [I
	iconst_1
	iaload
	invokestatic io/string_of_int(I)Ljava/lang/String;
	invokestatic io/print(Ljava/lang/String;)V
Label1:
	return
.limit stack 3
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
