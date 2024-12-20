# Herencia
'''Nuestro objetivo es aprovechar la herencia y ampliar nuestra clase 
    Guerrero con un atributo nuevo (el bono de daño de la espada)
    para ello nuestro constructor debe recibir un argumento mas'''


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



#   Tenemos que sobreescribir el Metodo __init__ heredado de Personaje
class Guerrero(Personaje):      
    def __init__(self, nombre, fuerza, inteligencia, defensa, vida, espada):
        super().__init__(nombre, fuerza, inteligencia, defensa, vida)        # Escribir super(). llamamos al metodo constructor, NO HACE FALTA AÑADIR SELF, digitamos sus atributos



# Aqui vamos a agregar un argumentos mas :
guts = Guerrero("Guts", 20, 10, 10, 100, 5)   # Creamos un objeto Guerrero() yu lo guardamos en una variables - y le asignamos sus atributos 

"""guts.atributos()    # esto no funcionara porque todavia no hemos inicializado los atributos heredados
                        # Podemos usar la funcion integrada super(), 
                        #
                        #       Esta funcion nos permite llamar a los Atributos y Metodos
                        #       de la super clase sin tener que escribirla directamente :)
                        #
                        #       Esto es util, por ejemplo si cambias el nombre de la superclase 
                        #       no tienes que preocuparte por cambiarlo tambien dentro del codigo

"""
guts.atributos()    # Funciona correctamente con la funcion super()  :)