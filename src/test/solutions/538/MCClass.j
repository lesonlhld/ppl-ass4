.source MCClass.java
.class public MCClass
.super java.lang.Object

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
.var 1 is x I from Label0 to Label1
	iconst_0
	istore_1
Label0:
	iconst_1
	istore_1
Label2:
	iload_1
	iconst_5
	if_icmpgt Label8
	iconst_1
	goto Label9
Label8:
	iconst_0
Label9:
	ifle Label3
	iload_1
	invokestatic io/string_of_int(I)Ljava/lang/String;
	invokestatic io/print(Ljava/lang/String;)V
Label4:
	iload_1
	iconst_1
	iadd
	istore_1
	goto Label2
Label3:
Label5:
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
