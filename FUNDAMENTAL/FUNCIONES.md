# FUNCIONES

Las funciones son parte fundamental de la programación, ya que nos permiten ejecutar bloques de código de manera reiterada, si tener que volver a escribirlo. Estas además deben tener una sola intensión o proposito, para hacerla más simple, todas las funciones tienen partes que la conforman, como es el caso del nombre, parametros y valor a retornar.

En diferentes lenguajes las funciones tienen formas distintas de ser declaradas, pero eso sólo es en sintaxis, pues las partes siguen siendo las mismas.

## Declaración

### Python

```python
#Declaración de una función
def getMayor(lista: list) -> int:
    if len(lista) > 0:
        max = lista[0]
        
        for num in lista:
            if num > max:
                max = num
        return max
    return -1

```

La instrucción **def** define que lo que se va a declarar es una función luego del espacio se da el nombre que va a llevar la función, luego de esta entre los parentesis vamos a encontrar los parametros y opcional el tipo de dato de este, una vez cerrado los parentesis encontramos luego el tipo de dato que retorna la función, este es opcional y de no demarcarse se deja abierto el tipo de dato que retorna.

### Java

```java
public int getMayor(List<int> lista){
    if(lista.size() > 0){
        int max = lista.get(0)
        for(int i = 0; i < lista.size(); i++){
            if(lista.get(i) > max){
                max = lista.get(i);
            }
        }
        return max;
    }
    return -1;
}
```

Vemos que usamos el public, para definir que esta función se puede invocar en cualquier parte después de ser declarada, luego encontramos **int** que es el tipo de dato que retorna, si quisieramos que fuera un booleano sería **boolean**, luego están los parentesis que tiene los parámetros con su tipo de dato de manera obligatoria.

## Invocaciones
Una vez que está declarada debe poder llamarse, para que se ejecute, esto se logra con poner el nombre de la función y pasar los parámetros.

### Python

```python
lista = [3, 6, 2, 9, 5, 10, 1]

print(getMayor(lista)) #salida -> 10
```

### Java

```java
List<Integer> listaEnteros = new ArrayList<>(Arrays.asList(1, 2, 3, 4, 5));

System.out.println(getMayor(listaEnteros)); //salida -> 5
```