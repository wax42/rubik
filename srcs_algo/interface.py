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


def web_affichage(liste):
    "Permet d'ouvrir une page internet qui affiche un mvt"
    try:
        arg = " ".join(liste)
    except:
        arg = str(liste)
    webbrowser.open("https://alg.cubing.net/?alg="+arg+"&type=alg&view=fullscreen")

def play():
    "Permet de lire tout seul les mouvements a faire"
    global numero_mvt
    next() #Passe au mouvement suivant
    if numero_mvt <= len(liste_mouvement_final)-1: #Si il reste des mvts a faire
        fenetre.after(int(vitesse),play) #Marquer une pause puis relancer la fonction play
    else: #Sinon ne rien faire
        print("fini") #afin de quitter la boucle


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



# TODO a suppr deguelasse
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


def pointeur(event):
    "Permet de changer de couleur une case"
    for i in range(1,55):#On parcours toutes les cases
            a = case2.coords(i) #On sort les coordonnes
            if a[0] < float(event.x) and float(event.x)<a[2] and a[1] < float(event.y) and float(event.y)<a[3] :
                selection(i)#Si le clic est sur les coordonnes on change la couleur de la case


def selection(i):
    "Fonction uttilise dans la fonction pointeur"
    global case2
    a = couleur_prise #On met dans a la couleur selectionne
    case2.itemconfig(i,fill=a) #On change la couleur de la case mais juste dans tkinter
    initialisation_case() #On reinitialise la couleur de chaque case en fonction des items du canvas
    dessin_3D(fenetre,x=width_fenetre-10,y = height_fenetre-100,anchor = SE) #On affiche le dessin 3D
    case2.bind("<Button-1>",pointeur)

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


