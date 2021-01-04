.source MCClass.java
.class public MCClass
.super java.lang.Object

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
.var 1 is i I from Label0 to Label1
	iconst_0
	istore_1
Label0:
Label2:
.var 2 is k I from Label0 to Label1
	bipush 10
	istore_2
	iload_1
	iconst_0
	if_icmple Label10
	iconst_1
	goto Label11
Label10:
	iconst_0
Label11:
	ifle Label6
	iload_2
	iload_1
	irem
	invokestatic io/string_of_int(I)Ljava/lang/String;
	invokestatic io/print(Ljava/lang/String;)V
	goto Label7
Label6:
Label7:
	iload_1
	iconst_1
	iadd
	istore_1
	iload_1
	bipush 10
	if_icmpgt Label14
	iconst_1
	goto Label15
Label14:
	iconst_0
Label15:
	ifle Label3
	goto Label2
Label3:
Label5:
Label1:
	return
.limit stack 7
.limit locals 3
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
