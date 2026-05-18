# pyrefly: ignore [missing-import]
from term_image.image import AutoImage
from PIL import Image

# Substitua pelo caminho da sua imagem
caminho_imagem = "sua_imagem.jpg"

# Carrega e exibe a imagem redimensionada automaticamente para o terminal
my_image = AutoImage(Image.open(caminho_imagem))
print(my_image)
