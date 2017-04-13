import itertools # Módulo que permitirá hacer las combinaciones.

datos = [] # Lista donde se almacenarán los elementos de la población.
medias = [] # Lista donde se almacenarán las medias calculadas con los datos de las muestras.
media_frec_prob = [] # Lista donde se almacenarán las medias junto con su frecuencia y su probabilidad.
suma_medias = 0 # Suma total de las medias muestrales.

print("\n\n")
print("*" * 60)
print("\n\t BIENVENIDO \n")
print("\n Objetivo: Calcular la distribución muestral de medias y \n\tdesplegar una tabla con los datos obtenidos\n")
print("*" * 60)
print("\n\n")

# Se lee el tamaño de la población (N).
# Se muestra un mensaje de error si el dato no es entero.
while True:
    try:
        N = int(input("-> Ingrese el tamaño de la población: "))
        break
    except ValueError:
        print("\nERROR: Ingrese un dato numérico. \n\n")

# Se lee cada uno de los elementos de la población.
# Se muestra un mensaje de error si el dato no se puede convertir a flotante.
for i in range(N):
    while True:
        try:
            dato = float(input("\tIngrese el dato {}: ".format(i+1)))
            datos.append(dato)
            break
        except ValueError:
            print("\n\tERROR: Ingrese un dato numérico. \n\n")

# Se lee el tamaño de las muestras (n).
# Se muestra un mensaje de error si el dato no es entero.
while True:
    try:
        n = int(input("\n\n-> Ingrese el tamaño de las muestras: "))
        break
    except ValueError:
        print("\n\tERROR: Ingrese un dato numérico. \n\n")

# Se lee el número de decimales que el usuario desea que se impriman.
# Se muestra un mensaje de error si el dato no es entero.
while True:
    try:
        decimales = int(input("\n\n-> Ingrese el número de decimales: "))
        break
    except ValueError:
        print("\n\tERROR: Ingrese un dato numérico. \n\n")

combinaciones = list(itertools.combinations(datos, n)) # Se obtienen las combinaciones de los datos, cada combinación de tamaño n
                                                       # El iterador con las combinaciones se convierte en una lista.

# Se suman todos los valores por cada combinación y se calcula su media.
# Después el valor obtenido se agrega a la lista de las medias.
for combinacion in combinaciones:
    suma = 0
    for valor in combinacion:
        suma += valor
    medias.append(suma / n)

# Por cada media se obtiene su frecuencia y su probabilidad.
for media in medias:
    frecuencia = medias.count(media) # "count(medias)" - devuelve el número de coincidencias de esa media en la lista.
    probabilidad = frecuencia/len(combinaciones)
    m_f_p = (media, frecuencia, probabilidad) # Se crea una tupla con el valor de la media, su frecuencia y su probabilidad.
    if m_f_p not in media_frec_prob: # Se compara si la tupla no se encuentra en la lista de medias, frecuencias y probabilidades.
        media_frec_prob.append(m_f_p)   

print("\n\n   x", " "*(decimales), " f     p(x)     x*p(x)") # Se despliega un número de espacios igual al número de decimales.
print("-"*(decimales*8)) # Se despliegan tantos guiones como el número de decimales por 8.

for tupla in media_frec_prob: # Por cada tupla en la lista de medias, frecuencias y probabilidades.
    # tupla = (media, frecuencia, probabilidad)
    # Se imprime el valor de la media, la frecuencia, la probabilidad en fracción y el producto de la media por su probabilidad.
    # Los valores se imprimen con el número de decimales que el usuario escogió.
    print('{t[0]:.{decimales}f}     {t[1]}     {t[1]}/{N}     {media_prob:.{decimales}f}'.format(t=tupla, N=len(combinaciones), media_prob=tupla[0]*tupla[2], decimales=decimales))
    suma_medias += tupla[0] * tupla[2] # Se suma el producto de la media por su probabilidad.

print("\n\n")
print("*" * 30)
print("\n RESULTADO: {:.{decimales}f} \n".format(suma_medias, decimales=decimales)) # Se imprime el valor de la suma de todas las medias por sus probabilidades.
print("*" * 30)
