"""
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
    
    def daño(self, enemigo):
        return self.fuerza - enemigo.fuerza
    

mi_personaje = Personaje("BitBoss", 10, 1, 5, 100)
mi_enemigo = Personaje("Enemy Stando", 8, 5, 3, 100)

mi_personaje.daño(mi_enemigo)

#
"""
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

    
    def esta_vivo(self):    # Este metodo nos devuelve un valor booleano
        return self.vida > 0 # comprueba si la vida es mayor que cero, True o False
    
    def morir(self):
        self.vida = 0
        print(self.nombre, "ha muerto")

    def daño(self, enemigo):  # el daño que recibe nuestro Personaje, y al otro personaje que llamaremos enemigo
        return self.fuerza - enemigo.defensa        

    def atacar(self, enemigo):
        daño = self.daño(enemigo)   # calculamos el daño
        enemigo.vida = enemigo.vida - daño
        print(self.nombre, "ha realizado", daño, "puntos de daño a", enemigo.nombre)     # informacion de la accion
        
        if enemigo.esta_vivo():
            print("La vida de", enemigo.nombre, "es", enemigo.vida)    # vida actual del enemigo
        else:   # entonces si la vida es diferente de cero hara lo siguiente :
            enemigo.morir()



# ahora le tenemos que pasar los atributos al constructor que hemos especificado antes
mi_personaje = Personaje("BitBoss", 10, 20, 50, 1000) # creamos un objeto a partir de la clase Personaje
mi_personaje.atributos() # llamamos a la funcino a traves de la variable mi_personaje
#mi_personaje.subir_nivel(1, 2, 0)   # subimos de nivel al personaje
mi_personaje.atributos()    # volvemos a mostrar los atributos

mi_enemigo = Personaje(
                        "Black Hat",  # Nombre
                         10,           # Fuerza
                         10,           # Inteligencia
                         3,            # Defensa
                         100)           # Vida
mi_enemigo.atributos()
#mi_enemigo.subir_nivel(50, 40, 10)
mi_enemigo.atributos()


mi_personaje.esta_vivo() # nos devuelve un true o un false
print(mi_personaje.esta_vivo())

mi_enemigo.esta_vivo()
print(mi_enemigo.esta_vivo())


# mi_personaje.morir()    # llamamos al metodo morir
# mi_personaje.atributos()    # mostramos los atributos actuales

# mi_enemigo.morir()
# mi_enemigo.atributos()

mi_personaje.daño(mi_enemigo)
print(mi_personaje.daño(mi_enemigo)) 



mi_personaje.atacar(mi_enemigo)
mi_enemigo.atributos()