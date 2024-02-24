from pyzbar import pyzbar
from PIL import Image

image = Image.open('qr.png')
qr_code = pyzbar.decode(image)[0]

data = qr_code.data.decode("utf-8")
print(data)