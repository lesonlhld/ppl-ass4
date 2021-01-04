.source MCClass.java
.class public MCClass
.super java.lang.Object
.field static x [Ljava/lang/String;

.method public static main([Ljava/lang/String;)V
	iconst_3
	anewarray java/lang/String
	dup
	iconst_0
	ldc "Hello"
	aastore
	dup
	iconst_1
	ldc "World"
	aastore
	dup
	iconst_2
	ldc "!"
	aastore
	putstatic MCClass/x [Ljava/lang/String;
.var 0 is args [Ljava/lang/String; from Label0 to Label1
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
	getstatic MCClass/x [Ljava/lang/String;
	iload_1
	ldc "i"
	aastore
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
	iconst_3
	if_icmpge Label16
	iconst_1
	goto Label17
Label16:
	iconst_0
Label17:
	ifle Label11
	getstatic MCClass/x [Ljava/lang/String;
	iload_1
	aaload
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
.limit stack 26
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
