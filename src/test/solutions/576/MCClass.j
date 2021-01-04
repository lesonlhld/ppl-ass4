.source MCClass.java
.class public MCClass
.super java.lang.Object

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
.var 1 is a I from Label0 to Label1
	iconst_5
	istore_1
.var 2 is b F from Label0 to Label1
	ldc 4.5
	fstore_2
Label0:
	iload_1
	fload_2
	invokestatic MCClass/foo(F)I
	iadd
	istore_1
	iload_1
	invokestatic io/string_of_int(I)Ljava/lang/String;
	invokestatic io/print(Ljava/lang/String;)V
Label1:
	return
.limit stack 3
.limit locals 3
.end method

.method public static foo(F)I
.var 0 is a F from Label0 to Label1
.var 1 is c F from Label0 to Label1
	ldc 5.5
	fstore_1
Label0:
	fload_1
	fload_0
	fadd
	invokestatic io/int_of_float(F)I
	ireturn
Label1:
.limit stack 3
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
