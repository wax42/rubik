try:
    from Tkinter import*
except:
    from tkinter import*
from random import randint,randrange
import webbrowser

def changer_val(a):
    "Change la valeur de la liste dico_condition, permet de gerer l'affichage"
    if  dico_condition[a]==0:  #Si la valeur = 0, la changer en 1
        dico_condition[a] =1
    else:
        dico_condition[a] = 0 #et inversement
    page_accueil()
def afficher_image(txt,nom_du_mvt = "B"):
    "Affiche une image de mouvement dans une zone (txt),à partir du nom de ce mouvement"
    if nom_du_mvt == "X" or nom_du_mvt == "XI": #Si on ne possede pas le mouvement x et xI,
        txt.insert(END,nom_du_mvt)          #il faut donc afficher du texte a la place
    else:
        image = PhotoImage(file="mvt_"+nom_du_mvt+".gif") #Sinon on affiche l'image
        dico_image["mvt_"+nom_du_mvt+".gif"] = image
        txt.image_create(END, image=image)


def debut():
    "Remet au début le rubik's cube"
    global numero_mvt,liste_etape
    liste_etape = []
    numero_mvt = 0 #numero_mvt est la variable qui gere la lecture de la liste_mouvement_final
    # et de la liste_inverse, Il faut donc le mettre a 0
    R[1],R[2],R[3],R[4],R[5],R[6],R[7],R[8],R[9],W[1],W[2],W[3],W[4],W[5],W[6],W[7],W[8],W[9],O[1],O[2],O[3],O[4],O[5],O[6],O[7],O[8],O[9],J[1],J[2],J[3],J[4],J[5],J[6],J[7],J[8],J[9],B[1],B[2],B[3],B[4],B[5],B[6],B[7],B[8],B[9],V[1],V[2],V[3],V[4],V[5],V[6],V[7],V[8],V[9] = rubik_cube_init
    #On remplace les informations des variables, permettant de gerer l'affichage
    #par les informations enrengistrer au debut dans rubik_cube_init
    page_accueil()

def vitesse_init():
    global vitesse
    vitesse = saisi.get()

def page_accueil():
    "Affiche la fenetre d'affichage/d'accueil"
    global menu_affichage,condition_rubik,numero_mvt,vitesse,saisi
    for c in fenetre.winfo_children(): #supprime tout les elements de la fenetre
        c.destroy()
    fenetre.wm_geometry("%dx%d+%d+%d" % (width_fenetre,height_fenetre, 0, 0))
    fenetre.minsize(width_fenetre,height_fenetre)#taille minimum de la fenetre
    if dico_condition["rubik"] == True: #Permet de gerer l'affichage du rubik's cube -1
        dessin_3D(fenetre,0,0,taille_carre= 15,text = "Rubik's cube(mvt -1)") #Creer le rubik's cube en haut a droite avec un mouvement en moins
    if len(liste_mouvement_final)-1 <= numero_mvt or numero_mvt== 0:
        dessin_3D(fenetre,width_fenetre*0.5,height_fenetre*0.5,taille_carre= width_fenetre*0.03,anchor = CENTER)
    else:  #affiche le rubik cube du centre avec un mouvement en plus
        liste_mouvement_final[numero_mvt+1]() #le mouvement en plus
        liste_etape_fonction()
        dessin_3D(fenetre,width_fenetre*0.5,height_fenetre*0.5,taille_carre=width_fenetre*0.03,anchor = CENTER)
        liste_inverse[numero_mvt+1]() #le mouvement en plus contraire

    if dico_condition["texte"] == True: #Permet de gerer l'affichage de la zone de texte
        texte_mvt(0,height_fenetre,anchor = SW)

    #Creation du nom Rolveur by Victor Guerand and Tom Casagrande
    zone= Text(fenetre,width=50,height=10,bg =liste_couleur_dessin["Fenetre"])
    zone.place(x= width_fenetre*0.4,y= 0,anchor = NW)
    zone.tag_configure('color', foreground='#476042',font=('Tempus Sans ITC', 80, 'italic')) #tag afin de definir le style, la couleur, et la taille
    zone.insert(END,"Rolveur","color","by Victor Guerand and Tom Casagrande") #insertion du texte avec le tag puis sans le tag

    saisi = Entry(fenetre, width=10)
    saisi.insert(END,str(vitesse))
    saisi.place(x=150,y=20)
    #Creation des menus
    texte_vitesse = Text(fenetre,width = 20,height = 1)
    texte_vitesse.insert(END,"Vitesse en ms:")
    texte_vitesse.place(x=150,y=0)
    Button(fenetre,text = "Entrer",command=vitesse_init,bg=liste_couleur_dessin["bouton"]).place(x=150,y=40)

    print(vitesse)
    menubar = Menu(fenetre)

    menufichier = Menu(menubar,tearoff=0) # menu parametre
    menufichier.add_command(label="Menu",command=fenetre_menu)
    menufichier.add_command(label="Reload",command=page_accueil)
    menufichier.add_command(label="melanger",command=melanger)
    menufichier.add_command(label="Quitter",command=fenetre.destroy)
    menubar.add_cascade(label="Parametre", menu=menufichier)


    menu_lecture = Menu(menubar,tearoff=0) # menu lecture
    menu_lecture.add_command(label="Play/Pause",command=play)
    menu_lecture.add_command(label="Debut",command=debut)
    menu_lecture.add_command(label="Precedent",command=back)
    menu_lecture.add_command(label="Suivant",command=next)
    menu_lecture.add_command(label="Initialisation",command=initialisation_rubikcube)
    menubar.add_cascade(label="Lecture", menu=menu_lecture)

    menu_affichage = Menu(menubar,tearoff=0)# menu affichage

    menu_modif = Menu(fenetre) # menu modifier la couleur
    menu_modif.add_command(label="Fond de la fenetre",command =lambda x="Fenetre":affichercolors(x))
    menu_modif.add_command(label="Fond Cadre des rubik's cubes",command =lambda x="Rubik":affichercolors(x))
    menu_modif.add_command(label="Fond zone de texte ",command =lambda x="zone_texte":affichercolors(x))
    menu_modif.add_command(label="Boutons ",command =lambda x="bouton":affichercolors(x))
    menu_affichage.add_cascade(label="modifier la couleur", menu=menu_modif)

    menu_aff = Menu(fenetre)# menu ajouter/enlever des options
    menu_aff.add_command(label="Rubik's cube (-1 mvt)",command =lambda a="rubik":changer_val(a))
    menu_aff.add_command(label="Boutons",command =lambda a="bouton":changer_val(a))
    menu_aff.add_command(label="Textes",command =lambda a="texte":changer_val(a))
    menu_affichage.add_cascade(label="Ajouter/enlever des options", menu=menu_aff)

    menu_couleur = Menu(fenetre)
    menubar.add_cascade(label="Affichage", menu=menu_affichage)

    menu_bonus = Menu(menubar,tearoff=0)
    menu_modif = Menu(fenetre)
    menu_modif.add_command(label="Comment resoudre le rubik'cube",command =lambda x="https://how-to-solve-a-rubix-cube.com/comment-resoudre-le-cube-rubik-fr/":webbrowser.open(x))
    menu_modif.add_command(label="Le rubik's cube pour les noobs",command =lambda x="http://www.rubiks-cube.fr/":webbrowser.open(x))
    menu_modif.add_command(label="Rubik's cube pdf",command =lambda x="http://www.ac-nice.fr/college-peiresc/admin/filemanager/userfiles/trousselier/Rubik_s_cube/Rubik_s_-_La_totale.pdf":webbrowser.open(x))
    menu_bonus.add_cascade(label="Site internet", menu=menu_modif)
    menu_bonus.add_command(label="Mode developpeur",command=page_dvlt)
    menu_bonus.add_command(label="Quitter",command=fenetre.destroy)
    menubar.add_cascade(label="En plus", menu=menu_bonus)



    # Affichage du menu
    fenetre.config(menu=menubar)


    variable =height_fenetre*0.5

    if dico_condition["bouton"] == True:#Permet de gerer l'affichage de la zone de texte
        Button(fenetre,image = image_play,command=play,bg=liste_couleur_dessin["bouton"]).place(x=width_fenetre*0.8+50,y=variable-100,anchor=NE)
        Button(fenetre,image = image_precedent,command=back,bg=liste_couleur_dessin["bouton"]).place(x=width_fenetre*0.8,y=variable,anchor=NE)
        Button(fenetre,image = image_suivant,command=next,bg=liste_couleur_dessin["bouton"]).place(x=width_fenetre*0.8,y=variable,anchor=NW)




def web_affichage(liste):
    "Permet d'ouvrir une page internet qui affiche un mvt"
    try:
        arg = " ".join(liste)
    except:
        arg = str(liste)
    webbrowser.open("https://alg.cubing.net/?alg="+arg+"&type=alg&view=fullscreen")




def affichercolors(i):
    "Affiche en {tableau} toute les couleurs disponiles"
    global colors,fenetre
    for c in fenetre.winfo_children():
        c.destroy()
    fichier = open("liste_couleur","r")
    colors = fichier.read()
    fichier.close()
    colors = colors.split(",")
    del colors[-1]
    Label(fenetre, text='Double  clique sur la couleur voulu').pack(fill='x')
    top = Frame(fenetre)
    colnum = int((len(colors)/3) ** 0.5)
    row = 0 #initialisation
    while colors:
        chunk, colors = colors[:colnum], colors[colnum:]
        for col, color in enumerate(chunk):
            lab = Label(top, text=color, bg=color)
            lab.grid(row=row, column=col, sticky='wens')
            lab.bind('<Double-1>', couleur_choisi(lab,i))
            lab.bind('<Enter>', lambda ev, lab=lab: lab.config(fg='white'))
            lab.bind('<Leave>', lambda ev, lab=lab: lab.config(fg='black'))
        row += 1
    top.pack(expand=True, fill='both')


def couleur_choisi(inst,i):
    "Permet de choissir une couleur dans afficher_colors(i)"
    def wrapper(event):
        inst.clipboard_clear()
        inst.clipboard_append(inst['text'])
        print(inst['text'])
        liste_couleur_dessin[i]  =  inst['text']
        if i =="Fenetre":
            fenetre.config(bg=liste_couleur_dessin[i])
        page_accueil()
    return wrapper



def fenetre_menu():
    "Affiche de la fenetre d'entree"
    fenetre.minsize(400,400) #On bloque la taille de la fenetre
    fenetre.maxsize(400,400) #On bloque la taille de la fenetre
    for c in fenetre.winfo_children():
        c.destroy()
    zone_dessin = Canvas(fenetre,width=width_fenetre, height=height_fenetre,cursor="rtl_logo") #Creation d un Canvas pour afficher l'image
    zone_dessin.place(x=0,y=0)
    zone_dessin.create_image(0,0,anchor=NW,image=photo_menu)#affichage de l'image
    #Creation des menus
    menubar = Menu(fenetre)
    menufichier = Menu(menubar,tearoff=0)# Menu resoudre
    menufichier.add_command(label="Entrer Rubik's cube",command=initialisation_rubikcube)
    menufichier.add_command(label="Rubik's cube au hasard",command=melanger)
    menubar.add_cascade(label="Resoudre", menu=menufichier)


    menu_bonus = Menu(menubar,tearoff=0)
    menu_modif = Menu(fenetre)#menu En plus
    menu_modif.add_command(label="Comment resoudre le rubik'cube",command =lambda x="https://how-to-solve-a-rubix-cube.com/comment-resoudre-le-cube-rubik-fr/":webbrowser.open(x))
    menu_modif.add_command(label="Le rubik's cube pour les noobs",command =lambda x="http://www.rubiks-cube.fr/":webbrowser.open(x))
    menu_modif.add_command(label="Rubik's cube pdf",command =lambda x="http://www.ac-nice.fr/college-peiresc/admin/filemanager/userfiles/trousselier/Rubik_s_cube/Rubik_s_-_La_totale.pdf":webbrowser.open(x))
    menu_bonus.add_cascade(label="Site internet", menu=menu_modif)
    menu_bonus.add_command(label="Mode developpeur",command=page_dvlt)
    menu_bonus.add_command(label="Quitter",command=fenetre.destroy)
    menubar.add_cascade(label="En plus", menu=menu_bonus)
    #affichage du menu
    fenetre.config(menu=menubar)


def texte_mvt(x,y,anchor = NE):
    "Creation du texte dans la page_accueil"
    global liste_mouvement_final
    liste = changer_liste(liste_mouvement_final)#Transforme la liste (mvt_X --- >X)
    zone_texte = Text(fenetre,width=int(width_fenetre*0.02),height=int(height_fenetre*0.04),bg =liste_couleur_dessin["zone_texte"]) #Creation de la zone de texte
    #Creation des tags
    zone_texte.tag_configure('color', foreground='#476042',font=('Tempus Sans ITC', 12, 'bold'))
    zone_texte.tag_configure('Etapeactuelle', foreground='red',font=('Tempus Sans ITC', 10, 'bold'))
    zone_texte.tag_configure('Etape', foreground='Black',font=('Tempus Sans ITC', 8, 'italic'))
    zone_texte.place(x=x,y=y,anchor = anchor)
    scrollb = Scrollbar(fenetre,command=zone_texte.yview) #Creation du scrool
    scrollb.place(x=width_fenetre*0.2,y=height_fenetre*0.5)
    zone_texte['yscrollcommand'] = scrollb.set
    zone_texte.insert(END,"Numero du mouvement:"+str(numero_mvt)+"\n",'color') #Affiche numero du mvt
    zone_texte.insert(END,"Mouvement restant:"+str(len(liste_mouvement_final)-numero_mvt)+"\n",'color')#Affiche mouvement restant

    zone_texte.insert(END,"Mouvement a faire:\n",'color')#Affiche mouvement a faire
    if numero_mvt <= len(liste_mouvement_final)-1:
        afficher_image(zone_texte,nom_du_mvt= liste[numero_mvt]) #Affiche LE (l'image du) mvt a faire
    zone_texte.insert(END,"\nListe des mouvements\n",'color') #Affiche liste des mouvements
    for i in range(len(liste)):
        if i == numero_mvt:
            zone_texte.insert(END,str(liste[i])+" ",'Etapeactuelle') # Affiche le mouvement a faire dans une couleur differente
        else:
            zone_texte.insert(END,str(liste[i])+" ",liste[i]) #Sinon affiche le mvt normalement


    zone_texte.insert(END,"\nEtape a faire:\n",'color') #Affiche etape a faire
    #initialisation des etapes
    liste_info = "Etape 1: Faire la croix","Etape 2:la croix bien aligné","Etape 3:Premiere couronne","Etape 4:Deuxieme couronne","Etape 5:la croix inverse","Etape 6:la croix inverse bien aligné","Etape 7:Positionnement des coins","Etape 8:Orientation des coins"
    for i in range(len(liste_info)):
        if i == len(liste_etape):
            zone_texte.insert(END,liste_info[i]+"\n",'Etapeactuelle') #affiche l'etape actuel d'une couleur differente
        else:
            zone_texte.insert(END,str(liste_info[i])+"\n","Etape") #Sinon affiche l etape normalement
    zone_texte.insert(END,"\n\n\n\n""created by Victor Guerand\nand Tom Casagrande",'Etape')
    #Creer un tag pour chaque mvt afin de pouvoir cliquer dessus
    zone_texte.tag_bind("X", "<1>",lambda e:web_affichage("x"))
    zone_texte.tag_bind("L", "<1>",lambda e:web_affichage("L"))
    zone_texte.tag_bind("R", "<1>",lambda e:web_affichage("R"))
    zone_texte.tag_bind("U", "<1>",lambda e:web_affichage("U"))
    zone_texte.tag_bind("F", "<1>",lambda e:web_affichage("F"))
    zone_texte.tag_bind("B", "<1>",lambda e:web_affichage("B"))
    zone_texte.tag_bind("XI", "<1>",lambda e:web_affichage("x-")) #Bug avec les mvts inverses
    zone_texte.tag_bind("LI", "<1>",lambda e:web_affichage("L-"))
    zone_texte.tag_bind("RI", "<1>",lambda e:web_affichage("R-"))
    zone_texte.tag_bind("UI", "<1>",lambda e:web_affichage("U-"))
    zone_texte.tag_bind("FI", "<1>",lambda e:web_affichage("F-"))
    zone_texte.tag_bind("BI", "<1>",lambda e:web_affichage("B-"))

def liste_etape_fonction():
    "Permet de trouver quand sont fait les etapes a partir du numero_mvt"
    if R[5] == R[4] and R[5] == R[2] and R[5] == R[6] and R[5] == R[8]:
        if len(liste_etape) == 0:
            liste_etape.append(numero_mvt)
        else:
            if B[5] == B[2] and J[5] == J[8] and W[5] == W[2] and V[2] == V[5]:
                if len(liste_etape) == 1:
                    liste_etape.append(numero_mvt)
                else:
                    if B[1] == B[5] and B[3] == B[5] and W[1] == W[5] and W[3] == W[5] and V[1] == V[5] and V[3] == V[5] and J[7] == J[5] and J[9] == J[5]:
                        if len(liste_etape) == 2:
                            liste_etape.append(numero_mvt)
                        else:
                            if W[4] == W[5] and W[6] == W[5] and V[4] == V[5] and V[6] == V[5] and B[4] == B[5] and B[6] == B[5] and J[4] == J[5] and J[6] == J[5]:
                                if len(liste_etape) == 3:
                                  liste_etape.append(numero_mvt)
                                else:
                                    if R[5] == R[4] and R[5] == R[2] and R[5] == R[6] and R[5] == R[8]:
                                        if len(liste_etape) == 4:
                                            liste_etape.append(numero_mvt)
                                        else:
                                            if B[5] == B[2] and J[5] == J[8] and W[5] == W[2] and V[2] == V[5]:
                                                if len(liste_etape) == 5:
                                                    liste_etape.append(numero_mvt)
                                                else:
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
                                                                                                    if len(liste_etape) == 6:
                                                                                                        liste_etape.append(numero_mvt)
                                                                                                    else:
                                                                                                        if R[1] == R[5] and R[3] == R[5] and V[1] == V[5] and V[3] == V[5] and B[1] == B[5] and B[3] == B[5] and J[7] == J[5] and J[3] == J[5]:
                                                                                                             liste_etape.append(numero_mvt)





def play():
    "Permet de lire tout seul les mouvements a faire"
    global numero_mvt
    next() #Passe au mouvement suivant
    if numero_mvt <= len(liste_mouvement_final)-1: #Si il reste des mvts a faire
        fenetre.after(int(vitesse),play) #Marquer une pause puis relancer la fonction play
    else: #Sinon ne rien faire
        print("fini") #afin de quitter la boucle

def page_dvlt():
    "Page de travail"
    global case
    for c in fenetre.winfo_children():
        c.destroy()

    fenetre.wm_geometry("%dx%d+%d+%d" % (width_fenetre,height_fenetre, 0, 0))
    fenetre.minsize(width_fenetre,height_fenetre)#taille minimum de la fenetre
    case = Canvas(fenetre, width=450, height=650, bg='dark grey')
    #defintion de la taille du fond du dessin et de sa couleur
    case.place(x=0,y=0)#permet d'afficher le dessin
    zonetexte = Canvas(fenetre,width=600, height=300, bg='cyan')
    zonetexte.place(x=450,y=0)
    texte_enter = Entry(fenetre,width=100)
    texte_enter.place(x=450,y=280)
    afficher_rubik_cube(case,fenetre)
    #GAUCHE
    Button(fenetre,text="D",command=mvt_D).pack(side =LEFT, padx =3, pady =3)
    Button(fenetre,text="U",command=mvt_U).pack(side =LEFT, padx =3, pady =3)
    Button(fenetre,text="F",command=mvt_F).pack(side =LEFT, padx =3, pady =3)
    Button(fenetre,text="B",command=mvt_B).pack(side =LEFT, padx =3, pady =3)
    Button(fenetre,text="L",command=mvt_L).pack(side =LEFT, padx =3, pady =3)
    Button(fenetre,text="R",command=mvt_R).pack(side =LEFT, padx =3, pady =3)
    Button(fenetre,text="Z",command=mvt_Z).pack(side =LEFT, padx =3, pady =3)
    Button(fenetre,text="X",command=mvt_X).pack(side =LEFT, padx =3, pady =3)
    Button(fenetre,text="Y",command=mvt_Y).pack(side =LEFT, padx =3, pady =3)
    Button(fenetre,text="DI",command=mvt_DI).pack(side =RIGHT, padx =3, pady =3)
    Button(fenetre,text="UI",command=mvt_UI).pack(side =RIGHT, padx =3, pady =3)
    Button(fenetre,text="FI",command=mvt_FI).pack(side =RIGHT, padx =3, pady =3)
    Button(fenetre,text="BI",command=mvt_BI).pack(side =RIGHT, padx =3, pady =3)
    Button(fenetre,text="LI",command=mvt_LI).pack(side =RIGHT, padx =3, pady =3)
    Button(fenetre,text="RI",command=mvt_RI).pack(side =RIGHT, padx =3, pady =3)
    Button(fenetre,text="ZI",command=mvt_ZI).pack(side =RIGHT, padx =3, pady =3)
    Button(fenetre,text="XI",command=mvt_XI).pack(side =RIGHT, padx =3, pady =3)
    Button(fenetre,text="YI",command=mvt_YI).pack(side =RIGHT, padx =3, pady =3)


    Button(fenetre,text="melanger",command=melanger).pack(side =LEFT, padx =3, pady =3)
    Button(fenetre,text="Sortir",command=fenetre.destroy).place(x=500,y=500)           #la fenetre
    Button(fenetre,text="P affichage",command=page_accueil).place(x=200,y=500)
    Button(fenetre,text="Test erreur",command=test_erreur).place(x=600,y=500)
    Button(fenetre,text="3D",command=dessin_3D).place(x=650,y=500)
    Button(fenetre,text="init",command=initialisation_rubikcube).place(x=700,y=500)
    Button(fenetre,text="liste inverse",command=creer_liste_inverse).place(x=700,y=350)
    Button(fenetre,text="<<",command=back).place(x=650,y=350)
    Button(fenetre,text="suppr mvt_Y",command=suppr_mvt_y).place(x=550,y=350)
    Button(fenetre,text=">>",command=next).place(x=750,y=350)
    Button(fenetre,text="condition aff",command=condition_afficher).place(x=750,y=500)
    Button(fenetre,text="Resoudre",command=resoudre).place(x=550,y=650)
    Button(fenetre,text="Croix",command=croix).place(x=550,y=600)
    Button(fenetre,text="Croix aligne",command=croix_bien_aligne).place(x=600,y=600)
    Button(fenetre,text="1 C",command=premiere_couronne).place(x=650,y=600)
    Button(fenetre,text="2 C",command=deuxieme_couronne).place(x=675,y=600)
    Button(fenetre,text="Croix inverse",command=croix_inverse).place(x=700,y=600)
    Button(fenetre,text="coin",command=coin_position).place(x=750,y=600)
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


def selection(i):
    "Fonction uttilise dans la fonction pointeur"
    global case2
    a = couleur_prise #On met dans a la couleur selectionne
    case2.itemconfig(i,fill=a) #On change la couleur de la case mais juste dans tkinter
    initialisation_case() #On reinitialise la couleur de chaque case en fonction des items du canvas
    dessin_3D(fenetre,x=width_fenetre-10,y = height_fenetre-100,anchor = SE) #On affiche le dessin 3D

def pointeur(event):
    "Permet de changer de couleur une case"
    for i in range(1,55):#On parcours toutes les cases
            a = case2.coords(i) #On sort les coordonnes
            if a[0] < float(event.x) and float(event.x)<a[2] and a[1] < float(event.y) and float(event.y)<a[3] :
                selection(i)#Si le clic est sur les coordonnes on change la couleur de la case
def initialisation_rubikcube():
    "Affiche la fenetre d'initialisation du rubik's cube"
    global chaine,couleur_prise,case2
    for c in fenetre.winfo_children(): # supp tt les elements de la fenetre
        c.destroy()
    fenetre.wm_geometry("%dx%d+%d+%d" % (width_fenetre,height_fenetre, 0, 0)) #Positionne la fenetre
    fenetre.minsize(width_fenetre,height_fenetre)#taille minimum de la fenetre
    dessin_3D(fenetre,x=width_fenetre-10,y = height_fenetre-100,anchor = SE) #Affiche le rubik's cube en 3D en bas a droite

    case2 = Canvas(fenetre, width=450, height=650, bg='dark grey')
    #defintion de la taille du fond du canvas et de sa couleur
    case2.pack()#permet d'afficher le canvas

    couleur_prise = "blue"
    Button(fenetre,bg="red",command=var_red,width =10,height = 5).place(x=100,y=100)
    Button(fenetre,bg="green",command=var_green,width =10,height = 5).place(x=100,y=200)
    Button(fenetre,bg="orange",command=var_orange,width =10,height = 5).place(x=100,y=300)
    Button(fenetre,bg="yellow",command=var_yellow,width =10,height = 5).place(x=200,y=100)
    Button(fenetre,bg="blue",command=var_blue,width =10,height = 5).place(x=200,y=200)
    Button(fenetre,bg="white",command=var_white,width =10,height = 5).place(x=200,y=300)
    Button(fenetre,text="Resoudre",command=valide_initialisation).place(x=100,y=10)
    afficher_rubik_cube(case2,fenetre) #affiche le rubik's cube en T sur le Canvas
    case2.bind("<Button-1>",pointeur)
def valide_initialisation():
    "Valide l'initialisation"
    test_erreur() #Si il y a pas d'erreur
    resoudre() #On resout le rubik cube

def var_red():
    "Change la variable couleur pour l'initialisation du rubik's cube"
    global couleur_prise
    couleur_prise = "red"
def var_blue():
    "Change la variable couleur pour l'initialisation du rubik's cube"
    global couleur_prise
    couleur_prise = "blue"
def var_white():
    "Change la variable couleur pour l'initialisation du rubik's cube"
    global couleur_prise
    couleur_prise = "white"
def var_orange():
    "Change la variable couleur pour l'initialisation du rubik's cube"
    global couleur_prise
    couleur_prise = "orange"
def var_green():
    "Change la variable couleur pour l'initialisation du rubik's cube"
    global couleur_prise
    couleur_prise = "green"
def var_yellow():
    "Change la variable couleur pour l'initialisation du rubik's cube"
    global couleur_prise
    couleur_prise = "yellow"


def initialisation_case():
    "Initialise les variables des cases en fonction de la couleur des cases dans tkinter"
    global W,J,R,B,V,O
    W = ["W"]
    J = ["J"]
    R = ["R"]
    B = ["B"]
    V = ["V"]
    O = ["O"]
    #creation de la face blanche au centre
    for i in range(1,55):
        b = case2.itemconfig(i,'fill')
        if i < 10:
            R.append(b[4])
        if i >9 and i<19:
            W.append(b[4])
        if i> 18 and i<28:
            O.append(b[4])
        if i>27 and i<37:
            J.append(b[4])
        if i>36 and i<46:
            B.append(b[4])
        if i>45 and i<55:
            V.append(b[4])


def afficher_rubik_cube(case,fenetre):
    "Affiche le rubik cube en T"
    taillecase = 50 #taille d'une case
    var_case = R,W,O,J
    x,y = R1_coord #point de depart R1_coord
    #initialisation
    c = 0
    b = 1
    for i in range(12):         #Boucle qui dure 12 fois
        for a in range(3):      #Boucle qui dure 3 fois
            case.create_rectangle(x,y,x+taillecase,y+taillecase, fill=var_case[c][b] ,width=2) #var_case[c][b] affiche la couleur voulu
            if b == 9:  #Si on a fini une face, on passe
                c = c+1   #a la ligne d'en dessous
                b = 1   #et on reinitialise B
            else:
                b += 1 #Sinon on parcours la liste de la premiere face
            x += taillecase #decalage des coordonnees d'une taille_case sur la droite
        x = R1_coord[0] #Remise a zero des coordonnes pour dessiner la case une ligne en dessous
        y += taillecase#decalage des coordonnees d'une taille_case en dessous
    x,y = B1_coord
    for i in range(3): #Meme chose mais que pour la liste B
        for a in range(3):
            case.create_rectangle(x,y,x+taillecase,y+taillecase, fill=B[b] ,width=2)
            if b == 9:
                b = 1
            else:
                b += 1
            x += taillecase
        x = B1_coord[0]
        y += taillecase
    x,y = V1_coord
    for i in range(3): #Meme chose mais que pour la liste V
        for a in range(3):
            case.create_rectangle(x,y,x+taillecase,y+taillecase, fill=V[b] ,width=2)
            if b == 9:
                b = 1
            else:
                b += 1
            x += taillecase
        x = V1_coord[0]
        y += taillecase



def instruction_texte(texte):
    "Permet d'afficher du texte dans la page de dvlpt"
    texte_save.append(texte)
    affichage_texte()
def affichage_texte():
    "Permet d'afficher du texte dans la page de dvlpt"
    if condition_aff==True:
        y =affichage_texte_y
        a = len(texte_save)-1
        affichage = []
        for i in range(a):
            affichage.append (Label(fenetre, width=100,text=texte_save[a-i]))
            affichage[i].place(x=450,y=y)
            y -= 20

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


def condition_afficher():
    "Permet d'afficher du texte dans la page de dvlpt"
    global condition_aff
    condition_aff = True-condition_aff
    instruction_texte("Condition_aff"+str(condition_aff))
    afficher_rubik_cube(case,fenetre)


def dessin_3D(fenetre,x=800,y=450,taille_carre = 25,anchor= NW,text = "Rubik cube"):
    "Affiche le rubik's en 3D, en fonction de la taille d'une case"
    dessin_3D = Canvas(fenetre, width=10*taille_carre, height=10*taille_carre,bg = liste_couleur_dessin["Rubik"])
    #defintion de la taille du fond du dessin et de sa couleur
    dessin_3D.place(x=x,y=y,anchor = anchor)#permet d'afficher le dessin
    texte = dessin_3D.create_text(taille_carre,10*taille_carre,text=text,anchor = SW) #Creer un texte sous le rubik cube
    #Initialisation
    W1_coord = [3*taille_carre,3*taille_carre]
    var_case = [W,J]
    b = 0
    #Permet de creer la face de devant et la face de derriere
    for a in range(0,2):
        if a == 1:
            W1_coord = [6*taille_carre,taille_carre]
            b = 6
        for i in range(0,3):
            for n in range(0,3):
                b += 1
                dessin_3D.create_rectangle(W1_coord[0],W1_coord[1],W1_coord[0]+taille_carre,W1_coord[1]+taille_carre,fill=var_case[a][b] ,width=2)
                W1_coord[0] +=  taille_carre
            if a ==1:
                b -= 6
            W1_coord[0] -= taille_carre*3
            W1_coord[1] += taille_carre
    #Initialisation
    var_case = [R,O]
    W1_coord = [3*taille_carre,3*taille_carre]
    #Permet de creer la face du haut et la face du bas
    b = 6
    for a in range(0,2):
        if a == 1:
            W1_coord = [3*taille_carre,9*taille_carre]
            b = 0
        for i in range(0,3):
            W1_coord[0] = 3*taille_carre+i*taille_carre*0.5
            for n in range(0,3):
                b += 1
                dessin_3D.create_polygon(W1_coord[0],W1_coord[1],W1_coord[0]+taille_carre*0.5,W1_coord[1]-taille_carre*0.5,W1_coord[0]+1.5*taille_carre,W1_coord[1]-taille_carre*0.5,W1_coord[0]+taille_carre,W1_coord[1],fill=var_case[a][b],width=2,outline='black')
                W1_coord[0] +=  taille_carre
            W1_coord[1] -= taille_carre*0.5
            if a == 0:
                b -= 6
    #Initialisation
    var_case = [V,B]
    W1_coord = [6*taille_carre,3*taille_carre]
    b = 0
    e = 1
    #Permet de creer la face de droite et la face de gauche
    for a in range(0,2):
        if a == 1:
            W1_coord = [taille_carre,3*taille_carre]
            e = -1
            b = 4
        for i in range(0,3):
            W1_coord[1] = i*taille_carre+3*taille_carre
            for n in range(0,3):
                 b += e
                 dessin_3D.create_polygon(W1_coord[0],W1_coord[1],W1_coord[0]+taille_carre*0.5,W1_coord[1]-taille_carre*0.5,W1_coord[0]+taille_carre*0.5,W1_coord[1]+taille_carre*0.5,W1_coord[0],W1_coord[1]+taille_carre,fill=var_case[a][b],width=2,outline='black')
                 W1_coord[0] += taille_carre*0.5
                 W1_coord[1] -= taille_carre*0.5
            if a== 1:
                b += 6
            W1_coord[0] -= 1.5* taille_carre
def fenetre_erreur(arg):
    "Affiche une fenetre d'erreur avec l'erreur en argument"
    fenetre_erreur = Tk()
    text = "Erreur initialisation impossible\n"+str(arg)
    label = Label(fenetre_erreur, text=text)
    label.pack()
    quit = Button(fenetre_erreur, text="Retour", command=fenetre_erreur.destroy)
    quit.pack()
    fenetre_erreur.mainloop()

def test_erreur():
    "Quand il y a plus de 9 cases dela meme couleur, affiche un msg d'erreur"
    a = W,R,J,V,B,O
    green = 0
    yellow = 0
    red = 0
    white = 0
    orange = 0
    blue = 0
    for i in range(len(a)):
        for elt in a[i]:
            if elt =="green":
                green += 1
            if elt =="blue":
                blue += 1
            if elt == "yellow":
                yellow += 1
            if elt == "orange":
                orange += 1
            if elt == "white":
                white += 1
            if elt =="red":
                red += 1
    MSG = green,blue,red,yellow,white,orange,"g b r j w o"
    if green != 9 or blue != 9 or red != 9 or yellow != 9 or white != 9 or orange != 9:
        fenetre_erreur(MSG)
    MSG = green,blue,red,yellow,white,orange,"g b r j w o"
    instruction_texte(MSG)
    test_arete()
    test_coin()
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
