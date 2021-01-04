.source MCClass.java
.class public MCClass
.super java.lang.Object

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
.var 1 is n I from Label0 to Label1
	iconst_m1
	istore_1
Label0:
	iload_1
	iconst_0
	if_icmpne Label7
	iconst_1
	goto Label8
Label7:
	iconst_0
Label8:
	ifle Label2
	ldc "n < 0"
	invokestatic io/print(Ljava/lang/String;)V
	goto Label4
Label2:
	iload_1
	iconst_0
	if_icmple Label11
	iconst_1
	goto Label12
Label11:
	iconst_0
Label12:
	ifle Label3
	ldc "n > 0"
	invokestatic io/print(Ljava/lang/String;)V
	goto Label4
Label3:
	ldc "n = 0"
	invokestatic io/print(Ljava/lang/String;)V
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
