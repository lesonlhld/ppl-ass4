.source MCClass.java
.class public MCClass
.super java.lang.Object
.field static x [[Ljava/lang/String;

.method public static main([Ljava/lang/String;)V
	iconst_2
	anewarray [Ljava/lang/String;
	dup
	iconst_0
	iconst_2
	anewarray java/lang/String
	dup
	iconst_0
	ldc "1"
	aastore
	dup
	iconst_1
	ldc "2"
	aastore
	aastore
	dup
	iconst_1
	iconst_2
	anewarray java/lang/String
	dup
	iconst_0
	ldc "3"
	aastore
	dup
	iconst_1
	ldc "4"
	aastore
	aastore
	putstatic MCClass/x [[Ljava/lang/String;
.var 0 is args [Ljava/lang/String; from Label0 to Label1
.var 1 is i I from Label0 to Label1
	iconst_0
	istore_1
.var 2 is j I from Label0 to Label1
	iconst_0
	istore_2
Label0:
	iconst_0
	istore_1
Label2:
	iload_1
	iconst_2
	if_icmpge Label8
	iconst_1
	goto Label9
Label8:
	iconst_0
Label9:
	ifle Label3
	iconst_0
	istore_2
Label10:
	iload_2
	iconst_2
	if_icmpge Label16
	iconst_1
	goto Label17
Label16:
	iconst_0
Label17:
	ifle Label11
	getstatic MCClass/x [[Ljava/lang/String;
	iload_1
	aaload
	iload_2
	aaload
	invokestatic io/print(Ljava/lang/String;)V
Label12:
	iload_2
	iconst_1
	iadd
	istore_2
	goto Label10
Label11:
Label13:
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
.limit stack 39
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
