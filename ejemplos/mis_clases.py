class Carro:

    def __init__(self,cl, mdl, an):
        
        self.color = cl
        self.modelo = mdl
        self.anio = an

    def __str__(self):

        return(f"El auto {self.color} es un {self.modelo} del anio {self.anio}")



class Computador:

    def __init__(self,cl, mdl, prz):
        
        self.color = cl
        self.modelo = mdl
        self.precio = prz
    def __str__(self):

        return(f"La computador {self.color} es una {self.modelo} con un valor de {self.precio}")

# Usted defina el nombre y los atributos
# Puede usar las mismas clases usadas en Java en los ejemplos estudiados


