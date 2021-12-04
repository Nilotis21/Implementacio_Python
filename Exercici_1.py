def main():
    n1 = int(input("Introduce un número: "))
    n2 = int(input("Introduce un número: "))
    if n1 < n2:
        for x in range(n1+1,n2,):
            print(x)
    else:
        print("Error")

if __name__ == '__main__':
    main()
