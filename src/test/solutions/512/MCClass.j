.source MCClass.java
.class public MCClass
.super java.lang.Object

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
.var 1 is n I from Label0 to Label1
	iconst_1
	istore_1
Label0:
	iload_1
	iconst_0
	if_icmpge Label4
	iconst_1
	goto Label5
Label4:
	iconst_0
Label5:
	ifle Label2
	ldc "n < 0"
	invokestatic io/print(Ljava/lang/String;)V
	goto Label3
Label2:
	ldc "n >= 0"
	invokestatic io/print(Ljava/lang/String;)V
Label3:
Label1:
	return
.limit stack 4
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