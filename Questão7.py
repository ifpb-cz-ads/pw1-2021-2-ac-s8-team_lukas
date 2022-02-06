def validar(max, min, palavra):
    tamanho = len(palavra)
    if tamanho >= max or tamanho <= min:
        print("Tamanho correto")
        return True
    else: 
        print("Tamanho errado")
        return False

palavra = "Teimoso"
min = 2
max = 6

validar(max, min, palavra)

