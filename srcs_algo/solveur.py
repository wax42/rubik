

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
        print("croix inverse bonne")
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
        # LA BOUCLE INFINI EST ICI

def technique_des_amis():
    mvt_U()
    mvt_R()
    mvt_UI()
    mvt_LI()
    mvt_U()
    mvt_RI()
    mvt_UI()
    mvt_L()

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


def main():
    pass





if __name__ == '__main__':
    main()
    