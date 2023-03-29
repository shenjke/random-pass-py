import random as r
symbols = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
for i in range(10):
    zapros = input("Введите длину пароля : ")

    zapros = int(zapros)

    password = ''

    for i in range(zapros):
        password += (r.choice(symbols)

    print(password)