# ******************* FUNCIONES *******************
def capturar_numero():
    print("digite un numero: ")
    num = int(input())
    return num


def verificar_par_impar(numero):
    if numero % 2 == 0:
        return "El numero es par"
    else:
        return "El numero es impar"

def imprimir_resultado(mensaje):
    print(mensaje)


# ******************* ZONA PRINCIPAL *******************
num = 1
while num != 0:
    num = capturar_numero()                 # Función 1
    if num != 0:
        mensaje = verificar_par_impar(num)  # Función 2
        imprimir_resultado(mensaje)         # Función 3

print("finalizo el programa")
