num=int(input("Digite um numero para fazer a tabuada: "))

for multi in range(1,11):
    resultado=num*multi
    print(f"{num} X {multi} = {resultado}")
print("Fim da tabuada!")
