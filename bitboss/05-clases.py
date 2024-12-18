# Metodo constructor que reciba sus valores

class Personaje:
    """
        Mirar la linea 22:
        Al implementar el metodo constructor estamos declarando con self
        que atributos del objeto se va a iniciañizar al momento de crearse,
        por lo que no es necesario al princiío de la clase (asi que lo vamos 
        a eliminar - en mi caso solo lo voy a comentar)
        
        nombre = "Default"
        fuerza = 0
        inteligenia = 0
        defensa = 0
        vida = 0
    """
    
    # Esta es la forma de declarar un constructor con argumentos
    """ self es un argumento que hace referencia asi mismo al objeto,
        y permite a traves del punto tener acceso a los atributos y 
        metodos de la clase"""
    def __init__(self, nombre, fuerza, inteligencia, defensa, vida):   # los atributos que usemos para inicializar el objeto
        self.nombre = nombre # nuestro objetivo es cambiar el nombre de la clase por el nombre que recibe del constructor
        self.fuerza = fuerza # lo mismo con la fuerza
        self.inteligenia = inteligencia
        self.defensa = defensa
        self.vida = vida 

# ahora le tenemos que pasar los atributos al constructor que hemos especificado antes
mi_personaje = Personaje("BitBoss", 10, 1, 5, 100)
print("El nombre del jugador es", mi_personaje.nombre)    # a traves del punto podemos consultar cada uno de los atributos
print("La fuerza del jugador es", mi_personaje.fuerza)
