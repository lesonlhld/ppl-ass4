.source MCClass.java
.class public MCClass
.super java.lang.Object

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
.var 1 is x I from Label0 to Label1
	iconst_5
	istore_1
.var 2 is y I from Label0 to Label1
	bipush 6
	istore_2
Label0:
	iload_1
	iload_2
	invokestatic MCClass/no_swap(II)V
	iload_1
	invokestatic io/string_of_int(I)Ljava/lang/String;
	invokestatic io/print(Ljava/lang/String;)V
	iload_2
	invokestatic io/string_of_int(I)Ljava/lang/String;
	invokestatic io/print(Ljava/lang/String;)V
Label1:
	return
.limit stack 3
.limit locals 3
.end method

.method public static no_swap(II)V
.var 0 is x I from Label0 to Label1
.var 1 is y I from Label0 to Label1
.var 2 is temp I from Label0 to Label1
	iconst_0
	istore_2
Label0:
	iload_0
	istore_2
	iload_1
	istore_0
	iload_2
	istore_1
Label1:
	return
.limit stack 5
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
