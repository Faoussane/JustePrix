import random
import json



def jeu(score):
    i = 0
    while 1:
        try:
            nbrEss = int(input('Entrez le nombre d\'essais  \t : '))
            break
        except:
            print('Entrez uniquement des nombres')
    nombre_mystere = random.randint(1, 100)
    print(nombre_mystere)
    while (nbrEss != i):
        i += 1
        while 1:
            try:
                nbr_user = int(input('Choisissez un nombre entre 1 à 100 \t :'))
                if (nbr_user > 0 and nbr_user < 101):
                    break
                else:
                    print('Respectez l\'intervalle svp')            
            except:
                print('Attention!!! Le caratère saisi n\'est pas un nombre \n RESSAYEZ SVP')
        if (nombre_mystere == nbr_user):
            print('🎉 Vous avez GAGNÉ 🎉')
            score += 1
            nombre_mystere = random.randint(1, 100)
        elif(nombre_mystere > nbr_user):
            print('C\'est moin!, le juste nombre est plus grand')
        else:
            print('C\'est plus!, le juste nombre est plus petit')
    print('_'*10)
    print(f'Nombre d\'essais : {i}  \nScore final : {score}')
    return score   

def scoreJSON(score):
    if score==0:
        with open('score.json', 'w') as f:
            json.dump('Pas de meilleur score pour l\'instant; Allez jouer !!!', f, indent=4)
    else:
        with open('score.json', 'w') as f:
            json.dump(score, f, indent=4) 
def LireScoreJSON():
    with open('score.json', 'r') as f:
        score=json.load(f)
        print(f'Meilleur score* : {score}')
def affiche():
    while True:
        print('__________BIENVENUE DANS LE JEUX DE JUSTE NOMBRE__________')
        print('\t 1-Jouer')
        print('\t 2-Meilleur score')
        print('\t 3-Quitter')
        while True:
            try:
                action = int(input('Choisissez une action : '))
                if (1<=action<=3):
                    break
                else:
                    print('Entrez uniquement des nombres entiers (1 - 3)')
            except:
                print('Entrez uniquement des nombres (1 - 3)')
        if action==1:
            score = 0
            score = jeu(score)
            with open('score.json', 'r') as f:
                scoreJSONvar=json.load(f)
                if isinstance(scoreJSONvar, int):
                    if scoreJSONvar < score:
                        scoreJSON(score)
                else:
                    scoreJSON(score)

        elif(action==2):
            LireScoreJSON()
        elif(action==3):
            break    

affiche()