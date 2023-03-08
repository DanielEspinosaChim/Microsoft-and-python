planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]#crea la listas entre[] y separado los argumentos con ,
#Puede acceder a cualquier elemento de una lista colocando el índice entre corchetes [] después del nombre de la variable de lista. Los índices comienzan a partir de 0, por lo que en el código siguiente, planets[0] es el primer elemento de la lista planets
print("The first planet is", planets[0])
print("The second planet is", planets[1])
print("The third planet is", planets[2])

# Output
# The first planet is Mercury
# The second planet is Venus
# The third planet is Earth

#También puede modificar valores de una lista mediante un índice. Para ello, asigne un nuevo valor, de la misma manera que asignaría un valor de variable. 
planets[3] = "Red Planet"
print("Mars is also known as", planets[3])

# Output
# Mars is also known as Red Planet

#Para obtener la longitud de una lista, use la función integrada len().
#El código siguiente crea una variable, number_of_planets. El código asigna esa variable con el número de elementos de la lista planets (8).
number_of_planets = len(planets)
print("There are", number_of_planets, "planets in the solar system.")

# Output:
# There are 8 planets in the solar system

#puede agregar y quitar elementos a una lista después de crearlas. Para agregar un elemento a una lista, use el método .append(value).
planets.append("Pluto")
number_of_planets = len(planets)
print("There are actually", number_of_planets, "planets in the solar system.")

# Output:
# There are actually 9 planets in the solar system.

#Puede quitar el último elemento de una lista llamando al método .pop() en la variable de lista
planets.pop()  # Goodbye, Pluto
number_of_planets = len(planets)
print("No, there are definitely", number_of_planets, "planets in the solar system.")#puede eliminar igual con el .remove()

#Los índices comienzan en cero y van en aumento. Los índices negativos comienzan al final de la lista y van hacia atrás.
print("The last planet is", planets[-1])
print("The penultimate planet is", planets[-2])

# Output
# The last planet is Neptune
# The penultimate planet is Uranus

#Para determinar dónde se almacena un valor en una lista, use el método index 
jupiter_index = planets.index("Jupiter")
print("Jupiter is the", jupiter_index + 1, "planet from the sun")

# Output
# Jupiter is the 5 planet from the sun
#el index siempre comienza en el 0

