from datetime import datetime

#Definir clases

class Producto:

    # Esto se conoce como método constructor y sirve para iniciar un objeto del tipo de la clase
    # En los parametros se indica lo que necesita como mínimo para poder crear el objeto
    def __init__(self, nombre:str, precio:float, existencias:int):
        self.nombre = nombre
        self.precio = precio
        self.existencias = existencias
        self.ventas = 0 #Unidades vendidas

    def vender(self, unidades:int) -> bool:

        if self.existencias >= unidades:
            self.existencias -= unidades      # los dos puntos condicionales, ciclos y funciones
            self.ventas += unidades

        else:
            return False
        
        return True
    
    def devolver(self, unidades:int) -> bool:
        
        if self.ventas >= unidades:

            self.existencias += unidades # aquí recuperas las unidades en el inventario
            self.ventas -= unidades
        
        else:
            return False
        
        return True

class Compra:

    productos = {} #colección, cualquier colección puede ser iterada
    total = 0
    fecha = datetime.now()

    def agregarProducto(self, producto:Producto, unidades:int):

        if producto.vender(unidades):

            if producto.nombre in self.productos:
                self.productos[producto.nombre]["unidades"] += unidades
            else:
                self.productos[producto.nombre] = {}
                self.productos[producto.nombre]["unidades"] = unidades
            
            self.productos[producto.nombre]["precio"] = producto.precio

            self.total += producto.precio * unidades
            print(f"Se han vendido {unidades} unidades de {producto.nombre}.")

        else:
            print(f"No hay suficientes existencias de {producto.nombre}, solo quedan {producto.existencias} unidades.")

    def removerProducto(self, producto:Producto, unidades:int):
        
        if producto.nombre in self.productos:
            if producto.devolver(unidades):
                self.productos[producto.nombre]["unidades"] -= unidades
                self.total -= producto.precio * unidades
            
                print(f"Se han removido {unidades} unidades de {producto.nombre}.")
            else:
                print("No se pudieron remover las {} unidades de {}, porque solo hay {} unidades vendidas.".format(unidades, producto.nombre, self.productos[producto.nombre]))

    def mostrarFactura(self):

        print("Factura")

        #esto es un for que se ejecuta tantas veces como productos existan en la compra
        for producto in self.productos:
            #precio x unidades ... subtotal
            print("{} x {} ... ${}".format(
                producto,
                self.productos[producto]["unidades"],
                self.productos[producto]["precio"] * self.productos[producto]["unidades"]
            ))

        #debe mostrarme así ->  Total:    $3000
        print(f"Total: ${self.total}")


mango = Producto("Mango", 500, 10)
compra = Compra()
compra.agregarProducto(mango, 7)
print(compra.total)
compra.removerProducto(mango, 4)
compra.agregarProducto(mango, 2)
compra.mostrarFactura()