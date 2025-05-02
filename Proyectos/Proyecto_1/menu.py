from app import productos, Producto, Compra

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
            pass
        
        case "4":
            pass

        case "5":
            pass

        case "6":
            break

        case _:
            print("La opcion ingresada es incorrecta")
            input("Presione Enter para continuar...")