import random
import re
import time
def ballgenerator():
    print ("pensando na sua resposta")
    time.sleep(random.randint(2,5))
    respostas= ['It is certain.','As I see it, yes.','Reply hazy, try again','Dont count on it.','It is decidedly so.']
    print(respostas[random.randint(0,respostas.__len__()-1)])


def pergunta():
    while True:
        x = input("Qual a sua pergunta? Para sair escreva \"exit\" \n")
        if re.match('^[A-Z][^?!.]*[?.!]$',x):
            ballgenerator()
        elif x!="exit":
            print ("ISSO NAO É UMA PERGUNTA MEU BOI")
        else:
            print ("BYE BYE")
            return


pergunta()