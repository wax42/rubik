



def suppr_mvt(x):
    "La fonction ne marche pas"
    global liste_mouvement
    #L'objectif serait de supprimer les mvts en trop
    #Par exemple quand il y a 4 mvts D, il faudrait les supprimer
    i = 0
    for i in range(len(liste_mouvement)):
        if liste_mouvement[i:i+3] == [x,x,x,x]:
            del liste_mouvement[i:i+3]
        elif liste_mouvement[i:i+2] == [x,x,x]:
            del liste_mouvement[i:i+2]
            liste_mouvement.insert(x+"I",i)
        if i >= len(liste_mouvement):
            break


def changer_liste(liste_mouvement):
        "exemple: [mvt_X]--->[X]"
    #modifie une liste comme l'exemple au dessus
    b = []
    for i in liste_mouvement:
            i = str(i)
            i = i.split()
            i = list(i[1])
            u=i[4:]
            u = list(u)
            u = "".join(u)
            b.append(u)
    liste_mouvement = list(b)
    return liste_mouvement # retourne la liste modifie


def suppr_mvt_y():
    "Supprime les mvts Y"
    global liste_mouvement
    #initialisation
    condition_mvt_Y = 0
    b = []
    for i in liste_mouvement:
            i = str(i)
            i = i.split()
            i = list(i[1])
            u=i[4]
            #on modifie i, afin d'avoir que la lettre du mvt dans u
            if u=="Y":
                if len(i) == 5: #Si i = mvt_YI, on enleve un a condition_mvt_y
                    condition_mvt_Y -= 1
                else:#Sinon on rajoute 1
                    condition_mvt_Y += 1
            if condition_mvt_Y == -1:
                condition_mvt_Y = 3
            if condition_mvt_Y == 4:
                condition_mvt_Y = 0
            if condition_mvt_Y == 1:#changement des mvts quand il y a un Y
                if u == "F":
                    u = "L"
                elif u == "L":
                    u = "B"
                elif u == "B":
                    u = "R"
                elif u == "R":
                    u = "F"
            if condition_mvt_Y == 2:#changement des mvts quand il y a 2 Y
                if u == "F":
                    u = "B"
                elif u == "L":
                    u = "R"
                elif u == "B":
                    u = "F"
                elif u == "R":
                    u = "L"
            if condition_mvt_Y == 3:#changement des mvts quand il y a 3 Y
                if u == "L":
                    u = "F"
                elif u == "B":
                    u = "L"
                elif u == "R":
                    u = "B"
                elif u == "F":
                    u = "R"
            i[4]=u
            i = "".join(i)
            i = eval(i)

            if u=="Y":
                del i
            else:
                b.append(i)

    liste_mouvement = list(b) #On remet la liste_modifie dans liste_mouvement


def valide_initialisation():
    "Valide l'initialisation"
    test_erreur() #Si il y a pas d'erreur
    resoudre() #On resout le rubik cube





def melanger():
    "Melange le rubik's cube en faisant au hasard plusieurs fois chaque mvt puis resout le rubik cube"
    nombreh = randrange(4)
    print (nombreh)
    while nombreh <3:
        mvt_D()
        nombreh = nombreh +1
    nombreh = randrange(4)

    while nombreh < 3:
        mvt_UI()
        nombreh = nombreh +1
    nombreh = randrange(4)
    while nombreh < 3:
        mvt_FI()
        nombreh = nombreh +1
    nombreh = randrange(4)
    while nombreh < 3:
        mvt_BI()
        nombreh = nombreh +1
    nombreh = randrange(4)
    while nombreh < 3:
        mvt_LI()
        nombreh = nombreh +1
    nombreh = randrange(4)
    while nombreh < 3:
        mvt_RI()
        nombreh = nombreh +1
    resoudre()

def mvt_D():
    "fait tourner la partie du bas du rubik's cube vers la droite ,ce mouvement s'appelle DOWN D  mouvement 1"
    V[7],V[8],V[9],J[1],J[2],J[3],B[7],B[8],B[9],W[7],W[8],W[9],O[1],O[2],O[3],O[4],O[6],O[7],O[8],O[9]  = W[7],W[8],W[9],V[9],V[8],V[7],J[3],J[2],J[1],B[7],B[8],B[9],O[7],O[4],O[1],O[8],O[2],O[9],O[6],O[3]
    liste_mouvement.append(mvt_D)
    if condition_aff ==True: #Permet d'afficher le mvt en cours dans la fenetre de dvlpt
        afficher_rubik_cube(case,fenetre)
        instruction_texte("mouvement D")
def mvt_DI():
    "inverse du mouvement 1 ,ce mouvement s'appelle DOWN DI mouvement 2"
    W[7],W[8],W[9],V[9],V[8],V[7],J[3],J[2],J[1],B[7],B[8],B[9],O[7],O[4],O[1],O[8],O[2],O[9],O[6],O[3] = V[7],V[8],V[9],J[1],J[2],J[3],B[7],B[8],B[9],W[7],W[8],W[9],O[1],O[2],O[3],O[4],O[6],O[7],O[8],O[9]
    liste_mouvement.append(mvt_DI)
    if condition_aff ==True:#Permet d'afficher le mvt en cours dans la fenetre de dvlpt
        afficher_rubik_cube(case,fenetre)
        instruction_texte("mouvement DI")
def mvt_U():
    "fait tourner la partie du haut du rubik's cube vers la gauche ,ce mouvement s'appelle UP U mouvement 3"
    V[1],V[2],V[3],J[7],J[8],J[9],B[1],B[2],B[3],W[1],W[2],W[3],R[1],R[2],R[3],R[4],R[6],R[7],R[8],R[9] = J[9],J[8],J[7],B[3],B[2],B[1],W[1],W[2],W[3],V[1],V[2],V[3],R[7],R[4],R[1],R[8],R[2],R[9],R[6],R[3]
    liste_mouvement.append(mvt_U)
    if condition_aff==True:#Permet d'afficher le mvt en cours dans la fenetre de dvlpt
        afficher_rubik_cube(case,fenetre)
        instruction_texte("mouvement U")
def mvt_UI():
    "inverse du mouvement 3 ,ce mouvement s'appelle UP UI mouvement 4"
    J[9],J[8],J[7],B[3],B[2],B[1],W[1],W[2],W[3],V[1],V[2],V[3],R[7],R[4],R[1],R[8],R[2],R[9],R[6],R[3] = V[1],V[2],V[3],J[7],J[8],J[9],B[1],B[2],B[3],W[1],W[2],W[3],R[1],R[2],R[3],R[4],R[6],R[7],R[8],R[9]
    liste_mouvement.append(mvt_UI)
    if condition_aff==True:#Permet d'afficher le mvt en cours dans la fenetre de dvlpt
        afficher_rubik_cube(case,fenetre)
        instruction_texte("mouvement UI")
def mvt_F():
    "ce mouvement s'appelle FRONT F mouvement 5"
    B[9],B[6],B[3],R[7],R[8],R[9],V[1],V[4],V[7],O[1],O[2],O[3],W[1],W[2],W[3],W[4],W[6],W[7],W[8],W[9] = O[3],O[2],O[1],B[9],B[6],B[3],R[7],R[8],R[9],V[7],V[4],V[1],W[7],W[4],W[1],W[8],W[2],W[9],W[6],W[3]
    liste_mouvement.append(mvt_F)
    if condition_aff==True:#Permet d'afficher le mvt en cours dans la fenetre de dvlpt
        afficher_rubik_cube(case,fenetre)
        instruction_texte("mouvement F")

def mvt_FI():
    "inverse du mouvement5, ce mouvement s'appelle FRONT FI mouvement 6"
    O[3],O[2],O[1],B[9],B[6],B[3],R[7],R[8],R[9],V[7],V[4],V[1],W[7],W[4],W[1],W[8],W[2],W[9],W[6],W[3] = B[9],B[6],B[3],R[7],R[8],R[9],V[1],V[4],V[7],O[1],O[2],O[3],W[1],W[2],W[3],W[4],W[6],W[7],W[8],W[9]
    liste_mouvement.append(mvt_FI)
    if condition_aff==True:#Permet d'afficher le mvt en cours dans la fenetre de dvlpt
        afficher_rubik_cube(case,fenetre)
        instruction_texte("mouvement FI")

def mvt_B():
    "Ce mouvement s'appelle BACK B mouvement 7"
    B[7],B[4],B[1],R[1],R[2],R[3],V[3],V[6],V[9],O[7],O[8],O[9],J[1],J[2],J[3],J[4],J[6],J[7],J[8],J[9] = R[1],R[2],R[3],V[3],V[6],V[9],O[9],O[8],O[7],B[1],B[4],B[7],J[7],J[4],J[1],J[8],J[2],J[9],J[6],J[3]
    liste_mouvement.append(mvt_B)
    if condition_aff==True:#Permet d'afficher le mvt en cours dans la fenetre de dvlpt
        afficher_rubik_cube(case,fenetre)
        instruction_texte("mouvement B")

def mvt_BI():
    "inverse du mouvement 7, ce mouvement s'appelle BACK BI mouvemment 8"
    R[1],R[2],R[3],V[3],V[6],V[9],O[9],O[8],O[7],B[1],B[4],B[7],J[7],J[4],J[1],J[8],J[2],J[9],J[6],J[3]  = B[7],B[4],B[1],R[1],R[2],R[3],V[3],V[6],V[9],O[7],O[8],O[9],J[1],J[2],J[3],J[4],J[6],J[7],J[8],J[9]
    liste_mouvement.append(mvt_BI)
    if condition_aff==True:#Permet d'afficher le mvt en cours dans la fenetre de dvlpt
        afficher_rubik_cube(case,fenetre)
        instruction_texte("mouvement BI")
def mvt_L():
    "Ce mouvement s'appelle LEFT L mouvement 9"
    R[1],R[4],R[7],W[1],W[4],W[7],O[1],O[4],O[7],J[1],J[4],J[7],B[1],B[2],B[3],B[4],B[6],B[7],B[8],B[9] = J[1],J[4],J[7],R[1],R[4],R[7],W[1],W[4],W[7],O[1],O[4],O[7],B[7],B[4],B[1],B[8],B[2],B[9],B[6],B[3]
    liste_mouvement.append(mvt_L)
    if condition_aff==True:#Permet d'afficher le mvt en cours dans la fenetre de dvlpt
        afficher_rubik_cube(case,fenetre)
        instruction_texte("mouvement L")
def mvt_LI():
    "inverse du mouvement 9,Ce mouvement s'appelle LEFT LI mouvement 10"
    J[1],J[4],J[7],R[1],R[4],R[7],W[1],W[4],W[7],O[1],O[4],O[7],B[7],B[4],B[1],B[8],B[2],B[9],B[6],B[3] = R[1],R[4],R[7],W[1],W[4],W[7],O[1],O[4],O[7],J[1],J[4],J[7],B[1],B[2],B[3],B[4],B[6],B[7],B[8],B[9]
    liste_mouvement.append(mvt_LI)
    if condition_aff==True:#Permet d'afficher le mvt en cours dans la fenetre de dvlpt
        afficher_rubik_cube(case,fenetre)
        instruction_texte("mouvement LI")
def mvt_R():
    "Ce mouvement s'appelle RIGHT R mouvement 11"
    R[3],R[6],R[9],W[3],W[6],W[9],O[3],O[6],O[9],J[3],J[6],J[9],V[1],V[2],V[3],V[4],V[6],V[7],V[8],V[9] = W[3],W[6],W[9],O[3],O[6],O[9],J[3],J[6],J[9],R[3],R[6],R[9],V[7],V[4],V[1],V[8],V[2],V[9],V[6],V[3]
    liste_mouvement.append(mvt_R)
    if condition_aff==True:#Permet d'afficher le mvt en cours dans la fenetre de dvlpt
        afficher_rubik_cube(case,fenetre)
        instruction_texte("mouvement R")
def mvt_RI():
    "inverse du mouvement 11, ce mouvement s'appelle RIGHT RI mouvement 12"
    W[3],W[6],W[9],O[3],O[6],O[9],J[3],J[6],J[9],R[3],R[6],R[9],V[7],V[4],V[1],V[8],V[2],V[9],V[6],V[3] = R[3],R[6],R[9],W[3],W[6],W[9],O[3],O[6],O[9],J[3],J[6],J[9],V[1],V[2],V[3],V[4],V[6],V[7],V[8],V[9]
    liste_mouvement.append(mvt_RI)
    if condition_aff==True:#Permet d'afficher le mvt en cours dans la fenetre de dvlpt
        afficher_rubik_cube(case,fenetre)
        instruction_texte("mouvement RI")
def mvt_Z():
    #741852963
    "change la disposition du rubik cube, rotation sur la droite"
    R[1],R[2],R[3],R[4],R[5],R[6],R[7],R[8],R[9],B[1],B[2],B[3],B[4],B[5],B[6],B[7],B[8],B[9],O[1],O[2],O[3],O[4],O[5],O[6],O[7],O[8],O[9],V[1],V[2],V[3],V[4],V[5],V[6],V[7],V[8],V[9] = B[7],B[4],B[1],B[8],B[5],B[2],B[9],B[6],B[3],O[7],O[4],O[1],O[8],O[5],O[2],O[9],O[6],O[3],V[7],V[4],V[1],V[8],V[5],V[2],V[9],V[6],V[3],R[7],R[4],R[1],R[8],R[5],R[2],R[9],R[6],R[3]
    W[1],W[2],W[3],W[4],W[6],W[7],W[8],W[9],J[7],J[4],J[1],J[8],J[2],J[9],J[6],J[3] = W[7],W[4],W[1],W[8],W[2],W[9],W[6],W[3],J[1],J[2],J[3],J[4],J[6],J[7],J[8],J[9]
    liste_mouvement.append(mvt_Z)
    if condition_aff==True:#Permet d'afficher le mvt en cours dans la fenetre de dvlpt
        afficher_rubik_cube(case,fenetre)
        instruction_texte("Mouvement Z")
def mvt_ZI():
    "change la disposition du rubik cube, rotation sur la gauche"
    B[7],B[4],B[1],B[8],B[5],B[2],B[9],B[6],B[3],O[7],O[4],O[1],O[8],O[5],O[2],O[9],O[6],O[3],V[7],V[4],V[1],V[8],V[5],V[2],V[9],V[6],V[3],R[7],R[4],R[1],R[8],R[5],R[2],R[9],R[6],R[3] = R[1],R[2],R[3],R[4],R[5],R[6],R[7],R[8],R[9],B[1],B[2],B[3],B[4],B[5],B[6],B[7],B[8],B[9],O[1],O[2],O[3],O[4],O[5],O[6],O[7],O[8],O[9],V[1],V[2],V[3],V[4],V[5],V[6],V[7],V[8],V[9]
    W[7],W[4],W[1],W[8],W[2],W[9],W[6],W[3],J[1],J[2],J[3],J[4],J[6],J[7],J[8],J[9] = W[1],W[2],W[3],W[4],W[6],W[7],W[8],W[9],J[7],J[4],J[1],J[8],J[2],J[9],J[6],J[3]
    liste_mouvement.append(mvt_ZI)
    if condition_aff==True:#Permet d'afficher le mvt en cours dans la fenetre de dvlpt
        afficher_rubik_cube(case,fenetre)
        instruction_texte("Mouvement ZI")
def mvt_XI():
    global R,W,O,J
    "rotation vers le bas"
    R,W,O,J = W,O,J,R
    V[1],V[2],V[3],V[4],V[6],V[7],V[8],V[9],B[1],B[2],B[3],B[4],B[6],B[7],B[8],B[9] = V[7],V[4],V[1],V[8],V[2],V[9],V[6],V[3],B[3],B[6],B[9],B[2],B[8],B[1],B[4],B[7]
    liste_mouvement.append(mvt_XI)
    if condition_aff==True:#Permet d'afficher le mvt en cours dans la fenetre de dvlpt
        afficher_rubik_cube(case,fenetre)
        instruction_texte("Mouvement XI")
def mvt_X():
    global R,W,O,J
    W,O,J,R = R,W,O,J
    "rotation vers le haut"
    V[7],V[4],V[1],V[8],V[2],V[9],V[6],V[3],B[3],B[6],B[9],B[2],B[8],B[1],B[4],B[7] = V[1],V[2],V[3],V[4],V[6],V[7],V[8],V[9],B[1],B[2],B[3],B[4],B[6],B[7],B[8],B[9]
    liste_mouvement.append(mvt_X)
    if condition_aff==True:#Permet d'afficher le mvt en cours dans la fenetre de dvlpt
        afficher_rubik_cube(case,fenetre)
        instruction_texte("Mouvement X")
def mvt_Y():
    "rotation vers la gauche"
    W[1],W[2],W[3],W[4],W[5],W[6],W[7],W[8],W[9],B[1],B[2],B[3],B[4],B[5],B[6],B[7],B[8],B[9],J[9],J[8],J[7],J[6],J[5],J[4],J[3],J[2],J[1],V[1],V[2],V[3],V[4],V[5],V[6],V[7],V[8],V[9] = V[1],V[2],V[3],V[4],V[5],V[6],V[7],V[8],V[9],W[1],W[2],W[3],W[4],W[5],W[6],W[7],W[8],W[9],B[1],B[2],B[3],B[4],B[5],B[6],B[7],B[8],B[9],J[9],J[8],J[7],J[6],J[5],J[4],J[3],J[2],J[1]
    R[3],R[6],R[9],R[2],R[8],R[1],R[4],R[7],O[1],O[2],O[3],O[4],O[6],O[7],O[8],O[9] = R[1],R[2],R[3],R[4],R[6],R[7],R[8],R[9],O[3],O[6],O[9],O[2],O[8],O[1],O[4],O[7]
    liste_mouvement.append(mvt_Y)
    if condition_aff==True:#Permet d'afficher le mvt en cours dans la fenetre de dvlpt
        afficher_rubik_cube(case,fenetre)
        instruction_texte("Mouvement Y")

def mvt_YI():
    "rotation vers la droite"
    V[1],V[2],V[3],V[4],V[5],V[6],V[7],V[8],V[9],W[1],W[2],W[3],W[4],W[5],W[6],W[7],W[8],W[9],B[1],B[2],B[3],B[4],B[5],B[6],B[7],B[8],B[9],J[9],J[8],J[7],J[6],J[5],J[4],J[3],J[2],J[1] = W[1],W[2],W[3],W[4],W[5],W[6],W[7],W[8],W[9],B[1],B[2],B[3],B[4],B[5],B[6],B[7],B[8],B[9],J[9],J[8],J[7],J[6],J[5],J[4],J[3],J[2],J[1],V[1],V[2],V[3],V[4],V[5],V[6],V[7],V[8],V[9]
    R[1],R[2],R[3],R[4],R[6],R[7],R[8],R[9],O[3],O[6],O[9],O[2],O[8],O[1],O[4],O[7] = R[3],R[6],R[9],R[2],R[8],R[1],R[4],R[7],O[1],O[2],O[3],O[4],O[6],O[7],O[8],O[9]
    liste_mouvement.append(mvt_YI)
    if condition_aff==True:#Permet d'afficher le mvt en cours dans la fenetre de dvlpt
        afficher_rubik_cube(case,fenetre)
        instruction_texte("Mouvement YI")


def test_arete():
    "Si deux aretes sont identiques affichent un msg d'erreur"
    #RAPPEL, les coins et les arrettes sont identiques tout le long
    #(W8,O2) (O8,J2) (V8,O6) (O4,B8) (B6,W4) (W2,R8) (V4,W6) (R6,V2) (R4,B2) (J8,R2) (J6,V6) (J4,B4)
    if W[8] == O[2]:
        instruction_texte("W8,O2")
        fenetre_erreur("W8,O2")
    elif O[8] == J[2]:
        instruction_texte("O8,J2")
        fenetre_erreur("O8,J2")
    elif V[8] == O[6]:
        fenetre_erreur("V8,O6")
        instruction_texte("V8,O6")
    elif O[4] == B[8]:
        instruction_texte("O4,B8")
        fenetre_erreur("O4,B8")
    elif B[6] == W[4]:
        instruction_texte("B6,W4")
        fenetre_erreur("B6,W4")
    elif W[2] == R[8]:
        instruction_texte("W2,R8")
        fenetre_erreur("W2,R8")
    elif V[4] == W[6]:
        instruction_texte("V4,W6")
        fenetre_erreur("V4,W6")
    elif R[6] == V[2]:
        instruction_texte("R6,W2")
        fenetre_erreur("R6,W2")
    elif R[4] == B[2]:
        instruction_texte("R4,B2")
        fenetre_erreur("R4,B2")
    elif J[8] == R[2]:
        instruction_texte("J8,R2")
        fenetre_erreur("J8,R2")
    elif J[6] == V[6]:
        instruction_texte("J6,V6")
        fenetre_erreur("J6,V6")
    elif J[4] == B[4]:
        instruction_texte("J4,B4")
        fenetre_erreur("J4,B4")
    else:
        instruction_texte("pas de probleme avec les aretes")

def test_coin():
    "Si deux coin d'un coin sont identique affiche un msg d'erreur"
    #(O1,W7,B9) (J1,O7,B7) (W1,R7,B3) (J3,O9,V9)(V1,W3,R9) (J7,R1,B1) (O3,W9,V7) (J9,R3,V3)
    if O[1] == W[7] or W[7] == B[9] or O[1] == B[9]:
        instruction_texte("O1,W7,B9")
        fenetre_erreur("O1,W7,B9")
    elif J[1] == O[7] or O[7] == B[7] or J[1] == B[7]:
        instruction_texte("J1,O7,B7")
        fenetre_erreur("J1,O7,B7")
    elif W[1] == R[7] or R[7] == B[3] or W[1] == B[3]:
        instruction_texte("W1,R7,B3")
        fenetre_erreur("W1,R7,B3")
    elif J[3] == O[9] or O[9] == V[9] or J[3] == V[9]:
        instruction_texte("J3,O9,V9")
        fenetre_erreur("J3,O9,V9")
    elif V[1] == W[3] or W[3] == R[9] or V[1] == R[9]:
        instruction_texte("V1,W3,R9")
        fenetre_erreur("V1,W3,R9")
    elif J[7] == R[1] or R[1] == B[1] or J[7] == B[1]:
        instruction_texte("J7,R1,B1")
        fenetre_erreur("J7,R1,B1")
    elif O[3] == W[9] or W[9] == V[7] or O[3] == V[7]:
        instruction_texte("O3,W9,V7")
        fenetre_erreur("O3,W9,V7")
    elif J[9] == R[3] or R[3] == V[3] or J[9] == V[3]:
        instruction_texte("J9,R3,V3")
        fenetre_erreur("J9,R3,V3")
    else:
        instruction_texte("pas de probleme avec les coins")
def creer_liste_inverse():
    "Creer la liste inverse de la liste_mouvement_final"
    global liste_inverse,numero_mvt,liste_mouvement_final
    liste_inverse = list(liste_mouvement_final)#On copie la liste_mouvement_final dans la liste_inverse
    b = []
    for i in liste_inverse: #Pour chaque element de la liste_inverse
        i = str(i)
        i = i.split()
        i = list(i[1])
        if len(i) == 5: #Si l"element n'a pas de I a la fin
            i.append("I") #On en rajoute un
        elif len(i) == 6: # Si l'element a un I a la fin
            del i[5] #On le supprime
        i = "".join(i)
        i = eval(i)
        b.append(i) #On stocke tous les elements dans b
    liste_inverse = list(b) #puis on copie b dans liste_inverse
    instruction_texte(len(liste_mouvement_final))
def back():
    "Permet de faire un mvt en -"
    global numero_mvt
    print(numero_mvt)
    if numero_mvt <= 0 :#Si le numero mvt est plus petit ou egale a 0
        instruction_texte("Numero du mouvement"+str(numero_mvt)) #On fait rien
    else:
        instruction_texte("Numero du mouvement"+str(numero_mvt))
        liste_inverse[numero_mvt-1]() #Sinon on fait le mvt-1
        numero_mvt -= 1 #et on enleve 1 a numero_mvt
        page_accueil() #Et on reaffiche la page d'accueil


def next():
    global numero_mvt
    if numero_mvt >= len(liste_mouvement_final):#Si le numero mvt est plus grand ou egale a la taille de la liste_mouvement_final
        instruction_texte("Numero du mouvement"+str(numero_mvt)) #On fait rien
    else:
        instruction_texte("Numero du mouvement"+str(numero_mvt))
        liste_mouvement_final[numero_mvt]() #Sinon on fait le mvt
        numero_mvt += 1#et on ajouter 1 a numero_mvt
        page_accueil()#Et on reaffiche la page d'accueil


def resoudre():
    "Permet de resoudre le rubik's cube"
    global liste_mouvement,liste_condition_etape,rubik_cube_init,liste_mouvement_final,numero_mvt
    #Initialisation
    liste_mouvement = []
    #On enrengistre les variables qui contiennent la coleur de chaque case
    rubik_cube_init = [R[1],R[2],R[3],R[4],R[5],R[6],R[7],R[8],R[9],W[1],W[2],W[3],W[4],W[5],W[6],W[7],W[8],W[9],O[1],O[2],O[3],O[4],O[5],O[6],O[7],O[8],O[9],J[1],J[2],J[3],J[4],J[5],J[6],J[7],J[8],J[9],B[1],B[2],B[3],B[4],B[5],B[6],B[7],B[8],B[9],V[1],V[2],V[3],V[4],V[5],V[6],V[7],V[8],V[9]]
    rubk_cube_init = list(rubik_cube_init)
    croix()
    croix_bien_aligne()
    premiere_couronne()
    deuxieme_couronne()
    #retourner le rubik cube
    mvt_X()
    mvt_X()
    croix_inverse()
    croix_bien_aligne()
    coin_position()
    derniere_etape()
    suppr_mvt_y()
    #On modifie les variables de chaque afin qu'elle soit comme au debut de de la resolution
    R[1],R[2],R[3],R[4],R[5],R[6],R[7],R[8],R[9],W[1],W[2],W[3],W[4],W[5],W[6],W[7],W[8],W[9],O[1],O[2],O[3],O[4],O[5],O[6],O[7],O[8],O[9],J[1],J[2],J[3],J[4],J[5],J[6],J[7],J[8],J[9],B[1],B[2],B[3],B[4],B[5],B[6],B[7],B[8],B[9],V[1],V[2],V[3],V[4],V[5],V[6],V[7],V[8],V[9] = rubik_cube_init
    #initialisation pour l'affichage
    numero_mvt = 0 #Index du mvt a faire
    liste_mouvement_final = list(liste_mouvement)
    creer_liste_inverse()
    page_accueil()#On affiche le tout dans notre fenetre d 'accueil

def croix():
    #incorporation des conditions pour chaque cas de la croix dans une liste
    liste_3emecas = [[V[4],mvt_FI],[B[6],mvt_F],[O[8],mvt_D,mvt_D,mvt_F,mvt_F],[O[6],mvt_DI,mvt_F,mvt_F],[O[4],mvt_D,mvt_F,mvt_F],[O[2],mvt_F,mvt_F],[W[2],mvt_F,mvt_UI,mvt_R],[W[6],mvt_UI,mvt_R],[W[4],mvt_U,mvt_LI],[W[8],mvt_F,mvt_U,mvt_LI]]
    liste_2case1 = [[O[6],mvt_DI,mvt_F,mvt_F],[O[8],mvt_D,mvt_D,mvt_F,mvt_F],[O[4],mvt_LI,mvt_LI],[O[2],mvt_F,mvt_F],[W[6],mvt_F,mvt_F,mvt_LI],[W[2],mvt_FI,mvt_LI],[W[8],mvt_F,mvt_LI],[W[4],mvt_LI],[V[4],mvt_FI],[B[6],mvt_F]]
    liste_2case2 = [[W[6],mvt_R],[W[4],mvt_LI],[W[8],mvt_F,mvt_LI],[W[2],mvt_F, mvt_R],[O[4],mvt_LI,mvt_LI],[O[6],mvt_R,mvt_R],[O[2],mvt_D,mvt_R,mvt_R],[O[8],mvt_D,mvt_LI,mvt_LI]]
    liste_1case = [[W[4], mvt_LI],[W[6], mvt_R],[W[2], mvt_F, mvt_R],[W[8], mvt_F, mvt_LI],[O[4], mvt_LI, mvt_LI],[O[6], mvt_R, mvt_R],[O[2],mvt_F, mvt_F]]
    liste_0case = [[W[4],mvt_LI],[W[6],mvt_R],[W[2],mvt_F,mvt_R],[W[8],mvt_F,mvt_LI],[B[6],mvt_F],[V[4],mvt_FI],[O[4],mvt_LI,mvt_LI],[O[6],mvt_R,mvt_R],[V[6],mvt_B],[B[4],mvt_BI]]
    condition_a = True
    if R[5] == R[4] and R[5] == R[2] and R[5] == R[6] and R[5] == R[8]: #Si les cases R[4],R[6],R[8],R[5] sont de la meme couleur
        #la croix est bonne
        print("la croix est bonne")
        instruction_texte("la croix est bonne")
    else:
        #On recherche quel cas on peut appliquer
        if R[5] != R[4] and R[5] == R[2] and R[5] == R[6] and R[8]== R[5]: #On peut appliquer le troisieme cas, mais il faut orienter le cube avant
            mvt_YI()                                                        #Donc mvt_YI()
        elif R[5] == R[4] and R[5] != R[2] and R[5] == R[6] and R[8]== R[5]:
            mvt_Y()
            mvt_Y()
        elif R[5] == R[4] and R[5] == R[2] and R[5] != R[6] and R[8]== R[5]:
            mvt_Y()
        elif R[5] == R[4] and R[5] == R[2] and R[5] == R[6] and R[8]!= R[5]:#On peut appliquer le troisieme cas
            instruction_texte("troisieme cas")
            for x in liste_3emecas: #On parcours la liste troisieme cas
                if x[0] == R[5]: #Si le premier terme est egale a R[5]
                    condition_a = False
                    for i in range(len(x)-1): #Alors on execute les fonctions qui suive la condition
                        x[i+1]()
                    break #fin de la boucle
            if condition_a == True:
                    mvt_Y()
                    mvt_UI()
        #Le raisonnement est le meme pour chaque cas
        elif R[4] == R[5] and R[8] == R[5] and R[2]!= R[5] and R[6]!=R[5]:
            mvt_Y()
            mvt_Y()
        elif R[6] == R[5] and R[8] == R[5] and R[2]!= R[5] and R[4]!=R[5] :
            mvt_YI()
        elif R[2] == R[5] and R[6] != R[5] and R[4]==R[5] and R[8]!=R[5]:
            mvt_Y()
        elif R[2] == R[5] and R[6] == R[5] and R[4]!=R[5] and R[8]!=R[5]:
            instruction_texte("deuxieme cas 1")
            for x in liste_2case1:
                if x[0] == R[5]:
                    condition_a = False
                    for i in range(len(x)-1):
                        x[i+1]()
                    break
            if condition_a == True:
                    mvt_Y()
                    mvt_UI()



        elif R[2] != R[5] and R[8] != R[5] and R[4] ==R[5] and R[6] == R[5]:
            mvt_Y()
        elif R[2] == R[5] and R[8] == R[5] and R[4] !=R[5] and R[6] != R[5]:
            instruction_texte("deuxieme cas 2")
            for x in liste_2case2:
                if x[0] == R[5]:
                    condition_a = False
                    for i in range(len(x)-1):
                        x[i+1]()
                    break
            if condition_a == True:
                    mvt_Y()
                    mvt_UI()

        elif R[2] != R[5] and R[8] == R[5] and R[4] !=R[5] and R[6] != R[5]:
            mvt_Y()
            mvt_Y()
        elif R[2] != R[5] and R[8] != R[5] and R[4] ==R[5] and R[6] != R[5]:
            mvt_Y()
        elif R[2] != R[5] and R[8] != R[5] and R[4] !=R[5] and R[6] == R[5]:
            mvt_YI()
        elif R[2] == R[5] and R[8] != R[5] and R[4] !=R[5] and R[6] != R[5]:
            instruction_texte("premier cas")
            for x in liste_1case:
                if x[0] == R[5]:
                    condition_a = False
                    for i in range(len(x)-1):
                        x[i+1]()
                    break
            if condition_a == True:
                    mvt_Y()
                    mvt_UI()
        elif R[2] != R[5] and R[8] != R[5] and R[4] !=R[5] and R[6] != R[5]:
            instruction_texte("0 cas")
            for x in liste_0case:
                print(x[0])
                if x[0] == R[5]:
                    condition_a = False
                    for i in range(len(x)-1):
                        x[i+1]()
                    break
            if condition_a == True:
                    mvt_Y()
                    mvt_UI()
        else:
            mvt_Y()
            mvt_UI()
        croix()

def croix_bien_aligne():
    "la croix est sur la face tout en haut(quand le rubik est en T)"
    if B[5] == B[2] and J[5] == J[8] and W[5] == W[2] and V[2] == V[5]:
        #la croix est bien aligne
        print("croix bien aligne")
        instruction_texte("croix bien aligne")
    else:
        if J[5] == J[8] and V[2] == V[5]:
            mvt_YI()
        elif V[2] == V[5] and W[2] == W[5]:
            mvt_Y()
            mvt_Y()
        elif W[2] == W[5] and B[5] == B[2]:
            mvt_Y()
        elif B[5] == B[2] and J[5] == J[8]:
            mvt_R()
            mvt_U()
            mvt_U()
            mvt_RI()
            mvt_UI()
            mvt_R()
            mvt_UI()
            mvt_RI()
            mvt_UI()
        elif  W[5] == W[2] and J[8] == J[5] and B[5] != B[2] and V[2] != V[5]:
            mvt_Y()
        elif  B[5] == B[2] and V[2] == V[5] and W[5] != W[2] and J[8] != J[5]:
            chaise_droite()
        else:
            mvt_U()
        croix_bien_aligne()
def premiere_couronne():
    "la croix est sur la face tout en haut(quand le rubik est en T)"
    if B[1] == B[5] and B[3] == B[5] and W[1] == W[5] and W[3] == W[5] and V[1] == V[5] and V[3] == V[5] and J[7] == J[5] and J[9] == J[5]:
        print("premiere couronne bonne")
        instruction_texte("premiere couronne bonne")
    else:
        if W[7] == V[5] and B[9] ==R[5] and O[1] == W[5]:
            ascenseur_simpl1()
        elif V[9] == W[5] and O[9]==V[5] and J[3]==W[5]:
            ascenseur_simpl2()
        elif W[9] == R[5] and V[7] == V[5]:
            ascenseur_1()
        elif W[9] == W[5] and V[7] == R[5]:
            ascenseur_2()
        elif O[3] == R[5] and W[9] == W[5]: #pour revenir a lascenseur 2
            mvt_RI()
            mvt_DI()
            mvt_DI()
            mvt_R()
            mvt_D()
        elif W[3] == R[5] or V[1] == R[5] or R[9] ==R[5] and W[3] != W[5]: #permet de faire descendre un coin mal pLace
            mvt_RI()
            mvt_DI()
            mvt_R()
        else:
            a = randint(0,1)
            if a ==0:
                mvt_Y()
            elif a==1:
                mvt_D()
        premiere_couronne()

def ascenseur_1():
    mvt_R()
    mvt_FI()
    mvt_RI()
    mvt_F()
def ascenseur_2():
    mvt_FI()
    mvt_R()
    mvt_F()
    mvt_RI()
def ascenseur_simpl1():
    mvt_RI()
    mvt_D()
    mvt_R()
def ascenseur_simpl2():
    mvt_F()
    mvt_DI()
    mvt_FI()
def deuxieme_couronne():
    global condition_mvt_Y,condition_mvt_D,condition_erreur
    if W[4] == W[5] and W[6] == W[5] and V[4] == V[5] and V[6] == V[5] and B[4] == B[5] and B[6] == B[5] and J[4] == J[5] and J[6] == J[5]:
        print("deuxieme couronne ok")
        instruction_texte("deuxieme couronne ok")
    else:
        if W[5] == W[8] and O[2] == V[5]:
            belge_droite()
        elif W[5] == W[8] and O[2] == B[5]:
            belge_gauche()

        elif O[2] == O[5] and O[4] == O[5] and O[6] == O[5] and O[8] == O[5] or W[8] == O[5] and O[4] == O[5] and O[6] == O[5] and O[8] == O[5]:
            if W[6] != W[5] or V[4] != V[5]:
                belge_droite()
            elif B[6] != B[5] or W[4] != W[5]:
                belge_gauche()
        else:
            if condition_mvt_Y == 3:
                mvt_D()
                condition_mvt_D += 1
                if condition_mvt_D == 1:
                    condition_mvt_Y = 0
                    condition_mvt_D = 0
                    condition_erreur += 1
            elif condition_erreur == 10:
                condition_erreur = 0
                if W[6] != W[5] or V[4] != V[5]:
                    belge_droite()
                elif B[6] != B[5] or W[4] != W[5]:
                    belge_gauche()
            else:
                mvt_Y()
                condition_mvt_Y += 1
        deuxieme_couronne()


def belge_droite():
    mvt_DI()
    mvt_RI()
    mvt_D()
    mvt_R()
    mvt_D()
    mvt_F()
    mvt_DI()
    mvt_FI()
def belge_gauche():
    mvt_D()
    mvt_L()
    mvt_DI()
    mvt_LI()
    mvt_DI()
    mvt_FI()
    mvt_D()
    mvt_F()

def croix_inverse():
    if R[5] == R[4] and R[5] == R[2] and R[5] == R[6] and R[5] == R[8]:
        instruction_texte("Croix inverse bonne")
    else:
        if R[5] == R[4] and R[5] == R[6]:
            mvt_F()
            mvt_R()
            mvt_U()
            mvt_RI()
            mvt_UI()
            mvt_FI()
        elif R[5] == R[2] and R[5] == R[6]:
            mvt_YI()
        elif R[5] == R[8] and R[5] == R[6]:
            mvt_Y()
            mvt_Y()
        elif R[5] == R[4] and R[5] == R[8]:
            mvt_Y()
        else:
            mvt_F()
            mvt_U()
            mvt_R()
            mvt_UI()
            mvt_RI()
            mvt_FI()
        croix_inverse()
def chaise_droite():
    mvt_R()
    mvt_U()
    mvt_U()
    mvt_RI()
    mvt_UI()
    mvt_R()
    mvt_UI()
    mvt_RI()
def technique_final():
    mvt_RI()
    mvt_DI()
    mvt_R()
    mvt_D()
def derniere_etape():
    if R[1] == R[5] and R[3] == R[5] and V[1] == V[5] and V[3] == V[5] and B[1] == B[5] and B[3] == B[5] and J[7] == J[5] and J[3] == J[5]:
        instruction_texte("Rubik cube fini")
        print("Rubik cube fini")
    else:
        if R[9] != R[5]:
            technique_final()
        else:
            mvt_U()
        derniere_etape()

def coin_position():
    global condition_mvt_Y_coin
    ""
    a = True
    if R[9] == R[5] or R[9] == V[5] or R[9] == W[5]:
        if V[1] == R[5] or V[1] == V[5] or V[1] == W[5]:
            if W[3] == R[5] or W[3] == V[5] or W[3] == W[5]:

                if R[1] == R[5] or R[1] == B[5] or R[1] == J[5]:
                    if B[1] == R[5] or B[1] == B[5] or B[1] == J[5]:
                        if J[7] == R[5] or J[7] == B[5] or J[7] == J[5]:

                            if R[3] == R[5] or R[3] == V[5] or R[3] == J[5]:
                                if V[3] == R[5] or V[3] == V[5] or V[3] == J[5]:

                                    if J[9] == R[5] or J[9] == V[5] or J[9] == J[5]:
                                        if R[7] == R[5] or R[7] == B[5] or R[7] == W[5]:
                                            if B[3] == R[5] or B[3] == B[5] or B[3] == W[5]:
                                                if W[1] == R[5] or W[1] == B[5] or W[1] == W[5]:
                                                    print("Coin bien place")
                                                    instruction_texte("Coin bien place")
                                                    a = False




    if a == True:
        if R[9] == R[5] or R[9] == V[5] or R[9] == W[5]:
                if V[1] == R[5] or V[1] == V[5] or V[1] == W[5]:
                    if W[3] == R[5] or W[3] == V[5] or W[3] == W[5]:
                        technique_des_amis()

        if condition_mvt_Y_coin == 4:
            technique_des_amis()
            condition_mvt_Y_coin = 0

        else:
            mvt_Y()
            condition_mvt_Y_coin += 1
        coin_position()
def technique_des_amis():
    mvt_U()
    mvt_R()
    mvt_UI()
    mvt_LI()
    mvt_U()
    mvt_RI()
    mvt_UI()
    mvt_L()
#####################################################################################################################################################
#"initialisation"
condition_mvt_Y,condition_mvt_D,condition_erreur = 0,0,0  #Variable pour deuxieme couronne
condition_mvt_Y_coin = 0 #variable pour position coin
R1_coord = 150,0
B1_coord = 0,150
V1_coord = 300,150
condition_aff = False
tzst = 0
numero_mvt = 0
liste_mouvement = ["b"]
couleur =['white','red','blue','green','orange','yellow']
arete_blanche = 0
a = 0
dico_condition = {} # Condition pour gerer l'affichage dans la fenetre accueil
dico_condition["rubik"] = True
dico_condition["texte"] = True
dico_condition["bouton"] = True
dico_condition["image"] = True

affichage_texte_y = 260 #Pour l'affichage du mode developpeur
texte_save = []
texte_save.append("rien")#L'affiche ne marche pas sur le premier terme de la liste
#Initialisation de la zone texte
vitesse = 4000
liste_etape = []
W = ["W"]
#creation de la face blanche au centre
for i in range(9):
    W.append(couleur[0])
R = ["R"]
#creation de la face rouge en haut
for i in range(9):
    R.append(couleur[1])
B = ["B"]
#creation de la face bleu
for i in range(9):
    B.append(couleur[2])
V = ["V"]
#creation de la face verte
for i in range(9):
    V.append(couleur[3])
O = ["O"]
#creation de la face orange sous la face du centre
for i in range(9):
    O.append(couleur[4])
J = ["J"]
#creation de la face en bas
for i in range(9):
    J.append(couleur[5])
liste_couleur_dessin = {} #Initialisation de la couleur de la fenetre d'accueil et de ses widgets
liste_couleur_dessin["Fenetre"] = "white"
liste_couleur_dessin["Rubik"] = "ivory2"
liste_couleur_dessin["zone_texte"] = "floral white"
liste_couleur_dessin["bouton"] = "red"
fenetre = Tk() #Creation de la fenetre
fenetre.title("Rolveur")#nom de la fentre
#Enrengistrement de la hauteur et l'epaisseur de l'ecran
width_fenetre = fenetre.winfo_screenwidth()
height_fenetre = fenetre.winfo_screenheight()
#Initialisation des images
dico_image = {}
photo_menu = PhotoImage(file="image_menu.gif")
dico_image["image_menu.gif"] = photo_menu
# fenetre.iconbitmap(default = "rolveur_logo.ico") #Icone de la fenetre
image_play = PhotoImage(file="play.gif")
image_precedent = PhotoImage(file="precedent.gif")
image_suivant = PhotoImage(file="suivant.gif")
image_menu = PhotoImage(file="home.gif")
dico_image["play.gif"] =  image_play
dico_image["precedent.gif"] =  image_precedent
dico_image["suivant.gif"] =  image_suivant
dico_image["home.gif"] =  image_menu
photo_menu = PhotoImage(file="image_menu.gif")
dico_image["image_menu.gif"] = photo_menu
fenetre.configure(bg = liste_couleur_dessin["Fenetre"])
fenetre.minsize(width_fenetre,height_fenetre)#taille minimum de la fenetre
# fenetre_menu()# ne marche pas
# page_dvlt()
# initialisation_rubikcube()
melanger()#Affichage de la fenetre du menu
fenetre.mainloop()#Boucle Principale
fenetre.destroy
