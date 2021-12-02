# This is a sample Python script.
# Press Mayús+F10 to execute it or replace it with your code.

def main():
    aux = aux2 = 0
    num = int(input("Introdueix un nombre enter: "))
    while num < 1:
        num = int(input("Introdueix un nombre enter: "))
    for x in range(num):
        aux += x
        if aux < num:
            print(x, end=" ")
            aux2 += x
    print("\nLa suma dels valors és: ", aux2)


if __name__ == '__main__':
    main()

'''def main():
    x = 0
    llista = list()
    #y = int(input("Cuantos valores introduciras: "))
    while x < 3 or x == 0:
        llista.append(int(input("Introdueix un valor: ")))
        x += 1
    print(llista)


if __name__ == '__main__':
    main()'''

''' #Rellenar un array de teclado con tres valores enteros
llista =list()
print(llista)

x = 0

while x < 3:
    llista.append(int(input("Introdueix un valor: ")))
    x+=1
    
print(llista)
'''

'''aux = aux2 = 0
    num = int(input("Introduce un nombre enter: "))
    while num < 1:
        num = int(input("Introduce un nombre enter: "))
    for x in range(num):
        aux += x
        if aux < num:
            print(x, end=" ")
            aux2 += x
    print("")
    print("La suma dels valors és: ", aux2)'''
