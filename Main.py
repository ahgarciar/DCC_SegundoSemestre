
import Solucion as claseSolucion

#algoritmo genetico:
#   POBLACION -> CONJUNTO DE SOLUCIONES INICIALES QUE SE IRAN MEJORANDO
#   CONFORME AVANZAN LAS GENERACIONES

#PASOS:
#   1.- GENERACIONDE LA POBLACION INICIAL
#   2.- CALCULAR LA FUNCION OBJETIVO DE LA POBLACION
#   3.- SELELECCIONAR INDIVIDUOS QUE PODRAN REPRODUCIRSE (CRUZARSE)
#   4.- REALIZAR EL CRUZAMIENTO (REPRODUCCION)
#   5.- MUTACION DE LOS INDIVIUDUSO NUEVOS
#   6.- CALCULAR LA FUNCION OBJETIVO DE LOS NUEVOS INDIVIDUOS
#   7.- SELECCION AMBIENTAL (QUEDARSE CON LOS MAS APTOS) ENTRE POBLACION E INDIVIDUOS NUEVOS
#   8.- SI NO SE ALCANZA EL CRITERIO DE PARO SE REGRESA AL PASO 3
#   9.- SI SE LOGRA EL CRITERIO DE PARO, ENTONCES, SE TERMINA EL ALGORITMO
#   10.- SE DEVUELVE EL MEJOR INDIVIDUO

#
#SELECCION ...
#       1.- TORNEO BINARIO
#       2.- RULETA  <--- DIVERSIDAD...!

#POBLACION
#
# ID1 -> VO +   ej: 2 +      proporcion -> 1/6
# ID2 -> VO +       3 +                    1/4
# ID3 -> VO +       2 +                    1/6
# ID4 -> VO +       4 +                    1/3
# ID5 -> VO +       1 +                    1/12
#  ________________= 12

###  -> generamos un numero aleatorio entre 0 y 1 ---->  0.65

#valor = 0.65
# ID1 ->  0.65-1/6 =   0.28
# ID2 -> 0.28 - 1/4 =  0.03
# ID3 -> 0.03 - 1/6  ###   <= 0   ->>>se selecciona al individuo 3 como padre
# ID4 -> 1/3
# ID5 -> 1/12


if __name__ == "__main__":
    poblacion = []
    tam_poblacion  = 10
    n = 5

    #Genera poblacion inicial
    for i in range(tam_poblacion):
        poblacion.append(claseSolucion.Solucion(n))
    #Calcula funcion objetivo
    for solucion in poblacion:
        solucion.calcVo()
    #Imprime poblacion:
    for solucion in poblacion:
        print(str(solucion.solucion), end= " -> ")
        print("vo : ", solucion.vo)

    print()



