.source MCClass.java
.class public MCClass
.super java.lang.Object

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
.var 1 is k I from Label0 to Label1
	iconst_0
	istore_1
.var 2 is i I from Label0 to Label1
	iconst_0
	istore_2
.var 3 is j Z from Label0 to Label1
	iconst_0
	istore_3
.var 4 is f I from Label0 to Label1
	bipush 11
	istore 4
Label0:
	iload_1
	iconst_1
	if_icmpge Label4
	iconst_1
	goto Label5
Label4:
	iconst_0
Label5:
	iload_2
	iconst_0
	if_icmpeq Label6
	iconst_1
	goto Label7
Label6:
	iconst_0
Label7:
	iand
	iload_1
	iconst_5
	if_icmple Label8
	iconst_1
	goto Label9
Label8:
	iconst_0
Label9:
	ior
	iload_3
	ifgt Label10
	iconst_1
	goto Label11
Label10:
	iconst_0
Label11:
	ior
	ifle Label2
	iload 4
	iconst_3
	irem
	istore 4
	goto Label3
Label2:
Label3:
	iload 4
	invokestatic io/string_of_int(I)Ljava/lang/String;
	invokestatic io/print(Ljava/lang/String;)V
Label1:
	return
.limit stack 16
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
