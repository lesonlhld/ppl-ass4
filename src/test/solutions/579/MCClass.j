.source MCClass.java
.class public MCClass
.super java.lang.Object

.method public static sum([I)I
.var 0 is x [I from Label0 to Label1
.var 1 is sum I from Label0 to Label1
	iconst_0
	istore_1
.var 2 is i I from Label0 to Label1
	iconst_0
	istore_2
Label0:
	iconst_0
	istore_2
Label2:
	iload_2
	iconst_5
	if_icmpge Label8
	iconst_1
	goto Label9
Label8:
	iconst_0
Label9:
	ifle Label3
	iload_1
	aload_0
	iload_2
	iaload
	iadd
	istore_1
Label4:
	iload_2
	iconst_1
	iadd
	istore_2
	goto Label2
Label3:
Label5:
	iload_1
	ireturn
Label1:
.limit stack 7
.limit locals 3
.end method

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
.var 1 is x [I from Label0 to Label1
	iconst_5
	newarray int
	dup
	iconst_0
	iconst_1
	iastore
	dup
	iconst_1
	iconst_2
	iastore
	dup
	iconst_2
	iconst_3
	iastore
	dup
	iconst_3
	iconst_4
	iastore
	dup
	iconst_4
	iconst_5
	iastore
	astore_1
.var 2 is y I from Label0 to Label1
	iconst_0
	istore_2
Label0:
	aload_1
	invokestatic MCClass/sum([I)I
	istore_2
	iload_2
	invokestatic io/string_of_int(I)Ljava/lang/String;
	invokestatic io/printStrLn(Ljava/lang/String;)V
	return
Label1:
.limit stack 10
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
