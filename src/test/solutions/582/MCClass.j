.source MCClass.java
.class public MCClass
.super java.lang.Object

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
.var 1 is a I from Label0 to Label1
	iconst_0
	istore_1
.var 2 is b I from Label0 to Label1
	iconst_0
	istore_2
.var 3 is c I from Label0 to Label1
	iconst_0
	istore_3
.var 4 is d I from Label0 to Label1
	iconst_0
	istore 4
Label0:
	ldc 1082000
	ineg
	istore_1
	ldc 1194957
	ineg
	istore_2
	sipush 8933
	ineg
	istore_3
	iload_1
	ineg
	istore 4
	iload_3
	invokestatic io/string_of_int(I)Ljava/lang/String;
	invokestatic io/print(Ljava/lang/String;)V
	iload_1
	invokestatic MCClass/call(I)I
	ineg
	istore_3
	iload_3
	invokestatic io/string_of_int(I)Ljava/lang/String;
	invokestatic io/print(Ljava/lang/String;)V
Label1:
	return
.limit stack 7
.limit locals 5
.end method

.method public static call(I)I
.var 0 is s I from Label0 to Label1
Label0:
	iload_0
	invokestatic io/string_of_int(I)Ljava/lang/String;
	invokestatic io/print(Ljava/lang/String;)V
	iload_0
	ireturn
Label1:
.limit stack 2
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
