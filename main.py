import random

newStr = []
inputPW = input("Enter a string: ")
directions = []

# Loop through each character in the string, add 0-4 random ASCII and special characters
consecutiveZero = False
for i in range(0, len(inputPW)):
    numOfFillers = random.randint(0, 2)
    if numOfFillers == 0 and consecutiveZero == True:
        numOfFillers = random.randint(1, 2)
        consecutiveZero = False
    
    if numOfFillers == 0:
        consecutiveZero = True
    
    newStr.append(inputPW[i])
    directions.append("←")
    for j in range(0, numOfFillers):
        newStr.append(chr(random.randint(32, 126))) if numOfFillers % 2 == 0 else newStr.append(chr(random.randint(65, 122)))
        directions.append("DEL")

directions.reverse()
print("Obfuscated password: " + "".join(newStr))
print("Directions: ", directions)

pw = []
for d in directions:
    char = newStr.pop()
    if(d == "←"):
        pw.insert(0, char)

print("Decoded pw: " + "".join(pw))