rainfall = {
    'october': 3.5,
    'november': 4.2,
    'december': 2.1
}

#El keys()método devuelve un objeto de lista que contiene todas las claves. Puede utilizar este método para iterar a través de 
# los elementos del diccionario.#en este ejemplo devuelve octubre...
for key in rainfall.keys():#key el nombre de la vriable
    print(f'{key}:{rainfall[key]}cm')#en la segunda instruccion le estas dicientdo que te tome el valor ue tiene key del diccionario
    #por eso te retorna el numero

# Output:
# october: 3.5cm
# november: 4.2cm
# december: 2.1cm
#Todavía puede usar corchetes ( [ ]) con un nombre de variable, en lugar del literal de cadena codificado de forma rígida.
#puede verificar si una clave existe utilizando el in
if 'december' in rainfall:
    rainfall['december'] = rainfall['december'] + 1#si existe el valor el reinfall le suma 1
else:
    rainfall['december'] = 1#si no, crea un valor con el nombre december que valga 1

for dato, valor in rainfall.items():        #forma de imprimir el nombre de la variave y su valor en diccionario clave_valor
     print(f'El valor de {dato} es {valor}')

    

# Because december exists, the value will be 3.1
#Similar a keys(), values()devuelve la lista de todos los valores de un diccionario sin sus respectivas claves. values()puede ser 
# útil cuando usa la clave con fines de etiquetado, como en el ejemplo anterior, en el que las claves son el nombre del mes. Puede usar
# values()para determinar la cantidad total de lluvia:
total_rainfall = 0#inicializas un contador
for value in rainfall.values():#values() va a pasar por todos los valores de las variables declaradas en el diccionario
    total_rainfall = total_rainfall + value#iteras una variable random para que valla pasndo uno por uno los valores y en esta linea pues hace la suma de toda la vida
  
print(f'There was {total_rainfall}cm in the last quarter')



# Output:
# There was 10.8cm in the last quarter