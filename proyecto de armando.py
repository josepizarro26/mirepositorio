   while True:
        try:
            producto["codigo"]=int(input("Ingrese el codigo  del articulo:    "))
            producto["nombre"]=str(input("Ingrese el nombre del articulo:    "))
            producto["precio"]=int(input("Ingrese el precio del articulo:    "))
            producto["cantidad_inicial"]=int(input("Ingrese la cantidad del articulo:    "))
            producto["bodega"]=str(input("Ingrese el nombre de la bodega a la cual pertenece  el articulo:    "))
            producto["pasillo"]=int(input("Ingrese el numero del pasillo al cual pertenece el articulo:    "))                
            producto["estante"]=int(input("Ingrese el numero del estante al cual pertenece el articulo:    "))
            producto["ingresos"]=producto["cantidad_inicial"]
            return producto
            break
        except:
            print("******Los datos ingresados no son correctos, favor verificarlos y volver a intentarlos******")    

def agregarproducto():
    producto=diccionario()
    codigo=producto["codigo"]
    nombre=producto["nombre"]
    precio=producto["precio"]
    cantidad_inicial=producto["cantidad_inicial"]
    saldo=producto["cantidad_inicial"]
    sql="INSERT INTO existencias(codigo, nombre, precio, cantidad_inicial, saldo) VALUES(?,?,?,?,?)"
    parametros=(codigo, nombre, precio, cantidad_inicial, saldo)
    conexion_instancia = conexion()
    conexion_instancia.ejecutar_consulta(sql, parametros)
    bodega=producto["bodega"]
    pasillo=producto["pasillo"]
    estante=producto["estante"]
    sql="INSERT INTO movimientos(codigo,saldo, ventas, retiros, ingresos) VALUES(?,?,?,?,?)"
    ventas=producto["ventas"]
    retiros=producto["retiros"]
    ingresos=producto["ingresos"]
    parametros=(codigo,saldo, ventas, retiros, ingresos)
    conexion_instancia = conexion()
    conexion_instancia.ejecutar_consulta(sql, parametros)
    
    def __init__(self, codigo, nombre, precio, cantidad,bodega, pasillo, estante, saldo_actual,entrada_producto,salida_producto.venta):
        self.codigo = codigo
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad

    def __str__(self):
        return f"Código: {self.codigo}, Nombre: {self.nombre}, Precio: {self.precio}, Cantidad: {self.cantidad}"


def agregar_producto():
    codigo = input("Ingrese el código del producto: ")
    nombre = input("Ingrese el nombre del producto: ")
    while True:
        try:
            precio = float(input("Ingrese el precio del producto: "))
            break
        except ValueError:
            print("Por favor, ingrese un precio válido.")
    while True:
        try:
            cantidad = int(input("Ingrese la cantidad del producto: "))
            break
        except ValueError:
            print("Por favor, ingrese una cantidad válida.")

    producto = Producto(codigo, nombre, precio, cantidad)
    productos.append(producto)
    print("Producto agregado correctamente.")


def agregar_ubicacion():
    if not productos:
        print("No hay productos para asignar ubicación.")
        return

    print("Productos disponibles:")
    for i, producto in enumerate(productos):
        print(f"{i + 1}. {producto.nombre}")

    while True:
        try:
            index = int(input("Ingrese el número del producto al que desea asignar ubicación: ")) - 1
            if 0 <= index < len(productos):
                break
            else:
                print("Ingrese un número válido.")
        except ValueError:
            print("Por favor, ingrese un número válido.")

    bodega = input("Ingrese la bodega: ")
    pasillo = input("Ingrese el pasillo: ")
    estante = input("Ingrese el estante: ")

    ubicacion = {
        "bodega": bodega,
        "pasillo": pasillo,
        "estante": estante
    }
    ubicaciones.append(ubicacion)
    print("Ubicación asignada correctamente.")


def registrar_movimiento():
    if not productos:
        print("No hay productos para registrar movimientos.")
        return

    print("Productos disponibles:")
    for i, producto in enumerate(productos):
        print(f"{i + 1}. {producto.nombre}")

    while True:
        try:
            index = int(input("Ingrese el número del producto al que desea realizar un movimiento: ")) - 1
            if 0 <= index < len(productos):
                break
            else:
                print("Ingrese un número válido.")
        except ValueError:
            print("Por favor, ingrese un número válido.")

    producto_seleccionado = productos[index]
    print(f"Producto seleccionado: {producto_seleccionado}")

    print("Opciones de movimiento:")
    print("1. Retiro")
    print("2. Adición")
    print("3. Consulta general")
    print("4. Consulta específica")

    while True:
        try:
            opcion = int(input("Seleccione la opción de movimiento: "))
            if 1 <= opcion <= 4:
                break
            else:
                print("Ingrese una opción válida.")
        except ValueError:
            print("Por favor, ingrese un número válido.")

    if opcion == 1:  # Retiro
        cantidad_disponible = producto_seleccionado.cantidad
        if cantidad_disponible == 0:
            print("No hay existencia disponible para este producto.")
            return

        while True:
            try:
                cantidad_retiro = int(input(f"Ingrese la cantidad a retirar (disponible: {cantidad_disponible}): "))
                if 0 < cantidad_retiro <= cantidad_disponible:
                    break
                else:
                    print("Ingrese una cantidad válida.")
            except ValueError:
                print("Por favor, ingrese una cantidad válida.")

        producto_seleccionado.cantidad -= cantidad_retiro
        movimiento = {
            "tipo": "Retiro",
            "producto": producto_seleccionado.nombre,
            "cantidad": cantidad_retiro
        }
        movimientos.append(movimiento)
        print("Retiro registrado correctamente.")

    # Los otros casos (Adición, Consulta general, Consulta específica) podrían seguir aquí...


productos = []
ubicaciones = []
movimientos = []

while True:
    print("\nBienvenido al sistema de gestión de productos.")
    print("1. Agregar producto")
    print("2. Asignar ubicación")
    print("3. Registrar movimiento")
    print("4. Salir")

    try:
        opcion = int(input("Seleccione una opción: "))
        if opcion == 1:
            agregar_producto()
        elif opcion == 2:
            agregar_ubicacion()
        elif opcion == 3:
            registrar_movimiento()
        elif opcion == 4:
            print("¡Hasta luego!")
            break
        else:
            print("Ingrese una opción válida.")
    except ValueError:
        print("Por favor, ingrese un número válido.")
