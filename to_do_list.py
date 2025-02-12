#criando uma lista vazia
lista_tarefas=[]
novo_item=""
print("Digite as tarefas ou 0 para sair: ")
cont=0
while novo_item!="0":
    cont+=1
    novo_item=input(f"Digite o {cont}o item da lista: ")
    if novo_item!="0":
        lista_tarefas.append(novo_item)
    print(list(lista_tarefas)) 
      
#len conta a quantidade de elementos da lista      
quant_tarefas=len(lista_tarefas)      
print(f"Voce tem {quant_tarefas} tarefas para fazer!")    
    