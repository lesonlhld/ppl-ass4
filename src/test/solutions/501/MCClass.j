.source MCClass.java
.class public MCClass
.super java.lang.Object
.field static x Ljava/lang/String;

.method public static main([Ljava/lang/String;)V
	ldc "hello"
	putstatic MCClass/x Ljava/lang/String;
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
	getstatic MCClass/x Ljava/lang/String;
	invokestatic io/print(Ljava/lang/String;)V
Label1:
	return
.limit stack 16
.limit locals 1
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
