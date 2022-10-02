verificando = True
biografia ='Mi nombre y apellido es Anabel Mamani Alarcon, soy de Bolivia vivo en la ciudad de sucre, tengo 20 años, curso la carrera de Ing. en Diseño y Animacion Digital'
while verificando :
    print ('1. Biografia')
    print ('2. Salida')
    elegir = input('Ingresar su eleccion Porfavor:')
    if elegir == '1':
        print (biografia)
    elif elegir == '2':
        verificando = False