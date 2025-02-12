import json

def mostra_alunos():
    for aluno in lista_alunos:
        print('-'*20)
        for campo in aluno:
            print(f"{campo} - {aluno[campo]}")


lista_alunos=[]
aluno={}
resposta="s"

print("---Cadastro de alunos---")

#leitura de arquivo ja salvo
with open("Cad_alunos.json") as file:
    lista_alunos = json.load

while resposta.lower()=="s":
    
    #entrada de dados
    nome=input("nome do aluno:")
    matricula=input("matricula do aluno:")
    mensalidade=float(input("mensalidade do aluno:"))
    
    #preenche o dicionario
    aluno["nome"]=nome
    aluno["matricula"]=matricula
    aluno["mensalidade"]=mensalidade
    
    #add o aluno na lista
    lista_alunos.append(aluno.copy())
    resposta=input("Deseja cadastrar outro aluno(s-sim ou n-não): ")

qnt_alunos=len(lista_alunos)    
print(f"foram cadastrados {qnt_alunos} alunos!")
    
#mostrar todos os alunos cadastrados
resp=input("Deseja listar os alunos cadastrados (s ou n): ").lower()
if resp =="s":
    for aluno in lista_alunos:
        print('-'*20)
        for campo in aluno:
            print(f"{campo} - {aluno[campo]}")
            
#perguntar se quer salvar no arquivo, se sim, salvar em um arquivo json, se nao, nao salvar
resp=input("Deseja salvar os alunos cadastrados (s ou n): ").lower()
if resp=='s':
    with open("Cad_alunos.json", "w") as arquivo:
        arquivo.write(json.dumps(lista_alunos))