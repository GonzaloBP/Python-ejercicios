class Usuario(object):
    """Modela un simple usuario"""

    def __init__(self, nombre, apellido, nombre_usuario, email, sexo, pais, edad):
        self.nombre = nombre
        self.apellido = apellido
        self.nombre_usuario = nombre_usuario
        self.email = email
        self.sexo = sexo
        self.pais = pais
        self.edad = edad

    def describir_usuario(self):
        print("Nombre de usuario: ", self.nombre_usuario)
        print("Nombre:", self.nombre, self.apellido)
        print("Email:", self.email)
        print("Sexo:", self.sexo)
        print("Pais de origen:", self.pais)
        print("Edad:", self.edad)

    def bienvenido_user(self):
        print("Un gusto de verte de vuelta por aqui:", self.nombre_usuario)