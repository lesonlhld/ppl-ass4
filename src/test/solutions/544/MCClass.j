.source MCClass.java
.class public MCClass
.super java.lang.Object

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
.var 1 is n I from Label0 to Label1
	iconst_1
	istore_1
.var 2 is i F from Label0 to Label1
	ldc 5.5
	fstore_2
Label0:
	ldc 4.5
	fload_2
	fcmpl
	ifle Label2
	fload_2
	invokestatic io/string_of_float(F)Ljava/lang/String;
	invokestatic io/printStrLn(Ljava/lang/String;)V
	goto Label4
Label2:
	iload_1
	bipush 10
	if_icmple Label7
	iconst_1
	goto Label8
Label7:
	iconst_0
Label8:
	ifle Label3
	ldc "Else If"
	invokestatic io/print(Ljava/lang/String;)V
	goto Label4
Label3:
	fload_2
	invokestatic io/int_of_float(F)I
	iconst_1
	isub
	istore_1
	iload_1
	invokestatic io/string_of_int(I)Ljava/lang/String;
	invokestatic io/print(Ljava/lang/String;)V
Label4:
Label1:
	return
.limit stack 6
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
