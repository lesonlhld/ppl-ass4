.source MCClass.java
.class public MCClass
.super java.lang.Object

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
.var 1 is x [[[I from Label0 to Label1
	iconst_2
	anewarray [[I
	dup
	iconst_0
	iconst_2
	anewarray [I
	dup
	iconst_0
	iconst_3
	newarray int
	dup
	iconst_0
	iconst_1
	iastore
	dup
	iconst_1
	iconst_2
	iastore
	dup
	iconst_2
	iconst_3
	iastore
	aastore
	dup
	iconst_1
	iconst_3
	newarray int
	dup
	iconst_0
	iconst_4
	iastore
	dup
	iconst_1
	iconst_5
	iastore
	dup
	iconst_2
	bipush 6
	iastore
	aastore
	aastore
	dup
	iconst_1
	iconst_2
	anewarray [I
	dup
	iconst_0
	iconst_3
	newarray int
	dup
	iconst_0
	bipush 7
	iastore
	dup
	iconst_1
	bipush 8
	iastore
	dup
	iconst_2
	bipush 9
	iastore
	aastore
	dup
	iconst_1
	iconst_3
	newarray int
	dup
	iconst_0
	bipush 10
	iastore
	dup
	iconst_1
	bipush 11
	iastore
	dup
	iconst_2
	bipush 12
	iastore
	aastore
	aastore
	astore_1
.var 2 is i I from Label0 to Label1
	iconst_0
	istore_2
.var 3 is j I from Label0 to Label1
	iconst_0
	istore_3
.var 4 is k I from Label0 to Label1
	iconst_0
	istore 4
.var 5 is sum I from Label0 to Label1
	iconst_0
	istore 5
Label0:
	iconst_0
	istore_2
Label2:
	iload_2
	iconst_2
	if_icmpge Label8
	iconst_1
	goto Label9
Label8:
	iconst_0
Label9:
	ifle Label3
	iconst_0
	istore_3
Label10:
	iload_3
	iconst_2
	if_icmpge Label16
	iconst_1
	goto Label17
Label16:
	iconst_0
Label17:
	ifle Label11
	iconst_0
	istore 4
Label18:
	iload 4
	iconst_3
	if_icmpge Label24
	iconst_1
	goto Label25
Label24:
	iconst_0
Label25:
	ifle Label19
	aload_1
	iload_2
	iload_3
	iload 4
	aload_1
	iload_2
	aaload
	iload_3
	aaload
	iload 4
	aaload
	iconst_2
	imul
	iconst_1
	iadd
	aastore
Label20:
	iload 4
	iconst_1
	iadd
	istore 4
	goto Label18
Label19:
Label21:
Label12:
	iload_3
	iconst_1
	iadd
	istore_3
	goto Label10
Label11:
Label13:
Label4:
	iload_2
	iconst_1
	iadd
	istore_2
	goto Label2
Label3:
Label5:
	iconst_0
	istore_2
Label26:
	iload_2
	iconst_2
	if_icmpge Label32
	iconst_1
	goto Label33
Label32:
	iconst_0
Label33:
	ifle Label27
	iconst_0
	istore_3
Label34:
	iload_3
	iconst_2
	if_icmpge Label40
	iconst_1
	goto Label41
Label40:
	iconst_0
Label41:
	ifle Label35
	iconst_0
	istore 4
Label42:
	iload 4
	iconst_3
	if_icmpge Label48
	iconst_1
	goto Label49
Label48:
	iconst_0
Label49:
	ifle Label43
	iload 5
	aload_1
	iload_2
	aaload
	iload_3
	aaload
	iload 4
	aaload
	iadd
	istore 5
Label44:
	iload 4
	iconst_1
	iadd
	istore 4
	goto Label42
Label43:
Label45:
Label36:
	iload_3
	iconst_1
	iadd
	istore_3
	goto Label34
Label35:
Label37:
Label28:
	iload_2
	iconst_1
	iadd
	istore_2
	goto Label26
Label27:
Label29:
	iload 5
	invokestatic io/string_of_int(I)Ljava/lang/String;
	invokestatic io/print(Ljava/lang/String;)V
Label1:
	return
.limit stack 46
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
