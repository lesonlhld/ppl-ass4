.source MCClass.java
.class public MCClass
.super java.lang.Object

.method public static call(IIFIZLjava/lang/String;Ljava/lang/String;)Ljava/lang/String;
.var 0 is a I from Label0 to Label1
.var 1 is b I from Label0 to Label1
.var 2 is c F from Label0 to Label1
.var 3 is d I from Label0 to Label1
.var 4 is e Z from Label0 to Label1
.var 5 is f Ljava/lang/String; from Label0 to Label1
.var 6 is g Ljava/lang/String; from Label0 to Label1
Label0:
	iload_0
	iload_1
	iadd
	fload_2
	invokestatic io/int_of_float(F)I
	iadd
	iload_3
	iadd
	aload 6
	invokestatic io/int_of_string(Ljava/lang/String;)I
	iadd
	invokestatic io/string_of_int(I)Ljava/lang/String;
	areturn
Label1:
.limit stack 2
.limit locals 7
.end method

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
.var 1 is a I from Label0 to Label1
	bipush 6
	istore_1
.var 2 is var F from Label0 to Label1
	ldc 214.45
	fstore_2
.var 3 is arr [I from Label0 to Label1
	iconst_5
	newarray int
	astore_3
	aload_3
	iconst_0
	iconst_1
	iastore
	aload_3
	iconst_1
	bipush 67
	iastore
	aload_3
	iconst_2
	bipush 32
	iastore
	aload_3
	iconst_3
	bipush 65
	iastore
	aload_3
	iconst_4
	bipush 23
	iastore
Label0:
	iload_1
	sipush 876
	fload_2
	ldc 6.5
	fmul
	aload_3
	iconst_3
	iaload
	iconst_1
	ldc "chuoi~~\n"
	ldc "953"
	invokestatic MCClass/call(IIFIZLjava/lang/String;Ljava/lang/String;)Ljava/lang/String;
	invokestatic io/print(Ljava/lang/String;)V
Label1:
	return
.limit stack 15
.limit locals 4
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
