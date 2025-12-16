import os

# Pega o caminho da pasta onde este arquivo (configuracao.py) está
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Une o caminho da pasta com a subpasta 'imagens' e o arquivo
IMAGEM_PRINCIPAL = os.path.join(BASE_DIR, 'imagens', 'produto_na_esteira.png')
TEMPLATE = os.path.join(BASE_DIR, 'imagens', 'componente_ok.png')

LIMITE_DE_CONFIANCA = 0.8 
COR_DETECCAO = (0, 255, 0)