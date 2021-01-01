.source MCClass.java
.class public MCClass
.super java.lang.Object

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
.var 1 is i I from Label0 to Label1
	iconst_0
	istore_1
.var 2 is c Z from Label0 to Label1
	iconst_1
	istore_2
Label0:
Label4:
	iload_1
	sipush 423
	if_icmpgt Label2
	iconst_1
	goto Label3
Label2:
	iconst_0
Label3:
	ifle Label5
.var 3 is b Z from Label0 to Label1
	iconst_1
	istore_3
.var 4 is a Z from Label0 to Label1
	iconst_0
	istore 4
	iload_1
	bipush 100
	if_icmpge Label8
	iconst_1
	goto Label9
Label8:
	iconst_0
Label9:
	istore_3
	iload_3
	iload_2
	iand
	ifgt Label10
	iconst_1
	goto Label11
Label10:
	iconst_0
Label11:
	iload 4
	iload_3
	iand
	ifgt Label12
	iconst_1
	goto Label13
Label12:
	iconst_0
Label13:
	ior
	iload_1
	iconst_1
	iadd
	sipush 234
	if_icmpne Label14
	iconst_1
	goto Label15
Label14:
	iconst_0
Label15:
	iand
	istore 4
	iload_1
	iconst_3
	iadd
	istore_1
	iload_1
	sipush 212
	if_icmpne Label18
	iconst_1
	goto Label19
Label18:
	iconst_0
Label19:
	ifle Label16
	goto Label7
	goto Label17
Label16:
Label17:
	iload 4
	istore_2
Label6:
	goto Label4
Label5:
Label7:
	iload_2
	invokestatic io/string_of_bool(Z)Ljava/lang/String;
	invokestatic io/print(Ljava/lang/String;)V
Label1:
	return
.limit stack 26
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
