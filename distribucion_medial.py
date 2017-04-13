import itertools

datos = []
medias = []
tabla_medias = []
suma_medias = 0

print("\n\nBienvenido, este programa calcula la distribución muestral de medias.\n\n")

while True:
    try:
        N = int(input("-> Ingrese el tamaño de N: "))
        break
    except ValueError:
        print("\nIngrese un dato numérico. \n\n")

for i in range(N):
    while True:
        try:
            dato = float(input("\tIngrese el dato {}: ".format(i+1)))
            datos.append(dato)
            break
        except ValueError:
            print("\nIngrese un dato numérico. \n\n")

while True:
    try:
        n = int(input("\n-> Ingrese el tamaño de n: "))
        break
    except ValueError:
        print("\nIngrese un dato numérico. \n\n")

while True:
    try:
        decimales = int(input("\n\n-> Ingrese el número de decimales: "))
        break
    except ValueError:
        print("\nIngrese un dato numérico. \n\n")

combinaciones = list(itertools.combinations(datos, n))

for combinacion in combinaciones:
    suma = 0
    for valor in combinacion:
        suma += valor
    medias.append(suma / n)

medias.sort()

for media in medias:
    frecuencia = medias.count(media)
    probabilidad = frecuencia/len(combinaciones)
    n = (media, frecuencia, probabilidad)
    if n not in tabla_medias:
        tabla_medias.append(n)

print("\n\n   x", " "*(decimales), " f     p(x)     x*p(x)")
print("-"*(decimales*8))
for tupla in tabla_medias:
    print('{t[0]:.{decimales}f}     {t[1]}     {t[1]}/{N}     {xp:.{decimales}f}'.format(t=tupla, N=len(combinaciones), xp=tupla[0]*tupla[2], decimales=decimales))
    suma_medias += tupla[0] * tupla[2]

print("\n\n Resultado: {}".format(suma_medias))
