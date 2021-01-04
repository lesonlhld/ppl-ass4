.source MCClass.java
.class public MCClass
.super java.lang.Object

.method public static sqrt(I)I
.var 0 is x I from Label0 to Label1
.var 1 is i I from Label0 to Label1
	iconst_0
	istore_1
Label0:
Label6:
	iload_1
	iload_1
	imul
	iload_0
	if_icmpge Label4
	iconst_1
	goto Label5
Label4:
	iconst_0
Label5:
	ifle Label7
	iload_1
	iconst_1
	ineg
	isub
	istore_1
Label8:
	goto Label6
Label7:
Label9:
	iload_1
	iconst_1
	isub
	ireturn
Label1:
.limit stack 6
.limit locals 2
.end method

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
.var 1 is n I from Label0 to Label1
	iconst_5
	istore_1
.var 2 is x I from Label0 to Label1
	iconst_0
	istore_2
.var 3 is i I from Label0 to Label1
	iconst_0
	istore_3
Label0:
	iconst_0
	istore_3
Label2:
	iload_3
	iload_1
	invokestatic MCClass/sqrt(I)I
	if_icmpge Label8
	iconst_1
	goto Label9
Label8:
	iconst_0
Label9:
	ifle Label3
	iload_3
	iload_1
	iadd
	istore_2
Label4:
	iload_3
	iconst_2
	iadd
	istore_3
	goto Label2
Label3:
Label5:
	iload_2
	invokestatic io/string_of_int(I)Ljava/lang/String;
	invokestatic io/print(Ljava/lang/String;)V
Label1:
	return
.limit stack 6
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
