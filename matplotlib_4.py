import matplotlib.pyplot as plt

import pandas_3


"""
    Basándote en el DataFrame creado, realiza un análisis visual de las 
    calificaciones de los estudiantes en las diferentes asignaturas. 
    Utiliza un gráfico de barras donde el eje x represente los nombres 
    de los estudiantes y el eje y represente las calificaciones
    obtenidas en cada asignatura.
"""
def mostrar_grafica_notas():
    """
    Función muestra un gráfico de barra con los alumnos en el eje de las axisas y
    los promedios de las notas en el eje de las ordenadas.
    """

    #creo un DataFrame a partir la función del ejercicio 3
    df = pandas_3.promedio_notas_asignatura_estudiante()

    #creo dos listas con los nombres y los promedios de las notas.
    lista_nombres = list(df["nombres"])
    lista_promedio = list(df["promedio"])

    # creo el gráfico con los datos.
    plt.bar(x=lista_nombres, height=lista_promedio)
    plt.title("Promedio Notas por Estudiante")
    plt.xlabel("Estudiantes")
    plt.ylabel("Notas")

    # mostrar el gráfico creado anteriormente.
    plt.show()

# ejecuto la función.
mostrar_grafica_notas()