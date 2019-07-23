
class RubikSolver():

    def __init__(self):
        pass






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





def main():






if __name__ == '__main__':
    main()
    