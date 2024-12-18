class Personaje:
    nombre = "Default"
    fuerza = 0
    inteligenia = 0
    defensa = 0
    vida = 0

mi_personaje = Personaje()
mi_personaje.nombre = "BitBoss"  # tambien podemos modificar los atributos
mi_personaje.fuerza = "10"
print("El nombre del jugador es", mi_personaje.nombre)    # a traves del punto podemos consultar cada uno de los atributos
print("La fuerza del jugador es", mi_personaje.fuerza)


"""
hasta ahora solo hemos usado el metodo constructor vacio por defecto,
para darles valores a los atributos cuando creamos el objeto hace 
falta crear un metodo constructor que reciba sus valores
"""
