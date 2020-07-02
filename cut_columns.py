import os
from os import walk
import csv
import pandas as pd
import tkinter as tk
from tkinter import filedialog

##fh = open('exemple.s')
##reader = csv.reader(fh, delimiter=' ')
##
####for ligne in reader:
####      print(ligne)
##
##tableau=[]
##for ligne in reader:
##      data=[elem for elem in ligne if elem!='']
##      tableau.append(data)
##
##
####for j in range (len(tableau)):
####      tableau[j]=[tableau[j][i] for i in range(len(tableau)) if tableau[j][i]!='']
##
##
##df = pd.DataFrame(data=tableau,columns=['c1','c2','c3','c4','c5','c6'])
##
##df.drop(['c4','c5','c6'],1,inplace=True)
##
##df.to_csv('myFile.csv', sep = '\t')




 
CURRENT_DIRECTORY = os.getcwd() # put directory of work !
 
def display():
    """Display file in current directory"""
    options = {
                'initialdir': CURRENT_DIRECTORY,
                'title': 'Choisissez votre fichier',
                'filetypes': (("all files", "*.*"),)
              }
 
    name_file = filedialog.askopenfilename(**options)
    print(name_file) # get name of file
##    h=open('test.s',"w")
    f = open(str(name_file), "r")
##    print(f.read())
    name_newfile=name_file[:len(name_file)-2]+'_raccourci.s'
    print(name_newfile)
    g = open(str(name_newfile), "w")

    for line in f:
        if line.strip():
            
            "sauvegarde des trois premières colonnes"
            
            g.write("  ".join(line.split()[:3]) + "\n")    
    f.close()
    g.close()
 
master = tk.Tk()
 
button_choice = tk.Button(master, text='Choix du fichier', command=display)
button_choice.pack()

master.mainloop()










##f = open('exemple.txt','wt')
##f.write('Reduced spectrum of betcrb')
##
##data=''
##espace='  '
###tri des colonnes
##for ligne in reader:
####      print(ligne)
##      if len(ligne)==10:
##            for i in range(1,4):
##                  data=str(ligne[2*i])
##                  print(data)
##                  if data[0]=='-':
##                        espace=' '
##                  f.write(espace+data)
##                  #réinitialisation espace
##                  espace='  '
##            f.write('\n')

         
