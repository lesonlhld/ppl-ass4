.source MCClass.java
.class public MCClass
.super java.lang.Object
.field static x [F

.method public static main([Ljava/lang/String;)V
	iconst_5
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
	dup
	iconst_3
	ldc 4.4
	fastore
	dup
	iconst_4
	ldc 5.5
	fastore
	putstatic MCClass/x [F
.var 0 is args [Ljava/lang/String; from Label0 to Label1
.var 1 is i I from Label0 to Label1
	iconst_0
	istore_1
Label0:
	iconst_0
	istore_1
Label2:
	iload_1
	iconst_5
	if_icmpge Label8
	iconst_1
	goto Label9
Label8:
	iconst_0
Label9:
	ifle Label3
	getstatic MCClass/x [F
	iload_1
	getstatic MCClass/x [F
	iload_1
	faload
	iconst_2
	invokestatic io/float_to_int(I)F
	fmul
	ldc 1.0
	fadd
	fastore
Label4:
	iload_1
	iconst_1
	iadd
	istore_1
	goto Label2
Label3:
Label5:
	iconst_0
	istore_1
Label10:
	iload_1
	iconst_5
	if_icmpge Label16
	iconst_1
	goto Label17
Label16:
	iconst_0
Label17:
	ifle Label11
	getstatic MCClass/x [F
	iload_1
	faload
	invokestatic io/string_of_float(F)Ljava/lang/String;
	invokestatic io/print(Ljava/lang/String;)V
Label12:
	iload_1
	iconst_1
	iadd
	istore_1
	goto Label10
Label11:
Label13:
Label1:
	return
.limit stack 34
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
