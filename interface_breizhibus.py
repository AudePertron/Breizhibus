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

        self.logo_bus = PhotoImage(file="C:/Users/utilisateur/Documents/GitHub/Breizhibus/Images/logo1.png")
        self.logo_f = tk.Label( self.master, image = self.logo_bus, bg=colors['noir'])
        self.logo_f.pack()

        # titre
        self.titre = tk.Label(self.master, text='Bienvenue chez Breizhibus, les bus qui vous mènent loin !', 
                        font=("Helvetica", 20), bg=colors['orange'] , fg=colors['noir'])
        self.titre.pack(fill='x', side='top')


        #frame boutons
        self.frame_boutons = tk.Frame(self.master, bg=colors['noir'])
        self.frame_boutons.pack(pady=25)

        #frame menu
        self.frame_menu = tk.Frame(self.master, bg=colors['noir'])
        self.frame_menu.pack()

        #fonction d'ajout de bouton
        fonctions = {'Afficher les lignes de bus': self.afficher_lignes,
                    "Voir les arrêts d'une ligne": self.afficher_arrets,
                    "Ajouter un nouveau bus" : self.saisir_bus}

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
            'Helvetica', '12', 'underline'))
        arrets_label.grid(row=0, column=1, padx=50)

        for i, value in enumerate(arrets, 1):
            label = tk.Label(arrets_frame, text=value,
                            bg=colors['orange'], font=('Helvetica', '12'))
            label.grid(row=i, column=1)
#  Enfin, lorsque vous affichez les arrêts par ligne, affichez aussi les bus par ligne.

        bus_label = tk.Label(arrets_frame, text=("Bus roulant sur cette ligne : " ), bg=colors['orange'], font=(
            'Helvetica', '12', 'underline'))
        bus_label.grid(row=0, column=2, padx=50)

        bus = Connexion.lister_bus(self.ligne_liste.get())
        for i, value in enumerate(bus, 1):
            label = tk.Label(arrets_frame, text=value,
                            bg=colors['orange'], font=('Helvetica', '12'))
            label.grid(row=i, column=2)


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

#un formulaire qui permet d'ajouter des bus en base et de les assigner à une ligne (un bus ne peut avoir qu'une seule ligne,
#  mais une ligne peut avoir plusieurs bus). Il faut aussi pouvoir les modifier et les supprimer;

    def saisir_bus(self):
        for widget in self.frame_menu.winfo_children():
            widget.pack_forget()

        display_frame = tk.Frame(self.frame_menu, bg=colors['orange'])
        display_frame.pack()

        def inserer():
            Connexion.ajouter_bus(ligne_liste.get(), entree_immat.get(), entree_places.get(), entree_numero.get() )# remplacer par leurs .get respectifs
            self.saisir_bus()

        for i, text in enumerate(['Ligne', 'Immatriculation', 'Places', 'Numero']):
            label = tk.Label(display_frame, text=text,  bg=colors['orange'], font=(
                'Helvetica', '12', 'underline'))
            label.grid(row=0, column=i)


        ligne_liste = ttk.Combobox(display_frame, width=20, values=list(
            Connexion.nom_lignes()), state="readonly")
        ligne_liste.set('Chosir une ligne')
        ligne_liste.grid(row=1, column=0, padx=10, pady=15)

        entree_immat = tk.Entry(
            display_frame, bg='white', width=20, justify='center', font=('', '9'))
        entree_immat.grid(row=1, column=1, padx=10, pady=15)

        entree_places = tk.Entry(display_frame, bg='white',
                                width=20, justify='center', font=('', '9'))
        entree_places.grid(row=1, column=2, padx=10, pady=15)

        entree_numero = tk.Entry(display_frame, bg='white',
                                width=20, justify='center', font=('', '9'))
        entree_numero.grid(row=1, column=3, padx=10, pady=15)

        bt_valider = tk.Button(display_frame, height=2, width=13, bg=colors['noir'], fg=colors['blanc'], bd=0, font=(
            'Helvetica', '11'), text="Valider", command=inserer)
        bt_valider.grid(row=2, columnspan=5, padx=20, pady=10)

