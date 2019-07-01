# CUAL ES LA SALIDA DEL PROGRAMA
# SI TIENE ERRORES CORRIJALOS
class InputOutString(object):
    def __init__(self):
        self.s = ""
    def getString(self):
        self.s = input()
        # t = self.s
    def printString(self):
        # l = t.upper()
        print(self.s.upper())
        # print(l)

strObj = InputOutString()
strObj.getString()
strObj.printString()
