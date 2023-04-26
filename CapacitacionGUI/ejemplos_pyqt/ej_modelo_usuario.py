class Usuario:
    
    def __init__(self, nombre, apellido, nick, psw):
        self.nombre = nombre
        self.apellido = apellido
        self.nick = nick
        self.psw = psw
        
    def __str__(self) -> str:
        return f"El usuario es: {self.nombre} {self.apellido} ({self.nick} - {self.psw})"