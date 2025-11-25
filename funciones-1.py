# *************** ZONA FUNCIONES ***************
def capturar_cantidad():
    print("Digite la cantidad de numeros para sumar: ")
    cantidad = int(input())
    return cantidad

def capturar_numeros(cantidad):
    lista_numeros = []
    for i in range(cantidad):
        print("Digite el Numero " + str(i + 1) + ": ")
        numero = int(input())
        lista_numeros.append(numero)
    return lista_numeros

def sumar_numeros(lista):
    suma = 0
    for n in lista:
        suma += n
    return suma

def imprimir_resultado(resultado):
    print("La sumatoria total es: " + str(resultado))
# *************** ZONA DE CODIGO PRINCIPAL***************
cantidad_datos = capturar_cantidad()                # Función 1
lista_datos = capturar_numeros(cantidad_datos)      # Función 1
resultado_final = sumar_numeros(lista_datos)        # Función 2
imprimir_resultado(resultado_final)                 # Función 3
