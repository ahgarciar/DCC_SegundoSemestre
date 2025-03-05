import random
import Solucion

rnd = random.Random(3)

def mutation(hijos):
    hijos_mutados = []
    for hijo in hijos:
        array = hijo.get_camino()[:]

        l = len(array) - 2

        # Obtener dos índices aleatorios distintos entre 1 y l
        r1 = 1 + rnd.randint(0, l - 1)
        r2 = 1 + rnd.randint(0, l - 1)

        while r1 >= r2:
            r1 = 1 + rnd.randint(0, l - 1)
            r2 = 1 + rnd.randint(0, l - 1)

        # Mover el elemento en r2 justo después de r1, desplazando los elementos intermedios
        temp = array[r2]
        for j in range(r2, r1, -1):
            array[j] = array[j - 1]
        array[r1 + 1] = temp

        hijos_mutados.append(Solucion.Solucion(array[:]))

    return hijos_mutados
