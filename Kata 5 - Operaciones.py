
#########################################################
#           Kata 5 Operadores aritmeticos               #
#########################################################

'''----------------------------------- Ejercicio 1 ------------------------------''' 

# Crear variables para almacenar dos distancias

earth_distance = 149597870 # km
jupiter_distance = 778547200 # km

distance_btw_planets =  jupiter_distance - earth_distance

print("Distancia entre Jupiter y Tierra es:" ,distance_btw_planets, "Km")

#convertir kilometros a millas 
distance_in_millas= distance_btw_planets * 0.621 
print("Distancia entre Jupiter y Tierra es:", round(distance_in_millas), "m")

'''----------------------------------- Ejercicio 2 ------------------------------''' 

# Almacenar las entradas del usuario


planeta1= input("Ingresar el valor de la distancia del primer planeta: " )
planeta2= input("Ingresar el valor de la distancia del Segundo planeta: " )

# Convierte las cadenas de ambos planetas a números enteros
planeta1=int(planeta1)
planeta2=int(planeta2)

# Realizar el cálculo y determinar el valor absoluto
distancia = planeta2 - planeta1
print("La distancia es: ", distancia)
# Convertir de KM a Millas
millas = distancia* 0.621
print("Distancia en millas: ", abs(millas),"M")