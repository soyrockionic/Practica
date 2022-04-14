titulos = open("Titulos_2021.txt", "r")
arch_titulos = titulos.read().split(";")

arch_dat = open("titulos_2021.dat", "w")

for peli in arch_titulos:
    if "2021" in peli:  
        arch_dat.write(peli+' ')

arch_dat = open("titulos_2021.dat", "r")
dat_titu = arch_dat.read().split()

print("-"*20)
for peli in dat_titu:
    pelicula = peli.split(",")
    print('{:<12}  {:<8}'.format(pelicula[0] ,pelicula[2]))
print("-"*20)