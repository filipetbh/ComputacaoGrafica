# -*- coding: UTF-8 -*-

import numpy as np
import cv2
from PIL import Image
import glob, os
from matplotlib import pyplot as plt
plt.rcParams['figure.figsize'] = (224, 224)

face_cascade = cv2.CascadeClassifier('modelo/haarcascade_frontalface_default.xml')


def faceDetect(path, facefilename):
    try:             
        img = cv2.imread(path)

        cv2.imwrite(facefilename, img)
        print ('Salvando a imagem:', facefilename)
        
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#faces = face_cascade.detectMultiScale(gray, 1.3, 5)
        faces = face_cascade.detectMultiScale(
                gray,
                scaleFactor=1.1,
                minNeighbors=5,
                minSize=(30, 30),
        )
        for (x,y,w,h) in faces:
            img = cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
            gray = cv2.rectangle(gray,(x,y),(x+w,y+h),(0,255,0),2)
#    roi_gray = gray[y:y+h, x:x+w]
            roi_color = img[y:y+h, x:x+w]

        cv2.imwrite(facefilename, img)
        print ('Salvando a imagem:', facefilename)
        
# cv2.imshow('img',img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

    except:
        print ('Erro ao converter a imagem')

# Modulo principal
if __name__ == "__main__":
    # Armazena o caminho informado na variavel d
    d = input ('Informe o diretorio de imagens:')
     
    if not os.path.exists(d):
        raise Exception('O diretorio informado nao existe')
         
    # 'Navega' ao diretorio informado
    os.chdir(d)
    # os.path.abspath(os.curdir) tambem retorna o diretorio corrente
    print ('Diretorio corrente:', os.getcwd())
 
    # Cria o diretorio para armazenar as imagens P&B
    os.mkdir('ImagesFaces')
     
    # Convertendo todas as imagens JPEG para escalas de cinza
    for fn in glob.glob('*.jpg'):
            print ('Processando:', fn)
 
            # obtem o nome do arquivo sem a extensao
            f = glob.os.path.splitext(fn)[0]
 
            # Converte a imagem escala de cinza e salva no diretorio GrayImages
            faceDetect(fn, 'ImagesFaces/' + f + '.jpg')
 
    print ('Concluido')














