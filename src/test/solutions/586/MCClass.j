.source MCClass.java
.class public MCClass
.super java.lang.Object

.method public static foo([F)V
.var 0 is x [F from Label0 to Label1
.var 1 is i I from Label0 to Label1
	iconst_0
	istore_1
Label0:
	iconst_0
	istore_1
Label2:
	iload_1
	iconst_3
	if_icmpge Label8
	iconst_1
	goto Label9
Label8:
	iconst_0
Label9:
	ifle Label3
.var 2 is y I from Label0 to Label1
	iconst_2
	istore_2
	aload_0
	iload_1
	faload
	invokestatic io/string_of_float(F)Ljava/lang/String;
	invokestatic io/printStrLn(Ljava/lang/String;)V
Label4:
	iload_1
	iconst_1
	iadd
	istore_1
	goto Label2
Label3:
Label5:
Label1:
	return
.limit stack 6
.limit locals 3
.end method

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
.var 1 is x [F from Label0 to Label1
	iconst_3
	newarray float
	dup
	iconst_0
	ldc 1.1
	fastore
	dup
	iconst_1
	ldc 2.2
	fastore
	dup
	iconst_2
	ldc 3.3
	fastore
	astore_1
Label0:
	aload_1
	invokestatic MCClass/foo([F)V
Label1:
	return
.limit stack 8
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
