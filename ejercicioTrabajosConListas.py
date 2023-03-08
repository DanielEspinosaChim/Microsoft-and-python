planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Neptune"]
user_planet = input("Please enter the name of the planet (with a capital letter to start)")#le dice que ponga el nombre del planeta con la primera letra en mayuscula
planet_index = planets.index(user_planet)#busca en planets, el valor introducido en user_planets
print("Here are the planets closer than " + user_planet)
print(planets[0:planet_index])#crea un nuevo vector del rango 0 hasta el indice de el planeta y imprime todos los anteriores
print("Here are the planets further than " + user_planet)
print(planets[planet_index + 1:])# crea un nuevo vextor que va desde en nodo del planeta y le sumas uno pra que tome hasta al planeta y termina hasta el fin de la lista