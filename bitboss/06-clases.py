# Metodo constructor que reciba sus valores

class Personaje:

    def __init__(self, nombre, fuerza, inteligencia, defensa, vida):   # los atributos que usemos para inicializar el objeto
        self.nombre = nombre # nuestro objetivo es cambiar el nombre de la clase por el nombre que recibe del constructor
        self.fuerza = fuerza # lo mismo con la fuerza
        self.inteligenia = inteligencia
        self.defensa = defensa
        self.vida = vida 

# ahora le tenemos que pasar los atributos al constructor que hemos especificado antes
mi_personaje = Personaje("BitBoss", 10, 1, 5, 100) # creamos un objeto a partir de la clase Personaje
print("El nombre del jugador es", mi_personaje.nombre)    # a traves del punto podemos consultar cada uno de los atributos
print("La fuerza del jugador es", mi_personaje.fuerza)
