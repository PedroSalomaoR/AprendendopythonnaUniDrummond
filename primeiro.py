print(" Em quantas vezes o guilherme quer parcelar seu celular de 2,5K? ") 
print("1, recebe 15 por cento de desconto")
print("2, recebe 3 por cento de descoto")
print("3, paga valor cheio")
print("4, paga com 2 por cento de juros")
print("5, paga com 10 por cento de juros")
resposta = input("escolha as parcelas: ")
vldr = 2500
a = 2500 * 85/100 
b = (2500 * 97/100)/2
c = 2500/3
d = (2500 * 102/100)/4
e = (2500 * 110/100)/5


if resposta == "1": 
    print("Sua conta ira ficar em ", a)
if resposta == "2":
    print("Voce pagara ",resposta, " Parcelas de R$",b)    
if resposta == "3":
    print("Voce pagara ",resposta, " Parcelas de R$",c)
if resposta == "4":
    print("Voce pagara ",resposta, " Parcelas de R$",d)
if resposta == "5":
    print("Voce pagara ",resposta, " Parcelas de R$",e)
else:
    print("Para de ser beta!")