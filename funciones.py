def rocket_parts():
    #print("payload, propellant, structure")
    return("payload, propellant, structure")
    #Si necesita usar el valor de una función, esa función debe devolver explícitamente. De lo contrario; se devolverá None.
#rocket_parts()
#se pueden asignar metodos a variables
output=rocket_parts()
#esto sera nulo por que el metodo no retorna nada 
print(output)

#una función integrada que requiere un argumento es any(). Esta función toma un objeto iterable (por ejemplo, una lista) y devuelve 
# True si algún elemento del objeto iterable es True. De lo contrario, devuelve False. si no le pones argumentos te saltara error
any([True, False, False])
True
any([False, False, False])
False

#otor ejemplo es con el str() si no le pasas parametros te imprime una cadena vacia
str()
''
str(15)
'15'
