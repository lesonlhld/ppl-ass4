.source MCClass.java
.class public MCClass
.super java.lang.Object
.field static arr [[I

.method public static foo()[[I
Label0:
	getstatic MCClass/arr [[I
	areturn
Label1:
.limit stack 2
.limit locals 0
.end method

.method public static main([Ljava/lang/String;)V
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
	putstatic MCClass/arr [[I
.var 0 is args [Ljava/lang/String; from Label0 to Label1
.var 1 is x I from Label0 to Label1
	iconst_1
	istore_1
.var 2 is i I from Label0 to Label1
	iconst_0
	istore_2
.var 3 is j I from Label0 to Label1
	iconst_0
	istore_3
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
	iconst_3
	if_icmpge Label16
	iconst_1
	goto Label17
Label16:
	iconst_0
Label17:
	ifle Label11
	invokestatic MCClass/foo()[[I
	iload_2
	aaload
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
Label4:
	iload_2
	iconst_1
	iadd
	istore_2
	goto Label2
Label3:
Label5:
	invokestatic io/printLn()V
	invokestatic MCClass/foo()[[I
	iload_1
	iconst_1
	isub
	iload_1
	iconst_1
	iadd
	bipush 7
	aastore
	iconst_0
	istore_2
Label18:
	iload_2
	iconst_2
	if_icmpge Label24
	iconst_1
	goto Label25
Label24:
	iconst_0
Label25:
	ifle Label19
	iconst_0
	istore_3
Label26:
	iload_3
	iconst_3
	if_icmpge Label32
	iconst_1
	goto Label33
Label32:
	iconst_0
Label33:
	ifle Label27
	invokestatic MCClass/foo()[[I
	iload_2
	aaload
	iload_3
	iaload
	invokestatic io/string_of_int(I)Ljava/lang/String;
	invokestatic io/print(Ljava/lang/String;)V
Label28:
	iload_3
	iconst_1
	iadd
	istore_3
	goto Label26
Label27:
Label29:
Label20:
	iload_2
	iconst_1
	iadd
	istore_2
	goto Label18
Label19:
Label21:
Label1:
	return
.limit stack 55
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
