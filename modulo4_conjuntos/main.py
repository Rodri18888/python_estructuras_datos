# Definir tienda_centro, tienda_norte y tienda_sur

tienda_centro = {"camisa", "pantalon", "zapatos", "reloj", "gorra", "abrigo"}
tienda_norte = {"pantalon", "gorra", "chaqueta", "reloj", "calcetines", "correa"}
tienda_sur = {"zapatos", "calcetines", "bufanda", "camisa", "pantalon"}

# Calcular catalogo_completo con union()

catalogo_completo = tienda_centro.union(tienda_norte, tienda_sur)
print("CATALOGO COMPLETO")
print(catalogo_completo)
print()

# Calcular productos_comunes con intersection()

productos_comunes = tienda_centro.intersection(tienda_norte, tienda_sur)
print("PRODUCTOS COMUNES")
print(productos_comunes)
print()

# Exclusivos de cada tienda con difference(union())


productos_exclusivos_centro = tienda_centro.difference(tienda_norte, tienda_sur)
productos_exclusivos_norte = tienda_norte.difference(tienda_centro, tienda_sur)
productos_exclusivos_sur = tienda_sur.difference(tienda_centro, tienda_norte)



productos_exclusivos = productos_exclusivos_centro.union(productos_exclusivos_norte, productos_exclusivos_sur)
print("PRODUCTOS EXCLUSIVOS")
print(f"Tienda centro: {productos_exclusivos_centro}")
print(f"Tienda sur: {productos_exclusivos_sur}")
print(f"Tienda norte: {productos_exclusivos_norte}")
print(f"Todas las tiendas: {productos_exclusivos}")
print()


# Verificar pares con isdisjoint()

print("PARES")
print(tienda_centro.isdisjoint(tienda_norte))
print(tienda_centro.isdisjoint(tienda_sur))
print(tienda_norte.isdisjoint(tienda_sur))
print()

# Definir usuario1, usuario2, usuario3

usuario1 = {"Terror", "Ciencia Ficción", "Acción", "Drama"}
usuario2 = {"Comedia", "Drama", "Romance", "Acción", "Ciencia Ficción"}
usuario3 = {"Documental", "Ciencia Ficción", "Terror", "Aventura"}


# Calcular con & | - ^ <= y mostrar resumen

comunes = usuario1 & usuario2 & usuario3
todos = usuario1 | usuario2 | usuario3

diferencia1_2 = usuario1 - usuario2
diferencia1_3 = usuario1 - usuario3
diferencia2_3 = usuario2 - usuario3

excl1_2 = usuario1 ^ usuario2
excl1_3 = usuario1 ^ usuario3
excl2_3 = usuario2 ^ usuario3


print("OPERACIONES LÓGICAS")
print(f"Comunes a todos (Intersección): {comunes}")
print(f"Universo total de géneros (Unión): {todos}")


print(f"\nExclusivos de Usuario 1 frente a Usuario 2 (Diferencia): {diferencia1_2}")
print(f"Géneros que no comparten U1 y U2 (Diferencia Simétrica): {excl1_2}")
print()

print("VERIFICACIÓN DE SUBCONJUNTOS")
es_subconjunto = usuario1 <= todos
print(f"¿Los gustos del Usuario 1 son parte del universo total?: {es_subconjunto}")

# Ejemplo de subconjunto falso
es_u1_de_u2 = usuario1 <= usuario2
print(f"¿Al Usuario 2 le gusta todo lo que le gusta al Usuario 1?: {es_u1_de_u2}")
print()

print("RESUMEN INTEGRADO")
print(f"Contamos con un total de {len(todos)} géneros distintos entre los tres usuarios.")
print(f"Los géneros que generan conflicto (no compartidos) entre U1 y U3 son: {excl1_3}")