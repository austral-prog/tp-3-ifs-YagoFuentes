def password():
    """
    Ejercicio 10 - Validador de Contraseña

    Leer una contraseña mediante input(). Validar que cumpla con los siguientes requisitos:
    1. Debe tener al menos 8 caracteres de longitud
    2. Debe contener al menos un número (usar el operador in para verificar cada dígito del 0 al 9)

    Si cumple ambos requisitos, imprimir "Contraseña valida".
    Si no cumple, imprimir cuál requisito falta.

    Ejemplo:
        Para la entrada "abc12345", la salida esperada es:
        Contraseña valida

        Para la entrada "abc123", la salida esperada es:
        Contraseña muy corta

        Para la entrada "abcdefgh", la salida esperada es:
        Debe contener un numero

        Para la entrada "abc", la salida esperada es:
        Contraseña muy corta
        Debe contener un numero
    """
    pass
    contrasena = input()
    longitudContrasena = len(contrasena)
    tieneNumero = (
            "0" in contrasena or "1" in contrasena or "2" in contrasena or
            "3" in contrasena or "4" in contrasena or "5" in contrasena or
            "6" in contrasena or "7" in contrasena or "8" in contrasena or
            "9" in contrasena
    )
    if longitudContrasena < 8 and not tieneNumero:
        print("Contraseña muy corta\nDebe contener un numero")
    elif longitudContrasena < 8 :
        print("Contraseña muy corta")
    elif  not tieneNumero :
        print("Debe contener un numero")
    else:
        print("Contraseña valida")
