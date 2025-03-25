""" #1 Crea una función que retorne los elementos pares de una lista """

""" Opción #1 """
def getPares(lista:list) -> list:
    #En esta lista vamos a guardar los número pares que encontremos en la lista que se nos ha pasado
    listaAuxiliar = []

    #En este ciclo vamos a recorrer la lista de números que se nos pasa
    for num in lista:
        #Si el número es par lo agregamos, ya que el % representa el módulo, es decir si al dividir el número por 2 el
        #residuo es 0, entonces es par y lo agregamos a la lita
        if num % 2 == 0:
            listaAuxiliar.append(num)
    
    return listaAuxiliar

lista = [1, 2, 3, 4, 5, 6, 7, 8]

print(getPares(lista))


""" #2 Crea una función que reciba 2 números y retorne el mayor de ellos """

""" Opción #1 """
def getMayor(num1, num2):
    #Si el número uno es mayor que el número dos nos regresa el valor del número uno, de lo contrario nos retorna el número 2
    return num1 if num1 > num2 else num2

""" Opción #2 """
def getMayor2(num1, num2):
    #Preguntamos si el número uno es mayor que el número 2 y de ser así retornamos el primero, de lo contrario no entra al condicioanl
    if num1 > num2 :
        return num1
    
    #al no pasar por el condicional automaticamente devuelve el segundo
    return num2

""" #3 Crea una función que retorne verdadero o falso según si un número es positivo o no """
def isPositivo(num) -> bool:
    #Por defecto los operadores como >, <, <=, >=, ==, not, son operadores booleanos y nos retornan valores de verdad
    #o sea, verdadero o falso (True o False), por lo que si preguntamos si número es mayor o igual que 0 y es verdadero
    #entonces es positivo o de no es negativo, por eso no hay necesidad de preguntar, sino devolver el resultado de inmediato
    return num >= 0

""" #4 Crea una función que dado un número retorne una lista de números que vayan desde el 0 hasta el número dado """

""" Opción #1 """
def getNumerosAntecesores(num: int) -> list:
    #Esta sentencia lo que hace es crear una lista, y el for se encarga de darle valor al elemento que está a su izquierda
    #según el valor que tenga el tope, en este caso va desde 0 hasta el valor del número más uno, porque recordemos que el
    #for no llega hasta el limite, sino que se queda una unidad atrás
    return [i for i in range(num+1)]

""" Opción #2 """
def getNumerosAntecesores2(num: int) -> list:
    #Iniciamos nuestar lista auxiliar vacía, para guardar los valore
    listaAntecesores = []

    #con el for vamos a recorrer desde el 0 hasta el número que se nos indica:
    for i in range(num + 1 ):
        #alamacenamos nuestro valor
        listaAntecesores.append(i)
    
    #al terminar el ciclo, como ya alcanzamso el número podemos devolver el listado
    return listaAntecesores