#.replace()método para buscar y reemplazar apariciones de un carácter o grupo de caracteres:
"Saturn has a daytime temperature of -170 degrees Celsius, while Mars has -28 Celsius.".replace("Celsius", "C")
'Saturn has a daytime temperature of -170 degrees C, while Mars has -28 C.'
text = "Temperatures on the Moon can vary wildly."
"temperatures" in text#en este caso es falso por que del texto estas busacando una palabrqa que no existe por la minuscula
False
"temperatures" in text.lower() #aqui es everdadero por que convirtes toda la cadena principal en minuscula y si coincide
True
# Así como el .split()método puede separar caracteres, el .join()método puede volver a unirlos.
#el .joi n necesita ser iterado como argumento
moon_facts = ["The Moon is drifting away from the Earth.", "On average, the Moon is moving about 4cm every year"]
'\n'.join(moon_facts)
'The Moon is drifting away from the Earth.\nOn average, the Moon is moving about 4cm every year'