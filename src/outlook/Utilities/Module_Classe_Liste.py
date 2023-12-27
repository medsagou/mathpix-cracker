# -*- coding: utf-8 -*-
"""
Created on Sat Feb  4 23:52:15 2023

@author: sagou
"""

# -*- coding: utf-8 -*-
"""
Created on Fri Dec  3 12:16:12 2021

@author: sagou
"""

class C_Liste(list):
    
    def __init__(self,sep=';'):
        self.separateur = sep
    
    def afficher_Liste(self):
        for i in range(len(self)):
            print(self[i],'\n')
    
    def Str_to_List(self,Ligne_Chaine):
        return Ligne_Chaine.split(self.separateur) 
    
    def Liste_to_Str(self,Liste_Elements):
        return self.separateur.join(Liste_Elements) 

    def changer_element(self,E):
        Liste_Tempo=[]
        for i in range(len(self)):
            Element_courant=self[i]
            if E != Element_courant:
               Liste_Tempo=Liste_Tempo + [Element_courant]
            else:               
                print("Veuillez saisir un élément à la place de : ",E,"\n")
                E_modifie= input("Veuillez saisir un élément : ")
                Liste_Tempo=Liste_Tempo + [E_modifie]
        return Liste_Tempo 
    
    



"""    
    def changer_element(E,Liste_Elements_Ligne):
        Liste_Tempo=[]
        for i in range(len(Liste_Elements_Ligne)):
            if E != Liste_Elements_Ligne[i]:
               Liste_Tempo=Liste_Tempo + [Liste_Elements_Ligne[i]]
            else:               
                print("Veuillez saisir un élément à la place de : ",E)
                E_modifie= input("Veuillez saisir un élément : ")
                Liste_Tempo=Liste_Tempo + [E_modifie]
        return Liste_Tempo       
"""    
"""
L=C_Liste([1,2,3])
L.afficher_Liste()
LL=C_Liste(L.changer_element(3))
LL.afficher_Liste()    
LLL=LL.changer_element(2)
print(LLL)
"""

 
