.source MCClass.java
.class public MCClass
.super java.lang.Object

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
.var 1 is x Z from Label0 to Label1
	iconst_0
	istore_1
.var 2 is a F from Label0 to Label1
	ldc 0.01
	fstore_2
.var 3 is b I from Label0 to Label1
	bipush 20
	istore_3
Label0:
	fload_2
	ldc 2.3e-13
	fcmpl
	ifgt Label4
	iconst_1
	goto Label5
Label4:
	iconst_0
Label5:
	ifgt Label10
	iconst_0
	iload_3
	bipush 21
	if_icmpne Label8
	iconst_1
	goto Label9
Label8:
	iconst_0
Label9:
	ior
	goto Label11
Label10:
	iconst_1
Label11:
	ifgt Label16
	iconst_0
	iload_3
	sipush 235
	if_icmpeq Label14
	iconst_1
	goto Label15
Label14:
	iconst_0
Label15:
	ior
	goto Label17
Label16:
	iconst_1
Label17:
	istore_1
	iload_1
	invokestatic io/string_of_bool(Z)Ljava/lang/String;
	invokestatic io/print(Ljava/lang/String;)V
Label1:
	return
.limit stack 12
.limit locals 4
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
