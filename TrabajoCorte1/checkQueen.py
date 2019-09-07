
x_axis_positions = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8}


while True:
    print("Ingrese la posición X de la reina (valores válidos: a, b, c, d, e, f, g, h):")
    x_axis = input()
    if x_axis in x_axis_positions:
        break
    else:
        print("Posición X inválida")


while True:
    print("Ingrese la posición X de la reina (valores válidos: 1, 2, 3, 4, 5, 6, 7, 8):")

   
    try:
        y_axis = int(input())
    except ValueError:
        print("Posición Y inválida")
    else:
        if 1 <= y_axis <= 8:
            break  
        else:
            print("Posición Y inválida")



def get_position(position1, edge1, position2=0, edge2=0):
    """Determina la cantidad de espacios disponibles a partir de la posición y el filo"""
    
    if edge2 != 0 and position2 != 0:
       
        return min(abs(position1 - edge1), abs(position2 - edge2))
    else:
       
        return abs(position1 - edge1)

print("Posiciones recibidas: " + x_axis + "X, " + str(y_axis) + "y")


print("Posiciones a la derecha: " + str(get_position(x_axis_positions[x_axis], 8)))
print("Posiciones a la izquierda: " + str(get_position(x_axis_positions[x_axis], 1)))
print("Posiciones hacia arriba: " + str(get_position(y_axis, 8)))
print("Posiciones hacia abajo: " + str(get_position(y_axis, 1)))


print("Posiciones diagonal derecha hacia arriba: " + str(get_position(y_axis, 8, x_axis_positions[x_axis], 8)))
print("Posiciones diagonal izquierda hacia arriba: " + str(get_position(y_axis, 8, x_axis_positions[x_axis], 1)))
print("Posiciones diagonal derecha hacia abajo: " + str(get_position(y_axis, 1, x_axis_positions[x_axis], 8)))
print("Posiciones diagonal izquierda hacia abajo: " + str(get_position(y_axis, 1, x_axis_positions[x_axis], 1)))

#Edwin García - Mauricio Pantoja