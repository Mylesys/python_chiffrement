####################################
        # Construction contenu onglet Polybe
        # Création Boutons
        self.btn_chiffrer_Polybe = Button(self.Polybe, text='Chiffrer', fg="blue", activebackground="blue", width=10,
                                        height=1, padx=10, pady=10)
        self.btn_chiffrer_Polybe.place(relx=0.34, rely=0.4)
        self.btn_dechiffrer_Polybe = Button(self.Polybe, text='Déchiffrer', fg="blue", activebackground="blue", width=10,
                                          height=1, padx=10, pady=10)
        self.btn_dechiffrer_Polybe.place(relx=0.53, rely=0.4)
        #
        ####################################
        ####################################
        # Création des zones de texte

        self.ent_phrase_Polybe = Entry(self.Polybe, width=50)
        self.ent_phrase_Polybe.place(relx=0.25, rely=0.1)
        self.ent_cle_Polybe = Entry(self.Polybe, width=50)
        self.ent_cle_Polybe.place(relx=0.25, rely=0.2)

        # Zone text_entry matrice
        self.ent_matrix_1 = Entry(self.Polybe, width=5)
        self.ent_matrix_1.place(relx=0.45, rely=0.30)
        self.ent_matrix_2 = Entry(self.Polybe, width=5)
        self.ent_matrix_2.place(relx=0.45, rely=0.35)
        self.ent_matrix_3 = Entry(self.Polybe, width=5)
        self.ent_matrix_3.place(relx=0.53, rely=0.30)
        self.ent_matrix_4 = Entry(self.Polybe, width=5)
        self.ent_matrix_4.place(relx=0.53, rely=0.35)

        # Labels zones de texte
        self.lbl_phrase_Polybe = Label(self.Polybe, text="Phrase à coder")
        self.lbl_phrase_Polybe.place(relx=0.05, rely=0.1)
        self.lbl_cle_Polybe = Label(self.Polybe, text="Clé de chiffrement")
        self.lbl_cle_Polybe.place(relx=0.05, rely=0.2)

        # Texte Réponse
        self.txt_phrase_chiffre_Polybe = Text(self.Polybe, width=35, height=5, padx=20, pady=10)
        self.txt_phrase_chiffre_Polybe.place(relx=0.25, rely=0.6)
        #