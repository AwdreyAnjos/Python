import os # importe lib para limpar o terminal do python
import random #importe para números aleátorios 

os.system('cls' if os.name == 'nt' else 'clear'); # para limpar o terminal
# cls para windows 
# clear para linux

print("              ------------------------------------");
print("              | BEM VINDO AO JOGO DE ADIVINHAÇÃO |");
print("              ------------------------------------\n");

print("------------------ ESCOLHA SUA DIFICULDADE ------------------\n")
f = 10;
m = 20;
d = 50;
print(" ---------> f (FACIL) | m (MEDIO) | d (DIFICIL) <------------\n");


for x in range(3): # Escolhendo dificuldade do sorteio
    escolha = input("----------> ");
    x = escolha;
    if escolha == "f": # nivel facil - random  1 ao 10
        numero_secreto = random.randint(1,f);
        break
    elif escolha == "m": # nivel medio - random 1 ao 20
        numero_secreto = random.randint(1,m);
        break
    elif escolha == "d": # nivel dificil - random 1 ao 50
        numero_secreto = random.randint(1,d);
        break
    else:
        print("\n------------- DIFICULDADE NÃO ENCONTRADA ---------------");
        print("------------------ TENTE NOVAMENTE -----------------\n")


for i in range(3): # for que vai rodar até o número de tentativas acabar

    numero_usuario = int(input("\nDigite seu número da sorte --> "));

    if numero_usuario == numero_secreto: #caso o usuário acerte
        print("\n                ***********************");
        print("                PARABÉNS VOCÊ ACERTOU!!");
        print("                ***********************");
        break

    elif i < 2 and numero_secreto < numero_usuario: #caso não esteja certo e seja maior que o sorteado
        print("\n        ======================================");
        print("          ERRADO, TEM MAIS",i+1,"DE 3 TENTATIVAS");
        print("\n             TENTE UM NÚMERO MAIS BAIXO");
        print("        ======================================");

    elif i < 2 and numero_secreto > numero_usuario: #caso não esteja certo e seja menor que o sorteado
        print("\n        ======================================");
        print("          ERRADO, TEM MAIS",i+1,"DE 3 TENTATIVAS");
        print("\n               TENTE UM NÚMERO MAIS ALTO");
        print("        ======================================");

    elif i >= 2: #caso o usuário erre todas as tentativas 
        print("                »»»»»»»»»»»»»»»»»»»");
        print("                 NÃO FOI DESSA VEZ!");
        print("                »»»»»»»»»»»»»»»»»»»");
        print("           O NÚMERO SORTEADO ERA ------> ", numero_secreto );

