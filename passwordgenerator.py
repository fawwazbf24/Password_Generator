import random

lower = "abcdefghijklmnopqrstuvwxyz"
upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
number = "1234567890"
symbol = "!#$%&*?"

merge = lower + upper + number + symbol
lenght = 10
password = "".join(random.sample(merge, lenght))

print("password saya :", password)
