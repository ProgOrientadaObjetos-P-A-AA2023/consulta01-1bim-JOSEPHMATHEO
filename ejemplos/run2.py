from mis_clases import Computador

# Crear dos objetos de la clase 02

# objeto 01

# crear

# Presentar objeto; usar el método __st__

miComputador = Computador("Azul","HP",round(1500.500,2))

print(miComputador)

# objeto 02

# crear ingresando valores por teclado

# Presentar objeto; usar el método __st__

color = input(("Ingrese el color de la computadora: "))
modelo = input(("Ingrese el modelo de la computadora: "))
valor = float(input(("Ingrese el valor de la computadora: ")))

miComputador2 = Computador(color,modelo,valor)

print(miComputador2)
