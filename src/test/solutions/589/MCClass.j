.source MCClass.java
.class public MCClass
.super java.lang.Object
.field static arr [I

.method public static sort([I)[I
.var 0 is arr [I from Label0 to Label1
.var 1 is i I from Label0 to Label1
	bipush 50
	istore_1
Label0:
	iconst_0
	istore_1
Label2:
	iload_1
	iconst_5
	if_icmpge Label8
	iconst_1
	goto Label9
Label8:
	iconst_0
Label9:
	ifle Label3
.var 2 is j I from Label0 to Label1
	iconst_3
	istore_2
	iload_1
	iconst_1
	iadd
	istore_2
Label10:
	iload_2
	iconst_5
	if_icmpge Label16
	iconst_1
	goto Label17
Label16:
	iconst_0
Label17:
	ifle Label11
	aload_0
	iload_1
	iaload
	aload_0
	iload_2
	iaload
	if_icmpge Label22
	iconst_1
	goto Label23
Label22:
	iconst_0
Label23:
	ifle Label18
.var 3 is temp I from Label0 to Label1
	iconst_0
	istore_3
	aload_0
	iload_1
	iaload
	istore_3
	aload_0
	iload_1
	aload_0
	iload_2
	iaload
	iastore
	aload_0
	iload_2
	iload_3
	iastore
	goto Label19
Label18:
Label19:
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
	aload_0
	areturn
Label1:
.limit stack 17
.limit locals 4
.end method

.method public static main([Ljava/lang/String;)V
	iconst_5
	newarray int
	dup
	iconst_0
	iconst_5
	iastore
	dup
	iconst_1
	bipush 7
	iastore
	dup
	iconst_2
	iconst_1
	iastore
	dup
	iconst_3
	iconst_2
	iastore
	dup
	iconst_4
	bipush 6
	iastore
	putstatic MCClass/arr [I
.var 0 is args [Ljava/lang/String; from Label0 to Label1
.var 1 is i I from Label0 to Label1
	bipush 100
	istore_1
Label0:
	iconst_0
	istore_1
Label2:
	iload_1
	iconst_5
	if_icmpge Label8
	iconst_1
	goto Label9
Label8:
	iconst_0
Label9:
	ifle Label3
	getstatic MCClass/arr [I
	iload_1
	iaload
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
	invokestatic io/printLn()V
	getstatic MCClass/arr [I
	invokestatic MCClass/sort([I)[I
	getstatic MCClass/arr [I
	iconst_0
	istore_1
Label10:
	iload_1
	iconst_5
	if_icmpge Label16
	iconst_1
	goto Label17
Label16:
	iconst_0
Label17:
	ifle Label11
	getstatic MCClass/arr [I
	iload_1
	iaload
	invokestatic io/string_of_int(I)Ljava/lang/String;
	invokestatic io/print(Ljava/lang/String;)V
Label12:
	iload_1
	iconst_1
	iadd
	istore_1
	goto Label10
Label11:
Label13:
Label1:
	return
.limit stack 35
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
