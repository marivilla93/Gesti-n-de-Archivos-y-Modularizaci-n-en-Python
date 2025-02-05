# Proyecto: [Proyecto]
# Estudiante: [Mariana Villalobos Vargas]
# Fecha de Inicio: [2025/02/04]
# Fecha de Entrega: [2025/02/04]
# Descripción: Este archivo contiene el punto de entrada principal del proyecto.
# Recuerda incluir tu nombre completo, la fecha en la que iniciaste el proyecto y la fecha estimada de entrega.
# Esto ayuda a mantener un registro claro del trabajo realizado.

# Módulo = Archivo
#from analisis_datos.estadisticas import media,calcular_mediana . #Para importar un módulo

from analisis_datos import *

lista_compras=generar_lista_de_compras()
print(lista_compras)

lista_parametro=[5,3,1,2,4]
print('Media:', media(lista_parametro))
print('Mediana:', calcular_mediana(lista_parametro))

#Importar un diccionario


