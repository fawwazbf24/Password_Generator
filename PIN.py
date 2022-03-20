import random,math
def generatePIN():
    PIN = ""
    for i in range(1,5):
        a = random.random()
        b = math.floor(a*10)
        PIN += str(b)
    return PIN
print("PIN of 4 digits :", generatePIN())