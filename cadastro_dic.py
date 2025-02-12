import json

cadastro={} #cria um dicionário vazio
#cadastro=dict{}
#add os campos com os valores 
cadastro["nome"]="Umberto Da Silva"
cadastro["cep"]="08074-352"
cadastro["cidade"]="São Paulo"
cadastro["email"]=input("Digite o seu email: ")
cadastro["endereco"]=input("Digite o seu endereço: ")
cadastro["telefone"]=input("Digite o telefone: ")

for campo in cadastro:
    print(f"{campo} : {cadastro[campo]}")
    
    
#json.dumps(cadastro) 
#gravando os dados em um arquivo
#"W"- write-escreve
#"r"-Read-ler    
with open("dados.json", "w") as arquivo:
    #arquivo.write("Texto de teste de escrita do arquivo")  
    arquivo.write(json.dumps(cadastro)) 
    