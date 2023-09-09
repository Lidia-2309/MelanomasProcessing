""" 
# TÉCNICA DE PRÉ-PROCESSAMENTO DULLRAZOR

A maioria das imagens de lesões cutâneas apresenta elementos indesejados, como sombras e cabelos, 
que podem dificultar a segmentação da lesão e introduzir informações errôneas sobre suas características. 
Portanto, é necessário aplicar algumas técnicas de visão artificial para eliminar qualquer componente de ruído.

Os pelos corporais são um dos fatores que podem afetar a segmentação da lesão. Para a detecção e remoção dos pelos, 
é utilizada uma técnica de pré-processamento denominada DullRazor, que consiste em aplicar uma série de operações 
morfológicas à imagem para gerar uma máscara que contenha os pelos. As etapas para aplicar o algoritmo DullRazor são:

1. Converta a imagem original em tons de cinza.
2. Fechando a imagem em tons de cinza, usando um kernel linear ou em forma de cruz.
3. Calcule a diferença entre a imagem resultante e a original.
4. Aplique limiar binário para obter uma máscara com os cabelos da imagem.
5. Substitua os pixels comuns entre a máscara e a imagem original, pelos pixels desta última. """


import cv2
import os
import shutil


# Diretório onde estão as pastas com as imagens
diretorio_principal = 'images_dermoscopic'

# Diretório de destino onde as imagens serão salvas
diretorio_destino = 'images_dullrazor'


for imagem in os.listdir(diretorio_principal):
    if imagem.lower().endswith(('.bmp')):
        imagem_path = os.path.join(diretorio_principal, imagem)
        #IMAGE ACQUISITION

        #Input image

        """ path='images_dermoscopic\IMD002.bmp' """

        #Read image
        image=cv2.imread(imagem_path,cv2.IMREAD_COLOR)
        #DULL RAZOR (REMOVE HAIR)

        #Gray scale
        grayScale = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY )
        #Black hat filter
        kernel = cv2.getStructuringElement(1,(9,9)) 
        blackhat = cv2.morphologyEx(grayScale, cv2.MORPH_BLACKHAT, kernel)
        #Gaussian filter
        bhg= cv2.GaussianBlur(blackhat,(3,3),cv2.BORDER_DEFAULT)
        #Binary thresholding (MASK)
        ret,mask = cv2.threshold(bhg,10,255,cv2.THRESH_BINARY)
        #Replace pixels of the mask
        dst = cv2.inpaint(image,mask,6,cv2.INPAINT_TELEA)   

            
            
        # Combine o caminho de destino com o nome do arquivo
        nome_arquivo_destino = imagem  # Pode personalizar o nome como desejar
            
        caminho_destino = os.path.join(diretorio_destino, nome_arquivo_destino)
            
        # Salve a imagem processada no diretório de destino
        cv2.imwrite(caminho_destino, dst)
            
        #Display images
            
        """ cv2.imshow("Original image",image)
            cv2.imshow("Cropped image",image)
            cv2.imshow("Gray Scale image",grayScale)
            cv2.imshow("Blackhat",blackhat)
            cv2.imshow("Binary mask",mask)
            cv2.imshow("Clean image",dst)

            cv2.waitKey()
            cv2.destroyAllWindows()
             """
            
            