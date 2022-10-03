import random #importe para números aleátorios 


print("------------------------------------");
print("| Bem vindo ao jogo de adivinhação |");
print("------------------------------------");

print("------------------ Escolha a dificuldade ------------------")
f = 10;
m = 20;
d = 50;
print("            f (FACIL) | m (MEDIO) | d (DIFICIL)")
escolha = input("------> ")

if escolha == "f":
    numero_secreto = random.randint(1,f)
elif escolha == "m":
    numero_secreto = random.randint(1,m)
elif escolha == "d":
    numero_secreto = random.randint(1,d)
else:
    print("DIFICULDADE NÃO ENCONTRADA")

print(numero_secreto)

for i in range(3): # for que vai rodar até o número de tentativas acabar
    numero_usuario = int(input("\nDigite seu número da sorte --> "));

    if numero_usuario == numero_secreto: #caso o usuário acerte
        print("\n***********************");
        print("PARABÉNS VOCÊ ACERTOU!!");
        print("***********************");
        break

    elif i < 2 and numero_secreto < numero_usuario: #caso não esteja certo e seja maior que o sorteado
        print("\n====================================")
        print("Errado, tem mais",i+1,"de 3 Tentativas")
        print("\nTente um número mais baixo")
        print("====================================")

    elif i < 2 and numero_secreto > numero_usuario: #caso não esteja certo e seja menor que o sorteado
        print("\n====================================")
        print("Errado, tem mais",i+1,"de 3 Tentativas")
        print("\nTente um número mais alto")
        print("====================================")

    elif i >= 2: #caso o usuário erre todas as tentativas 
        print("»»»»»»»»»»»»»»»»»»»")
        print("Não foi dessa vez!!")
        print("»»»»»»»»»»»»»»»»»»»")
        print("O NÚMERO SORTEADO ERA ------> ", numero_secreto )

