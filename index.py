
# LLAMAMIENTOS DE FUNCIONES PARA USARLAS EN EL INDEX

from reglas_funciones.reglas import reglas_usuario
from reglas_funciones.facil import nivel_facil
from reglas_funciones.medio import nivel_medio
from reglas_funciones.dificil import nivel_dificil



while True:

    # MENU DE USUARIO CON OPCIONES

    print("""
        Bienvenido al juego de adivinanza
        1. Reglas.
        2. Nivel de juego: facil.
        3. Nivel de juego: Medio.
        4. Nivel de juego: Dificil.
        5. Salir.
        """)
    
    # ENTRADA DE USUARIO Y SELECCION DE OPCIONES

    usuario = int(input("selecciona una opcion: "))
    try:

        # MENU DE OPCIONES CON EL USO DE CADA FUNCION 

        if usuario == 1:
            reglas_usuario()
        elif usuario == 2:
            nivel_facil( )
        elif usuario == 3:
            nivel_medio()
        elif usuario == 4:
            nivel_dificil()
        elif usuario == 5:

            # SALIDA DEL PROGRAMA 

            print("Muchas gracias por jugar, hasta la proxima.")
            break
    
    # MENEJO DE ERRORES

    except ValueError:
        print("Error de digitacion volver a ingresar.")
