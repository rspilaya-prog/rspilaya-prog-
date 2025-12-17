class Ave:
    def volar(self):
        print("El ave vuela")

class Pinguino(Ave):
    def volar(self):
        print("El pingüino no vuela")

def hacer_volar(ave):
    ave.volar()

ave = Ave()
pinguino = Pinguino()

hacer_volar(ave)
hacer_volar(pinguino)
