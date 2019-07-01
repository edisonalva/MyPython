# CORRIJA EL PROGRAMA
nterms = int(input("Ingrese el valor de m --> "))
n1=0
n2=1
count=0
if nterms <=0:
    print("Por favor ingrese un entero positivo")
elif nterms == 1:
    print("Serei de Fibonacci de ", nterms,":", n1)
    print(n1)
else:
     print("Serei de Fibonacci de ", nterms,":")
     while count < nterms:
        print(n1, end=' , ')
        nth = n1 + n2
        n1=n2
        n2=nth
        count +=1
