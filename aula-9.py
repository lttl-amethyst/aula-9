#1
for i in range(1, 11):
    print(i)

contador = 1

while contador <= 10:

    print(contador)
    contador += 1
 

#2
for i in range(5):
    print("repetição")

contador = 0 
while contador <= 4:
    print("repetição")
    contador += 1


contador = 1

while contador <= 25:

    print(contador)
    contador += 1
 

#3
for numero in range (1, 11):
    if numero %2 == 0:
        print(numero)

contador = 0

while contador <= 9:

    contador +=1
    if contador %2 == 0:
        print(contador)
    continue