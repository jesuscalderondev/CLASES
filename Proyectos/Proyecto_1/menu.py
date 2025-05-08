from app import productos, ventas, Producto, Compra, esValido
from datetime import datetime

while True: 

    print("""
1. Ver producto más vendido
2. Ver producto menos vendido
3. Gestionar inventario
4. Ver ganancias del día
5. Realizar venta
6. Salir
""")
    
    opcion = input("Opción: ")

    match opcion:
        


        case "1":

            if len(productos) > 0:
            
                masVendido = productos[0]

                for producto in productos:
                    
                    if producto.ventas >= masVendido.ventas:
                        masVendido = producto

                print(f"El más vendido es {masVendido.nombre} con {masVendido.ventas} unidades")
            
            else:
                print("No hay productos registrados")

        case "2":

            if len(productos) > 0:

                menosVendido = productos[0]
                
                for producto in productos:
                    if producto.ventas <= menosVendido.ventas:
                        menosVendido = producto
            
                print(f"El menos vendido es {menosVendido.nombre} con {menosVendido.ventas} unidades")
                
            else:
                print("No hay productos registrados")

        case "3":

            #¿Cuándo hago gestión de inventario?
            #1. Cuando agregamos productos
            #2. Cuando eliminamos productos
            #3. Cuando modificamos productos (cambiar nombre, precio o stock)
 
            while True:
                
                print("""   
1. Agregar producto
2. Eliminar producto
3. Modificar producto
4. Volver
""")
                opcionSub = input("Opción: ")

                #Match es como un switch que lo que hace es recuperar el valor de la variable y va a realizar alguna
                #acción dependiendo del valor de la misma
                match opcionSub:

                    case "1":

                        nombre = input("Ingrese el nombre: ")
                        precio = input("Ingrese el precio: ")
                        existencias = input("Ingrese las existencias: ")

                        precio = float(precio)
                        existencias = int(existencias)
                        
                        if esValido(nombre):
                            producto = Producto(nombre, precio, existencias)
                            productos.append(producto)
                            
                            print("El producto fue gregado.")

                        else:
                            print("El producto ya existe.")
                            

                    case "2":
                        
                        nombre = input("Ingrese el nombre: ")
                        existe = False

                        for producto in productos:
                            if producto.nombre == nombre:
                                producto.eliminar()
                                existe = True
                                print("El producto ha sido eliminado.")
                                break
                        
                        if not existe:
                            print("El producto solicitado no existe")
            

                    case "3":
                        #Yo pido el nombre actual del producto que quiero editar o actualizar
                        nombre = input("Ingrese el nombre del producto que desea modificar:  ")
                        existe = False
                        
                        #recorro la lista de productos
                        for producto in productos:

                            #comparo los nombres de los productos con el nombre que estoy buscando
                            if producto.nombre == nombre:

                                #Si yo entro aquí quiere decir que encontré el producto que estoy buscando

                                #Aquí pido el nuevo nombre que va a tener el producto
                                nuevoNombre = input("Ingrese el nuevo nombre, sino desea modificarlo presione 'Enter': ")
                                precio = input("Ingrese el nuevo precio, sino desea modificarlo presione 0 (cero) y luego 'Enter': ")
                                
                                precio = float(precio)
                                producto.actualizar(precio, nuevoNombre)
                                existe = True
                                print("El producto ha sido modificado")

                        if not existe:

                            print("El producto solicitado a modificar no existe")

                    
                    case "4":
                        break

                                
                    case _:
                        print("Opción incorrecta, por favor elige una de las anteriores.")
  
        case "4": #Ver ganancias del dia

            hoy = datetime.now().date()
            suma = 0
            
            for venta in ventas:

                if venta.fecha == hoy:
                    suma += venta.total

            print(f'Las ganancias del dia son: {suma}')
                

        case "5": #Realizar venta
            
            compra = Compra()

            while True:

                for indice in range(len(productos)):
                    producto = productos[indice] #obtengo el producto

                    #Se debe ver lo siguiente, de esta manera
                    # 1. El Nombre del Producto
                    # 2. El Nombre del Otro Producto
                    # 3. ETC.
                    print(f"{indice + 1}. {producto.nombre}")

                opcionProducto = input("¿Qué producto desea agregar a su carrito? Ejemplo: 2, si ya no desea agregar productos ingrese 0\nOpción: ")
                opcionProducto = int(opcionProducto)

                if opcionProducto == 0:
                    break

                productoAComprar = productos[opcionProducto - 1]

                unidades = input(f"¿Cuántas unidades desea comprar (Max. {productoAComprar.existencias})?")

                unidades = int(unidades)

                compra.agregarProducto(productoAComprar, unidades)
            
            pregunta = input("¿Desea retirar algún producto? Sí (s) o No (n)\nOpción: ")

            if pregunta.lower() == "s":

                while True:
                    
                    for indice in range(len(compra.productos)):

                        producto = compra.productos[indice] #obtengo el producto

                        #Se debe ver lo siguiente, de esta manera
                        # 1. El Nombre del Producto
                        # 2. El Nombre del Otro Producto
                        # 3. ETC.
                        print(f"{indice + 1}. {producto.nombre}")

                    opcionProducto = input("¿Qué producto desea retirar de su carrito? Ejemplo: 2, si ya no desea retirar productos ingrese 0\nOpción: ")
                    opcionProducto = int(opcionProducto)

                    if opcionProducto == 0:
                        break

                    productoRetirar = productos[opcionProducto - 1]

                    unidades = input(f"¿Cuántas unidades desea retirar?")

                    unidades = int(unidades)

                    compra.removerProducto(productoRetirar, unidades)
            
            ventas.append(compra)
            compra.mostrarFactura()

            pass

        case "6":
            break

        case _:
            print("La opcion ingresada es incorrecta")
            input("Presione Enter para continuar...")