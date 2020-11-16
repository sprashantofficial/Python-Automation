import os

for file in os.listdir("C:\Users\spras\Desktop\Python"):
    if file.startswith("test"):
        exFile = os.path.join("C:\Users\spras\Desktop\Python", file)
        exec(open(exFile).read())
        break
