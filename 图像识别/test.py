from PIL import Image
import pytesseract
text=pytesseract.image_to_string(Image.open('deggao.jpg'),lang='chi_sim')
print(text)
