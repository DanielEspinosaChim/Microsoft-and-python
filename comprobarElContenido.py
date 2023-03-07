temperatures = "Mars Average Temperature: -60 C"
#Para extraer la temperatura promedio en Marte, puede hacerlo bien con los siguientes métodos:
parts = temperatures.split(':')#Este codigo inica que todo lo que este depues de : es la temperatura
parts#produce una lista de dos elementos
['Mars average temperature', ' -60 C']
parts[-1]#el uso de ese[-1] indica el ultimo elemento en este caso la tempeatura
' -60 C'

mars_temperature = "The highest temperature on Mars is about 30 C"
for item in mars_temperature.split():
 if item.isnumeric():
        print(item)
...
30
#.isnumeric()método que busca si en la cadena hay una parte que parezca numerica, .isdecimal()puede buscar cadenas que parezcan decimales.
#Determina si una cadena es un carácter que representa un número
#.startswith() para encontrar negativos
#De manera similar, el .endswith()método ayuda a verificar el último carácter de una cadena:
if "30 C".endswith("C"):
    print("This temperature is in Celsius")
'This temperature is in Celsius'

