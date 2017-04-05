import itertools

datos = []
medias = []
tabla_medias = []
suma_medias = 0

print("\n\nBienvenido, este programa calcula la distribución muestral de medias.\n\n")

N = int(input("-> Ingrese el tamaño de N: "))
for i in range(N):
    dato = float(input("\tIngrese el dato {}: ".format(i+1)))
    datos.append(dato)
n = int(input("\n-> Ingrese el tamaño de n: "))

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

print("\n\n x \t f \t p(x) \t x*p(x)")
print("-------------------------------")
for tupla in tabla_medias:
    print("{0:.3f} \t {1} \t {2}/{3} \t {4:.3f}".format(tupla[0], tupla[1], tupla[1], len(combinaciones), tupla[0] * tupla[2]))
    suma_medias += tupla[0] * tupla[2]

print("\n\n Resultado: {}".format(suma_medias))

