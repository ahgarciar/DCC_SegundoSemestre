import random
import Solucion

rnd = random.Random(3)

def PMX(padres):
    hijos = []

    for p in range(0, len(padres) - 1, 2):
        padre1 = padres[p].get_camino()
        padre2 = padres[p + 1].get_camino()

        hijo1 = [-1] * len(padre1)
        hijo2 = [-1] * len(padre2)

        lim_inf = 1 + rnd.randint(0, len(padre1) - 3)
        lim_sup = 1 + rnd.randint(0, len(padre1) - 3)

        while lim_inf >= lim_sup:
            lim_inf = 1 + rnd.randint(0, len(padre1) - 3)
            lim_sup = 1 + rnd.randint(0, len(padre1) - 3)

        hijo1[lim_inf:lim_sup + 1] = padre1[lim_inf:lim_sup + 1]
        hijo2[lim_inf:lim_sup + 1] = padre2[lim_inf:lim_sup + 1]

        def completar_hijo(hijo, padre1, padre2):
            mapeo = {}
            for i in range(lim_inf, lim_sup + 1):
                mapeo[padre1[i]] = padre2[i]

            for i in range(len(hijo)):
                if hijo[i] == -1:
                    valor = padre2[i]
                    while valor in mapeo:
                        valor = mapeo[valor]
                    hijo[i] = valor

        completar_hijo(hijo1, padre1, padre2)
        completar_hijo(hijo2, padre2, padre1)

        hijos.append(Solucion.Solucion(hijo1))
        hijos.append(Solucion.Solucion(hijo2))

    return hijos
