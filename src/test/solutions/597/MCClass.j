.source MCClass.java
.class public MCClass
.super java.lang.Object
.field static a F

.method public static main([Ljava/lang/String;)V
	ldc 1.0
	putstatic MCClass/a F
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
	ldc 4325.43674
	putstatic MCClass/a F
	getstatic MCClass/a F
	ldc 432.57523
	fadd
	getstatic MCClass/a F
	invokestatic io/int_of_float(F)I
	invokestatic MCClass/foo(I)I
	invokestatic io/float_to_int(I)F
	fsub
	putstatic MCClass/a F
	getstatic MCClass/a F
	invokestatic io/string_of_float(F)Ljava/lang/String;
	invokestatic io/print(Ljava/lang/String;)V
Label1:
	return
.limit stack 4
.limit locals 1
.end method

.method public static foo(I)I
.var 0 is x I from Label0 to Label1
Label0:
	iload_0
	iload_0
	bipush 12
	irem
	imul
	iload_0
	iload_0
	bipush 12
	irem
	idiv
	iadd
	ireturn
Label1:
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
