.source MCClass.java
.class public MCClass
.super java.lang.Object

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
.var 1 is x I from Label0 to Label1
	bipush 20
	istore_1
Label0:
Label2:
	iconst_1
	ifle Label3
	iload_1
	iconst_0
	if_icmple Label10
	iconst_1
	goto Label11
Label10:
	iconst_0
Label11:
	ifle Label16
	iconst_1
	iload_1
	iconst_3
	if_icmpge Label14
	iconst_1
	goto Label15
Label14:
	iconst_0
Label15:
	iand
	goto Label17
Label16:
	iconst_0
Label17:
	ifle Label6
	ldc "oke"
	invokestatic io/printStrLn(Ljava/lang/String;)V
	goto Label5
	goto Label7
Label6:
	ldc "Error"
	invokestatic io/printStrLn(Ljava/lang/String;)V
Label7:
	iload_1
	iconst_3
	isub
	istore_1
Label4:
	goto Label2
Label3:
Label5:
Label1:
	return
.limit stack 9
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
