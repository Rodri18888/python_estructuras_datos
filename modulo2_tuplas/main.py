# Definir catalogo como tupla de subtuplas

catalogo = (
    ("Inception", "Christopher Nolan", 2010, 8.8),
    ("Parasite", "Bong Joon-ho", 2019, 8.5),
    ("The Godfather", "Francis Ford Coppola", 1972, 9.2),
    ("Interstellar", "Christopher Nolan", 2014, 8.6),
    ("Spirited Away", "Hayao Miyazaki", 2001, 8.6),
)


# Recorrer catalogo con for desempaquetando los cuatro campos

for nombre, director, año, puntuacion in catalogo:
    print(f"Nombre: {nombre}, director: {director}, año: {año}, puntuacion: {puntuacion}")



# Usar operador * para separar primera pelicula del resto

primero, *resto = catalogo

print(resto)


# Definir buscar_por_director(director)

def buscar_por_director(director):
    print("Peliculas de director en especifico:")
    for nombre, director_buscar, año, puntuacion in catalogo:
        if director_buscar == director:
             print(f"Nombre: {nombre}, director: {director}, año: {año}, puntuacion: {puntuacion}")
            
          



# Definir obtener_estadisticas(peliculas)

def obtener_estadisticas(peliculas):
    
    puntuaciones = [pelicula[3] for pelicula in peliculas]
    
    minimo = min(puntuaciones)
    maximo = max(puntuaciones)
    promedio = sum(puntuaciones) / len(puntuaciones)
    
    return minimo, maximo, promedio
    
    
   
# Llamar a buscar_por_director e imprimir coincidencias

buscar_por_director("Christopher Nolan")
buscar_por_director("Hayao Miyazaki")



# Desempaquetar retorno de obtener_estadisticas

p_min, p_max, p_prom = obtener_estadisticas(catalogo)



# Imprimir minima, maxima y promedio

print(f"Puntuación mínima: {p_min}")
print(f"Puntuación máxima: {p_max}")
print(f"Puntuación promedio: {p_prom:.2f}")


