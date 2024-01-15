#class Ave:
#    def volr(self):
#        return "estoy volando"
    
#class Pinguino(Ave):
#    def volar(self):
#        return "no puedo volar"
    
#def hacer_volar(ave = Ave):
#    return ave.volar()

#print(hacer_volar(Pinguino()))

class Ave:
    pass

class AveVoladdora(Ave):
    def volar(self):
        return"estoy volando"

class AveNoVoladdora(Ave):
    pass