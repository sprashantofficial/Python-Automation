# https://i.pinimg.com/originals/df/43/98/df4398136446ca1e6e4961b06d3d4582.jpg

import requests

url = input('Enter the URL: ')

file_rename_input = input('Do you want to rename the image? T or F: ').upper()
if file_rename_input == 'T':
    name = input('Name of the image: ')
else:
    name = url[(url.rfind('/') + 1):]

image = requests.get(url).content
with open(name, 'wb') as handler:
    handler.write(image)

print(f'Downloaded image -> {name} successfully')