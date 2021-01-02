.source MCClass.java
.class public MCClass
.super java.lang.Object

.method public static abs(I)I
.var 0 is x I from Label0 to Label1
Label0:
	iload_0
	iconst_0
	if_icmplt Label4
	iconst_1
	goto Label5
Label4:
	iconst_0
Label5:
	ifle Label2
	iload_0
	ireturn
Label2:
	iload_0
	ineg
	ireturn
Label3:
Label1:
	return
.limit stack 4
.limit locals 1
.end method

.method public static ok(II[I)Z
.var 0 is x2 I from Label0 to Label1
.var 1 is y2 I from Label0 to Label1
.var 2 is a [I from Label0 to Label1
.var 3 is i I from Label0 to Label1
	iconst_0
	istore_3
Label0:
	iconst_1
	istore_3
Label2:
	iload_3
	iload_0
	if_icmpge Label6
	iconst_1
	goto Label7
Label6:
	iconst_0
Label7:
	ifle Label3
	aload_2
	iload_3
	iaload
	iload_1
	if_icmpne Label10
	iconst_1
	goto Label11
Label10:
	iconst_0
Label11:
	iload_3
	iload_0
	isub
	invokestatic MCClass/abs(I)I
	aload_2
	iload_3
	iaload
	iload_1
	isub
	invokestatic MCClass/abs(I)I
	if_icmpne Label12
	iconst_1
	goto Label13
Label12:
	iconst_0
Label13:
	ior
	ifle Label8
	iconst_0
	ireturn
Label8:
Label9:
Label4:
	iload_3
	iconst_1
	iadd
	istore_3
	goto Label2
Label3:
Label5:
	iconst_1
	ireturn
Label1:
.limit stack 12
.limit locals 4
.end method

.method public static xuat(I[I)V
.var 0 is n I from Label0 to Label1
.var 1 is a [I from Label0 to Label1
.var 2 is i I from Label0 to Label1
	iconst_0
	istore_2
Label0:
	iconst_1
	istore_2
Label2:
	iload_2
	iload_0
	if_icmpgt Label6
	iconst_1
	goto Label7
Label6:
	iconst_0
Label7:
	ifle Label3
	ldc " "
	invokestatic io/print(Ljava/lang/String;)V
	aload_1
	iload_2
	iaload
	invokestatic io/string_of_int(I)Ljava/lang/String;
	invokestatic io/print(Ljava/lang/String;)V
Label4:
	iload_2
	iconst_1
	iadd
	istore_2
	goto Label2
Label3:
Label5:
	invokestatic io/printLn()V
Label1:
	return
.limit stack 7
.limit locals 3
.end method

.method public static try(II[I)V
.var 0 is i I from Label0 to Label1
.var 1 is n I from Label0 to Label1
.var 2 is a [I from Label0 to Label1
.var 3 is j I from Label0 to Label1
	iconst_0
	istore_3
Label0:
	iconst_1
	istore_3
Label2:
	iload_3
	iload_1
	if_icmpgt Label6
	iconst_1
	goto Label7
Label6:
	iconst_0
Label7:
	ifle Label3
	iload_0
	iload_3
	aload_2
	invokestatic MCClass/ok(II[I)Z
	ifle Label8
	aload_2
	iload_0
	iload_3
	iastore
	iload_0
	iload_1
	if_icmpne Label12
	iconst_1
	goto Label13
Label12:
	iconst_0
Label13:
	ifle Label10
	iload_1
	aload_2
	invokestatic MCClass/xuat(I[I)V
	goto Label11
Label10:
Label11:
	iload_0
	iconst_1
	iadd
	iload_1
	aload_2
	invokestatic MCClass/try(II[I)V
	goto Label9
Label8:
Label9:
Label4:
	iload_3
	iconst_1
	iadd
	istore_3
	goto Label2
Label3:
Label5:
Label1:
	return
.limit stack 12
.limit locals 4
.end method

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
.var 1 is a [I from Label0 to Label1
	bipush 20
	newarray int
	astore_1
	aload_1
	iconst_0
	iconst_0
	iastore
	aload_1
	iconst_1
	iconst_0
	iastore
	aload_1
	iconst_2
	iconst_0
	iastore
	aload_1
	iconst_3
	iconst_0
	iastore
	aload_1
	iconst_4
	iconst_0
	iastore
	aload_1
	iconst_5
	iconst_0
	iastore
	aload_1
	bipush 6
	iconst_0
	iastore
	aload_1
	bipush 7
	iconst_0
	iastore
	aload_1
	bipush 8
	iconst_0
	iastore
	aload_1
	bipush 9
	iconst_0
	iastore
	aload_1
	bipush 10
	iconst_0
	iastore
	aload_1
	bipush 11
	iconst_0
	iastore
	aload_1
	bipush 12
	iconst_0
	iastore
	aload_1
	bipush 13
	iconst_0
	iastore
	aload_1
	bipush 14
	iconst_0
	iastore
	aload_1
	bipush 15
	iconst_0
	iastore
	aload_1
	bipush 16
	iconst_0
	iastore
	aload_1
	bipush 17
	iconst_0
	iastore
	aload_1
	bipush 18
	iconst_0
	iastore
	aload_1
	bipush 19
	iconst_0
	iastore
.var 2 is n I from Label0 to Label1
	iconst_5
	istore_2
Label0:
	iconst_1
	iload_2
	aload_1
	invokestatic MCClass/try(II[I)V
Label1:
	return
.limit stack 25
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
