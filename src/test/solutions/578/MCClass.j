.source MCClass.java
.class public MCClass
.super java.lang.Object
.field static x [[I

.method public static main([Ljava/lang/String;)V
	iconst_2
	iconst_2
	multianewarray [[I 2
	putstatic MCClass/x [[I
	getstatic MCClass/x [[I
	iconst_0
	aaload
	iconst_0
	iconst_1
	iastore
	getstatic MCClass/x [[I
	iconst_0
	aaload
	iconst_1
	iconst_2
	iastore
	getstatic MCClass/x [[I
	iconst_1
	aaload
	iconst_0
	iconst_3
	iastore
	getstatic MCClass/x [[I
	iconst_1
	aaload
	iconst_1
	iconst_4
	iastore
.var 0 is args [Ljava/lang/String; from Label0 to Label1
.var 1 is i I from Label0 to Label1
	iconst_0
	istore_1
.var 2 is j I from Label0 to Label1
	iconst_0
	istore_2
Label0:
	iconst_0
	istore_1
Label2:
	iload_1
	iconst_2
	if_icmpge Label8
	iconst_1
	goto Label9
Label8:
	iconst_0
Label9:
	ifle Label3
	iconst_0
	istore_2
Label10:
	iload_2
	iconst_2
	if_icmpge Label16
	iconst_1
	goto Label17
Label16:
	iconst_0
Label17:
	ifle Label11
	getstatic MCClass/x [[I
	iload_1
	iload_2
	iload_1
	iload_2
	iadd
	aastore
Label12:
	iload_2
	iconst_1
	iadd
	istore_2
	goto Label10
Label11:
Label13:
Label4:
	iload_1
	iconst_1
	iadd
	istore_1
	goto Label2
Label3:
Label5:
	iconst_0
	istore_1
Label18:
	iload_1
	iconst_2
	if_icmpge Label24
	iconst_1
	goto Label25
Label24:
	iconst_0
Label25:
	ifle Label19
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
	getstatic MCClass/x [[I
	iload_1
	aaload
	iload_2
	iaload
	invokestatic io/string_of_int(I)Ljava/lang/String;
	invokestatic io/print(Ljava/lang/String;)V
Label28:
	iload_2
	iconst_1
	iadd
	istore_2
	goto Label26
Label27:
Label29:
Label20:
	iload_1
	iconst_1
	iadd
	istore_1
	goto Label18
Label19:
Label21:
Label1:
	return
.limit stack 21
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
