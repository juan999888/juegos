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

    def valvida(self):
        return self.vida > 0

    def cvida(self):
        print("La vida de mindy es: ", self.vida)
    
    def morir(self):
        self.vida = 0

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
    def __init__(self, cant_p, daño):
        self.cant_p = cant_p
        self.daño = daño

    def red_vida(self):
        mindy.vida = mindy.vida - self.daño
        if mindy.valvida():
            print("se le redujo", self.daño, "de vida a", mindy.nombre, "por caer en los pinchos")
        else:
            mindy.morir()
            print(mindy.nombre, "ha muerto al caer en los pinchos")

class liquido_SC:
    def __init__(self, nombrel, color, dañol):
        self.nombrel = nombrel
        self.color = color
        self.dañol = dañol
    
    def red_vidal(self):
        mindy.vida = mindy.vida - self.dañol
        if mindy.valvida():
            print("se le redujo", self.dañol, "de vida a", mindy.nombre, "por caer en", self.nombrel)
        else:
            mindy.morir()
            print(mindy.nombre, "ha muerto por caer en", self.nombrel)


mindy = mindy_SC("Mindy", 3, 240, 180)
pinchos = pinchos_SC(1, 1)
pinchos.red_vida()
mindy.cvida()
lava = liquido_SC("Lava","rojo", 3)
lava.red_vidal()
mindy.cvida()
