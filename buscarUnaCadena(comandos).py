#La forma más sencilla de descubrir si una palabra, un carácter o un grupo de caracteres dado existe en una cadena es utilizar el in
"Moon" in "This text will describe facts and challenges with space travel"
False
"Moon" in "This text will describe facts about the Moon"
True
#Un enfoque para encontrar la posición de una palabra específica en una cadena es usar el .find()
temperatures = """Saturn has a daytime temperature of -170 degrees Celsius,
... while Mars has -28 Celsius."""
temperatures.find("Moon")
-1
#El .find()método devuelve un -1cuando no se encuentra la palabra, o devuelve el índice (el número que representa el lugar en la cadena). Así es como se comportaría si está buscando la palabra Marte 
temperatures.find("Mars")
65
#65es la posición donde "Mars"aparece en la cadena.
#Otra forma de buscar contenido es utilizar el .count()método, que devuelve el número total de apariciones de una determinada palabra en una cadena:
temperatures.count("Mars")
1
temperatures.count("Moon")
0
# puede convertir una cadena en letras minúsculas utilizando el .lower()
"The Moon And The Earth".lower()
'the moon and the earth'
#.upper()método que hace lo contrario, convirtiendo cada carácter a mayúsculas
"The Moon And The Earth".upper()
'THE MOON AND THE EARTH'
