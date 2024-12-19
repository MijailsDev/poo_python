# Abstraccion
# Metodo constructor que reciba sus valores

class Personaje:

    def __init__(self, nombre, fuerza, inteligencia, defensa, vida):   # los atributos que usemos para inicializar el objeto
        self.nombre = nombre # nuestro objetivo es cambiar el nombre de la clase por el nombre que recibe del constructor
        self.fuerza = fuerza # lo mismo con la fuerza
        self.inteligencia = inteligencia
        self.defensa = defensa
        self.vida = vida 

# Metodo que nos muestre el listado del objeto(el valor de sus atributos)
    def atributos(self): # como se va a encargar de mostrar los atributos, solo necesita el self para poder tener acceso a ellos
        print(self.nombre, ":", sep="")
        print(".Fuerza:", self.fuerza)
        print(".Inteligenicia", self.inteligencia)
        print(".Defensa", self.defensa)
        print(".Vida", self.vida)

# Metodo para poder subir de nivel a nuestro personaje, sumandole estadisticas nuevas a las actuales         
    def subir_nivel(self, fuerza, inteligencia, defensa): # self para poder modificar los atributos
        self.fuerza = self.fuerza + fuerza
        self.inteligencia = self.inteligencia + inteligencia
        self.defensa = self.defensa + defensa

# Metodo para saber si el personaje esta vivo o no
    def esta_vivo(self):    # Este metodo nos devuelve un valor booleano
        return self.vida > 0 # comprueba si la vida es mayor que cero, True o False
    
# Metodo que representa la accion de morir del Personaje    - si su vida == 0 --> esta muerto
    def morir(self):
        self.vida = 0
        print(self.nombre, "ha muerto")

# ahora le tenemos que pasar los atributos al constructor que hemos especificado antes
mi_personaje = Personaje("BitBoss", 10, 1, 5, 100) 
mi_personaje.morir()    # llamamos al metodo morir
mi_personaje.atributos()    # mostramos los atributos actuales

