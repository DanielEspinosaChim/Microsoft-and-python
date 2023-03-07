#Para anidar condiciones, aplique sangría a las condiciones internas y todo lo que tenga el mismo nivel de sangría se ejecutará en el mismo bloque de código:
a = 16
b = 25
c = 27
if a > b:
    if b > c:
        print ("a is greater than b and b is greater than c")
    else: 
        print ("a is greater than b and less than c")
elif a == b:
    print ("a is equal to b")
else:
    print ("a is less than b")