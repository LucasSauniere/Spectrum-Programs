import astropy.io.fits as pyfits
from os import walk
import os
from matplotlib import pyplot as plt
import numpy as np
import tkinter as tk
from tkinter import filedialog

####def extraction_fichier(nom_fichier):
######      if fichier!=[]:
######      print(fichier[0])
####      a=pyfits.open(nom_fichier)
####      #level 2
####      header=a[0].header
####                              
####      nom_fichier=str(header['DATE-OBS'])+'.txt'
####      f = open(str(nom_fichier)[:len(str(nom_fichier))-2]+'.s','wt')
####      f.write("Date d'Observation:        "+str(header['DATE-OBS']))
####      f.write('\n')
####      wvl = a[1].data['Wavelength1']
####      sp = a[1].data['Beam1']
####
######      return(header['BERV'],header['DATE-OBS'])
####
####
####def liste_fichiers():
####      for folder in os.listdir(r'C:\Users\lucas\Desktop\Stage IRAP\Spectres\Neo_Bta_CrB'):
####            file_list=[]
####            for (repertoire, sousrepertoires, fichier) in walk(r'C:\Users\lucas\Desktop\Stage IRAP\Spectres\Neo_Bta_CrB'):
####                  file_list.extend(fichier)
######                  for f in file_list:
######                        extraction_fichier(f)
####      return(file_list)
####
####def start():
####      l=liste_fichiers()
####      for f in l:
####            extraction_fichier(f)

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
      file=pyfits.open(name_file)
      name_newfile=name_file[:len(name_file)-5]
##    print(name_newfile)

      données=file[1].data
      wvl=données['Wavelength1']
      inten=données['Intensity']
      ##wvl=wvl.tolist()
      ##inten=inten.tolist()

      #l'ordre des longueurs d'onde semble inversé
      wvl=wvl[::-1]
      inten=inten[::-1]
      
      txt=open(name_newfile+'.s',"w")

      n=len(wvl)
      for k in range(n):
            l,i=wvl[k],inten[k]
            #on repasse en nanomètres
            l=l/10
##            txt.write(str(l)+'  '+str(i)+'\n')
            txt.write(str(l)+'  '+str(i)+'  '+str(k)+'\n')


      txt.close()
      file.close()
     
master = tk.Tk()
 
button_choice = tk.Button(master, text='Choix du fichier', command=display)
button_choice.pack()
 
master.mainloop()
  


##plt.plot(wvl,inten)
##plt.show()


