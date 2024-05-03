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
    df = pandas_3.promedio_notas_asignatura_estudiante()
    lista_nombres = list(df["nombres"])
    lista_promedio = list(df["promedio"])
    plt.bar(x=lista_nombres, height=lista_promedio)
    plt.title("Promedio Notas por Estudiante")
    plt.xlabel("Estudiantes")
    plt.ylabel("Notas")
    plt.show()

mostrar_grafica_notas()