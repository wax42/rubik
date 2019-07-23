
couleur =['white','red','blue','green','orange','yellow']


class Rubik():

    def __init__(self):
        self.W = ["W"]
        
        #creation de la face blanche au centre
        for i in range(9):
            self.W.append(couleur[0])
        self.R = ["R"]
        #creation de la face rouge en haut
        for i in range(9):
            self.R.append(couleur[1])
        self.B = ["B"]
        #creation de la face bleu
        for i in range(9):
            self.B.append(couleur[2])
        self.V = ["V"]
        #creation de la face verte
        for i in range(9):
            self.V.append(couleur[3])
        self.O = ["O"]
        #creation de la face orange sous la face du centre
        for i in range(9):
            self.O.append(couleur[4])
        self.J = ["J"]
        #creation de la face en bas
        for i in range(9):
            self.J.append(couleur[5])


    def mvt_D(self):
        pass


    def mvt_DI(self):
        pass


    def mvt_U(self):
        pass


    def mvt_UI(self):
        pass


    def mvt_F(self):
        pass


    def mvt_FI(self):
        pass

    def mvt_B(self):
        pass

    def mvt_BI(self):
        pass

    def mvt_L(self):
        pass

    def mvt_LI(self):
        pass

    def mvt_R(self):
        pass

    def mvt_RI(self):
        pass

    def mvt_Z(self):
        pass

    def mvt_ZI(self):
        pass

    def mvt_XI(self):
        pass

    def mvt_X(self):
        "rotation vers le haut"
        pass

    def mvt_Y(self):
        "rotation vers la gauche"
        pass

    def mvt_YI(self):
        "rotation vers la droite"
        pass


