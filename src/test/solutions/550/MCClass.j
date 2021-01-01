.source MCClass.java
.class public MCClass
.super java.lang.Object

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
.var 1 is x I from Label0 to Label1
	iconst_5
	istore_1
Label0:
Label2:
	iconst_1
	ifle Label3
Label8:
	iload_1
	iconst_0
	if_icmplt Label6
	iconst_1
	goto Label7
Label6:
	iconst_0
Label7:
	ifle Label9
	iload_1
	iconst_2
	ineg
	iadd
	istore_1
Label10:
	goto Label8
Label9:
Label11:
	iload_1
	iconst_0
	if_icmpge Label14
	iconst_1
	goto Label15
Label14:
	iconst_0
Label15:
	ifle Label12
	goto Label5
	goto Label13
Label12:
Label13:
Label4:
	goto Label2
Label3:
Label5:
	iload_1
	invokestatic io/float_to_int(I)F
	invokestatic io/string_of_float(F)Ljava/lang/String;
	invokestatic io/print(Ljava/lang/String;)V
Label1:
	return
.limit stack 8
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
