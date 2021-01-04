.source MCClass.java
.class public MCClass
.super java.lang.Object

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
.var 1 is n I from Label0 to Label1
	iconst_0
	istore_1
.var 2 is t1 I from Label0 to Label1
	iconst_0
	istore_2
.var 3 is t2 I from Label0 to Label1
	iconst_1
	istore_3
.var 4 is nextTerm I from Label0 to Label1
	iconst_0
	istore 4
.var 5 is i I from Label0 to Label1
	iconst_0
	istore 5
Label0:
	ldc "Enter the number of terms: "
	invokestatic io/print(Ljava/lang/String;)V
	bipush 15
	istore_1
	ldc "Fibonacci Series: "
	invokestatic io/print(Ljava/lang/String;)V
	iload_1
	invokestatic io/string_of_int(I)Ljava/lang/String;
	invokestatic io/printStrLn(Ljava/lang/String;)V
	iconst_0
	istore 5
Label2:
	iload 5
	iload_1
	if_icmpge Label8
	iconst_1
	goto Label9
Label8:
	iconst_0
Label9:
	ifle Label3
	iload 5
	iconst_0
	if_icmpne Label14
	iconst_1
	goto Label15
Label14:
	iconst_0
Label15:
	ifle Label10
	iload_2
	invokestatic io/string_of_int(I)Ljava/lang/String;
	invokestatic io/print(Ljava/lang/String;)V
	goto Label4
	goto Label11
Label10:
Label11:
	iload 5
	iconst_1
	if_icmpne Label20
	iconst_1
	goto Label21
Label20:
	iconst_0
Label21:
	ifle Label16
	iload_3
	invokestatic io/string_of_int(I)Ljava/lang/String;
	invokestatic io/print(Ljava/lang/String;)V
	goto Label4
	goto Label17
Label16:
Label17:
	iload_2
	iload_3
	iadd
	istore 4
	iload_3
	istore_2
	iload 4
	istore_3
	iload 4
	invokestatic io/string_of_int(I)Ljava/lang/String;
	invokestatic io/print(Ljava/lang/String;)V
Label4:
	iload 5
	iconst_1
	iadd
	istore 5
	goto Label2
Label3:
Label5:
Label1:
	return
.limit stack 13
.limit locals 6
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
