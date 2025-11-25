# ******************* FUNCIONES *******************
def capturar_mes():
    print("Digite un número del 1 al 12: ")
    num = int(input())
    return num

def obtener_nombre_mes(num):
    match num:
        case 1:
            return "Enero"
        case 2:
            return "Febrero"
        case 3:
            return "Marzo"
        case 4:
            return "Abril"
        case 5:
            return "Mayo"
        case 6:
            return "Junio"
        case 7:
            return "Julio"
        case 8:
            return "Agosto"
        case 9:
            return "Septiembre"
        case 10:
            return "Octubre"
        case 11:
            return "Noviembre"
        case 12:
            return "Diciembre"
        case _:
            return "Número inválido. Debe ser entre 1 y 12."

def imprimir_mes(nombre_mes):
    print("El mes es: " + nombre_mes)

# ******************* CÓDIGO PRINCIPAL (MAIN) *******************
numero_mes = capturar_mes()               # Función 1
nombre_mes = obtener_nombre_mes(numero_mes)  # Función 2
imprimir_mes(nombre_mes)                  # Función 3
