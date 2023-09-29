class mindy_SC:
    def __init__(self, nombre, vida, mindy_x, mindy_y):
        self.nombre = nombre
        self.vida = vida
        self.mindy_x = mindy_x
        self.mindy_y = mindy_y

    def moverse1(self):
        self.mindy_x += 10
    def moverse2(self):
        self.mindy_x -= 10
    def salto(self):
        self.mindy_y += 10
    def caer(self):
        self.mindy_y -= 10

    def cvida(self):
        print("Vida: ", self.vida)

mindy = mindy_SC("Mindy", 3, 240, 180)

class boton_SC:
    def __init__(self, texture, valor, estado):
        self.texture = texture
        self.valor = valor
        self.estado = estado
    def presionar(self):
        self.estado = 1
        print(self.estado)
        if self.estado == 1:
            self.estado = 0

class pinchos_SC:
    def __init__(self, cant_p):
        self.cant_p = cant_p
