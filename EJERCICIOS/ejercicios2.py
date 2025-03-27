""" Crea una función que te permita seleccionar y retornar los valores positivos de una lista """

def obtenerNumerosPositivos(lista: list) -> list:
    listaAuxiliar = []
    
    #range es una función que solo recibe números, no listas, porque él crea la lista, ejemplo range(3) es [0, 1, 2]
    #para recorrer una lista usamos el (in), ya que eso dice (en lista = in lista)
    for i in lista:
        if i >= 0:
            listaAuxiliar.append(i)
    return listaAuxiliar

""" Crea una función que determine si un número es multiplo de otro """

def esMultiplo(num1, num2) -> bool:
    #Un número es multiplo de otro cuando al usar el modulo del primero en el segundo me da 0, ejemplo
    # 25 % 5 == 0, eso es un número que es multiplo, porque el 25 es multiplo de 5
    return num1 % num2 == 0


""" Crea una función que retorne los divisores de un número """

def obtenerDivisores(numero: int) -> list:
    listaAuxiliar = []
    
    #debemos pasar por todos los números desde el inicio hasta llegar al número que se nos pasó
    for i in range(numero +1):
    #el condicional va a ser si i es divisor del número
        if i != 0 and numero % i == 0:
            listaAuxiliar.append(i)
    return listaAuxiliar

""" Crea una función que determine la media de una lista de números, pero solo tenga en cuenta los negativos """
def obtenerMediaNegativos(lista: list) -> float:
    #para una media necesito la suma y la cantidad de numerosnume
    cantidad = 0
    suma = 0
    #cuando veas estos simbolos += significa que ese valor incrementa
    for numero in lista:
        if numero < 0:
            cantidad += 1
            suma += numero

    media = suma/cantidad
    return media


""" Define una función que retorne el exponencial de un número recibiendo el exponencial también
por ejemplo 5 a la 3 eso es igual a 5 * 5 * 5 = 125, exponencial 3 y el numero 5
4 a la 16 4 * 4 * 4 * 4...
2 a la 4 -> 2 * 2 * 2 * 2
"""

def obtenerExponencial(numero: int, exponente: int) ->int:
    resultado = 1

    #cuando me encuentro dentro un range un número al principio o una variab le, quiere decir que desde ahí va a empezar el for
    #minetras que el segundo valor o variable es donde se va a detener
    for contador in range(exponente):
        resultado = resultado * numero
    
    return resultado
