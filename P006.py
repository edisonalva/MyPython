# QUE HACE EL SIGUIENTE PROGRAMA
# MUESTRE LA SALIDA
def hacealgo(li):
    newli=[]
    seen = set()
    for item in li:
        if item not in seen:
            seen.add(item)
            newli.append(item)
    return newli

li=[12,24,35,24,88,120,155,88,120,155]
print(hacealgo(li))
