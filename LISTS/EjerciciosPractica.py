# Ingresar por teclado los nombres de 5 personas y almacenarlos en 
# una lista. Mostrar el nombre de persona menor en orden alfabético.


#Solucion 1

""" def ingresar_datos():
    nombres = []
    for x in range(5):
        nombre = input("Ingrese nombre de la persona "+ str(x+1) + ":")
        nombres.append(nombre)
    return nombres

def ordenar_nombres(nombres):
    menor = nombres[0]
    for x in range(1,len(nombres)):
        if nombres[x] < menor:
            menor = nombres[x]
    return menor

nombres = ingresar_datos()
menor = ordenar_nombres(nombres)
print(menor) """

####################################################################################

#Solucion IA

""" def ingresar_datos():
    nombres = []
    for x in range(5):
        while True:
            nombre = input(f"Ingrese nombre de la persona {x+1}: ").strip()
            if nombre:  # Verifica que no esté vacío
                nombres.append(nombre.lower())  # Convertir a minúsculas para comparación
                break
            print("Error: No puede ingresar un nombre vacío")
    return nombres

def ordenar_nombres(nombres):
    return min(nombres)  # Usa la función min() incorporada

nombres = ingresar_datos()
menor = ordenar_nombres(nombres)
print("El nombre menor en orden alfabético es:", menor.capitalize()) """

# Cargar una lista con 5 elementos enteros. Imprimir el mayor y un mensaje 
# si se repite dentro de la lista (es decir si dicho valor se encuentra en 
# 2 o más posiciones en la lista)

lista = [1,4,5,1,5,5]

def encuentra_mayor(lista):
    mayor = lista[0]
    for x in range(1,len(lista)):
        if lista[x] > mayor:
            mayor = lista[x]
    return mayor

def encuentra_repetido(mayor,lista):
    contador = 0
    for x in range(len(lista)):
        if lista[x] == mayor:
            contador+=1
    return contador    


mayor = encuentra_mayor(lista)
contador = encuentra_repetido(mayor,lista)

print(f"El numero mayor de la lista es: {mayor}")

if contador > 1:
    print(f"Este valor se repite {contador} veces en la lista") 
else:
    print("El número no se repite en la lista")    