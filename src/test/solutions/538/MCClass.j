.source MCClass.java
.class public MCClass
.super java.lang.Object

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
.var 1 is n F from Label0 to Label1
	ldc 101.0
	fstore_1
Label0:
	fload_1
	ldc 100.0
	fcmpl
	ifge Label7
	iconst_1
	goto Label8
Label7:
	iconst_0
Label8:
	ifle Label2
	fload_1
	ldc 3.3
	fmul
	fstore_1
	goto Label4
Label2:
	fload_1
	ldc 101.0
	fcmpl
	iflt Label11
	iconst_1
	goto Label12
Label11:
	iconst_0
Label12:
	ifle Label3
	fload_1
	ldc 5.3
	fdiv
	fstore_1
	goto Label4
Label3:
Label4:
	fload_1
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
