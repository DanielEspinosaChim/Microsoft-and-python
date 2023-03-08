seconds = 1042
display_minutes = 1042 / 60   #puedes hacer la division igual con //
print(display_minutes)

# Output: 17

seconds = 1042
display_minutes = 1042 // 60
display_seconds = 1042 % 60#con el % toma el residuo y se divide a la vez

print(display_minutes)
print(display_seconds)

# Output:
# 17
# 22

#Python respeta el orden de operación de las matemáticas. El orden de operación dicta que las expresiones deben evaluarse en el siguiente orden:

#paréntesis
#Exponentes
#Multiplicación y división
#Adición y sustracción

result_1 = 1032 + 26 * 2
result_2 = 1032 + (26 * 2)
# The answer is the same in both cases - 1084