.source MCClass.java
.class public MCClass
.super java.lang.Object

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
.var 1 is i I from Label0 to Label1
	bipush 10
	istore_1
Label0:
Label4:
	iconst_0
	ifgt Label2
	iconst_1
	goto Label3
Label2:
	iconst_0
Label3:
	ifle Label5
	iload_1
	iconst_0
	if_icmpge Label11
	iconst_1
	goto Label12
Label11:
	iconst_0
Label12:
	ifle Label8
	goto Label7
	goto Label10
Label8:
	iload_1
	iconst_2
	irem
	iconst_0
	if_icmpne Label13
	iconst_1
	goto Label14
Label13:
	iconst_0
Label14:
	ifle Label9
	iload_1
	iconst_1
	isub
	istore_1
	goto Label6
	goto Label10
Label9:
	iload_1
	invokestatic io/string_of_int(I)Ljava/lang/String;
	invokestatic io/print(Ljava/lang/String;)V
Label10:
	iload_1
	iconst_1
	isub
	istore_1
Label6:
	goto Label4
Label5:
Label7:
Label1:
	return
.limit stack 12
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
