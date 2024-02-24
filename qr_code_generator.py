import qrcode

qr = qrcode.QRCode(box_size=50, border=3)

user_input = input('Enter your data: ')
qr.add_data(user_input)

image = qr.make_image(fill_color='black', back_color='white')
image.save('qr.png')

print('QR code generated successfully!!')