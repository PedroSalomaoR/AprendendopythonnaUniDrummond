#Estrutura de dados lista
lista1=[1,2,3,4,5,6,7,8]
lista2=["joao", 30, "Sei la oq", 265.2]
lst_multi_cpf=range(10,1,-1)

print(list(lst_multi_cpf))
soma=0
for mult in lst_multi_cpf:
    soma+=mult
    print(soma)