import sys
fichero = open("contador.txt","a+")
fichero.seek(0)
content = fichero.readline()
if len(content)==0:
    content="0"
    fichero.write(content)
fichero.close()
try:
    contador=int(content)
    if len(sys.argv)==2:
        if sys.argv[1]=="inc":
            contador=contador+1
        elif sys.argv[1]=="dec":
            contador=contador-1
    print(contador)
    fichero=open("contador.txt","w")
    fichero.write(str(contador))
    fichero.close()
except:
    print("Error") 
