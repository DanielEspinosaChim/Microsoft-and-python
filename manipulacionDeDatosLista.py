#Puede recuperar una parte de una lista mediante una segmentación. Una segmentación usa corchetes, pero en lugar de un solo elemento, tiene los índices inicial y final. Cuando se usa una segmentación, se crea una lista que comienza en el índice inicial y termina antes del índice final 
planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]
planets_before_earth = planets[0:2]
print(planets_before_earth)

# Output: ['Mercury', 'Venus'] notese que no imprime la tierra ya que ese es el rango limite y termina una antes

planets_after_earth = planets[3:8]
print(planets_after_earth) 

# Output
# ['Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune'] este si imprime todo, recuerda que este empieza de 0 a 7, entonces llega hasta uno antes del 8 y si imprime mi lista full
# Si no coloca el índice de detención en la segmentación, Python asume que quiere ir al final de la lista:
planets_after_earth = planets[3:]
print(planets_after_earth)

# Output
# ['Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']
#Una segmentación crea una lista nueva. No modifica la lista actual.




