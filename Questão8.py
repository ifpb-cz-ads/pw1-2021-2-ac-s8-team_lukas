def encontra(palavra, lista):
    cont = 0
    for s in lista:
        if palavra in s:
            cont = cont + 1
            return True 
    if cont == 0:
        return False

palavra = "treino"
lista=["treino", "teste", "ok"]

if encontra(palavra, lista) == True:
    print("A palavra se encontra na lista")
else: print("A palavra não se encontra na lista")