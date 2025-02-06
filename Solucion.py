import random as rnd

# vector binario 0, 1 .... n
class Solucion:
    def __init__(self, n):
        self.solucion = []
        self.vo = -1;

        for i in range(n):
            self.solucion.append(rnd.randint(0,1))

    def calcVo(self):
        self.vo = sum(self.solucion)


if __name__ == "__main__":
    solucion = Solucion(5)
    solucion.calcVo()
    print(str(solucion.solucion))
    print("vo : " , solucion.vo)
