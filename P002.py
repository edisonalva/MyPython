# CUAL ES LA SALIDA
l=[]
for i in range(100,150):
    if(i%7==0) and (i%5!=0):
        l.append(str(i))
t=','.join(l)
print(t)
