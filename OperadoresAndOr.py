#Ocasionalmente, es posible que desee combinar expresiones de prueba para evaluar varias condiciones en una instrucción if, elifo . elseEn este caso, usaría los operadores booleanos andy or.
#or se ejecutara si una de las condiciones es verdadera
a = 23
b = 34
if a == 34 or b == 34:
    print(a + b)
    
print("..........................")
#and con and solo ejecutara si las dos condiciones son verdaderas
a = 23
b = 34
if a == 34 and b == 34:#no se evaluara por que la condicion es false
    print (a + b)