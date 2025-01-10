# -*- coding: utf-8 -*-
"""Untitled0.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/11yFJPuBs7sbd7MUthBaxhhw0C5kdiHQS
"""

import pandas as pd

data = {
    'termino': ['Estadistica', 'dato', 'Tema de conjuntos', 'Axiomas', 'probabilidad', 'probabilidad'],
    '¿Que se?': ['es la rama matematica que nos permite saber si algo puede llegar a pasar', 'es el conjunto de inofrmacion', 'Son familias que pertenecen a mas familias', 'conjunto de valores predominantes', 'Capacidad de de ver mas haya para calcular el que pasara', 'cosas que ocurren'],
    '¿que deseo aprender?': ['Poder analisar de manera correcta los datos', 'saber como utilizar los datos completamente a mi favor', 'entender mas el teorema de los conjuntos', 'entender realmente que es son los axiomas', 'saber analizar las probabilidades para una mejor toma de desision', 'Poder predecir eventos para tener una mejor preparacion'],
    '¿que aprendí?': [""] * 6
}

tabla = pd.DataFrame(data)

# Ask the user if they want to fill in the "¿que aprendí?" column
fill_aprendi = input("¿Desea llenar la columna '¿que aprendí?' ahora? (si/no): ").lower()

if fill_aprendi == "si":
    for index in range(len(tabla)):
        # Prompt the user for each row
        aprendizaje = input(f"¿Qué aprendió sobre '{tabla['termino'][index]}'? ")
        tabla.loc[index, '¿que aprendí?'] = aprendizaje

print(tabla)

nota = 'En el transcurso de la materia me gustaria ser capaz de realizar las tablas por mi cuenta y no utilizar IA y corregir lo poco que evita que se ejecute la el codigo'
print(nota)

"""Estadististica, es una herramienta que se encarga de la recoleccion y organizacion de los datos.
Se utilizan para ver patrones y relaciones entre ellos.

es proporcionar herramientas para tomar la mejor desicion.

la estadistica se vierte atraves de dos ramas, descriptiva e inferencial

descriptiva, utiliza herramientas para poder describir los datos, utiliza herramientas como medidas centrales, disperciones, grafico.

las metricas nos advierten sobre cuellos de botellas.

estadistica inferencial: es la rama que nos permite ver el comportamiento sobre unoversos, esta en base en la posibilidad, probabilidad, muestreo, Hipotesis.

probabilidad es la rama que nos permite analizar el comportamiento sobre algun evento, o universo.

muestreo sacamos ciertas caracteristicas, las  cuales nos ayudan a realizar una hipotesis.

aplicaciones de 4 areas especificas

-investigacion cientifica
-medicina
-economia
-ciencia social

lso videojuegos como los sims estan basados en estadistica para su modelo de sociedad.

es una herramienta esencial para comprender el mundo que nos rodea, nos ayuda a ver las cosas que normalmente no vemos.

los superiores no tienen normalmente conocimientos tecnicos

pasos a seguir un analisis estadisticos:

1=recoleccion y organizacion de la inforacion n
2=el calculo de medidas descriptivas (se busca resumir esos datos)
3=Presentacion de los datos (se presenta de manera visual y de manera atractiva)
4=Identiicacion de patrones y relaciones

tencia centra, puntos centricos de la data (datos)
-media
.moda
-mediana
-media geometrica

Medidas de Dispersion
-Rango
-varianza
-Desviacion est.

Posicionamiento
Deciles
Cuartides
Percentiles (porcentaje)

--------------------------estadistica Inferencial-------------------------------

es la rama de la estadistica que se encarga de sacar concluciones apartir de muestras.

Utiliza metodos probalilistico basado en los eventos ocurridos en los universos

pasos a seguir

1=estimacion de parametro
2=Congetura de hipotesis y su prueba
3=Intervalos de confianza
4=Modelado estadistico

-----------------------------------Actividad------------------------------------

area: rendimiento de un sistema
 buscamos rendimiento y evitar los cuellos de botella

 Comenzamos con el analisis en el rendimiento del sistema, comparando el proceso y actual, con el proceso obtenido anteriormente, para obtener una media del mismo, abriendo posibilidad de observar un cuello de botella.

 Los datos mas importantes que podemos analizar en este caso, son:

 -el rendimiento anterior y el actual
 -mapeo de procesos
 -analisis de tiempo en procesos
 -procesos en primer y sengudo plano
 -carga de estres y limite de usuarios




"""