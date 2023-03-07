# f-strings . Estas cadenas parecen plantillas y usan los nombres de variables de su código
mass_percentage = "1/6"
print(f"On the Moon, you would weigh about {mass_percentage} of your weight on Earth")
#On the Moon, you would weigh about 1/6 of your weight on Earth
#Las variables van entre llaves y la cadena debe usar el fprefijo.
#Aparte de que f-strings es menos detallado que cualquier otra opción de formato, es posible usar expresiones entre llaves.
#. Por ejemplo, si desea representar el 1/6valor como un porcentaje con un decimal, puede usar la round()función directamente:
round(100/6, 1)
16.7
print(f"On the Moon, you would weigh about {round(100/6, 1)}% of your weight on Earth")
#On the Moon, you would weigh about 16.7% of your weight on Earth
#El uso de una expresión no requiere una llamada de función. Cualquiera de los métodos de cadena también es válido.
subject = "interesting facts about the moon"
f"{subject.title()}"
'Interesting Facts About The Moon'