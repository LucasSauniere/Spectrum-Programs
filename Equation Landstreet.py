from math import *

'Données physiques constantes'


c=3e8 #300.000km/s


'propriétés électron'
m=9.1e-31
e=1.6e-19


##" Spin orbit interaction sigma "
##
##sigma=((m*c)**2/2)*(1/r)


###############
'Programme de lecture du fichier param'

'extraction de geq et leq'
leq=1
geq=1

###############

lambda0=leq
z=geq

delta_lambda=1

'formule avec lambda, pas lambda0'
##B=(delta_lambda*4*pi*m*c**2)/(z*lambd0*e)

B=delta_lambda/(4.67e-13*z*lambda0**2)












