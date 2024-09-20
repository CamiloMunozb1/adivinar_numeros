
# IMPORTAR LA LIBRERIA "RANDOM" PARA EL USO DE NUMEROS ALEATORIOS

import random

# DEFINIR UNA FUNCION PARA SU USO EN EL INDEX

def nivel_medio():

    # FIJAR UN RANGO DEL 1 AL 100

    numero_aleatorio = random.randint(1,101)

    # VARIABLE QUE NOS AYUDARA A DEFINIR EL NUMERO

    numero = None

    # NUMERO DE INTENTOS

    intentos = 5

    # BUCLE EL CUAL DEBE RASTREAR SI EL NUMERO INGRESADO ES DIFERENTE AL NUMERO ALEATORIO

    while numero != numero_aleatorio:
        try:
                
                # INGRESO DEL NUMOERO AL USUARIO

                numero = int(input("Ingresa un numero: "))

                # CONDICION QUE VERIFICA QUE EL NUMERO INGRESADO ES IGUAL AL ALEATORIO Y SALE DEL PROGRAMA

                if numero == numero_aleatorio:
                    print(f"Felicitaciones encontraste el numero {numero}")
                    break

                # CONDICION SI EL NUMERO ES DEMSASIDO ALTO AL NUMERO ALEATORIO Y SE RESTA UN INTENTO

                elif numero > numero_aleatorio:
                    print(f"El numero es demasiado alto. Intenta con un numero mas bajo, te quedan {intentos} intentos")
                    intentos -= 1
                
                # CONDICION SI EL NUMERO ES DEMASIADO BAJO AL NUMERO ALEATORIO Y SE RESTA UN INTENTO

                elif numero < numero_aleatorio:
                    print(f"El numero es demasiado bajo. Intenta con un numero mas alto, te quedan {intentos} intentos")
                    intentos -=1

        # MANEJO DE ERRORES

        except ValueError:
                print("Error de digitacion, volver a intentar.")
        
        # CONDICION POR SI EL NUMERO DE INTENTOS LLEGA A CERO Y SALE DEL PROGRAMA
        
        if intentos == 0:
                print(f"Lo siento, se acabaron los intentos. El numero era {numero_aleatorio}")
                break
    