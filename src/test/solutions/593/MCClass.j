.source MCClass.java
.class public MCClass
.super java.lang.Object
.field static m I
.field static i I

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
.var 1 is a I from Label0 to Label1
	iconst_1
	istore_1
.var 2 is b I from Label0 to Label1
	sipush 5645
	istore_2
Label0:
	iconst_1
	putstatic MCClass/i I
	iload_1
	iload_2
	invokestatic MCClass/test2(II)I
	putstatic MCClass/m I
	iconst_2
	putstatic MCClass/i I
	iload_1
	getstatic MCClass/m I
	invokestatic MCClass/test2(II)I
	putstatic MCClass/m I
	getstatic MCClass/m I
	invokestatic io/string_of_int(I)Ljava/lang/String;
	invokestatic io/printStrLn(Ljava/lang/String;)V
Label1:
	return
.limit stack 7
.limit locals 3
.end method

.method public static test2(II)I
.var 0 is x I from Label0 to Label1
.var 1 is y I from Label0 to Label1
Label0:
Label2:
	iload_1
	bipush 11
	irem
	bipush 6
	irem
	iconst_4
	if_icmplt Label8
	iconst_1
	goto Label9
Label8:
	iconst_0
Label9:
	ifle Label6
	iload_1
	iload_0
	imul
	istore_1
	goto Label7
Label6:
Label7:
	iload_0
	iconst_1
	iadd
	istore_0
	iload_0
	bipush 10
	if_icmpge Label10
	iconst_1
	goto Label11
Label10:
	iconst_0
Label11:
	ifle Label3
	goto Label2
Label3:
Label5:
	ldc "Lap lan "
	invokestatic io/print(Ljava/lang/String;)V
	getstatic MCClass/i I
	invokestatic io/string_of_int(I)Ljava/lang/String;
	invokestatic io/printStrLn(Ljava/lang/String;)V
	iload_1
	ireturn
Label1:
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
