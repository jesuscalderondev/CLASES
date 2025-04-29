# Proyecto #1

## Objetivo
Repasar lo visto en las diferentes clases, como, ciclos, tipos de datos, colecciones, clases, condicionales, etc

## Descripción
Realizar un programa que permita llevar un punto de venta, que debe cumplir los siguientes requerimientos en forma de historias de usuario

* Como usuario deseo tener un perfil de administrador que tenga las siguienetes funciones:
    - Registrar productos
    - Actualizar productos
    - Eliminar productos
    - Vender productos

* Como usuario de la aplicación deseo que tenga un menú para consultar los siguientes apartados
    - Producto más vendido
    - Producto menos vendido
    - Gestionar inventario (Sub menú)
    - Ganancias del día
    - Realizar venta


## ¿Qué necesitamos? (DISEÑO)

Necesitamos registrar los productos para poder llevar el inventario y también registrar cada venta para poder obtener los registros del producto más vendido, el menos vendido y también las ganancias del día

## ¿Cómo lo hacemos? (CONCEPCIÓN)

Lo haremos con clases, para encapsular los datos de cada objeto, en este caso, productos y ventas


```python

class Producto:
    
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio

producto1 = Producto("Mango", 500)
producto2 = Producto("Manzana", 900)
producto3 = Producto("Pera", 1000)

```

