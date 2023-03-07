moon_radius = "The Moon has a radius of 1,080 miles"#normalmente se le ponen solo 2 comillas
'The "near side" is the part of the Moon that faces the Earth'# si hay una sub cadena y esta entre comillas dobles, para que se imprimasn essas comillas se ponen comillas de uno y la palabra se le ponen comillas dobles
"We only see about 60% of the Moon's surface"#de igual manera si en la cadena hay apostrofe imprima con comillllas dobles
"""We only see about 60% of the Moon's surface, this is known as the "near side".""" # si el texto intercala entre comillas dobles y simples se le ponen comillas triples
print("......................................................")
multiline = "Facts about the Moon:\n There is no atmosphere.\n There is no sound."# el /n da el salto de linea como java
print(multiline)
# igual da el salto de linea con las comilla triples
multiline = """Facts about the Moon:
...  There is no atmosphere.
...  There is no sound."""
print(multiline)
