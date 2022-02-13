from lifestore_file import lifestore_products, lifestore_sales, lifestore_searches

def contabilizar_ventas_busquedas(top, lista_id, titulo, columnas):
  """Contabiliza el mayor numero de ventas o busquedas por ID, se calcula busquedas o ventas 
  dependiendo de la lista pasada por parametro.

  Args:
    top(int): Indica resultados se van a imprimir en pantalla.
    lista_id(list): Puede contener los ID de los productos que se encuentran en la lista lifestore_sales
                    o los ID de la lista lifestore_searches.
    titulo(string): Es el titulo que se va a imprimir de los resultados.
    columnas(list): Son el nombre de las columnas de cada resultado.

  return:
    Retorna un diccionario con ID del producto como llave y como valor una lista
    que contiene el nombre, categoria y la cantidad de veces que se vendio o busco el producto.
  """

  id_contabilizados = dict(zip(lista_id,map(lambda x: lista_id.count(x),lista_id)))    # Crea un diccionario con ID como llave y como valor el numero de veces que vendio o busco ese producto
  resultado = sorted(id_contabilizados.items(), key=lambda x: x[1], reverse=True)      # Ordena los resultados de mayor a menos dependiendo el valor de cada llave del diccionario.

  info_contabilizados = {id[0]:[info[1], info[3], id[1]] for id in resultado for info in lifestore_products if id[0] == info[0]} # Crea un diccionario con ID del producto como llave y de valor una lista
                                                                                                                                 # que contiene el nombre, categoria y veces que se vendio o busco el producto.
  print(titulo)   # Imprime el titulo
  print("{:<6} {:<6} {:<15} {:<10} {:<10}".format('', columnas[0], columnas[1], columnas[2], columnas[3])) # Imprime el nombre de las columnas

  for num, id in enumerate(resultado[:top]):
    print("{:<6} {:<6} {:<15} {:<10} {:<10}".format(num + 1, id[0], info_contabilizados[id[0]][0][:15], id[1], info_contabilizados[id[0]][1])) # Se imprimen los resultados
  print("\n")

  return info_contabilizados

def extraccion_id(lista_1, lsita_2):
  """Extrae los ID de las listas lifestore_sales y lifestore_searches
  """
  return [id[1] for id in lista_1 if id[4] == 0], [id[1] for id in lsita_2]

def contabilizar_por_categoria(top, dicc_1, dicc_2, titulo, columnas, categorias):
  """Contabiliza el menor numero de ventas o busquedas de cada producto por categoria, se calcula busquedas o ventas 
  dependiendo de la lista pasada por parametro.

  Args:
    top(int): Indica resultados se van a imprimir en pantalla.
    dicc_1(dict): Puede contener los ID como llave de los productos que se encuentran en la lista lifestore_sales
                  o los ID de la lista lifestore_searches, y como valor el numero de ventas o busquedas de ese ID.
    dicc_2(dict): Puede contener los ID como llave de los productos que no encuentran en la lista lifestore_sales
                  o los ID que no estan en la lista lifestore_searches, y como valor el numero de ventas o busquedas de ese ID.
    titulo(string): Es el titulo que se va a imprimir de los resultados.
    columnas(list): Son el nombre de las columnas de cada resultado.
    categorias(list): Contiene las categorias de los productos.
  """

  resultado = {**dicc_1, **dicc_2} # Se unen los dos diccionarios en uno solo
  id_ordenados = sorted(resultado.items(), key=lambda x: x[1][2], reverse=False) # Se ordena el diccionario de menor a mayor con base a su ventas o busquedas.
  temporal_productos = []  # Almacena de manera temporal los productos encontrados de la categoria actual
  for categoria in categorias:
    for id in id_ordenados:
      if id[1][1] == categoria: # Si la categoria del actual producto coicide se agrega a temporal_productos
        temporal_productos.append(id)
        if len(temporal_productos) == top: # Si ya se encontraron los primeros (top) productos se detiene el segundo for
          break

    print(f"{titulo} {categoria.upper()}:") # Se imprime el titulo y columnas
    print("{:<6} {:<6} {:<33} {:<10}".format('', columnas[0], columnas[1], columnas[2]))

    for num, id in enumerate(temporal_productos):
      print("{:<6} {:<6} {:<33} {:<10}".format(num + 1, id[0], id[1][0][:30], id[1][2])) # Se imprime los resultados
    print("\n") 

    temporal_productos = [] # Se incializa la lista
    
    
def promedio_puntuacion(orden, titulo, columnas):
  """Se calcula cuales son los productos con mejor reseña o peor, calculando el promedio
  de las reseñas y las veces que se califico.

  Args:
    order(bool): Indica como se va a ordenar el diccionario.
    titulo(string): Es el titulo que se va a imprimir de los resultados.
    columnas(list): Son el nombre de las columnas de cada resultado.
  """

  resenas = {} # Guarda como llave el ID del producto y como valor la reseña.
  for venta in lifestore_sales:
    if venta[1] not in resenas:
      resenas[venta[1]] = [venta[2]]
    resenas[venta[1]].append(venta[2])
  

  resenas_promedio = {key:[sum(resenas[key])/len(resenas[key]), len(resenas[key])] for key in resenas } # Se crea un diccionario con ID del producto como llave y 
                                                                                                        # como valor el promedio de las reseñas de producto y cuantas veces se califico.

  resultado = sorted(resenas_promedio.items(), key=lambda x: x[1][0]+x[1][1], reverse=orden)[:6] # Se ordena el diccionario con base a la suma del promedio y la cantidad de veces calificado.

  info_resenas = {id[0]:info[1] for id in resultado for info in lifestore_products if id[0] == info[0]} # Se obtiene el nombre de los productos.
 
  print(titulo)  # Se imprime el titulo y columnas
  print("{:<6} {:<6} {:<15} {:<10} {:<10}".format('', columnas[0], columnas[1], columnas[2], columnas[3]))

  for num, id in zip(range(1,6), resultado): # Se imprimen los resultados
    print("{:<6} {:<6} {:<15} {:<10} {:<10}".format(num, id[0], info_resenas[id[0]][:15], round(id[1][0],2), id[1][1]))
  print("\n") 
  
  
def calcular_venta(lista_id):
  """Se calcula el total de ingresos en base a las ventas realizadas

  Args:
    lista_id(list): Lista que contiene los ID de los productos vendidos.
  """

  id_contabilizados = dict(zip(lista_id,map(lambda x: lista_id.count(x),lista_id))) # Se contabiliza las ventas de cada producto
  # Se multiplica el numero de ventas de cada producto por su precio, al final se suma todo.
  total_ingtresos = sum([info[2] * id_contabilizados[id] for id in id_contabilizados for info in lifestore_products if id == info[0]])
  # Se imprimen los resultados
  print(f"El total de ingresos es de: ${total_ingtresos}\n")
  
  
def ventas_mes_year():
  """Se calculas las ventas realizadas por mes y año.

    returns:
      resumen_ventas(dict): Es resumen por mes de las ganancias, numero de ventas y ventas promedio por mes.
      ventas_anual(dict): Contiene las ventas por año.
  """
  venta_fecha = [id for id in lifestore_sales if id[4] == 0] # Se extraen las ventas sin devoluciones.
  precio_id = {producto[0]:producto[2] for producto in lifestore_products} # Se crear un diccionario con ID como llave y precio del producto como valor.
  # Se crear un diccionario con los meses.
  meses = {'01':'Enero', '02':'Febrero', '03':'Marzo', '04':'Abril', '05':'Mayo', '06':'Junio', '07':'Julio', '08':'Agosto', '09':'Septiembre', '10':'Octubre', '11':'Noviembre', '12':'Diciembre'} 

  ventas_mensuales = {} # Guarda las ventas por mes.
  ventas_anual = {} # Guarda las ventas por año.

  # Se calculan las ventas por mes y año.
  for venta in venta_fecha:
    mes = venta[3].split('/')[1]
    year = venta[3].split('/')[2]
    if mes not in ventas_mensuales:
      ventas_mensuales[mes] = [0, 0]
    if year not in ventas_anual:
      ventas_anual[year] = [0,0]
    ventas_mensuales[mes][0] += precio_id[venta[1]]
    ventas_mensuales[mes][1] += 1
    ventas_anual[year][0] += precio_id[venta[1]]
    ventas_anual[year][1] += 1

    # Se crea diccionario que es un resumen por mes de las ganancias, numero de ventas y ventas promedio por mes.
  resumen_ventas = {meses[key]:[ventas_mensuales[key][0], ventas_mensuales[key][1], ventas_mensuales[key][0]/ventas_mensuales[key][1]] 
                    for key in ventas_mensuales}

  return resumen_ventas, ventas_anual



def venta_year(ventas):
  """Imprime los resultados de las ventas de cada año
  """

  for year in ventas:
    print(f"Se realizaron {ventas[year][1]} ventas en el año {year} que genero una ganancia de ${ventas[year][0]}.\n")
    
def resumen_ventas_meses(dicc_1, titulo, columnas, index):
  """Imprime los resultados de las ventas por mes, los resultados se ordenan segun el valor de index.

  Args:
    dicc_1(dict): Almacena la información de las ventas por mes.
    titulo(string): Es el titulo que se va a imprimir de los resultados.
    columnas(list): Son el nombre de las columnas de cada resultado.
    index(int): Indica como se ordenaran los resultados ya sea por Ganacia,
                ventas o pomedio de ventas al mes.
  """
  resumen_ventas = sorted(dicc_1.items(), key=lambda x:x[1][index], reverse=True)
  print(titulo)
  print("{:<6} {:<10} {:<10} {:<10} {:<10}".format('', columnas[0], columnas[1], columnas[2], columnas[3]))

  for num, mes in enumerate(resumen_ventas):
    print("{:<6} {:<10} {:<10} {:<10} {:<10}".format(num + 1, mes[0], mes[1][0],  mes[1][1], round(mes[1][2],2)))
  print("\n")
