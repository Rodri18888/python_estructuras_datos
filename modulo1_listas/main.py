# Definir inventario con tres productos [nombre, cantidad, precio]

inventario = [
    {"nombre": "camisas", "cantidad": 14, "precio": 30000},
    {"nombre": "pantalones", "cantidad": 23, "precio": 60000},
    {"nombre": "zapatos", "cantidad": 8, "precio": 100000}
]

# Definir actualizar_precio(producto, nuevo_precio)

def actualizar_precio(producto, nuevo_precio):
    for p in inventario:
        if p["nombre"] == producto:
            p["precio"] = nuevo_precio
            

# Definir registrar_venta(producto, cantidad)

def registrar_venta(producto, cantidad):
    for p in inventario:
        if p["nombre"] == producto:
            cantidad_actual = p["cantidad"]
            p["cantidad"] = cantidad_actual - cantidad
            
            
# Definir anadir_producto(producto, cantidad, precio)

def anadir_producto(producto, cantidad, precio):
    inventario.append({"nombre": producto, "cantidad": cantidad, "precio": precio})
    

# Definir mostrar_inventario()

def mostrar_inventario():
    print("---Inventario---")
    for p in inventario:
        print(f"Nombre: {p["nombre"]}, Cantidad: {p["cantidad"]} , Precio: {p["precio"]}")
        print()
      

# Llamar a actualizar_precio con el segundo producto

actualizar_precio("pantalones", 70000)


# Llamar a registrar_venta con el primer producto

registrar_venta("camisas", 6)


# Llamar a anadir_producto con un producto nuevo

anadir_producto("relojes", 8, 80000)


# Llamar a mostrar_inventario

mostrar_inventario()