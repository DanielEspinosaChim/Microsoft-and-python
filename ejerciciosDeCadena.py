#El marcador de posición de la variable en la cadena es %s. Después de la cadena, use otro %carácter seguido del nombre de la variable.
mass_percentage = "1/6"
print("On the Moon, you would weigh about %s of your weight on Earth" % mass_percentage)
#"On the Moon, you would weigh about 1/6 of your weight on Earth"

#ejemplo mas complejo 
print("""Both sides of the %s get the same amount of sunlight,
... but only one side is seen from %s because
... the %s rotates around its own axis when it orbits %s.""" % ("Moon", "Earth", "Moon", "Earth"))
#Both sides of the Moon get the same amount of sunlight,
#but only one side is seen from Earth because
#the Moon rotates around its own axis when it orbits Earth.
#El .format()método usa llaves ( {}) como marcadores de posición dentro de una cadena y usa la asignación de variables para reemplazar texto.
mass_percentage = "1/6"
print("On the Moon, you would weigh about {} of your weight on Earth".format(mass_percentage))
#On the Moon, you would weigh about 1/6 of your weight on Earth

print("""You are lighter on the {0}, because on the {0} 
... you would weigh about {1} of your weight on Earth""".format("Moon", mass_percentage))#el 1 indica la primera variable que desclaraste
#You are lighter on the Moon, because on the Moon you would weigh about 1/6 of your weight on Earth
#En lugar de llaves vacías, la sustitución es usar números. Los {0}medios para usar el primer argumento (índice de cero) para .format(), que en este caso es Moon. Para la repetición simple {0}funciona bien, pero reduce la legibilidad. Para mejorar la legibilidad, use argumentos de palabras clave .format()y luego haga referencia a los mismos argumentos entre llaves:
print("""You are lighter on the {moon}, because on the {moon} 
... you would weigh about {mass} of your weight on Earth""".format(moon="Moon", mass=mass_percentage))
#You are lighter on the Moon, because on the Moon you would weigh about 1/6 of your weight on Earth