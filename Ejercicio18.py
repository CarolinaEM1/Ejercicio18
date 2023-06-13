#Ejercicio 18

cadena = input("Digite una cadena: ")

lista = []

for i in cadena:
    if i not in lista: #Si el caracter aun no está en la lista
        lista.append(i) # Lo agregamos a la lista

print(f"\nLista de caracteres sin repetir: \n{lista}")

#Carolina EM