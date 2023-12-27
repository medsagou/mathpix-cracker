from .Class_Files import C_File

import random

def get_name():
    path = "../data/names"
    names_file = C_File(file_name=path)
    names = names_file.fichier_to_Liste()
    if names_file != []:
        return names[random.randint(0, len(names)-1)]
    else:
        print("error getting the name")
