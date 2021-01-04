.source MCClass.java
.class public MCClass
.super java.lang.Object

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
.var 1 is n [F from Label0 to Label1
	iconst_5
	newarray float
	dup
	iconst_0
	ldc 3.34
	fastore
	dup
	iconst_1
	ldc 6.67
	fastore
	dup
	iconst_2
	ldc 8.03
	fastore
	dup
	iconst_3
	ldc 32.57
	fastore
	dup
	iconst_4
	ldc 54.108
	fastore
	astore_1
.var 2 is i I from Label0 to Label1
	iconst_0
	istore_2
.var 3 is k I from Label0 to Label1
	bipush 10
	istore_3
.var 4 is j I from Label0 to Label1
	iconst_1
	istore 4
Label0:
	iconst_0
	istore_2
Label2:
	iload_2
	iload_3
	if_icmpge Label8
	iconst_1
	goto Label9
Label8:
	iconst_0
Label9:
	ifle Label3
	aload_1
	iload_2
	iconst_5
	irem
	aload_1
	iload_2
	iconst_5
	irem
	faload
	iload_2
	invokestatic io/float_to_int(I)F
	fadd
	fastore
	aload_1
	iload_2
	iconst_5
	irem
	faload
	invokestatic io/string_of_float(F)Ljava/lang/String;
	invokestatic io/print(Ljava/lang/String;)V
Label4:
	iload_2
	iload 4
	iload 4
	imul
	iadd
	istore_2
	goto Label2
Label3:
Label5:
Label1:
	return
.limit stack 14
.limit locals 5
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
