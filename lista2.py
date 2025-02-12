frutas=["uva", "laranja", "Banana", "Pera", "maca"]

for fruta in frutas:
    print(fruta)

nova_fruta=input("Digite outra fruta: ")

#add um novo elemento na lista    
frutas.append(nova_fruta)
print(list(frutas))

nova_fruta=input("Digite outra fruta: ")
#add um novo elemento na posicao q eu quiser 
frutas.insert(2,nova_fruta)

print(list(frutas))

fruta_remover=input("Qual fruta voce quer remover? ")

if fruta_remover in frutas:
    frutas.remove(fruta_remover)
else:
    print(f"Nao foi possivel remover {fruta_remover}, pois ela nao esta contido na lista de frutas")        
print(list(frutas))

#Remove o ultimo da lista
ultima_fruta=frutas.pop()
print(list(frutas))

print(f"A fruta que foi removida é {ultima_fruta}")