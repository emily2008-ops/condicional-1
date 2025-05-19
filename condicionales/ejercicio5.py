placa = input("Ingrese la placa del bus: ")
pasajeros = int(input("Número de pasajeros transportados: "))
ruta = input("Ruta donde prestó el servicio (A o B): ")

if ruta == "A":
    pasaje = 1200
elif ruta == "B":
    pasaje = 1000
else:
    print("Ruta inválida.")
    pasaje = 0

dinero = pasajeros * pasaje

if pasaje > 0:
    print("El bus con placa ",placa)
    print ("recolectó ",dinero)