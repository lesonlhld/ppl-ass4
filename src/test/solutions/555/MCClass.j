.source MCClass.java
.class public MCClass
.super java.lang.Object

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
.var 1 is x F from Label0 to Label1
	ldc 1.2
	fstore_1
.var 2 is a F from Label0 to Label1
	ldc 200.0
	fstore_2
.var 3 is b F from Label0 to Label1
	ldc 32.3
	fstore_3
Label0:
Label2:
	fload_2
	fload_3
	fadd
	fload_1
	fadd
	fstore_1
	ldc 1000.1
	fload_1
	fcmpl
	ifle Label3
	goto Label2
Label3:
Label5:
	fload_1
	invokestatic io/string_of_float(F)Ljava/lang/String;
	invokestatic io/print(Ljava/lang/String;)V
Label1:
	return
.limit stack 7
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
