def distance_from_earth(destination):
    if destination == "Moon":
        return "238,855"
    else:
        return "Unable to compute to that destination"
    
#distance_from_earth() si lo dejo asi con parametros vacios me manda error por que ya declare que le tengo que pasar un valor tipo cadena

print(distance_from_earth('Moon'))
x=distance_from_earth('marte')#esta sera el else por que le paso un argumento distinto a Moon
print(x)

#funciones con varios argumentos
def days_to_complete(distance, speed):
    hours = distance/speed
    return hours/24

impr=days_to_complete(383839, 83)
print(impr)


#funciones que llevan funciones como argumento
x=round(days_to_complete(238855, 75))
print(x)
print(round(days_to_complete(238855, 75)))
133
