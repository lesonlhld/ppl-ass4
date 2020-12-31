.source MCClass.java
.class public MCClass
.super java.lang.Object

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
.var 1 is a I from Label0 to Label1
	bipush 123
	istore_1
Label0:
	iload_1
	iconst_3
	irem
	iconst_0
	if_icmpne Label5
	iconst_1
	goto Label6
Label5:
	iconst_0
Label6:
	ifle Label2
	ldc "a % 3 == 0"
	invokestatic io/printStrLn(Ljava/lang/String;)V
	goto Label4
Label2:
	iload_1
	iconst_3
	irem
	iconst_1
	if_icmpne Label7
	iconst_1
	goto Label8
Label7:
	iconst_0
Label8:
	ifle Label3
	ldc "a % 3 == 1"
	invokestatic io/printStrLn(Ljava/lang/String;)V
	goto Label4
Label3:
	ldc "a % 3 == 2"
	invokestatic io/printStrLn(Ljava/lang/String;)V
Label4:
Label1:
	return
.limit stack 6
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
