class Notificador:
    def __init__(self, usuario, nombre):
        self.usuario = usuario
        self.nombre = nombre
    
    def notificar(seld):
        raise NotImplementedError
    
class NotificadorEmail(Notificador):
    def notificar (self):
        print(f'Enviando mensaje por E-MAIL a {self.usuario.email}')
        

class NotificadorSMS(Notificador):
    def notificar (self):
        print(f'Enviando mensaje por E-MAIL a {self.usuario.sms}')