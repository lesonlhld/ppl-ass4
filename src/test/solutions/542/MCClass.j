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
	if_icmpge Label6
	iconst_1
	goto Label7
Label6:
	iconst_0
Label7:
	ifle Label12
	iconst_1
	iload_2
	iconst_0
	if_icmpeq Label10
	iconst_1
	goto Label11
Label10:
	iconst_0
Label11:
	iand
	goto Label13
Label12:
	iconst_0
Label13:
	ifgt Label18
	iconst_0
	iload_1
	iconst_5
	if_icmple Label16
	iconst_1
	goto Label17
Label16:
	iconst_0
Label17:
	ior
	goto Label19
Label18:
	iconst_1
Label19:
	ifgt Label22
	iconst_0
	iload_3
	ifgt Label20
	iconst_1
	goto Label21
Label20:
	iconst_0
Label21:
	ior
	goto Label23
Label22:
	iconst_1
Label23:
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
