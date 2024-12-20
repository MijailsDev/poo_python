# Herencia

class Personaje:

    def __init__(self, nombre, fuerza, inteligencia, defensa, vida):   
        self.nombre = nombre 
        self.fuerza = fuerza 
        self.inteligencia = inteligencia
        self.defensa = defensa
        self.vida = vida 


    def atributos(self): 
        print(self.nombre, ":", sep="")
        print(".Fuerza:", self.fuerza)
        print(".Inteligenicia", self.inteligencia)

        print(".Defensa", self.defensa)
        print(".Vida", self.vida)


    def subir_nivel(self, fuerza, inteligencia, defensa): 
        self.fuerza = self.fuerza + fuerza
        self.inteligencia = self.inteligencia + inteligencia
        self.defensa = self.defensa + defensa


    def esta_vivo(self):    
        return self.vida > 0 
    

    def morir(self):
        self.vida = 0
        print(self.nombre, "ha muerto")


    def daño(self, enemigo):  
        return self.fuerza - enemigo.defensa  


    def atacar(self, enemigo):
        daño = self.daño(enemigo)  
        enemigo.vida = enemigo.vida - daño
        print(self.nombre, "ha realizado", daño, "puntos de daño a", enemigo.nombre)     

        if enemigo.esta_vivo():
            print("La vida de", enemigo.nombre, "es", enemigo.vida)    
        else:   
            enemigo.morir()




''' Queremos hacer nuestra clase Guerrero heredando de Personaje
    es facil de hacer:'''   

class Guerrero(Personaje):      # La clase Guerrero va a heredar de la clase Personaje
    pass

guts = Guerrero("Guts", 20, 10, 10, 100)   # Creamos un objeto Guerrero() yu lo guardamos en una variables - y le asignamos sus atributos 

'''Compribamos que podemos acceder a los atributos,
    y podemos usar Metodos como esta_vivo() o atributos()'''
print(guts.nombre)
print(guts.esta_vivo())
print(guts.atributos())


