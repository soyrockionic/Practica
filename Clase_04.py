arch = open("Nombres.txt", "w")
archi = open("Notas.txt", "w")

arch.write("Luciana ")
arch.write("Sofia Juan ")
arch.write("Walter ")
archi.write("70 50 37 60")

arch.close()
archi.close()


def leer() : 
    pro = open("promocionados.csv", "w")

    arch = open("Nombres.txt", "r")
    arch1 = arch.read().split()
    archi = open("Notas.txt", "r")
    archi1 = archi.read().split()

    for val1, val2 in zip(arch1, archi1) :
        print('{:<12}  {:<8}'.format(val1,val2))
        if int(val2) >= 60 :
            pro.write(val1+' ')

    arch.close()
    archi.close()
    pro.close()


def main() :
    print("-"*20)
    leer()
    print("-"*20)


if __name__ == "__main__" :
    main()