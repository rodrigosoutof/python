import pytesseract  # C:\Program Files\Tesseract-OCR - Caminho do tesseract
import cv2

# 1- Ler a imagem
imagem = cv2.imread('sorocaba.png')

# 2 - Utilizar tesseract para extrair texto da imagem
# C:\Program Files\Tesseract-OCR
caminho = r'C:\Program Files\Tesseract-OCR'
pytesseract.pytesseract.tesseract_cmd = caminho + r'\tesseract.exe'
texto = pytesseract.image_to_string(imagem)

print(texto)
