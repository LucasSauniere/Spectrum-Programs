import astropy.io.fits as pyfits
from os import walk
import os

def extraction_fichier(nom_fichier):
##      if fichier!=[]:
##      print(fichier[0])
      a=pyfits.open(nom_fichier)
      #level 2
      header=a[0].header
                              
      nom_fichier=str(header['DATE-OBS'])+'.txt'
      f = open(str(nom_fichier),'wt')
      f.write("Date d'Observation:        "+str(header['DATE-OBS']))
      f.write('\n\nCorrection de vitesse héliocentrique:          '+str(header['BERV']) )

##      return(header['BERV'],header['DATE-OBS'])


def liste_fichiers():
      for folder in os.listdir(r'C:\Users\lucas\Desktop\Stage IRAP\Spectres\Neo_Bta_CrB'):
            file_list=[]
            for (repertoire, sousrepertoires, fichier) in walk(r'C:\Users\lucas\Desktop\Stage IRAP\Spectres\Neo_Bta_CrB'):
                  file_list.extend(fichier)
##                  for f in file_list:
##                        extraction_fichier(f)
      return(file_list)

def start():
      l=liste_fichiers()
      for f in l:
            extraction_fichier(f)
            
##file=pyfits.open('NEO_20200106_045959_st3.fits')




