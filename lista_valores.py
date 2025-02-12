lista_numeros=[]
valor=1

while valor!=0:
    valor=float(input("Digite um valor: "))
    if valor!=0:
        lista_numeros.append(valor)
    print(list(lista_numeros))    
    
total_valores=sum(lista_numeros)
        
print(list(lista_numeros))
print(f"A soma dos valores da lista é {total_valores}")
print("Agora vou ordenar a lista")
lista_numeros.sort()
#do menor para o maior
print(list(lista_numeros))

lista_numeros.sort(reverse=True)
#do maior para o menor
print(list(lista_numeros))