.source MCClass.java
.class public MCClass
.super java.lang.Object

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
.var 1 is x [Z from Label0 to Label1
	iconst_3
	newarray boolean
	dup
	iconst_0
	iconst_1
	bastore
	dup
	iconst_1
	iconst_0
	bastore
	dup
	iconst_2
	iconst_1
	bastore
	astore_1
.var 2 is i I from Label0 to Label1
	iconst_0
	istore_2
Label0:
	aload_1
	iconst_1
	aload_1
	iconst_0
	baload
	ifle Label2
	iconst_1
	aload_1
	iconst_2
	baload
	iand
	goto Label3
Label2:
	iconst_0
Label3:
	bastore
	iconst_0
	istore_2
Label4:
	iload_2
	iconst_3
	if_icmpge Label10
	iconst_1
	goto Label11
Label10:
	iconst_0
Label11:
	ifle Label5
	aload_1
	iload_2
	baload
	invokestatic io/string_of_bool(Z)Ljava/lang/String;
	invokestatic io/print(Ljava/lang/String;)V
Label6:
	iload_2
	iconst_1
	iadd
	istore_2
	goto Label4
Label5:
Label7:
Label1:
	return
.limit stack 15
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
