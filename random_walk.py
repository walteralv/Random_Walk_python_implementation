import random as random
#instalar la libreria bokeh en caso de no tenerla
from bokeh.plotting import figure, output_file, show

#funcion de movimiento
def Move(steps):
    move = random.choice([-1, 1]) #decide moverse aletoriamente dependiendo del eje esignado
    last = len(steps)
    delta = steps[last-1] + move #variacion 
    steps.append(delta)
    return steps

#funcion para igualar listas
def equal_array(steps):
    last = len(steps)
    steps.append(steps[last-1])
    return steps

# funcion Principal
def random_direction(steps_x, steps_y, num):
    for i in range(num):
        direc = random.choice([-1,1])
        if direc == -1: #se mueve en el eje x
            steps_x = Move(steps_x)
            steps_y = equal_array(steps_y)
        else: #se mueve en el eje y 
            steps_y = Move(steps_y)
            steps_x = equal_array(steps_x)
    return steps_x, steps_y

if __name__ == "__main__":
    
    # Inicializa las listas 
    steps_x = [0]
    steps_y = [0]

    # Inicio del programa: ingresa la cantidad de steps(pasos) mediante consola
    num = int(input('Numero de steps aleatorios: '))
    random_direction(steps_x, steps_y, num)

    #plotting
    output_file("random_walk.html")
    plot = figure(plot_width=1000, plot_height=600)
    plot.line(steps_x, steps_y, line_width=2)
    show(plot)