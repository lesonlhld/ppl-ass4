.source MCClass.java
.class public MCClass
.super java.lang.Object

.method public static fact(I)I
.var 0 is n I from Label0 to Label1
Label0:
	iload_0
	iconst_0
	if_icmpne Label5
	iconst_1
	goto Label6
Label5:
	iconst_0
Label6:
	ifle Label2
	iconst_1
	ireturn
Label2:
	iload_0
	iconst_0
	if_icmple Label7
	iconst_1
	goto Label8
Label7:
	iconst_0
Label8:
	ifle Label3
	iload_0
	iload_0
	iconst_1
	isub
	invokestatic MCClass/fact(I)I
	imul
	ireturn
Label3:
	iload_0
	ireturn
Label4:
Label1:
	return
.limit stack 7
.limit locals 1
.end method

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
	iconst_3
	invokestatic MCClass/fact(I)I
	invokestatic io/string_of_int(I)Ljava/lang/String;
	invokestatic io/printStrLn(Ljava/lang/String;)V
	iconst_5
	ineg
	invokestatic MCClass/fact(I)I
	invokestatic io/string_of_int(I)Ljava/lang/String;
	invokestatic io/print(Ljava/lang/String;)V
Label1:
	return
.limit stack 1
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
