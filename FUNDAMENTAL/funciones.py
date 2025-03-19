numeroMaximo = 2

def getNumeroMaximo(lista:list)->int:
    numeroMaximo = lista[0]
    for i in lista:
        if i > numeroMaximo:
            numeroMaximo = i
    return numeroMaximo

def printNumeroPrimo(lista:list):
    for num in lista:
        if num != 1:
            divisores = 1
            for mod in range(2, num + 1):
                if num % mod == 0:
                    divisores += 1
            if divisores == 2:
                print(num)
                break
        else:
            print(num)
            break

""" Crea una función que reciba una lista de números, que retorne el número de elementos
mayores que 8 """

def getNumeroMayorOcho(lista:list)->int:
    count = 0
    for i in lista:
        if i > 8:
            count += 1
    return count

def getNumerosMayorOcho(lista: list)-> list:
    numeromayoresocho = []
    for i in lista:
        if i > 8:
            numeromayoresocho.append(i)
    return numeromayoresocho

    
def printNumeroTablaMultiplicar(numero: int):
    for i in range(1, 11):
        print(numero, "x", i, "=", numero*i)

def hacerOperaciones(numero1: int, numero2:int):
    if numero2 > 0:
        print("Suma:", numero1 + numero2)
        print("Resta:", numero1 - numero2)
        print("Multiplicación:", numero1 * numero2)
        print("División:", numero1 / numero2)
    else:
        print("La división entre 0 no se puede realizar")
