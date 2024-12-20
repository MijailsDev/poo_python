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

# Metodo que calcule el daño de nuestro Personaje a otro Personaje
    def daño(self, enemigo):  # el daño que recibe nuestro Personaje, y al otro personaje que llamaremos enemigo
        return self.fuerza - enemigo.defensa  # vamos a devolver el daño realizado de una forma muy simple

# Metodo atacar, se encargara de calcular el daño y modificar la vida del enemigo con ese daño 
    def atacar(self, enemigo):
        daño = self.daño(enemigo)   # calculamos el daño
        enemigo.vida = enemigo.vida - daño
        print(self.nombre, "ha realizado", daño, "puntos de daño a", enemigo.nombre)     # informacion de la accion
        print("La vida de", enemigo.nombre, "es", enemigo.vida)    # vida actual del enemigo


# ahora le tenemos que pasar los atributos al constructor que hemos especificado antes
mi_personaje = Personaje("BitBoss", 10, 1, 5, 100) 
mi_enemigo = Personaje("Enemy Stando", 8, 5, 3, 100)    # creamos un personaje que representa al enemigo 
mi_personaje.atacar(mi_enemigo)
mi_enemigo.atributos()  # mostramos la vida actual despues de recibir el ataque


"""
________________
Notas Importanes|
________________|
    
    Acerca de esta linea -> daño = self.daño(enemigo)

El self no es redundante, porque está haciendo un trabajo muy importante en la llamada al método. 
Te explico paso a paso por qué:

1.El uso del self dentro de un método: En una clase, el self es una convención que se utiliza 
  para referirse al objeto actual que está ejecutando el código. Cuando llamas a un método 
  dentro de la misma clase, necesitas usar self para hacer referencia a ese objeto.
  
2.El self dentro del método daño: Dentro del método daño, tienes la siguiente línea:
    return self.fuerza - enemigo.defensa
    
  Aquí, el self está accediendo a los atributos del objeto que invoca el método. Es decir, el 
  self.fuerza es la fuerza del personaje atacante (el objeto actual). Así que, dentro del método,
  el self se usa para acceder a las propiedades del personaje que está atacando.

3.Por qué necesitamos self.daño(enemigo) fuera del método?: La razón por la que usamos 
  self cuando llamamos a daño dentro del método atacar es porque estamos llamando al método
  de la clase desde un objeto. Entonces, necesitamos especificar a qué objeto de la clase
  estamos llamando el método daño. Sin el self, Python no sabría a qué objeto pertenece el 
  método daño.  
    * self.daño(enemigo): Aquí, self indica que estamos llamando al método daño en el 
      objeto actual (el que está realizando el ataque).
    * El parámetro enemigo es el objeto del enemigo que pasamos para calcular el daño.
"""