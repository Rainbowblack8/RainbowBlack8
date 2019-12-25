c="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
num='0123456789'
alphabet='abcdefghijklmnopqrstuvwxyz'
message = input("Enter your message: ")
key = 1
encrypted = ""
for letter in message:
    position = c.find(letter)
    newpos = position + key
    if letter in c :
        if newpos== 26:
            newpos=newpos -26
        encrypted=encrypted + c[newpos]

    position1= alphabet.find(letter)
    newposition1= position1 + key
    if letter in alphabet:
        if newposition1== 26:
            newposition1= newposition1-26
        encrypted = encrypted + alphabet[newposition1]

    position2 = num.find(letter)
    newposition2= position2 + key
    if letter in num :
        if newposition2 ==10:
            newposition2 = newposition2 - 10
        encrypted= encrypted+ num[newposition2]
    if letter==' ':
        encrypted=encrypted+ letter


print("Your encrypted message:" + encrypted)
