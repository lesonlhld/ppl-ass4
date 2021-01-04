.source MCClass.java
.class public MCClass
.super java.lang.Object

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
.var 1 is a I from Label0 to Label1
	iconst_0
	istore_1
Label0:
	ldc "True"
	invokestatic io/bool_of_string(Ljava/lang/String;)Z
	ifle Label2
.var 2 is b Ljava/lang/String; from Label0 to Label1
	ldc "hello"
	astore_2
	iload_1
	invokestatic io/float_to_int(I)F
	ldc 2.0
	fadd
	invokestatic io/string_of_float(F)Ljava/lang/String;
	invokestatic io/printStrLn(Ljava/lang/String;)V
	goto Label3
Label2:
Label3:
	iload_1
	invokestatic io/float_to_int(I)F
	ldc 2.0
	fadd
	invokestatic io/string_of_float(F)Ljava/lang/String;
	invokestatic io/print(Ljava/lang/String;)V
Label1:
	return
.limit stack 3
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
