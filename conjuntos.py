numeros="7218237637212323434483486398578567436483682737"

conj_num=set(numeros) #convertendo a string para um conjunto

print(numeros)
print(conj_num)#para ver a diferenca de conjunto(set) e uma string

#lendo o conjunto
conjunto={"um","dois","tres", "quatro"}
for elemento in conjunto:
    print(elemento)
print('-'*20) 
for elemento in conjunto:
    print(elemento)   
    
#add elementos ao conjunto
conjunto.add("Coisa")     
conjunto.add(362)   
conjunto.add(367)

print(conjunto)

#remover elementos do conjunto
conjunto.remove("dois")#gera erro se o elemento nao existir
descartado=conjunto.discard(367)#nao gera erro
print(conjunto)
print(descartado)
conjunto.clear() #apaga todo o conjunto
print(conjunto)

lista_frutas=["laranja", "uva", "banana","uva","pera", "banana"]
print(lista_frutas)

#remover os itens repetidos da lista
set_frutas=set(lista_frutas)
lista_frutas=list(set_frutas)
print(lista_frutas)
