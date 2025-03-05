import random
import Solucion

rnd = random.Random(3)

def torneo_binario(poblacion, total_padres):
    padres = []

    for _ in range(total_padres):
        indice1 = rnd.randint(0, len(poblacion) - 1)

        # Asegurar que indice2 sea diferente de indice1
        indice2 = indice1
        while indice2 == indice1:
            indice2 = rnd.randint(0, len(poblacion) - 1)

        P1 = poblacion[indice1]
        P2 = poblacion[indice2]

        if P1.get_val_obj() < P2.get_val_obj():
            padres.append(Solucion.Solucion(P1.get_camino(), P1.get_val_obj()))
        else:
            padres.append(Solucion.Solucion(P2.get_camino(), P2.get_val_obj()))

    return padres
