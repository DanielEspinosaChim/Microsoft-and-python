from datetime import timedelta, datetime

def arrival_time(hours=51):
    now = datetime.now()
    arrival = now+timedelta (hours=hours)#timedelta sirve para que se pueda sumar precticamente vale 1 y lo multiplica*51
    return arrival.strftime("Arrival: %A %H:%M")#da formato al tiempo

x=arrival_time()
print(x)

#convinacion de argumentos y argumentos de palabras clave
from datetime import timedelta, datetime

def arrival_time(destination, hours=51):
    now = datetime.now()
    arrival = now + timedelta(hours=hours)
    return arrival.strftime(f"{destination} Arrival: %A %H:%M")#concatena destination con la funcion f para imprimir

x=arrival_time('Moon')#al ya requerir un argumento nu puedo dejar los parametros vacios
print(x)