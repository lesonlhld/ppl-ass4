.source MCClass.java
.class public MCClass
.super java.lang.Object

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
.var 1 is i I from Label0 to Label1
	iconst_0
	istore_1
.var 2 is k I from Label0 to Label1
	bipush 10
	istore_2
.var 3 is a [I from Label0 to Label1
	iconst_5
	newarray int
	astore_3
	aload_3
	iconst_0
	iconst_0
	iastore
	aload_3
	iconst_1
	iconst_0
	iastore
	aload_3
	iconst_2
	iconst_0
	iastore
	aload_3
	iconst_3
	iconst_0
	iastore
	aload_3
	iconst_4
	iconst_0
	iastore
.var 4 is c Ljava/lang/String; from Label0 to Label1
	ldc "12"
	astore 4
Label0:
Label4:
	iload_1
	iload_2
	if_icmpeq Label2
	iconst_1
	goto Label3
Label2:
	iconst_0
Label3:
	ifle Label5
	aload_3
	iload_1
	iconst_4
	irem
	aload_3
	iload_1
	iconst_4
	irem
	iaload
	iload_1
	iadd
	aload 4
	invokestatic io/int_of_string(Ljava/lang/String;)I
	iadd
	iastore
	aload_3
	iload_1
	iconst_4
	irem
	iaload
	invokestatic io/string_of_int(I)Ljava/lang/String;
	invokestatic io/print(Ljava/lang/String;)V
	iload_1
	iconst_1
	iadd
	istore_1
Label6:
	goto Label4
Label5:
Label7:
Label1:
	return
.limit stack 15
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
