class StaticError(Exception):pass
class IllegalOperandException(StaticError):
	def __init__(self,msg):
	# msg:string
		self.s = msg
	def __str__(self):
		return "IllegalOperandException(\"" + self.s +"\")"
class IllegalRuntimeException(StaticError):
	def __init__(self,msg):
	# msg:string
		self.s = msg
	def __str__(self):
		return "IllegalRuntimeException(\"" + self.s +"\")"