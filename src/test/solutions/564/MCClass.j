.source MCClass.java
.class public MCClass
.super java.lang.Object

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
.var 1 is row I from Label0 to Label1
	iconst_2
	istore_1
.var 2 is col I from Label0 to Label1
	iconst_3
	istore_2
.var 3 is arr [[I from Label0 to Label1
	iconst_2
	iconst_3
	multianewarray [[I 2
	astore_3
	aload_3
	iconst_0
	aaload
	iconst_0
	iconst_1
	iastore
	aload_3
	iconst_0
	aaload
	iconst_1
	iconst_2
	iastore
	aload_3
	iconst_0
	aaload
	iconst_2
	iconst_3
	iastore
	aload_3
	iconst_1
	aaload
	iconst_0
	iconst_4
	iastore
	aload_3
	iconst_1
	aaload
	iconst_1
	iconst_5
	iastore
	aload_3
	iconst_1
	aaload
	iconst_2
	bipush 6
	iastore
.var 4 is sum I from Label0 to Label1
	iconst_0
	istore 4
.var 5 is i I from Label0 to Label1
	iconst_0
	istore 5
.var 6 is j I from Label0 to Label1
	iconst_0
	istore 6
Label0:
	iconst_0
	istore 5
Label2:
	iload 5
	iload_1
	if_icmpge Label6
	iconst_1
	goto Label7
Label6:
	iconst_0
Label7:
	ifle Label3
	iconst_0
	istore 6
Label8:
	iload 6
	iload_2
	if_icmpge Label12
	iconst_1
	goto Label13
Label12:
	iconst_0
Label13:
	ifle Label9
	iload 4
	aload_3
	iload 5
	aaload
	iload 6
	iaload
	iadd
	istore 4
Label10:
	iload 6
	iconst_1
	iadd
	istore 6
	goto Label8
Label9:
Label11:
Label4:
	iload 5
	iconst_1
	iadd
	istore 5
	goto Label2
Label3:
Label5:
	iload 4
	invokestatic io/string_of_int(I)Ljava/lang/String;
	invokestatic io/print(Ljava/lang/String;)V
Label1:
	return
.limit stack 23
.limit locals 7
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
