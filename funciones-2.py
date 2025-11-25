# ******************* FUNCIONES *******************
def mostrar_menu():
    print("digite la letra 'A' para Actualizar Sistema")
    print("digite la letra 'E' para Eliminar Catalogo")
    print("digite la letra 'C' para Crear Productos")
    print("digite la letra 'S' para salir del programa")


def capturar_opcion():
    opcion = input("Digite una opción: ")
    return opcion


def procesar_opcion(letra):
    if letra == 'S' or letra == 's':
        print("finalizo con exito \n")
        return False     # Detener el ciclo
    else:
        print("Sigue dentro del proceso del DO WHILE \n")
        return True      # Continuar el ciclo

# ******************* ZONA DE CODIGO PRINCIPAL *******************
while True:
    mostrar_menu()                     # Función 1
    opcion_usuario = capturar_opcion() # Función 2
    continuar = procesar_opcion(opcion_usuario)  # Función 3
    
    if not continuar:
        break

print("EL DO-WHILE ha finalizado \n")
