# -*- coding: utf-8 -*-
"""
Created on Sat Feb  4 14:25:58 2023

@author: sagou
"""
import os
import os.path
from os import chdir, mkdir


from .print_sagou import print_error, print_success, print_info
class C_Dossier():

   
    def __init__(self,sep=""):
       self.separateur=sep
    
    def dossier_courant(self):
        return os.getcwd()

    def existe_dossier(self,Chemin):
        if os.path.exists(Chemin) :
            return True
        else:
            return False 
        
    def changer_dossier(self,Chemin):
        if C_Dossier.existe_dossier(Chemin):
            return(chdir(Chemin))
 
        
    def creer_dossier(self,Chemin):
        if not C_Dossier.existe_dossier(Chemin):
             return(mkdir(Chemin))
         
            
import os.path
from .Module_Classe_Liste import C_Liste
            

class C_File():
    #____________________________________________________________________________________________________________________________________________________________
    # Le constructeur d'une instance d'un fichier
    # Ce constructeur permet d'attribuer à une instance de fichier son nom (vide par défaut) 
    # Ce constructeur permet de spécifier le séparateur des éléments s'il existe (également vide par défauté)su
    # Un séparateur peut être un ";", une "," un "#', etc.  
    def __init__(self,file_name="",sep=";", sep2="+"):
        self.nomFichier=file_name
        self.separateur=sep
        self.separateur2=sep2
    
    #____________________________________________________________________________________________________________________________________________________________
    # Vérifie si un fichier exite ou non.
    def existe_fichier(self):
         if os.path.isfile(self.nomFichier):
             return True
         else:
             return False
    #____________________________________________________________________________________________________________________________________________________________
    # Vérifie si un fichier exite ou non.
    def specifier_Nom_fichier(self):
        while True:
            print("\n")
            print("Instanciation et saisie d'un nouveau fichier de travail :\n")
            self.nomFichier=input("Entrez le chemin de votre fichier : "+"\n")
            if self.existe_fichier():
                print("le fichier spécifié existe déjà dans le répertoire courant, veuillez recommencer")
            else:
                break  
    #____________________________________________________________________________________________________________________________________________________________
    # Créer un fichier vide sans supprimer le fichier de même nom s'il existe
    def create_file(self):
        f = open(self.nomFichier,"x") #Création d'un fichier vide. Ici, le fichier n'est pas écrasé contrairement au mode 'w'  
        f.close()
    
    #____________________________________________________________________________________________________________________________________________________________
    # Créer un fichier vide avec suppression du fichier de même nom s'il existe
    def create_file_2(self):
        f = open(self.nomFichier,"w") #Création d'un fichier vide. Ici, le fichier existant qui porte le même nom est écrasé contrairement mode 'x'  
        f.close()
    
    #____________________________________________________________________________________________________________________________________________________________
    # Créer un fichier vide avec possibilité de dialogue avant de supprimer un fichier de même nom s'il existe dans le même répertoire (dossier)
    def creer_fichier_3(self):
        if os.path.exists(self.nomFichier):         # Condition pour vérifier si jamais le fichier à créer existe déjà dans le répertoire courant
            print("Il existe un fichier qui porte le même nom"+"\n")
            print("Voulez-vous l'écraser ?")
            while True:                             # Itération (boucle infinie) pour prévenir les événetuelles erreurs de frappe (autre chose que '1' et '2') (Attention, il faut absolument provoquer quelque part dans la boucle une rupture avec "break" )
                # Menu local pour exposer les dexu cas de figures (on peut également créer une instance de la classe Menu ici)
                print("Veuillez choisir ce qu'il faut faire, selon les options suivantes : "+"\n")
                print("1. Ecraser le fichier existant")
                print("2. Garder le fichier")
                rep=input("Veuillez taper 1 ou 2 ")
                if rep=='1':                        # Cas où l'utilisateur choisit d'écraser le fichier existant 
                    self.creer_fichier_2()          # Appel à laméthode creer_fichier_2()
                    break                           # rupture de la boucle d'itération => on sort de la boucle infinie while
                elif rep=='2':                      # Cas où l'utilisateur choisit de ne pas écraser le fichier existant (pas besoin dans ce cas de faire appel à la méthode creer_fichier_1()) 
                    break                           # rupture de la boucle d'itération => on sort de la boucle infinie while
                else:                               # cas où l'utilisateur n'a tapé ni "1", ni"2"
                    print("Erreur de frappe"+"\n")
        else:                                       # cas où le fichier à créer n'existe pas dans le répertoire courant
            self.creer_fichier_1()                  # Appel à laméthode creer_fichier_1()
    
    #____________________________________________________________________________________________________________________________________________________________
    def ActiverFichier(self,Message):
        print(Message)
        self.specifier_Nom_fichier()
        self.creer_fichier_3()                      
 
    #____________________________________________________________________________________________________________________________________________________________
    # Supprimer un fichier
    def supprimer_fichier(self):
        if os.path.exists(self.nomFichier):         # Condition pour vérifier si jamais le fichier à créer existe déjà dans le répertoire courant
            os.remove(self.nomFichier)
            print("Le fichier a été supprimé")
        else:
            print("Le fichier spécifié n'existe pas dans le répertoire courant")

    #____________________________________________________________________________________________________________________________________________________________
    # Ajouter un élément
    def enregistrer_Element(self,Element):
        with open(self.nomFichier,'a') as F:   # Ouverture du fichier en mode lecture.
             F.write(Element)

    #____________________________________________________________________________________________________________________________________________________________
    # Ajouter un ensemble d'éléments sous forme de liste
    def Liste_to_Fichier(self,Liste): # 'creer_Fichier_Avec_Liste_Elements(self,ListeElements)' Créer d'un fichier à partir d'une liste : chaque élément de la liste représente une ligne du fichier
        with open(self.nomFichier,'w') as F:   # Ouverture du fichier en mode écriture : à ce niveau si le fichier existe il va être écrasé
            F.writelines(Liste)
    def Liste_stript(self, L):
        for i in range(len(L)):
            L[i] = L[i].strip()
        return L

    def str_to_fichier(self,string):
        with open(self.nomFichier,'a') as F:   # Ouverture du fichier en mode écriture : à ce niveau si le fichier existe il va être écrasé
             F.write(string)
             F.write("\n")
        return
    def str_to_fichier2(self,string):
        with open(self.nomFichier,'w') as F:
             F.write(string)
             F.write("\n")
        return

    def dict_to_file(self, D):
        if type(D) == dict and D != {}:
            with open(self.nomFichier, 'w') as F:
                for c, v in D.items():
                    F.write(str(c) + ";" + str(v))
                    F.write("\n")
            return True
        else:
            print_error("WE HAD A PROBLEM WHILE SAVING YOUR DICT", console=self.console)
             
    def Liste_to_str_to_Fichier(self,Liste_1): 
       Liste = self.Liste_to_Str1(Liste_1)
       with open(self.nomFichier,'a') as F:   # Ouverture du fichier en mode écriture : à ce niveau si le fichier existe il va être écrasé
            
            F.writelines(Liste)   
            F.writelines('\n')
    #____________________________________________________________________________________________________________________________________________________________
    # Lire le contenu d'un fichier et le retourne en le plaçant dans une liste
    def fichier_to_Liste(self):  # extration d'une liste depuis un fichier  : chaque ligne du fichier représente un élément de cette liste
            with open(self.nomFichier, 'r') as f:    # Ouverture du fichier en mode lecture.
                return f.readlines()
    def Fichier_to_str(self):
        with open (self.nomFichier,'r') as f:
            return f.read()

    def supprimer_element(self,element):
        ch = self.Fichier_to_str()
        print(ch)
        chh = ch.replace(element,'')
        print(chh)
        self.str_to_fichier(ch)
        
    #____________________________________________________________________________________________________________________________________________________________
    # Afficher un fichier ligne par ligne
    def afficher_lignes_fichier(self):
        print("\n Affichage des lignes du fichier \n")
        with open(self.nomFichier, 'r') as F:
            for ligne in F:
                print (ligne)               
        print("\n Fin affichage des lignes du fichier")

    #____________________________________________________________________________________________________________________________________________________________
    # Afficher un fichier ligne par ligne et pour chaque ligne mot par mot
    def afficher_mots_fichier(self):
        i=0 # uttiliser comme un simple compteur pour afficher dans un message afin de le rendre plus explicite
        with open(self.nomFichier, 'r') as F:
            for ligne in F:
               i+=1
               print("Affichage des éléments du contenu la ligne : ",i,"\n") # message explicite
               L=C_Liste(ligne.split(self.separateur)) # Création d'une instance de la classe 'C_Liste'
               L.afficher_Liste()  # ici on fait appel à la méthode 'afficher_Liste()' de la classe 'C_Liste'


    def existe_element_fichier(self,Element):
        Liste_Lignes_du_Fichier=self.Fichier_to_Liste() # extraire_liste(nomFichier)
        if Liste_Lignes_du_Fichier!=[]:
            for i in range(len(Liste_Lignes_du_Fichier)):
                if Element in Liste_Lignes_du_Fichier[i]:
                    return(True)
        return(False)
                 
    
    def existe_element_fichier2(self,element):
        Liste_Lignes_du_Fichier=self.Fichier_to_Liste() # extraire_liste(nomFichier)
        if Liste_Lignes_du_Fichier!=[]:
            for i in range(len(Liste_Lignes_du_Fichier)):
                L=Liste_Lignes_du_Fichier[i].split(self.separateur)
                if element in L:
                    return(True)
        return(False)
    
    
    def existe_element_fichier3(self,element):
        Liste_Lignes_du_Fichier=self.Fichier_to_Liste() # extraire_liste(nomFichier)
        if Liste_Lignes_du_Fichier!=[]:
            for i in range(len(Liste_Lignes_du_Fichier)):
                L=Liste_Lignes_du_Fichier[i].split(self.separateur)
                if element in L:
                    return(True, Liste_Lignes_du_Fichier[i])
        return(False,False)

    
    
    def modifier_element_fichier(self,Element):
        Nouvelle_Liste=[] # on commence par créer une nouvelle liste, inialisée à vide. Cette liste va nous servir à sauvegarder un 
        Liste_Lignes_du_Fichier=self.Fichier_to_Liste() # extraire_liste(nomFichier)
        if Liste_Lignes_du_Fichier!=[]:
            for i in range(len(Liste_Lignes_du_Fichier)):
                Ligne_Courante=Liste_Lignes_du_Fichier[i] # La variable 'Ligne_Courante' est utilisée pour donner plus de clarté sur le plan pédagogique, on peut à la place utiliser directement directement 'Liste_Lignes_du_Fichier[i]'
                Liste_Elements_Ligne_Courante=self.Str_to_List(Ligne_Courante) # Ici on transforme la chaîne de caractère 'Ligne_Courante'  en une liste 'Liste_Elements_Ligne_Courante' 
                if Element not in Liste_Elements_Ligne_Courante:
                    Nouvelle_Liste=Nouvelle_Liste+[Ligne_Courante+'\n']
                else:
                    Nouvelle_Liste=C_Liste(Liste_Elements_Ligne_Courante) # Nouvelle_Liste est une instance de la classe C_Liste
                    Nouvelle_Liste_Elements=Nouvelle_Liste.changer_element(Element)
                    Nouvelle_Ligne_Modifiee=self.Liste_to_Str(Nouvelle_Liste_Elements)
                    Nouvelle_Liste=Nouvelle_Liste+[Nouvelle_Ligne_Modifiee+'\n']    
            self.Liste_to_Fichier(Nouvelle_Liste) # creer_Fichier_depuis_Liste(nomFichier,Nouvelle_Liste)
            
    def ajouter_a_la_fin_de_la_ligne(self,ID,Element,sep):
        Nouvelle_Liste=[] # on commence par créer une nouvelle liste, inialisée à vide. Cette liste va nous servir à sauvegarder un 
        Liste_Lignes_du_Fichier=self.Fichier_to_Liste() # extraire_liste(nomFichier)
        if Liste_Lignes_du_Fichier!=[]:
            for i in range(len(Liste_Lignes_du_Fichier)):
                Ligne_Courante=Liste_Lignes_du_Fichier[i] # La variable 'Ligne_Courante' est utilisée pour donner plus de clarté sur le plan pédagogique, on peut à la place utiliser directement directement 'Liste_Lignes_du_Fichier[i]'
                Liste_Elements_Ligne_Courante=self.str_to_liste(Ligne_Courante) # Ici on transforme la chaîne de caractère 'Ligne_Courante'  en une liste 'Liste_Elements_Ligne_Courante' 
                if ID not in Liste_Elements_Ligne_Courante:
                    Nouvelle_Liste=Nouvelle_Liste+[Ligne_Courante+'\n']
                else:
                    Liste_Elements_Ligne_Courante[-1] = Liste_Elements_Ligne_Courante[-1].replace('\n','') +sep+ str(Element)
                    
                    Nouvelle_Liste_Elements=Liste_Elements_Ligne_Courante
                    Nouvelle_Ligne_Modifiee=self.Liste_to_Str1(Nouvelle_Liste_Elements)
                    Nouvelle_Liste=Nouvelle_Liste+[Nouvelle_Ligne_Modifiee+'\n']    
            self.Liste_to_Fichier(Nouvelle_Liste) # creer_Fichier_depuis_Liste(nomFichier,Nouvelle_Liste)
       
    
    def Liste_to_Str1(self,Liste_Elements):
        return self.separateur.join(map(str, Liste_Elements))
    
    def Liste_to_Str2(self,Liste_Elements):
        return self.separateur2.join(Liste_Elements)
    
    def supprimer_element_fichier(self,Element):
        Nouvelle_Liste=[] # on commence par créer une nouvelle liste, inialisée à vide. Cette liste va nous servir à sauvegarder un 
# erreur d'écriture        Liste_Lignes_du_Fichier=Fichier_to_Liste(self) # extraire_liste(nomFichier)
        Liste_Lignes_du_Fichier=self.Fichier_to_Liste() # extraire_liste(nomFichier)
        if Liste_Lignes_du_Fichier!=[]:
            for i in range(len(Liste_Lignes_du_Fichier)):
                if Element not in Liste_Lignes_du_Fichier[i]:
                    Nouvelle_Liste=Nouvelle_Liste+[Liste_Lignes_du_Fichier[i]+'\n']
# écriture erronée  Liste_to_Fichier(self.nomFichier,Nouvelle_Liste) # creer_Fichier_depuis_Liste(nomFichier,Nouvelle_Liste)
            self.Liste_to_Fichier(Nouvelle_Liste) # creer_Fichier_depuis_Liste(nomFichier,Nouvelle_Liste)
            
    def supprimer_ligne_fichier(self,Element_ligne):
        Nouvelle_Liste=[] # on commence par créer une nouvelle liste, inialisée à vide. Cette liste va nous servir à sauvegarder un 
# erreur d'écriture        Liste_Lignes_du_Fichier=Fichier_to_Liste(self) # extraire_liste(nomFichier)
        Liste_Lignes_du_Fichier=self.Fichier_to_Liste() # extraire_liste(nomFichier)
        if Liste_Lignes_du_Fichier!=[]:
            for i in range(len(Liste_Lignes_du_Fichier)):
                if Element_ligne not in Liste_Lignes_du_Fichier[i]:
                    Nouvelle_Liste=Nouvelle_Liste+[Liste_Lignes_du_Fichier[i]]
                else:
                    continue
# écriture erronée  Liste_to_Fichier(self.nomFichier,Nouvelle_Liste) # creer_Fichier_depuis_Liste(nomFichier,Nouvelle_Liste)
            self.Liste_to_Fichier(Nouvelle_Liste) # creer_Fichier_depuis_Liste(nomFichier,Nouvelle_Liste)
            
    def supprimer_ligne_fichier2(self,Element_ligne):
        Nouvelle_Liste=[] # on commence par créer une nouvelle liste, inialisée à vide. Cette liste va nous servir à sauvegarder un 
# erreur d'écriture        Liste_Lignes_du_Fichier=Fichier_to_Liste(self) # extraire_liste(nomFichier)
        Liste_Lignes_du_Fichier=self.Fichier_to_Liste() # extraire_liste(nomFichier)
        if Liste_Lignes_du_Fichier!=[]:
            for i in range(len(Liste_Lignes_du_Fichier)):
                if Element_ligne+"\n" not in Liste_Lignes_du_Fichier[i].split(self.separateur)[-1].split(self.separateur2) and Element_ligne not in Liste_Lignes_du_Fichier[i].split(self.separateur)[-1].split(self.separateur2):
                    Nouvelle_Liste=Nouvelle_Liste+[Liste_Lignes_du_Fichier[i]]
                else:
                    continue
# écriture erronée  Liste_to_Fichier(self.nomFichier,Nouvelle_Liste) # creer_Fichier_depuis_Liste(nomFichier,Nouvelle_Liste)
            self.Liste_to_Fichier(Nouvelle_Liste) #
            
    def modiffier_ligne(self,Element_ligne,nv_ligne):
        Nouvelle_Liste=[] 
        Liste_Lignes_du_Fichier=self.Fichier_to_Liste() 
        if Liste_Lignes_du_Fichier!=[]:
            for i in range(len(Liste_Lignes_du_Fichier)):
                if Element_ligne not in Liste_Lignes_du_Fichier[i]:
                    Nouvelle_Liste=Nouvelle_Liste+[Liste_Lignes_du_Fichier[i]]
                else:
                    Nouvelle_Liste = Nouvelle_Liste+[nv_ligne + '\n']
            self.Liste_to_Fichier(Nouvelle_Liste) #
        return
        
            

    def str_to_liste(self, string):
        return string.split(self.separateur)
    
    
    def nbre_ligne(self):
        return len(self.Fichier_to_Liste())
       

    def str_to_liste2(self, string):
        return string.split(self.separateur2)


