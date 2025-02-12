senha="777777"
senhadigitada=""

while senhadigitada != senha:
    senhadigitada=input("Digite a senha com 6 digitos: ")
    
    if len(senhadigitada) != 6:
        print("Essa senha náo tem 6 digitos!")       
    else:
        if senhadigitada == senha:
            print("Senha correta!")
        else:
            print("Senha incorreta!")             
            
print("Entrou no sistema!")