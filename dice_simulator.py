import random

def dice_roll(num):
    list = []
    for i in range(num):
        rand_num = random.randint(1,6)
        list.append(rand_num)
    
    print(*list, sep=', ')

while True:
    input_num = input("How many dice rolls you want?")
    if input_num.lower() == "exit":
        break

    dice_roll(int(input_num))