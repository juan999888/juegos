class mindy_SC:
    def __init__(self, nombre, vida, mindy_x, mindy_y):
        self.nombre = nombre
        self.vida = vida
        self.mindy_x = mindy_x
        self.mindy_y = mindy_y

    def moverse1(self):
        mindy_x += 10
    def moverse2(self):
        mindy_x -= 10
    def salto(self):
        mindy_y += 10
    def caer(self):
        mindy_y -= 10

    def cvida(self):
        print("Vida: ", self.vida)

mindy = mindy_SC("Mindy", 3, 240, 180)

class boton_SC:
    def __init__(self, color, valor, estado):
        self.color = color
        self.valor = valor
        self.estado = estado