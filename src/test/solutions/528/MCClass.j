.source MCClass.java
.class public MCClass
.super java.lang.Object

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
.var 1 is x I from Label0 to Label1
	bipush 7
	istore_1
Label0:
	iload_1
	iconst_4
	irem
	iconst_0
	if_icmpne Label8
	iconst_1
	goto Label9
Label8:
	iconst_0
Label9:
	ifle Label2
	iconst_0
	istore_1
	goto Label5
Label2:
	iload_1
	iconst_4
	irem
	iconst_1
	if_icmpne Label12
	iconst_1
	goto Label13
Label12:
	iconst_0
Label13:
	ifle Label3
	iconst_1
	istore_1
	goto Label5
Label3:
	iload_1
	iconst_4
	irem
	iconst_2
	if_icmpne Label16
	iconst_1
	goto Label17
Label16:
	iconst_0
Label17:
	ifle Label4
	iconst_2
	istore_1
	goto Label5
Label4:
	iconst_3
	istore_1
Label5:
	iload_1
	invokestatic io/string_of_int(I)Ljava/lang/String;
	invokestatic io/print(Ljava/lang/String;)V
Label1:
	return
.limit stack 13
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