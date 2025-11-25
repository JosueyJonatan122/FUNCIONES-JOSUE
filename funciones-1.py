# *************** ZONA FUNCIONES ***************
def capturar_numero():
    print ( "dijite el numero: ")
    num = int(input())
    return num

def tipo_de_numero(numero):
    if numero > 0:
        print("el numero es positivo")
        
    elif numero== 0:
        print("el numero es NEUTRO")
        
    else:
        print("el numero es negativo")
        
def imprimir_resultado(mensaje):
    print(mensaje)
    
# ******************* ZONA PRINCIPAL *******************

num = 1
while num != 0:
    num = capturar_numero()                 # Función 1
    if num != 0:
        mensaje= tipo_de_numero(num)
        imprimir_resultado(mensaje)
        
print("finalizo el programa")
