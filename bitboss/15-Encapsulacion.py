# Encapsulacion
"""
vamos a impedir que sea accesibles desde fuera de la clase

para ello se usa dos guion bajo delante del Atributo o Metodo
"""


'''
 # nosotros no queremos que queremos que el Metodo morir() se
    use desde fuera de la clase
    es un Metodo que solo queremos que sea gestionado por atacar()
    
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



mi_personaje = Personaje("BitBoss", 10, 1, 5, 100) 
mi_enemigo = Personaje("Enemy Stando", 8, 5, 3, 7)    

#mi_personaje.morir()    # como puedes osbservar NO encuentra el Metodo morir(
#mi_personaje.__morir()     # igual con los 2 guiones bajos
'''no se puede usar externamente'''

mi_personaje.atacar(mi_enemigo)     # Pero si podemos acceder a traves del metodo atacar()
