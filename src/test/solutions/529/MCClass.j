.source MCClass.java
.class public MCClass
.super java.lang.Object

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
.var 1 is var Z from Label0 to Label1
	iconst_1
	istore_1
.var 2 is x Z from Label0 to Label1
	iconst_0
	istore_2
.var 3 is ilv F from Label0 to Label1
	ldc 4000.0
	fstore_3
.var 4 is nvh F from Label0 to Label1
	ldc 2.3
	fstore 4
Label0:
	fload 4
	ldc 123.45
	fcmpl
	ifeq Label4
	iconst_1
	goto Label5
Label4:
	iconst_0
Label5:
	istore_1
	iload_1
	ifle Label10
	iconst_1
	fload_3
	fload 4
	fcmpl
	ifge Label8
	iconst_1
	goto Label9
Label8:
	iconst_0
Label9:
	iand
	goto Label11
Label10:
	iconst_0
Label11:
	istore_2
	iload_2
	invokestatic io/string_of_bool(Z)Ljava/lang/String;
	invokestatic io/print(Ljava/lang/String;)V
Label1:
	return
.limit stack 11
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
