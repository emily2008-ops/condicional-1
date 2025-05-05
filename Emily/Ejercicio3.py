Calificacion =float(input("Ingrese nota"))

if Calificacion >=4.5:
    print("Superior")
elif Calificacion>=3.9 and Calificacion<4.5:
    print("Alto")   
elif Calificacion<=3.0  and Calificacion<3.9:
    print("Basico")  
elif Calificacion>=1.0 and Calificacion<3.0:
    print("Bajo")   
else:
    print("Estudiante no evaluado")    