# -*- coding: utf-8 -*-
#Trabalho 1 "B"
#Matheus Araujo
#Belchior Neto
#Joao Vitor De Jesus
#Gianluca

aux=0
error=[0]
erro=0
import random

def menu():
    print "  ___________________________________________ "
    print " |                                           |"
    print " |         __________________________        |"
    print " |        |                          |       |"
    print " |--------|      Jogo da Forca       |-------|"
    print " |        |__________________________|       |"
    print " |                                           |"
    print " |                                           |"
    print " |  _____                                    |"
    print " | |     |                                   |"
    print " | |     |                                   |"
    print " | |   (+_+)                                 |"
    print " | |    /|\                                  |"
    print " | |    / \                                  |"
    print " | |                                         |"
    print " |/ \                                        |"
    print " |                                           |"
    print " |(1) Iniciar o Jogo                         |"
    print " |(2) Desenvolvedores                        |"
    print " |(3) Instrucoes                             |"
    print " |(4) Sair                                   |"
    print " |___________________________________________|"

    escolha = input("Numero:")

    if escolha > 4 or escolha < 1:
        print "Digite um numero valido, por favor "
        menu()
    elif escolha == 1:
        for r in range (0,100):
            print ""
        while error[0] < 6:

            ver()
           
            aux1=0
            for x in range (0,len(palavrinha)):
                if traco[x] == palavrinha[x]:
                    aux1 += 1
            if aux1 == len(palavrinha):
                print imprimir()
                print""
                print""
                print" Y O U  W I N "
                return menu()
              
    elif escolha == 2:
        for p in range(0,100):
         print""
        print "Desevolvedores:"
        print ""
        print "Matheus Araujo"
        print "Belchior Neto"
        print "Joao Vitor De Jesus"
        print "Gianluca"
        return menu()
    elif escolha == 3:
        print "Bem-Vindo ao Jogo Da Forca."
        print "1- Utilize somente letras minusculas."
        print "2- Letras maiusculas, caracteres especiais e numeros seram contados como erro."
        print "3- NAO Coloque 2 letras nos campos de digitacao seram contados como erro caso ocorra."
        print "Bom Jogo e Boa Sorte"
        menu()
    elif escolha == 4:
        for p in range(0,100):
            print""
        return " Y O U  L E F T "

def erro1():
    if error[0] == 1:
        print "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
        print ""
        print " =======+                  "
        print " ||     |                  "        
        print " ||     ^                  "
        print " ||   (+_+)                " 
        print " ||                        "
        print " ||                        "
        print " ||                        "
        print "/__\                       "

    elif error[0] == 2:
        print "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
        print ""

        print " =======+                  "
        print " ||     |                  "        
        print " ||     ^                  "
        print " ||   (+_+)                "
        print " ||     |                  "
        print " ||                        "
        print " ||                        "
        print "/__\                       "
    elif error[0] == 3:
        print "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
        print ""

        print " =======+                  "
        print " ||     |                  "        
        print " ||     ^                  "
        print " ||   (+_+)                "
        print " ||     |\                 "
        print " ||                        "
        print " ||                        "
        print "/__\                       "
    elif error[0] == 4:
        print "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
        print ""

        print " =======+                  "
        print " ||     |                  "        
        print " ||     ^                  "
        print " ||   (+_+)                "
        print " ||    /|\                 "
        print " ||                        "
        print " ||                        "
        print "/__\                       "
    elif error[0] == 5:
        print "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
        print ""

        print " =======+                  "
        print " ||     |                  "        
        print " ||     ^                  "
        print " ||   (+_+)                "
        print " ||    /|\                 "
        print " ||      \                 "
        print " ||                        "
        print "/__\                       "
    elif error[0] == 6:
        print "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
        print ""

        print " =======+                  "
        print " ||     |                  "        
        print " ||     ^                  "
        print " ||   (+_+)                "
        print " ||    /|\                 "
        print " ||    / \                 "
        print " ||                        "
        print "/__\                       "

        print "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
        print ""
        print ""
        print "    G A M E   O V E R   " 
        ex=0
        while ex == 100000000000000000000000000000000000000000000000000000:
            ex += 1
        print menu()
def imprimir():
    print ''
    print ''
    for i in range(0,len(traco)):
        print traco[i],
    print ''
    return ''

arq = open ('dados.txt','r')
conteudo = arq.readlines()
arq.close()

indice = random.randint(0,len(conteudo)-1)
palavra = conteudo[indice]
traco = []

for i in range(0,len(palavra)-1):
    traco.append('_ '),

aux1=0
palavrinha=[]
for x in range (0,len(palavra)-1):
 palavrinha.append(palavra[x])
exu = [" "]
def ver():
        erro=0
        passe=0
        print imprimir()
        letra = raw_input('Digite uma letra: ')
        
        
        for k in range(0,len(exu)):
          if letra == exu[k]:
              passe += 1
              
            
        exu.append(letra)
        aux=0
        if passe == 0:
            for i in range(0,len(palavra)):
                if letra == palavra[i]:
                    traco[i] = letra
                else:
                   aux += 1               
                   if aux == len(palavra):
                        erro += 1
                        error[0] += erro
                    
                    

            erro1()
        else:
            print"Por favor, utilize outra letra."
            ver()


print menu()

