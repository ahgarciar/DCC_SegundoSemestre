
class Solucion:
    def __init__(self, camino=None, val_obj=0.0):
        self.camino = camino if camino is not None else []
        self.val_obj = val_obj

    def get_camino(self):
        return self.camino

    def get_val_obj(self):
        return self.val_obj

    def set_camino(self, camino):
        self.camino = camino

    def set_val_obj(self, val_obj):
        self.val_obj = val_obj

    def __hash__(self):
        return hash(self.val_obj)

    def __eq__(self, other):
        if not isinstance(other, Solucion):
            return False
        return self.val_obj == other.val_obj

    def __lt__(self, other):
        return self.val_obj < other.val_obj

    def __le__(self, other):
        return self.val_obj <= other.val_obj

    def __gt__(self, other):
        return self.val_obj > other.val_obj

    def __ge__(self, other):
        return self.val_obj >= other.val_obj
