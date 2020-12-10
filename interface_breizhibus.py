import tkinter as tk
from tkinter import PhotoImage
from tkinter import filedialog
from connexion import Connexion
from tkinter import ttk

colors = {
    'orange':'#f9690c',
    'noir':'#030100',
    'blanc' :'#f9f5f5'
}

class Interface:
    def __init__(self, master):
        self.master = master
        self.master.title("Breizhibus")
        self.master.geometry('1200x600')
        self.master.minsize(1200, 600)
        self.master.configure(bg=colors['noir'])

        #logo
        logo = PhotoImage(file="C:/Users/utilisateur/Documents/GitHub/breizhibus/Images/logo.png")
        logo_f = tk.Label( image = logo)
        logo_f.pack(pady=10, padx=10, side='top', fill=tk.BOTH)

        # titre
        titre = tk.Label(self.master, text='Bienvenue chez Breizhibus, les bus qui vous mènent loin !', 
                        font=("Helvetica", 20), bg=colors['orange'] , fg=colors['noir'])
        titre.pack(fill='x', side='top')


        #frame boutons
        self.frame_boutons = tk.Frame(self.master, bg=colors['noir'])
        self.frame_boutons.pack(pady=25)

        #frame menu
        self.frame_menu = tk.Frame(self.master, bg=colors['noir'])
        self.frame_menu.pack()

        #fonction d'ajout de bouton
        fonctions = {'Afficher les lignes de bus': self.afficher_lignes,
                    "Voir les arrêts d'une ligne": self.afficher_arrets}

        for i, (key, value) in enumerate(fonctions.items()):
            ligne = tk.Button(self.frame_boutons, height=2, width=22, bg=colors['orange'], bd=0, font=(
                'Helvetica', '12'), text=key, command=value)
            ligne.grid(row=0, column=i, padx=5, ipadx=12)


        #bouton afficher lignes
    def afficher_lignes(self):
        for widget in self.frame_menu.winfo_children():
            widget.pack_forget()

        lignes_frame = tk.Frame(self.frame_menu, bg=colors['orange'])
        lignes_frame.pack()

        lignes= Connexion.lister_lignes()  

        lignes_label = tk.Label(lignes_frame, text="Lignes :", bg=colors['orange'], font=(
            'Helvetica', '20', 'underline'))
        lignes_label.grid(row=0, column=1, padx=50)

        for i, value in enumerate(lignes, 1):
            label = tk.Label(lignes_frame, text=value,
                            bg=colors['orange'], font=('Helvetica', '12'))
            label.grid(row=i, column=1)
     

    def afficher(self, ligne):      #affiche les arrets par lignes
        for widget in self.frame_menu.winfo_children():
            widget.pack_forget()

        arrets_frame = tk.Frame(self.frame_menu, bg=colors['orange'])
        arrets_frame.pack()
        arrets= Connexion.lister_arrets(self.ligne_liste.get()) 

        arrets_label = tk.Label(arrets_frame, text=("Arrêts de la ligne : " + str(self.ligne_liste.get())), bg=colors['orange'], font=(
            'Helvetica', '20', 'underline'))
        arrets_label.grid(row=0, column=1, padx=50)

        for i, value in enumerate(arrets, 1):
            label = tk.Label(arrets_frame, text=value,
                            bg=colors['orange'], font=('Helvetica', '12'))
            label.grid(row=i, column=1)

    def afficher_arrets(self):          #affiche le bouton de choix de ligne
        for widget in self.frame_menu.winfo_children():
            widget.pack_forget()

        arrets_frame = tk.Frame(self.frame_menu, bg=colors['orange'])
        arrets_frame.pack()

        #liste lignes
        self.ligne_liste = ttk.Combobox(arrets_frame, width=20, values=list(Connexion.lister_lignes()), state="readonly")
        self.ligne_liste.set('Chosir une ligne')
        self.ligne_liste.bind('<<ComboboxSelected>>', self.afficher)
        self.ligne_liste.grid(row=1, column=1, padx=10, pady=15)

###un formulaire qui permet d'ajouter des bus en base et de les assigner à une ligne (un bus ne peut avoir qu'une seule ligne,
#  mais une ligne peut avoir plusieurs bus). Il faut aussi pouvoir les modifier et les supprimer;
#  Enfin, lorsque vous affichez les arrêts par ligne, affichez aussi les bus par ligne.
