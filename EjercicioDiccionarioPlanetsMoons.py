planet_moons = {
    'mercury': 0,
    'venus': 0,
    'earth': 1,
    'mars': 2,
    'jupiter': 79,
    'saturn': 82,
    'uranus': 27,
    'neptune': 14,
    'pluto': 5,
    'haumea': 2,
    'makemake': 1,
    'eris': 1#en los diccionarios tienes que separar con coma cada uno y el igual se oone con: 
}

moons=planet_moons.values()#para obtener todos los valores dentro del diccionario(los numeros)
total_planets = len(planet_moons.keys())#total de planetas es igual a lo largo d la lista planet_moons y con el.keys para saber 
#los datos dentro del diccionario(el total de variables o sus nombres)
#Terminarás este ejercicio determinando el número promedio de lunas. Comience creando una variable llamada total_moons; este será 
# su contador para el número total de lunas. Luego agregue un forciclo para recorrer la lista de moons, agregando cada valor a 
# total_moons. Finalmente, calcule el promedio dividiendo total_moonspor total_planetsy mostrando el valor.
total_moons = 0
for moon in moons:#variable random moon recrre a moons 
    total_moons = total_moons + moon

average = total_moons / total_planets#lo que ya sacaste sumando todos los valores de moons lo divides entre total planets
#total_planets lo obtienes con el keyes

print(f'Each planet has an average of {average} moons')
