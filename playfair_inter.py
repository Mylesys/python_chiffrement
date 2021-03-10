####################################
        # Création des zones de texte

        self.phrase_cesar_input = StringVar()
        self.cle_cesar_input = StringVar()

        self.ent_phrase_PlayFair = Entry(self.PlayFair, textvariable=self.phrase_cesar_input, width=50)
        self.ent_phrase_PlayFair.place(relx=0.25, rely=0.1)
        self.ent_cle_PlayFair = Entry(self.PlayFair, textvariable=self.cle_cesar_input, width=50)
        self.ent_cle_PlayFair.place(relx=0.25, rely=0.2)

        # Création Boutons
        self.btn_chiffrer_cesar = Button(self.PlayFair, text='Chiffrer', fg="blue",
                                         activebackground="blue", width=10, height=1, padx=10, pady=10,
                                         command=lambda: self.chiffrer_cesar(self.ent_phrase_cesar.get(),
                                                                             self.ent_cle_cesar.get()))
        self.btn_chiffrer_cesar.place(relx=0.29, rely=0.4)
        self.btn_dechiffrer_cesar = Button(self.PlayFair, text='Déchiffrer', fg="blue",
                                           activebackground="blue", width=10, height=1, padx=10, pady=10,
                                           command=lambda: self.dechiffrer_cesar(self.ent_phrase_cesar.get(),
                                                                                 self.ent_cle_cesar.get()))
        self.btn_dechiffrer_cesar.place(relx=0.48, rely=0.4)


        ####################################
        # Labels zones de texte
        self.lbl_phrase_cesar = Label(self.PlayFair, text="Phrase à coder")
        self.lbl_phrase_cesar.place(relx=0.05, rely=0.1)
        self.lbl_cle_cesar = Label(self.PlayFair, text="Clé de chiffrement")
        self.lbl_cle_cesar.place(relx=0.05, rely=0.2)

        # Texte Réponse
        self.txt_phrase_chiffre_cesar = Text(self.PlayFair, width=50, height=5)
        self.txt_phrase_chiffre_cesar.place(relx=0.25, rely=0.4)

# Zone text_entry matrice
self.ent_matrix_1 = Entry(self.PlayFair, width=5)
self.ent_matrix_1.place(relx=0.4, rely=0.30)
self.ent_matrix_2 = Entry(self.PlayFair, width=5)
self.ent_matrix_2.place(relx=0.4, rely=0.35)
self.ent_matrix_3 = Entry(self.PlayFair, width=5)
self.ent_matrix_3.place(relx=0.4, rely=0.40)
self.ent_matrix_4 = Entry(self.PlayFair, width=5)
self.ent_matrix_4.place(relx=0.4, rely=0.45)
self.ent_matrix_5 = Entry(self.PlayFair, width=5)
self.ent_matrix_5.place(relx=0.4, rely=0.50)

self.ent_matrix_6 = Entry(self.PlayFair, width=5)
self.ent_matrix_6.place(relx=0.48, rely=0.30)
self.ent_matrix_7 = Entry(self.PlayFair, width=5)
self.ent_matrix_7.place(relx=0.48, rely=0.35)
self.ent_matrix_8 = Entry(self.PlayFair, width=5)
self.ent_matrix_8.place(relx=0.48, rely=0.40)
self.ent_matrix_9 = Entry(self.PlayFair, width=5)
self.ent_matrix_9.place(relx=0.48, rely=0.45)
self.ent_matrix_10 = Entry(self.PlayFair, width=5)
self.ent_matrix_10.place(relx=0.48, rely=0.50)

        ####################################
        #Application principale
        ####################################
        self.appli.geometry("600x600+10+10")
        self.appli.resizable(0, 0)
        self.appli.mainloop()