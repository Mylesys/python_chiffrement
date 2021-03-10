from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter import filedialog
from tkinter import *
from ttkthemes import ThemedTk


class appli(Tk):

    def __init__(self):
        #         self.appli = Tk()
        self.appli = ThemedTk(theme="black")  # Thème black parce que c'est mieux
        self.appli.title("Méthodes de chiffrement")
        self.tabControl = ttk.Notebook(self.appli)

        self.initUI()

    def initUI(self):
        # Les frame onglets
        self.Introduction = ttk.Frame(self.tabControl)
        self.Polybe = ttk.Frame(self.tabControl)
        self.César = ttk.Frame(self.tabControl)
        self.Hill = ttk.Frame(self.tabControl)
        self.PlayFair = ttk.Frame(self.tabControl)
        self.Vigenère = ttk.Frame(self.tabControl)
        self.Homophone = ttk.Frame(self.tabControl)
        self.Atbash = ttk.Frame(self.tabControl)

        self.tabControl.add(self.Introduction, text='Introduction')
        self.tabControl.add(self.Polybe, text='Carré de Polybe')
        self.tabControl.add(self.Atbash, text='Atbash')
        self.tabControl.add(self.César, text='César')
        self.tabControl.add(self.Homophone, text='Homophone')
        self.tabControl.add(self.Hill, text='Hill')
        self.tabControl.add(self.PlayFair, text='PlayFair')
        self.tabControl.add(self.Vigenère, text='Vigenère')



        self.tabControl.pack(expand=1, fill="both")

        ###############
        # Onglets
        ###############
        # Onglet César
        ttk.Label(self.César, text="Chiffre de César")
        # Onglet Polybe
        ttk.Label(self.Polybe, text="Carré de Polybe")
        # Onglet Hill
        ttk.Label(self.Hill, text="Hill")
        # Onglet PlayFair
        ttk.Label(self.PlayFair, text="Méthode de PlayFair")
        # Onglet Vigenère
        ttk.Label(self.Vigenère, text="Chiffre de Vigenère")
        # Onglet Homophone avec carré de polybe
        ttk.Label(self.Homophone, text="Chiffrement Homophone avec carré de polybe")
        # Onglet Atbash
        ttk.Label(self.Atbash, text="Chiffre de Vigenère")


        # Onglet principal
        ttk.Label(self.Introduction, text="")

        ####################################
        # Onglet Introduction
        self.txt_intro = ttk.Label(self.Introduction,
                                   text="Cette application vous offre la possibilité de chiffrer et déchiffrer des messages \n avec différentes méthodes telles que :\n \n le chiffre de César, Hill, PlayFair, Vigenère, etc ... Bon amusement !!! \n Pour accéder aux différentes méthodes de chiffrement je vous invite à \n visiter les différents onglets disponibles ! \n Bon amusement ! \n Les imports obligatoires sont : - tkinter \n - ttk \n - Themedttk \n Leur installation préalable doit être effectuée sur votre IDE ! \n Merci et bon amusement !",
                                   #             foreground="#86d1f7",  # Set the text color
                                   #             background="#17008a"  # Set the background color
                                   )
        self.txt_intro.place(relx=0.2, rely=0.3)



        ####################################
        # Construction contenu onglet Polybe
        # Création Boutons
        self.btn_chiffrer_Polybe = Button(self.Polybe, text='Chiffrer', fg="blue", activebackground="blue", width=10,
                                          height=1, padx=10, pady=10, command=lambda: self.chiffrer_Polybe(self.ent_phrase_ Polybe.get(),
                                                                             self.ent_cle_Polybe.get()))
        self.btn_chiffrer_Polybe.place(relx=0.34, rely=0.3)
        self.btn_dechiffrer_Polybe = Button(self.Polybe, text='Déchiffrer', fg="blue", activebackground="blue",
                                            width=10,height=1, padx=10, pady=10, command=lambda: self.dechiffrer_Polybe(self.ent_phrase_Polybe.get(),
                                                                             self.ent_cle_Polybe.get()))
        self.btn_dechiffrer_Polybe.place(relx=0.53, rely=0.3)
        #
        ####################################
        ####################################
        # Création des zones de texte

        self.ent_phrase_Polybe = Entry(self.Polybe, width=50)
        self.ent_phrase_Polybe.place(relx=0.25, rely=0.1)
        self.ent_cle_Polybe = Entry(self.Polybe, width=50)
        self.ent_cle_Polybe.place(relx=0.25, rely=0.2)

        # Zone text_entry matrice
        self.txt_tab_polybe = Text(self.Polybe, width=35, height=5, padx=20, pady=10)
        self.txt_tab_polybe.place(relx=0.25, rely=0.4)

        # Labels zones de texte
        self.lbl_phrase_Polybe = Label(self.Polybe, text="Phrase à coder : ")
        self.lbl_phrase_Polybe.place(relx=0.05, rely=0.1)
        self.lbl_cle_Polybe = Label(self.Polybe, text="Clé de chiffrement : ")
        self.lbl_cle_Polybe.place(relx=0.05, rely=0.2)
        self.lbl_resultat = Label(self.Polybe, text="Résultat : ")
        self.lbl_resultat.place(relx=0.05, rely=0.6)
        self.lbl_tab_polybe = Label(self.Polybe, text="Affichage du carré : ")
        self.lbl_tab_polybe.place(relx= 0.05, rely = 0.4)

        # Texte Réponse
        self.txt_phrase_chiffre_Polybe = Text(self.Polybe, width=35, height=5, padx=20, pady=10)
        self.txt_phrase_chiffre_Polybe.place(relx=0.25, rely=0.6)
        #
        ####################################
        # Construction contenu onglet César

        ####################################
        # Création des zones de texte

        self.phrase_cesar_input = StringVar()
        self.cle_cesar_input = StringVar()

        self.ent_phrase_cesar = Entry(self.César, textvariable=self.phrase_cesar_input, width=50)
        self.ent_phrase_cesar.place(relx=0.25, rely=0.1)
        self.ent_cle_cesar = Entry(self.César, textvariable=self.cle_cesar_input, width=50)
        self.ent_cle_cesar.place(relx=0.25, rely=0.2)

        # Création Boutons
        self.btn_chiffrer_cesar = Button(self.César, text='Chiffrer', fg="blue",
                                         activebackground="blue", width=10, height=1, padx=10, pady=10,
                                         command=lambda: self.chiffrer_cesar(self.ent_phrase_cesar.get(),
                                                                             self.ent_cle_cesar.get()))
        self.btn_chiffrer_cesar.place(relx=0.34, rely=0.4)
        self.btn_dechiffrer_cesar = Button(self.César, text='Déchiffrer', fg="blue",
                                           activebackground="blue", width=10, height=1, padx=10, pady=10,
                                           command=lambda: self.dechiffrer_cesar(self.ent_phrase_cesar.get(),
                                                                                 self.ent_cle_cesar.get()))
        self.btn_dechiffrer_cesar.place(relx=0.53, rely=0.4)

        # def on_click(event):
        #     phrase_cesar = ent_phrase_cesar.get()
        #     cle_cesar= int(ent_cle_cesar.get())
        #     chiffrer_cesar(phrase_cesar, cle_cesar)

        # btn_chiffrer_cesar.bind("<Button-1>", on_click)

        #
        ####################################
        # Labels zones de texte
        self.lbl_phrase_cesar = Label(self.César, text="Phrase à coder")
        self.lbl_phrase_cesar.place(relx=0.05, rely=0.1)
        self.lbl_cle_cesar = Label(self.César, text="Clé de chiffrement")
        self.lbl_cle_cesar.place(relx=0.05, rely=0.2)

        # Texte Réponse
        self.txt_phrase_chiffre_cesar = Text(self.César, width=38, height=5)
        self.txt_phrase_chiffre_cesar.place(relx=0.25, rely=0.6)

        ####################################
        # Construction contenu onglet Hill
        # Création Boutons
        self.btn_chiffrer_Hill = Button(self.Hill, text='Chiffrer', fg="blue", activebackground="blue", width=10,
                                        height=1, padx=10, pady=10)
        self.btn_chiffrer_Hill.place(relx=0.34, rely=0.4)
        self.btn_dechiffrer_Hill = Button(self.Hill, text='Déchiffrer', fg="blue", activebackground="blue", width=10,
                                          height=1, padx=10, pady=10)
        self.btn_dechiffrer_Hill.place(relx=0.53, rely=0.4)
        #
        ####################################
        ####################################
        # Création des zones de texte

        self.ent_phrase_Hill = Entry(self.Hill, width=50)
        self.ent_phrase_Hill.place(relx=0.25, rely=0.1)
        self.ent_cle_Hill = Entry(self.Hill, width=50)
        self.ent_cle_Hill.place(relx=0.25, rely=0.2)

        # Zone text_entry matrice
        self.ent_matrix_1 = Entry(self.Hill, width=5)
        self.ent_matrix_1.place(relx=0.45, rely=0.30)
        self.ent_matrix_2 = Entry(self.Hill, width=5)
        self.ent_matrix_2.place(relx=0.45, rely=0.35)
        self.ent_matrix_3 = Entry(self.Hill, width=5)
        self.ent_matrix_3.place(relx=0.53, rely=0.30)
        self.ent_matrix_4 = Entry(self.Hill, width=5)
        self.ent_matrix_4.place(relx=0.53, rely=0.35)

        # Labels zones de texte
        self.lbl_phrase_Hill = Label(self.Hill, text="Phrase à coder")
        self.lbl_phrase_Hill.place(relx=0.05, rely=0.1)
        self.lbl_cle_Hill = Label(self.Hill, text="Clé de chiffrement")
        self.lbl_cle_Hill.place(relx=0.05, rely=0.2)

        # Texte Réponse
        self.txt_phrase_chiffre_Hill = Text(self.Hill, width=35, height=5, padx=20, pady=10)
        self.txt_phrase_chiffre_Hill.place(relx=0.25, rely=0.6)


        ####################################
        # Construction contenu onglet PlayFair
        ####################################
        #
        ####################################
        # Création des zones de texte

        self.phrase_PlayFair_input = StringVar()
        self.cle_PlayFair_input = StringVar()

        self.ent_phrase_PlayFair = Entry(self.PlayFair, textvariable=self.phrase_PlayFair_input, width=50)
        self.ent_phrase_PlayFair.place(relx=0.25, rely=0.1)
        self.ent_cle_PlayFair = Entry(self.PlayFair, textvariable=self.cle_PlayFair_input, width=50)
        self.ent_cle_PlayFair.place(relx=0.25, rely=0.2)

        # Création Boutons
        self.btn_chiffrer_PlayFair = Button(self.PlayFair, text='Chiffrer', fg="blue",
                                         activebackground="blue", width=10, height=1, padx=10, pady=10,
                                         command=lambda: self.chiffrer_PlayFair(self.ent_phrase_PlayFair.get(),
                                                                             self.ent_cle_PlayFair.get()))
        self.btn_chiffrer_PlayFair.place(relx=0.34, rely=0.6)
        self.btn_dechiffrer_PlayFair = Button(self.PlayFair, text='Déchiffrer', fg="blue",
                                           activebackground="blue", width=10, height=1, padx=10, pady=10,
                                           command=lambda: self.dechiffrer_PlayFair(self.ent_phrase_PlayFair.get(),
                                                                                 self.ent_cle_PlayFair.get()))
        self.btn_dechiffrer_PlayFair.place(relx=0.53, rely=0.6 )

        ####################################
        # Labels zones de texte
        self.lbl_phrase_PlayFair = Label(self.PlayFair, text="Phrase à coder")
        self.lbl_phrase_PlayFair.place(relx=0.05, rely=0.1)
        self.lbl_cle_PlayFair = Label(self.PlayFair, text="Clé de chiffrement")
        self.lbl_cle_PlayFair.place(relx=0.05, rely=0.2)



        # Texte Réponse
        self.txt_phrase_chiffre_PlayFair = Text(self.PlayFair, width=38, height=5)
        self.txt_phrase_chiffre_PlayFair.place(relx=0.25, rely=0.7)


        ####################################
        # Application principale
        ####################################
        self.appli.geometry("600x600+10+10")
        self.appli.resizable(0, 0)
        self.appli.mainloop()



########################################################################################################################
    ############################################
    # Définitions des fonctions de chiffrement #
    ###################################
    # Chiffrement de César

    def chiffrer_cesar(self, phrase_cesar, cle_cesar):
        print("Phrase = ", phrase_cesar)
        print("Cle = ", cle_cesar)
        cle_cesar = int(cle_cesar)
        txt_achiffrer_cesar = phrase_cesar.upper()
        lg = len(txt_achiffrer_cesar)
        txt_msg_chiffre_cesar = ""

        for i in range(lg):
            if (ord(txt_achiffrer_cesar[i]) > 90 or ord(txt_achiffrer_cesar[i]) < 65):
                txt_msg_chiffre_cesar += txt_achiffrer_cesar[i]
            else:
                asc = ord(txt_achiffrer_cesar[i]) + cle_cesar
                txt_msg_chiffre_cesar += chr(asc + 26 * ((asc < 65) - (asc > 90)))

        print("Message codé      :", txt_msg_chiffre_cesar)
        self.txt_phrase_chiffre_cesar.delete(1.0, "end") #Efface l'ancien résulat de chiffrement/déchiffrement
        self.txt_phrase_chiffre_cesar.insert(1.0, txt_msg_chiffre_cesar) #Ecriture du résultat  de chiffrement/déchiffrement dans la zone de texte

    #
    ####################################

    def dechiffrer_cesar(self, phrase_cesar, cle_cesar):
        # cle=22 # Décalage par rapport à Y (code ASCII : 22 + 1 = 23e lettre de l'alphabet)
        # cle_cesar = int(input("Quelle est la clé pour le déchiffrement?")) #Code pour lancement console

        # phrase_cesar = str(input("Quelle est le message à déchiffrer ?"))
        print("Phrase = ", phrase_cesar)
        print("Cle = ", cle_cesar)
        cle_cesar = int(cle_cesar)
        txt_achiffrer_cesar = phrase_cesar.upper()
        lg = len(txt_achiffrer_cesar)
        MessageClair = ""

        for i in range(lg):
            if ((ord(txt_achiffrer_cesar[i]) > 90 or ord(txt_achiffrer_cesar[i]) < 65)):
                MessageClair += txt_achiffrer_cesar[i]
            else:
                asc = ord(txt_achiffrer_cesar[i]) - cle_cesar
                MessageClair += chr(asc + 26 * ((asc < 65) - (asc > 90)))

        print("Message décodé : ", MessageClair)
        self.txt_phrase_chiffre_cesar.delete(1.0, "end")
        self.txt_phrase_chiffre_cesar.insert(1.0, MessageClair)
    #
    ####################################


appli()

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    appli()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
