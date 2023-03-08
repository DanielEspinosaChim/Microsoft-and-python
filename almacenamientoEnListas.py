gravity_on_earth = 1.0
gravity_on_the_moon = 0.166
#la gavedad en otros planetas
gravity_on_planets = [0.378, 0.907, 1, 0.377, 2.36, 0.916, 0.889, 1.12]
bus_weight = 12650 # in kilograms, on Earth kilogramos del autobus en la tierra

print("On Earth, a double-decker bus weighs", bus_weight, "kg")
print("On Mercury, a double-decker bus weighs", bus_weight * gravity_on_planets[0], "kg")#si en el vector hay numeros puedes multiplicar con su indice del vector
# Output
# On Earth, a double-decker bus weighs 12650 kg
# On Mercury, a double-decker bus weighs 4781.7 kg

bus_weight = 12650 # in kilograms, on Earth

print("On Earth, a double-decker bus weighs", bus_weight, "kg")
print("The lightest a bus would be in the solar system is", bus_weight * min(gravity_on_planets), "kg")#min toma el valor minimo del vector
print("The heaviest a bus would be in the solar system is", bus_weight * max(gravity_on_planets), "kg")#max toma el valor maximo del vector

# Output
# On Earth, a double-decker bus weighs 12650 kg
# The lightest a bus would be in the solar system is 4769.05 kg
# The heaviest a bus would be in the solar system is 29854 kg