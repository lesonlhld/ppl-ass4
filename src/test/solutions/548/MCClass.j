.source MCClass.java
.class public MCClass
.super java.lang.Object

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
.var 1 is x I from Label0 to Label1
	ldc 6452342
	istore_1
Label0:
Label2:
	iconst_1
	ifle Label3
	iload_1
	iconst_0
	if_icmpge Label9
	iconst_1
	goto Label10
Label9:
	iconst_0
Label10:
	ifle Label6
	goto Label5
	goto Label8
Label6:
	iload_1
	iconst_1
	if_icmple Label11
	iconst_1
	goto Label12
Label11:
	iconst_0
Label12:
	ifle Label7
	iload_1
	iconst_3
	isub
	istore_1
	goto Label8
Label7:
	ldc "Error"
	invokestatic io/printStrLn(Ljava/lang/String;)V
	goto Label5
Label8:
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
