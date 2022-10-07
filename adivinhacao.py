from cgi import print_directory
import os # importe lib para limpar o terminal do python
import random
from re import X #importe para números aleátorios 

os.system('cls' if os.name == 'nt' else 'clear'); # para limpar o terminal
# cls para windows 
# clear para linux

print("\t------------------------------------");
print("\t| BEM VINDO AO JOGO DE ADIVINHAÇÃO |");
print("\t------------------------------------\n");

print("\t----- ESCOLHA SUA DIFICULDADE -----\n")
dificuldades = {'F':10,'M':20,'D': 50};
tentativas = 3;
print("\tf (FACIL) | m (MEDIO) | d (DIFICIL)\n");

x = False

while True: # Escolhendo dificuldade do sorteio
    escolha = input("\t----> ").upper(); #Deixa todas as letras em maiusculo

    if (dificuldades.get(escolha,None) != None): #Procura a letra que usuario adicionou no dicionario das
        limite = dificuldades.get(escolha)
        numero_secreto = random.randint(1,limite);
        break

    else:
        print("\n\t--- DIFICULDADE NÃO ENCONTRADA ---");
        print("\t--------- TENTE NOVAMENTE --------\n");

while x < tentativas: # for que vai rodar até o número de tentativas acabar

    numero_usuario = int(input("\n\tDigite seu número da sorte --> "));

    if (numero_usuario > limite):#Caso o usuário digite um número maior que o limite
        print("\n\t**************************************")
        print("\tNÚMERO MAIOR DO QUE O LIMITE DO SORTEIO");
        print("\n\tTENTE NOVAMENTE!! LIMITE 0 - {}".format(limite));
        print("\t**************************************")

    elif (numero_usuario < 0): #Caso o usuário digite um número menor que 0
        print("\n\t************************************")
        print("\tNÚMEROS NEGATIVOS NÃO SÂO ACEITOS")
        print("\n\tTENTE NOVAMENTE!! LIMITE 0 - {}".format(limite));
        print("\t************************************")

    elif (x >= 2): #caso o usuário erre todas as tentativas 
        print("\n\t»»»»»»»»»»»»»»»»»»»");
        print("\tNÃO FOI DESSA VEZ!");
        print("\t»»»»»»»»»»»»»»»»»»»");
        print("\tO NÚMERO SORTEADO ERA -> {}\n".format(numero_secreto));
        x += 1

    elif (numero_usuario == numero_secreto): #caso o usuário acerte
        print("\n\t***********************");
        print("\tPARABÉNS VOCÊ ACERTOU!!");
        print("\t***********************");
        break

    elif (numero_secreto < numero_usuario): #caso não esteja certo e seja maior que o sorteado
        print("\n\t======================================");
        print("\tERRADO, FORAM {} DE 3 TENTATIVAS".format(x+1));
        print("\n\tTENTE UM NÚMERO MAIS BAIXO");
        print("\t======================================");
        x += 1;

    elif (numero_secreto > numero_usuario): #caso não esteja certo e seja menor que o sorteado
        print("\n\t======================================");
        print("\tERRADO, FORAM {} DE 3 TENTATIVAS".format(x+1));
        print("\n\tTENTE UM NÚMERO MAIS ALTO");
        print("\t======================================");
        x += 1


