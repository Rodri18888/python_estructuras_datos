# Definir ventas con 6 productos (producto, unidades, precio, categoria)

ventas = [
    {"nombre": "Laptop", "precio": 1200, "unidades": 5, "categoria": "Electronica"},
    {"nombre": "Mouse", "precio": 25, "unidades": 50, "categoria": "Accesorios"},
    {"nombre": "Teclado", "precio": 45, "unidades": 20, "categoria": "Accesorios"},
    {"nombre": "Monitor", "precio": 300, "unidades": 10, "categoria": "Electronica"},
    {"nombre": "Cable HDMI", "precio": 15, "unidades": 100, "categoria": "Accesorios"},
    {"nombre": "Silla Gamer", "precio": 250, "unidades": 4, "categoria": "Muebles"}
]

# List comp: valor_total = unidades * precio

valor_total = [float(v["precio"]) * int(v["unidades"]) for v in ventas]
print(f"Valores totales: {valor_total}")
print()

# List comp con filtro: productos_destacados (valor > 1000)

productos_destacados = [v["nombre"] for v in ventas if(float(v["precio"]) * int(v["unidades"])) > 1000]
print(f"Productos destacados (>1000): {productos_destacados}")
print()

# Dict comp: producto_info  nombre: {valor, unidades}

producto_info = { v["nombre"]: {"valor": float(v["precio"]) * int(v["unidades"]), "unidades": int(v["unidades"])} for v in ventas}
print(f"Info detallada: {producto_info}")
print()

# Dict comp con filtro: ranking_premium (precio > 50) desc

premium_raw = {v["nombre"]: float(v["precio"]) * float(v["unidades"]) for v in ventas if (float(v["precio"])) > 50}

ranking_premium = dict(sorted(premium_raw.items(), key=lambda item: item[1], reverse=True))
print(f"Ranking Premium: {ranking_premium}")
print()

# Set comp: categorias_unicas

categorias_unicas = {v["categoria"] for v in ventas}
print(f"Categorías presentes: {categorias_unicas}")
print()

# Set comp con filtro: productos_baratos (precio <= 50)

productos_baratos = {v["nombre"] for v in ventas if (float(v["precio"])) <= 50}
print(f"Set de productos económicos: {productos_baratos}")
print()

# Combinar: resumen_formateado dict comp filtrado

resumen_formateado = [f"{str(v['nombre']).upper()}: ${float(v['precio']) * float(v['unidades'])}" for v in ventas]

# Calcular e imprimir gran_total

gran_total = sum([float(v["precio"]) * int(v["unidades"]) for v in ventas])

print("RESUMEN DE VENTAS")
for linea in resumen_formateado:
    print(linea)
print("-" * 25)
print(f"TOTAL GENERAL: ${gran_total}")