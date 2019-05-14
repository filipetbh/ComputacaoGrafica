# -*- coding: utf-8 -*-
"""
Created on Tue Apr 23 18:31:52 2019

@author: filipe.teixeira
"""

from PIL import Image
import glob, os
import cv2
 
def convertToMedia(path, mediafilename):
    try:
        # abre a imagem na escala de cinza
#        im = Image.open(path).convert("L")
        # salva a imagem
        
#        im.save(grayfilename)
        
        
        img = cv2.imread(path)
        img_filtro_media = cv2.blur(img, ( 5, 5))
        cv2.imwrite(mediafilename, img_filtro_media)
        print ('Salvando a imagem:', mediafilename)

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
 
    print ('Convertendo as imagens PNG para JPEG')
    for fn in glob.glob('*.png'):
            print ('Convertendo %s para PNG', fn)
            # obtem o nome do arquivo sem a extensao
            f = glob.os.path.splittext(fn)[0]
            # Abre a imagem
            imagem = Image.open(fn)
 
            # obtem o nome do arquivo sem a extensao
            f = glob.os.path.splittext(fn)[0]
            imagem.save(f + '.png', 'PNG')
            print (f +'.png salvo com sucesso.')
 
    # Cria o diretorio para armazenar as imagens P&B
    os.mkdir('MediaImages')
     
    # Convertendo todas as imagens JPEG para escalas de cinza
    for fn in glob.glob('*.jpg'):
            print ('Processando:', fn)
 
            # obtem o nome do arquivo sem a extensao
            f = glob.os.path.splitext(fn)[0]
 
            # Converte a imagem escala de cinza e salva no diretorio GrayImages
            convertToMedia(fn, 'MediaImages/' + f + '.jpg')
 
    print ('Concluido')