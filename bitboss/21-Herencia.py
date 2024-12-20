# Herencia
'''Crear un Atributo nuevo para la espada'''


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



class Guerrero(Personaje):    

    def __init__(self, nombre, fuerza, inteligencia, defensa, vida, espada):
        super().__init__(nombre, fuerza, inteligencia, defensa, vida)        # Escribir super(). llamamos al metodo constructor, NO HACE FALTA AÑADIR SELF, digitamos sus atributos
        self.espada = espada    # creamos nuevo Atributo nuevo para la espada y asignarle el argumento correspondiente -  lo llamamos a traves del objeto 



# Aqui vamos a agregar un argumentos mas :
guts = Guerrero("Guts", 20, 10, 10, 100, 5)   # Creamos un objeto Guerrero() yu lo guardamos en una variables - y le asignamos sus atributos 

guts.atributos()
print(guts.espada)      # comprobamos el valor de la espada
