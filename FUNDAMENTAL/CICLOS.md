# CICLOS

## FOR

### ¿Qué es?
Es una instrucción que contiene un bloque de código que se ejectutará siempre y cuando se cumpla la condición declarada en su parametro, esta mayormente es repetitiva, es decir que se ejecutará de manera finita.

### ¿Cuándo usar?
Un for debe usarse o es recomendado usarlo cuando hay una acción repetitiva y determinada por una cantidad, sea por medida de un arreglo, lista o lo que se pueda determinar como una colección de datos, tiene partes fundamentales cómo lo son la inciación de una variable que funcionaría como iteradora, otra parte que es la condicional y la encargada de que se ejecute el ciclo de manera finita, esta va relacionada directamente con la variable iteradora, por ultimo la instrucción de incremento o decremento según se requiera, esto para poder cumplir también con la finalización del ciclo, ya que sin esta no habría cambio en el valor del iterador.

### Ejemplo de uso

```python
sueldoInicial = 500
for mes in range(12):
    sueldoDelMes = sueldoInicial + mes * 5
```

## WHILE

### ¿Qué es?
En su traducción al español es mientras, entonces mientras se cumple la condición esta permanecerá activa, ejecutando también un bloque de código hasta que no sea válida la condición.

### ¿Cuándo se usa?
Se usa mayormente cuando se quiere crear un bucle infinito o que sea persistente y no vaya con una variable númerica.

### Ejemplo de uso

```python
salir = False

while(salir == False):
    nombre = input("Ingrese el nombre del paciente: ")

    respuesta = input("Desea agregar un nuevo paciente\n[Y/N]: ")

    salir = respuesta == "N"
```