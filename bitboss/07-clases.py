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
    
        

# ahora le tenemos que pasar los atributos al constructor que hemos especificado antes
mi_personaje = Personaje("BitBoss", 10, 1, 5, 100) # creamos un objeto a partir de la clase Personaje
mi_personaje.atributos() # llamamos a la funcino a traves de la variable mi_personaje

