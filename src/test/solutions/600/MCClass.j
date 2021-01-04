.source MCClass.java
.class public MCClass
.super java.lang.Object

.method public static abs(I)I
.var 0 is x I from Label0 to Label1
Label0:
	iload_0
	iconst_0
	if_icmplt Label6
	iconst_1
	goto Label7
Label6:
	iconst_0
Label7:
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
	if_icmpge Label8
	iconst_1
	goto Label9
Label8:
	iconst_0
Label9:
	ifle Label3
	aload_2
	iload_3
	iaload
	iload_1
	if_icmpne Label14
	iconst_1
	goto Label15
Label14:
	iconst_0
Label15:
	ifgt Label20
	iconst_0
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
	if_icmpne Label18
	iconst_1
	goto Label19
Label18:
	iconst_0
Label19:
	ior
	goto Label21
Label20:
	iconst_1
Label21:
	ifle Label10
	iconst_0
	ireturn
Label10:
Label11:
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
	if_icmpgt Label8
	iconst_1
	goto Label9
Label8:
	iconst_0
Label9:
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
.limit stack 6
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
	if_icmpgt Label8
	iconst_1
	goto Label9
Label8:
	iconst_0
Label9:
	ifle Label3
	iload_0
	iload_3
	aload_2
	invokestatic MCClass/ok(II[I)Z
	ifle Label10
	aload_2
	iload_0
	iload_3
	iastore
	iload_0
	iload_1
	if_icmpne Label16
	iconst_1
	goto Label17
Label16:
	iconst_0
Label17:
	ifle Label12
	iload_1
	aload_2
	invokestatic MCClass/xuat(I[I)V
	goto Label13
Label12:
Label13:
	iload_0
	iconst_1
	iadd
	iload_1
	aload_2
	invokestatic MCClass/try(II[I)V
	goto Label11
Label10:
Label11:
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
.limit stack 11
.limit locals 4
.end method

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
.var 1 is a [I from Label0 to Label1
	bipush 20
	newarray int
	dup
	iconst_0
	iconst_0
	iastore
	dup
	iconst_1
	iconst_0
	iastore
	dup
	iconst_2
	iconst_0
	iastore
	dup
	iconst_3
	iconst_0
	iastore
	dup
	iconst_4
	iconst_0
	iastore
	dup
	iconst_5
	iconst_0
	iastore
	dup
	bipush 6
	iconst_0
	iastore
	dup
	bipush 7
	iconst_0
	iastore
	dup
	bipush 8
	iconst_0
	iastore
	dup
	bipush 9
	iconst_0
	iastore
	dup
	bipush 10
	iconst_0
	iastore
	dup
	bipush 11
	iconst_0
	iastore
	dup
	bipush 12
	iconst_0
	iastore
	dup
	bipush 13
	iconst_0
	iastore
	dup
	bipush 14
	iconst_0
	iastore
	dup
	bipush 15
	iconst_0
	iastore
	dup
	bipush 16
	iconst_0
	iastore
	dup
	bipush 17
	iconst_0
	iastore
	dup
	bipush 18
	iconst_0
	iastore
	dup
	bipush 19
	iconst_0
	iastore
	astore_1
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
