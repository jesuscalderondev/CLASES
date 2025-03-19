# CDIO

## Concepción
que es donde imaginamos cómo hacerlo, más no con qué

## Diseño
que se va a utilizar para hacerlo *

## Implementación
programar el código

## Operar
probarlo o testearlo

### Ejemplo

*C:* debo buscar entre todos los usuarios cuál tiene ese número de telefono y la contraseña

*D:* sé que debo utilizar un ciclo para pasar por cada uno de los usuarios y verificar sus datos, para esto utilizaría un if

*I:*

```java
for(int i = 0; i < usuarios.size(); i++){
    Usuario usuario = usuarios.get(i);
    if(usuario.getTelefono() == telefono && usuario.getContrasena().equals(contrasena)){
        //Lo llevamos a la ventana de inicio
    }
}
```

## ¿Cuándo usar un for?

Un for debe usarse o es recomendado usarlo cuando hay una acción repetitiva y determinada por una cantidad, sea por medida de un arreglo, lista o lo que se pueda determinar como una colección de datos, tiene partes fundamentales cómo lo son la inciación de una variable que funcionaría como iteradora, otra parte que es la condicional y la encargada de que se ejecute el ciclo de manera finita, esta va relacionada directamente con la variable iteradora, por ultimo la instrucción de incremento o decremento según se requiera, esto para poder cumplir también con la finalización del ciclo, ya que sin esta no habría cambio en el valor del iterador.

### Ejemplo

Si quisiera mostrar la información de los productos que tengo en mi lista debería verse algo así 

```java
for(int i = 0; i < productos.size(); i++;){
    System.out.println(productos.get(i).getNombre())
}
```


## Pendiente

Crear un script que me permita sumar la nota de N cantidad de estudiantes, sabiendo que con N cantidad, me refiero a una cantidad cualquiera, que puede ser 5 o 10 o 20 o 3.

Para esto deberías usar ciclos, entradas por teclado (scanner), operaciones como suma y división. Debes justificar por qué cada paso, con tus palabras.