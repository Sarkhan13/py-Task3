massiv = []

for i in range(1,101):
    if(i % 2 != 0):
        print(i, end="")
        massiv.append(i)
        
for i in range(1,101):
    if(i % 2 == 0):
        print(i)
        massiv.append(i)

print(massiv)