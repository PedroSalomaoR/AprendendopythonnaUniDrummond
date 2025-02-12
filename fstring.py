curso="Estrutura de dados"
duracao= 100
valor=1500.69
from datetime import datetime
hoje= datetime.now()
print(hoje)
print(f"Data: {hoje:%d-%m-%y}")

print(f" {curso} tem de {duracao} horas e com o valor de {valor}R$ ")