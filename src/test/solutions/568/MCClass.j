.source MCClass.java
.class public MCClass
.super java.lang.Object

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
.var 1 is a Z from Label0 to Label1
	iconst_1
	istore_1
.var 2 is b I from Label0 to Label1
	iconst_0
	istore_2
Label0:
	iload_1
	ifgt Label4
	iconst_1
	goto Label5
Label4:
	iconst_0
Label5:
	ifle Label2
	iconst_5
	istore_2
	goto Label3
Label2:
Label8:
	iload_2
	iconst_3
	if_icmpge Label6
	iconst_1
	goto Label7
Label6:
	iconst_0
Label7:
	ifle Label9
	iload_2
	iconst_1
	iadd
	istore_2
Label10:
	goto Label8
Label9:
Label11:
Label3:
	invokestatic io/printLn()V
	iload_2
	invokestatic io/string_of_int(I)Ljava/lang/String;
	invokestatic io/print(Ljava/lang/String;)V
Label1:
	return
.limit stack 12
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
