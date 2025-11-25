# ******************* FUNCIONES *******************
def capturar_cantidad():
    print("Digite la cantidad de numeros para sumar: ")
    cantidad = int(input())
    return cantidad

def capturar_numeros(cantidad):
    lista = []
    for i in range(cantidad):
        print("Digite el Numero " + str(i + 1) + ": ")
        numero = int(input())
        lista.append(numero)
    return lista

def sumar_lista(lista):
    suma = 0
    for n in lista:
        suma += n
    return suma

def imprimir_resultado(suma):
    print("La sumatoria total es: " + str(suma))

# ******************* CÓDIGO CENTRAL MAIN ***************************
cantidad_numeros = capturar_cantidad()          # Función 1
lista_numeros = capturar_numeros(cantidad_numeros)  # Función 1
resultado = sumar_lista(lista_numeros)          # Función 2
imprimir_resultado(resultado)                   # Función 3
