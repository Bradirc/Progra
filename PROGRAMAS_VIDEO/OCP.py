class Notificador:
    def __init__(self, usuario,mensaje):
        self.usuario = usuario
        self.mensaje = mensaje

    def notificar(self):
        raise NotImplementedError
    
class NotificadorEmail(Notificador):
    def Notificar(self):
        print(f"Enviado mensaje por mail a{self.usuario.email}")


class NotificadorSMS(Notificador):
    def Notificar(self):
        print(f"Enviado SMS a {self.usuario.sms}")

class NotificadorWhatsApp(Notificador):
    def Notificar(self):
        print(f"Enviado whatsapp a {self.usuario.whatsapp}")
        
        