# Encapsulacion
"""
vamos a impedir que sea accesibles desde fuera de la clase

para ello se usa dos guion bajo delante del Atributo o Metodo
"""


'''
 # nosotros no queremos que nos Atributos sean accesibles directamente,
    esto implicara cambiarlo en toda la clase,
    por lo cual es importante saber cuales van a ser privadas antes de empezar
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
    

    def morir(self):
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
            enemigo.morir()



mi_personaje = Personaje("BitBoss", 10, 1, 5, 100) 
mi_enemigo = Personaje("Enemy Stando", 8, 5, 3, 7)    

#print(mi_personaje.fuerza)  # vemos que ya no se puede acceder a Fuerza
#print(mi_personaje.__fuerza)  # no se puede acceder ni con doble guion bajo

mi_personaje.__fuerza = 0   # tampoco se puede modificar - aunque no nos muestre error
mi_personaje.atributos()    # los metodos al ser funciones dentro de la clase, si tienen acceso a los atributos