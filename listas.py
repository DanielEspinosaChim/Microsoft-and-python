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