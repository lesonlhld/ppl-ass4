.source MCClass.java
.class public MCClass
.super java.lang.Object

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
.var 1 is x [I from Label0 to Label1
	iconst_3
	newarray int
	astore_1
	aload_1
	iconst_0
	iconst_1
	iastore
	aload_1
	iconst_1
	iconst_2
	iastore
	aload_1
	iconst_2
	iconst_3
	iastore
.var 2 is y [I from Label0 to Label1
	iconst_3
	newarray int
	astore_2
	aload_2
	iconst_0
	iconst_4
	iastore
	aload_2
	iconst_1
	iconst_5
	iastore
	aload_2
	iconst_2
	bipush 6
	iastore
.var 3 is i I from Label0 to Label1
	iconst_0
	istore_3
Label0:
	aload_1
	aload_2
	aload_1
	iconst_1
	bipush 10
	iastore
	iconst_0
	istore_3
Label2:
	iload_3
	iconst_3
	if_icmpge Label8
	iconst_1
	goto Label9
Label8:
	iconst_0
Label9:
	ifle Label3
	aload_1
	iload_3
	iaload
	invokestatic io/string_of_int(I)Ljava/lang/String;
	invokestatic io/print(Ljava/lang/String;)V
Label4:
	iload_3
	iconst_1
	iadd
	istore_3
	goto Label2
Label3:
Label5:
	invokestatic io/printLn()V
	iconst_0
	istore_3
Label10:
	iload_3
	iconst_3
	if_icmpge Label16
	iconst_1
	goto Label17
Label16:
	iconst_0
Label17:
	ifle Label11
	aload_1
	iload_3
	iaload
	invokestatic io/string_of_int(I)Ljava/lang/String;
	invokestatic io/print(Ljava/lang/String;)V
Label12:
	iload_3
	iconst_1
	iadd
	istore_3
	goto Label10
Label11:
Label13:
Label1:
	return
.limit stack 21
.limit locals 4
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
