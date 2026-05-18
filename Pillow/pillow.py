from PIL import Image

# Caracteres usados para representar a intensidade (do mais escuro ao mais claro)
ASCII_CHARS = ["@", "#", "S", "%", "?", "*", "+", ";", ":", ",", "."]

def resize_image(image, new_width=100):
    """ Redimensiona a imagem mantendo a proporção """
    width, height = image.size
    ratio = height / width / 1.65 # 1.65 ajusta a proporção dos caracteres
    new_height = int(new_width * ratio)
    resized_image = image.resize((new_width, new_height))
    return resized_image

def grayify(image):
    """ Converte a imagem para tons de cinza """
    return image.convert("L")

def pixels_to_ascii(image):
    """ Mapeia pixels para caracteres ASCII """
    pixels = image.getdata()
    characters = "".join([ASCII_CHARS[pixel // 25] for pixel in pixels])
    return characters

def main(path, new_width=100):
    """ Função principal para processar a imagem """
    try:
        image = Image.open(path)
    except Exception as e:
        print(f"Não foi possível abrir a imagem: {e}")
        return

    # Processamento
    new_image_data = pixels_to_ascii(grayify(resize_image(image, new_width)))
    
    # Formatação (quebra de linha)
    pixel_count = len(new_image_data)
    ascii_image = "\n".join(
        new_image_data[i : i + new_width] for i in range(0, pixel_count, new_width)
    )
    
    print(ascii_image)
    
    # Opcional: Salvar em um arquivo .txt
    with open("ascii_image.txt", "w") as f:
        f.write(ascii_image)

# --- Execute o script ---
# Substitua 'sua_imagem.jpg' pelo caminho da sua imagem
main('sua_imagem.jpg')
