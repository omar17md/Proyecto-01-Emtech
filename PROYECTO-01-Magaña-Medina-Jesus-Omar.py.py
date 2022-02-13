from lifestore_file import lifestore_products, lifestore_sales, lifestore_searches
from funciones import *

"""
Programador: Jesus Omar Magaña Medina
Proyecto 01 - Emtech

CREDENCIALES para LOGIN:
usurio: emtech2022
password: proyecTO-01
"""

usuario, password, intentos, mensaje = "emtech2022", "proyecTO-01", 3, ""

print(f"""{'*' * 10}Bienvenido al sistema de informacion de ventas de LifeStore{'*' * 10}
Por favor ingrese su usario y contraseña""")
while True:
  print(mensaje)
  usuario_login = input('Usuario: ')
  password_login = input('Password: ')

  if usuario == usuario_login and password == password_login:
    print("Login exitoso, accediendo....")
    break
  else:
    intentos -= 1
    if intentos == 0:
      print("Se terminaron los intentos permitidos\nSaliendo...")
      exit()
    else:
      mensaje = f"Usuario o Password incorrectos, intente de nuevo\nIntentos restantes: {intentos}" 


id_ventas, id_busquedas = extraccion_id(lifestore_sales, lifestore_searches) # Se extraen los ID que aparecen en las listas
                                                                             # lifestore_sales y lifestore_searches

id_sin_ventas = {id[0]:[id[1], id[3], 0] for id in lifestore_products if id[0] not in id_ventas} # Se crear un diccionario con ID del producto como llave el nombre, 
                                                                                                 # categoria y 0 de los productos no vendidos.
id_sin_busquedas = {id[0]:[id[1], id[3], 0] for id in lifestore_products if id[0] not in id_busquedas} # Se crear un diccionario con ID del producto como llave el nombre, 
                                                                                                       # categoria y 0 de los productos no buscados.
categorias = set([categoria[3] for categoria in lifestore_products]) # Se crear una lista con las categorias de los productos

###################### PUNTO 1 Productos más vendidos y productos rezagados.
print(f"{'-'* 25}Productos mas vendidos y buscados{'-'* 25}\n")
# Los 5 productos mas vendidos
productos_vendidos = contabilizar_ventas_busquedas(5, id_ventas, "Los 5 productos mas vendidos son:", ['ID','Nombre', 'Cantidad', 'Categoria'])
# Los 10 productos mas buscados
productos_buscados = contabilizar_ventas_busquedas(10, id_busquedas, "Los 10 productos mas buscados son:", ['ID','Nombre', 'Busquedas', 'Categoria'])
print("-" * 80 + "\n")

print(f"{'-'* 25}Productos menos vendidos y buscados por categoria{'-'* 25}\n")
# Se genera un listado con los 5 productos con menores ventas por categoria
contabilizar_por_categoria(5, productos_vendidos, id_sin_ventas, "Los 5 productos menos vendidos de", ["ID", "Nombre", "Cantidad"], categorias)
# Se genera un listado con los 10 productos con menores busquedas por categoria
contabilizar_por_categoria(10, productos_buscados, id_sin_busquedas, "Los 10 productos menos buscados de", ["ID", "Nombre", "Cantidad"], categorias)
print("-" * 80 + "\n")

###################### PUNTO 2 Productos por reseña en el servicio.
print(f"{'-'* 25}Productos mejores y peores calificiados{'-'* 25}\n")
# Los 5 productos con mejores reseñas
promedio_puntuacion(True, "Los 5 productos con mejor reseñas son:", ['ID','Nombre', 'Puntuación', 'Numero de veces calificado'])
# Los 5 productos con peores reseñas
promedio_puntuacion(False, "Los 5 productos con peor reseñas son:", ['ID','Nombre', 'Puntuación', 'Numero de veces calificado'])
print("-" * 80 + "\n")

###################### PUNTO 3 Total de ingresos y ventas promedio mensuales, total anual y meses con más ventas al año.
print(f"{'-'* 25}Ventas por mes y año{'-'* 25}")
# Se calcula las ventas por mes y año
resumen_ventas, ventas_anual = ventas_mes_year()

# Total de ingresos
calcular_venta(id_ventas)

# Ventas por año
venta_year(ventas_anual)

# Ventas por mes
resumen_ventas_meses(resumen_ventas, "Meses con mas ganancias:", ["Mes", "Ganancia", "Ventas", "Promedio de ventas al mes"], 0)
resumen_ventas_meses(resumen_ventas, "Meses con mas ventas:", ["Mes", "Ganancia", "Ventas", "Promedio de ventas al mes"], 1)
resumen_ventas_meses(resumen_ventas, "Ventas promedio por mes:", ["Mes", "Ganancia", "Ventas", "Promedio de ventas al mes"], 2)
print("-" * 80 + "\n")


