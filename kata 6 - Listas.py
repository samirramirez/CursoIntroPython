
###########################################################################
########                KATA 6 MANEJO DE LISTAS                     ####### 
###########################################################################

'''--------------------- Ejercicio1: Crear y usar listas de Python -----------------------'''


# Creamos la lista planets 

print("--- T H E     P  L A N E T S ---\n\n")
planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']
print('These are the', len(planets), 'planets')

# Mostramos los elementos de la lista

for elem  in planets:
    print(elem)


print("\n")

# Agregamos a plutón y mostramos el último elemento

planets.append('Pluto')
print(f"The last planet is {planets[-1]}")
print(planets)

print("\n")

'''------------- Ejercicio 2: Trabajando con datos de una lista ------------------'''

print("----- Planets closest and farthest from the sun ------ \n")
#planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]

# Solicitamos el nombre de un planeta 
wanted_planet = input("Planet's name: ").title()
print("\n")

# Busca el planeta en la lista
planet_index = planets.index(wanted_planet)

# Muestra los planetas más cercanos al sol
print('Here are the planets closer than ' + wanted_planet)
print(planets[0:planet_index])

print("\n")
# Muestra los planetas más lejanos al sol

print('Here are the planets further than ' + wanted_planet)
print(planets[planet_index + 1:])

