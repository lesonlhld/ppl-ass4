.source MCClass.java
.class public MCClass
.super java.lang.Object

.method public static foo([FF)V
.var 0 is a [F from Label0 to Label1
.var 1 is b F from Label0 to Label1
.var 2 is i I from Label0 to Label1
	iconst_0
	istore_2
Label0:
Label4:
	iload_2
	iconst_5
	if_icmpge Label2
	iconst_1
	goto Label3
Label2:
	iconst_0
Label3:
	ifle Label5
	aload_0
	iload_2
	fload_1
	aload_0
	iload_2
	faload
	ldc 74.431
	fmul
	fadd
	fastore
	aload_0
	iload_2
	faload
	invokestatic io/string_of_float(F)Ljava/lang/String;
	invokestatic io/printStrLn(Ljava/lang/String;)V
	iload_2
	iconst_1
	iadd
	istore_2
Label6:
	goto Label4
Label5:
Label7:
Label1:
	return
.limit stack 9
.limit locals 3
.end method

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
.var 1 is c [F from Label0 to Label1
	iconst_5
	newarray float
	astore_1
	aload_1
	iconst_0
	ldc 13.4
	fastore
	aload_1
	iconst_1
	ldc 52.63
	fastore
	aload_1
	iconst_2
	ldc 2500.0
	fastore
	aload_1
	iconst_3
	ldc 0.013543
	fastore
	aload_1
	iconst_4
	ldc 5823.35
	fastore
.var 2 is temp F from Label0 to Label1
	ldc 2344.2
	fstore_2
Label0:
	aload_1
	fload_2
	invokestatic MCClass/foo([FF)V
Label1:
	return
.limit stack 9
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
