fat=int(input("Digite um numero para saber seu fatorial: "))
num=1

for cont in range(fat,0,-1):
    num*=cont
    
print(f"O fatorial de {fat} é {num}")    
print(f"{fat} != {num}")