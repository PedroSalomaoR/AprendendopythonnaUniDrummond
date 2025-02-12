aluno={
    "nome":"José da Silva",
    "idade": 25,
    "matricula":"437593653",
    "dependentes":[
       "José Jr." , "Maria Da Silva" 
    ],
    "mensalidade": 2342.50,
    "endereco":{
        "rua":"rua dois",
        "numero": 20,
        "cep": "08434-222"
    },
    "telefones":["(11)98764-4563", "(21)90881-2434"]
    }

#print(aluno["nome"])
#aluno["mensalidade"]=aluno["mensalidade"]*1.1
#print(aluno["mensalidade"])


#se o campo nao existe, ele é add no dicionário
aluno["cpf"]='12345678900'
print(aluno)

aluno_endereco=aluno.get("none")
print(aluno_endereco)