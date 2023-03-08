def variable_length(*args):#se usa *args por que no se sabe la cantdad de variables que va en los parametros
    print(args)
    
def sequence_time(*args):
    total_minutes = sum(args)
    if total_minutes < 60:
        return f"Total time to launch is {total_minutes} minutes"
    else:
        return f"Total time to launch is {total_minutes/60} hours"
    
x=sequence_time(3,40,23)
print(x)
#Al igual que con los argumentos de variable, no es necesario usar kwargs cuando se usan argumentos de palabra clave variable.
# Puede usar cualquier nombre de variable válido. Aunque es habitual ver **kwargs o **kw, debe intentar usar la misma convención en 
# un proyecto.
def variable_length(**kwargs):#se rquieren 2 asteriscos por que son dos tipos de palabras clave es como un diccionario, pero con argumentos
    print(kwargs)
    #ej variable_length(tanks=1, day="Wednesday", pilots=3)
#{'tanks': 1, 'day': 'Wednesday', 'pilots': 3}
    
def crew_members(**kwargs):
    print(f"{len(kwargs)} astronauts assigned for this mission:")
    for title, name in kwargs.items():
        print(f"{title}: {name}")

# ej >>> crew_members(captain="Neil Armstrong", pilot="Buzz Aldrin", command_pilot="Michael Collins")
#3 astronauts assigned for this mission:
#captain: Neil Armstrong
#pilot: Buzz Aldrin
#command_pilot: Michael Collins

crew_members(capi="neil Amstrong",fisico="javier",alcargo="io")#no repitas las palabras clave o manda error
