#Python usa llaves ({ }) y dos puntos (:) para indicar un diccionario. Puede crear un diccionario vacío y agregar valores más 
# adelante, o bien rellenarlo en el momento de la creación. Cada clave o valor está separado por dos puntos y el nombre de cada 
# clave se incluye entre comillas como un literal de cadena. Como la clave es un literal de cadena, puede usar el nombre que sea 
# adecuado para describir el valor.
planet = {
    'name': 'Earth',
    'moons': 1
}


#lectura de valores de dicicionrio 
#Puede leer valores dentro de un diccionario. Los objetos de diccionario tienen un método get que puede usar para acceder a un valor
# mediante su clave. Si quiere imprimir name, puede usar el código siguiente:
print(planet.get('name'))

# Displays Earth
# planet['name'] is identical to using planet.get('name')
print(planet['name'])#una forma mas facil de escribir lo mismo sin el get y es lo que mas usan los programadores, solo poner[]

# Displays Earth
#También puede modificar valores dentro de un objeto de diccionario, con el método update. Este método acepta un diccionario como 
# parámetro y actualiza los valores existentes con los nuevos que proporcione. Si quiere cambiar name para el diccionario planet, puede 
# usar lo siguiente, por ejemplo:
planet.update({'name': 'Makemake'})

# name is now set to Makemake

print(planet['name'])#dentro del diccionario planet, imprimo planet que vale makemke
# igual se puede asignar un valor diferente a la variable de un diccionario de la siguiente manera
planet['name'] = 'Makemake'


# name is now set to Makemake
#La principal ventaja de usar update es la capacidad de modificar varios valores en una operación. Los dos ejemplos siguientes son
# lógicamente los mismos, pero la sintaxis es diferente. Puede usar la sintaxis que crea más adecuada. La mayoría de los 
# desarrolladores eligen corchetes para actualizar valores individuales.

#En el ejemplo siguiente se hacen las mismas modificaciones en la variable planet y se actualizan el nombre y las lunas. Tenga en cuenta
# que al usar update realiza una sola llamada a la función, mientras que el uso de corchetes implica dos llamadas.

# Using update
planet.update({
    'name': 'Jupiter',
    'moons': 79
})

# Using square brackets
planet['name'] = 'Jupiter'
planet['moons'] = 79

#para meter valores a un diccionaro los puedes meter con[]
planet[orbital_period]=4333 #agrega al diccionario orbital period y le da el valor de 4333
#Los nombres de clave, como todo lo demás en Python, distinguen mayúsculas de minúsculas. Como resultado, 'name' y 'Name' se consideran
# dos claves independientes en un diccionario de Python.
#Para quitar una clave, use pop. pop devuelve el valor y quita la clave del diccionario. Para quitar orbital period, puede usar el 
# código siguiente:
planet.pop('orbital period')

# planet dictionary now contains: {
#   name: 'jupiter'
#   moons: 79
# }


