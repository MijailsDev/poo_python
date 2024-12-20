# Encapsulacion


'''
    get_fuerza
    set_fuerza

Ahora no queremos que se pueda cambiar fuerza por un numero
negativo

'''

class Personaje:

    def __init__(self, nombre, fuerza, inteligencia, defensa, vida):   
        self.__nombre = nombre 
        self.__fuerza = fuerza 
        self.__inteligencia = inteligencia
        self.__defensa = defensa
        self.__vida = vida 


    def atributos(self): 
        print(self.__nombre, ":", sep="")
        print(".Fuerza:", self.__fuerza)
        print(".Inteligenicia", self.__inteligencia)

        print(".Defensa", self.__defensa)
        print(".Vida", self.__vida)


    def subir_nivel(self, fuerza, inteligencia, defensa): 
        self.__fuerza = self.__fuerza + fuerza
        self.__inteligencia = self.__inteligencia + inteligencia
        self.__defensa = self.__defensa + defensa


    def esta_vivo(self):    
        return self.__vida > 0 
    

    def __morir(self):
        self.__vida = 0
        print(self.__nombre, "ha muerto")


    def daño(self, enemigo):  
        return self.__fuerza - enemigo.__defensa  


    def atacar(self, enemigo):
        daño = self.daño(enemigo)  
        enemigo.__vida = enemigo.__vida - daño
        print(self.__nombre, "ha realizado", daño, "puntos de daño a", enemigo.__nombre)     

        if enemigo.esta_vivo():
            print("La vida de", enemigo.__nombre, "es", enemigo.__vida)    
        else:   
            enemigo.__morir()

# El Metodo GET devolvera el atributo
    def get_fuerza(self):
        return self.__fuerza
    
# Agregamos una condicion para el numero negativo de fuerza
    def set_fuerza(self, fuerza):
        if fuerza < 0:
            print("Error, has introducido un valor negativo")
        else:
            self.__fuerza = fuerza


mi_personaje = Personaje("BitBoss", 10, 1, 5, 100) 
mi_enemigo = Personaje("Enemy Stando", 8, 5, 3, 5)    

print(mi_personaje.get_fuerza())    # probamos el GET, y nos muestra la fuerza de nuestro personaje
mi_personaje.set_fuerza(-5)         # probamos con un nuemro negativo
mi_personaje.atributos()

'''Realmente el Python todos los Atributos y Metodos son Publicos !!!'''