# SCRIPT PARA EXTRAIR IMAGENS DE SUBPASTAS 

import os
import shutil

# Diretório onde estão as pastas com as imagens
diretorio_principal = 'path_principal'

# Diretório de destino onde as imagens serão salvas
diretorio_destino = 'path_destino'

# Função para encontrar e extrair a imagem de uma pasta
def extrair_imagem_da_pasta(pasta):
    for subpasta in os.listdir(pasta):
        subpasta_path = os.path.join(pasta, subpasta)
        if os.path.isdir(subpasta_path) and subpasta.endswith('_roi'):
            for imagem in os.listdir(subpasta_path):
                if imagem.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp')):
                    imagem_path = os.path.join(subpasta_path, imagem)
                    # Copiar a imagem para o diretório de destino
                    shutil.copy(imagem_path, diretorio_destino)

# Iterar sobre todas as pastas no diretório principal
for pasta_principal in os.listdir(diretorio_principal):
    pasta_principal_path = os.path.join(diretorio_principal, pasta_principal)
    if os.path.isdir(pasta_principal_path):
        extrair_imagem_da_pasta(pasta_principal_path)

