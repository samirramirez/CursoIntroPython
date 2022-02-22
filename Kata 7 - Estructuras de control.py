
###########################################################################
########                KATA 7 ESTRUCTURAS DE CONTROL               ####### 
###########################################################################

'''--------------- Ejercicio 1: Uso de ciclos *while* en Python --------------- '''

# Variables
new_planet=""
planets=[]

print("Si no desea agregar más planetas escriba 'done'\n")
while new_planet.lower() != 'done':
    if new_planet:
        planets.append(new_planet)
    new_planet = input('Escribe el nombre del planeta: ')


print("\nLos planetas en la lista son: ")
for planet in planets:
    print(planet)