'''
@Auteur : Sean OMBE
@Mail : patrick.ombe@gmail.com
'''

from scipy import misc
import matplotlib.pyplot as plt

def zomming(image):
    nline = int(0.25 * image.shape[0])
    ncol  = int(0.25 * image.shape[1])
    return image[nline:-nline,ncol:-ncol]

def constraste(image):
    image[image>210] = 200
    image[image<45]  = 70
    return image

#Le but est de zoommer dans cette image et faire des modif sur certain élément pixel

face = misc.face(gray= True)
plt.imshow(face, cmap=plt.cm.gray)
plt.show()

#Zoom
face = zomming(face)
plt.imshow(face, cmap=plt.cm.gray)
plt.show()

#Modification de contraste
face = constraste(face)
plt.imshow(face, cmap=plt.cm.gray)
plt.show()