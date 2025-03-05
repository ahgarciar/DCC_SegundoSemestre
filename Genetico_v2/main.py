import random
import numpy as np
import Solucion
import Seleccion
import Cruza
import Muta

def cargar_instancia():
    with open("Instancia.txt", "r") as file:
        lines = file.readlines()

    amount_vertices = int(lines[0].strip())
    Mp = np.zeros((amount_vertices, amount_vertices))

    for i, line in enumerate(lines[1:]):
        valores = list(map(float, line.split()))
        for j in range(amount_vertices):
            if i != j:
                Mp[i][j] = valores[j]
    return amount_vertices,Mp


def evaluar_solucion(camino):
    return sum(Mp[camino[i]][camino[i + 1]] for i in range(len(camino) - 1))


amount_vertices, Mp = cargar_instancia()

print("\nMatriz de Distancias:")
for fila in Mp:
    print(fila)

MAX_GENERATIONS = 2
size_population = 12
poblacion = []

rnd = random.Random(3)

for _ in range(size_population):
    posibles_ciudades = [-1] * amount_vertices
    camino = [0] * (amount_vertices + 1)
    posibles_ciudades[0] = 0

    val_obj = 0
    ciudades_restantes = amount_vertices - 1

    k = 1
    while ciudades_restantes > 0:
        t = rnd.randint(0, amount_vertices - 1)
        if posibles_ciudades[t] == -1:
            camino[k] = t
            val_obj += Mp[camino[k - 1]][t]
            ciudades_restantes -= 1
            posibles_ciudades[t] = 0
            k += 1

    val_obj += Mp[camino[k - 1]][camino[k]]
    poblacion.append(Solucion.Solucion(camino[:], val_obj))

cont_gen = 1
while cont_gen <= MAX_GENERATIONS:
    padres = Seleccion.torneo_binario(poblacion, size_population // 2)
    hijos = Cruza.PMX(padres)
    hijos = Muta.mutation(hijos)

    for hijo in hijos:
        costo = evaluar_solucion(hijo.get_camino())
        hijo.set_val_obj(costo)
        poblacion.append(hijo)

    poblacion.sort()

    mejor_camino = poblacion[0].get_camino()
    mejor_val_obj = poblacion[0].get_val_obj()
    print("\nDatos generacion: ", cont_gen)
    print("Mejor Camino:", mejor_camino)
    print("Mejor Val. Obj.:", mejor_val_obj)

    poblacion = poblacion[:size_population // 2]  # //Se quedan solo las mejores soluciones

    cont_gen += 1

print("\nDatos Finales:")
mejor_camino = poblacion[0].get_camino()
mejor_val_obj = poblacion[0].get_val_obj()
print("\n\nMejor Camino:", mejor_camino)
print("Mejor Val. Obj.:", mejor_val_obj)

