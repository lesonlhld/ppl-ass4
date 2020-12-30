import sys,os
import subprocess

JASMIN_JAR = "./external/jasmin.jar"

class StaticError(Exception):pass
class IllegalOperandException(StaticError):
	def __init__(self,msg):
	# msg:string
		self.s = msg
	def __str__(self):
		return "Illegal Operand: " + self.s +"\n"
class IllegalRuntimeException(StaticError):
	def __init__(self,msg):
	# msg:string
		self.s = msg
	def __str__(self):
		return "Illegal Runtime: " + self.s +"\n"

def test(testNum):
    path = "./test/solutions/" + str(testNum)
    
    try:
        subprocess.call("java  -jar "+ JASMIN_JAR + " " + path + "/MCClass.j",shell=True,stderr=subprocess.STDOUT)
        
        subprocess.call("java -cp ./lib" + os.pathsep + ". MCClass",shell=True)
    except StaticError as e:
        print(str(e))
    except subprocess.CalledProcessError as e:
        raise RuntimeError("command '{}' return with error (code {}): {}".format(e.cmd, e.returncode, e.output))
    
if __name__ == "__main__":
   test(sys.argv[1])
