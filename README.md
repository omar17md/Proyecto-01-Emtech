# Proyecto-01-Emtech
## Caso LifeStore

Elaborado por: Jesus Omar Magaña Medina

***

## Introducción
Python es uno de los lenguajes más utilizados en la actualidad por su facilidad de programar, es un lenguaje multiparadigma, y es uno de los más usados en el área de Ciencia de Datos. En este reporte se aborda el problema de la tienda LifeStore que es una tienda virtual que maneja una amplia gama de artículos, la tienda ha detectado una acumulación importante en su inventario y a su vez se ha identificado una reducción en las búsquedas de un grupo importante de productos, con ayuda del poder de Python y con los datos que tenemos en tres listas de Python que contienen las ventas de los productos, información de los productos y búsquedas de los productos (lifestore_products, lifestore_sales, lifestore_searches respectivamente) se dará un resumen de la información que se tiene así como una solución posible para los problemas presentados. Para dar solución se usará las herramientas dados por el lenguaje de programación Python como estructuras de control y datos, ciclos, etc.

***

## Explicación del código
El código se divide en tres archivos,  PROYECTO-01-Magaña-Medina-Jesus-Omar.py que es el archivo principal(main), funciones.py que contiene todas las funciones necesarias para el procesamiento de datos y lifestore_file.py donde están los datos de la tienda LifeStore.

### Variables base
Las siguientes variables son usadas para calcular los diferentes puntos solicitados, estas variables son las siguientes:
  * id_ventas(list): Una lista que guarda los ID de los productos que fueron vendidos (no cuentan las devueltos).
  * id_busquedas(list): Una lista que guarda los ID de los productos que fueron buscados.

``` python
id_ventas, id_busquedas = extraccion_id(lifestore_sales, lifestore_searches)
```

Como notaremos la anterior línea manda llamar a la función extracción_id que recibe como parámetro las listas lifestore_sales y lifestore_searches. 

Esta función recibe como parámetro las dos listas mencionadas anteriormente guardadas en las variables lista_1 y lista_2 respectivamente, la función extrae los ID de los productos de ambas listas, para ello se usó comprensión de listas, la primera comprensión regresa una lista con los ID de los productos vendidos siempre y cuando en esa venta no se devolvió el producto, la otra lista retornada regresa los ID de los productos buscados.

``` python
def extraccion_id(lista_1, lsita_2):
  """Extrae los ID de las listas lifestore_sales y lifestore_searches
  """
  return [id[1] for id in lista_1 if id[4] == 0], [id[1] for id in lsita_2]
 ```
 
Después creamos diccionarios necesarios para los posteriores cálculos, estos son los siguientes:
* id_sin_ventas(dict): Un diccionario que guarda como llave los ID de los productos que no han tenido ninguna venta y su valor es una lista que almacena el nombre y categoría del producto además de que se agrega un 0 indicando que no tuvo ninguna venta.
* id_sin_busquedas(dict): Un diccionario que guarda como llave los ID de los productos que no han sido buscados ninguna vez y su valor es una lista que almacena el nombre y categoría del producto además de que se agrega un 0 indicando que no ha tenido ninguna búsqueda.
* categorías(list): Una lista con todas las categorías de los productos, primero se extraen todas las categorías encontradas en la lista lifestore_products, después se usa la función set para tener valores únicos.

``` python
id_sin_ventas = {id[0]:[id[1], id[3], 0] for id in lifestore_products if id[0] not in id_ventas} # Se crear un diccionario con ID del producto como llave el nombre, 
                                                                                                 # categoria y 0 de los productos no vendidos.
id_sin_busquedas = {id[0]:[id[1], id[3], 0] for id in lifestore_products if id[0] not in id_busquedas} # Se crear un diccionario con ID del producto como llave el nombre, 
                                                                                                       # categoria y 0 de los productos no buscados.
categorias = set([categoria[3] for categoria in lifestore_products]) # Se crear una lista con las categorias de los productos
``` 

### PRODUCTOS MÁS VENDIDOS Y BUSCADOS
Para el primer punto que es generar un listado de los 5 productos con mayores ventas y una con los 10 productos con mayores búsquedas se realizó una función llamada contabilizar_ventas_busquedas que contabiliza el mayor número de ventas o búsquedas por ID, se calcula búsquedas o ventas dependiendo de la lista pasada por parámetro(id_ventas, id_busquedas), recibe por parámetro  las siguientes variables:

* top(int): Indica resultados se van a imprimir en pantalla.
* lista_id(list): Puede contener los ID de los productos que se encuentran en la lista lifestore_sales o los ID de la lista lifestore_searches.
* titulo(string): Es el título que se va a imprimir de los resultados.
* columnas(list): Son el nombre de las columnas de cada resultado.

Lo primero que hace es crear un diccionario con ID del producto como llave y como valor el número de veces que se vendió ese producto, esto se hace con ayuda de las funciones map, zip, count y dict, el resultado es guardado en id_contabilizados, luego es ordenado por los valores del diccionario ósea el número de ventas, esta es hecho por la función sorted, el diccionario resultante es guardado en resultado, después se crear un diccionario con ayuda de comprensión de diccionarios donde la llave es el ID del producto y de valor una lista con el nombre, la categoría y el número de ventas del producto. Se imprime los resultados, se imprime solamente los primeros top productos, recordando que top es una variable. Por último se regresa el diccionario con la información de los productos vendidos o buscados según sea el caso.
``` python
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
```

Una vez explicada la función anterior, en el archivo principal se manda a llamar esta función para cada punto.

``` python
# Los 5 productos mas vendidos
productos_vendidos = contabilizar_ventas_busquedas(5, id_ventas, "Los 5 productos mas vendidos son:", ['ID','Nombre', 'Cantidad', 'Categoria'])
# Los 10 productos mas buscados
productos_buscados = contabilizar_ventas_busquedas(10, id_busquedas, "Los 10 productos mas buscados son:", ['ID','Nombre', 'Busquedas', 'Categoria'])
```

### POR CATEGORÍA LOS PRODUCTOS CON MENORES VENTAS Y MENOS BUSCADOS
Para este punto que pide dos listados por categoría con los productos con menores ventas y menos buscados se creó una función llamada contabilizar_por_categoria que contabiliza el menor número de ventas o búsquedas de cada producto por categoría, se calcula búsquedas o ventas dependiendo de la lista pasada por parámetro, esta función recibe por parámetro los siguientes parámetros:

* top(int): Indica resultados se van a imprimir en pantalla.
* dicc_1(dict): Puede contener los ID como llave de los productos que se encuentran en la lista lifestore_sales o los ID de la lista lifestore_searches, y como valor el número de ventas o busquedas de ese ID.
* dicc_2(dict): Puede contener los ID como llave de los productos que no encuentran en la lista lifestore_sales o los ID que no están en la lista lifestore_searches, y como valor el número de ventas o búsquedas de ese ID.
* titulo(string): Es el título que se va a imprimir de los resultados.
* columnas(list): Son el nombre de las columnas de cada resultado.
* categorias(list): Contiene las categorías de los productos.
* 
Lo primero que se hace es unir los dos diccionarios en uno, el diccionario final se llama resultado, una vez unidos los dos diccionarios se ordena en base al número de búsquedas o ventas del producto de menor a mayor, el resultado se guarda en id_ordenado. Se crea una lista temporal_productos que almacena de manera temporal los productos encontrados de la categoría actual. Después de ayuda con un for anidado se va recorriendo cada categoría en el diccionario categorias y cada id del diccionario id_ordenados, si el producto en la actual iteración es de la categoría actual se agrega a la lista temporal_productos, si esta lista es igual a top quiere decir que ya se encontró la cantidad de productos solicitados entonces se rompe el for interior y se procede a imprimir los resultados. Por último, se inicializa de nuevo la lista temporal_productos y se procede a la siguiente categoría.

``` python
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
```

Ya explicada la función anterior en el archivo principal se manda a llamar a la función con los parámetros necesarios ya sea para buscar los 5 productos más vendidos por categoría o los 10 productos menos buscados por categoría.

``` python
# Se genera un listado con los 5 productos con menores ventas por categoria
contabilizar_por_categoria(5, productos_vendidos, id_sin_ventas, "Los 5 productos menos vendidos de", ["ID", "Nombre", "Cantidad"], categorias)
# Se genera un listado con los 10 productos con menores busquedas por categoria
contabilizar_por_categoria(10, productos_buscados, id_sin_busquedas, "Los 10 productos menos buscados de", ["ID", "Nombre", "Cantidad"], categorias)
```

### PRODUCTOS POR RESEÑA EN EL SERVICIO
Para este segundo punto que se solicitaba los 5 mejores productos reseñados y los 5 peores. Para esto se creó una función llamada promedio_puntuacion que calcula cuales son los productos con mejor reseña o peor, calculando el promedio de las reseñas y las veces que se calificó. Esta función recibe por parámetro las siguientes variables:

* order(bool): Indica cómo se va a ordenar el diccionario.
* titulo(string): Es el título que se va a imprimir de los resultados.
* columnas(list): Son el nombre de las columnas de cada resultado.
* 
Primero se crea un diccionario llamado resenas que guarda como llave el ID del producto y como valor la reseña que se le dio al producto. Con ayuda de un for se recorre cada venta realizada y se van agregando los ID de los productos como llave y las reseñas que ha tenido ese producto. Una vez teniendo esos datos con ayuda de comprensión de diccionarios se crea otro diccionario con ID como llave y una lista como valor que contiene el promedio de las reseñas y el número de reseñas, después se ordena en base a la suma de promedios más el número de reseñas y el valor de la variable orden, esto con el fin de tener una mejor referencia en cuales son los mejores productos o peores, después se obtiene el nombre del producto y se imprime los resultados obtenidos.

``` python
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
```

Una vez explicada la función anterior se procede a llamar la desde el archivo principal con los parámetros necesarios.

``` python
# Los 5 productos con mejores reseñas
promedio_puntuacion(True, "Los 5 productos con mejor reseñas son:", ['ID','Nombre', 'Puntuación', 'Numero de veces calificado'])
# Los 5 productos con peores reseñas
promedio_puntuacion(False, "Los 5 productos con peor reseñas son:", ['ID','Nombre', 'Puntuación', 'Numero de veces calificado'])
```

### Total ingresos
Para calcular el total de ingresos se creó una función llamada calcular_venta que recibe como parámetro:

*	lista_id(list): Lista que contiene los ID de los productos vendidos.
*	
Primero se contabiliza las veces que se vendió cada producto con ayuda de las funciones map, zip, count y dict aplicados a la lista lista_id. después se multiplica el número de ventas de cada producto por su precio, al final se suma todo y se obtiene el total de ingresos y se imprime el resultado.

**Nota**: No se toma en cuenta las ventas con devoluciones.

``` python
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
```

En el archivo principal se manda a llamar a la función explicada anteriormente para calcular e imprimir el total de ingresos.

``` python
# Total de ingresos
calcular_venta(id_ventas)
```

### VENTAS POR AÑO Y POR MESES
Para calcular las ventas por año y por mes se creó una función llamada ventas_mes_year que no recibe ningún parámetro. La primera acción que hace esta función es crear por de medio de comprensión de listas una lista con las ventas que no tuvieron una devolución, la lista se guarda en venta_fecha, procedemos utilizando un diccionario con ID del producto como llave y el precio como valor, este diccionario se llama precio_id, se crea un diccionario con el número del mes como llave y el nombre del mes como valor esto con el fin de cuando tengamos los meses que hubo venta sustituir el número del mes por el nombre. Se crear dos diccionarios más uno llamada ventas_mensuales que guardara las ventas por mes y ventas_anuales que guardara las ventas mensuales.

Con ayuda de un for se itera por cada venta realizada y de la fecha de esa venta se extrae el mes y año con ayuda de la función Split, después procedemos a guardar en los diccionarios ventas_mensuales y ventas_anuales respectivamente el ingreso de la venta y un acumulador de las ventas de ese mes.

Ya casi para terminar se crea diccionario llamado resumen_ventas que es un resumen por mes de las ganancias, número de ventas y ventas promedio por mes, se retorna el resumen_ventas y ventas_anual.


``` python
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
```

Ya explicada la función anterior se procede a llamar la en el archivo principal, los diccionarios retornados por la función se guardan en resumen_ventas y ventas_anual respectivamente.

``` python
# Se calcula las ventas por mes y año
resumen_ventas, ventas_anual = ventas_mes_year()
```

Ya teniendo el diccionario que contiene las ventas anuales se procede a imprimir su contenido con ayuda de la funcion venta_year que recibe como parámetro el diccionario previamente mencionado, esta función imprime los resultados con ayuda de un for por cada año que hubo una venta, se imprime el número de ventas, el año y la ganancia obtenida ese año.

**Nota**: No se toman en cuenta las ventas donde hubo una devolución.

``` python
def venta_year(ventas):
  """Imprime los resultados de las ventas de cada año
  """

  for year in ventas:
    print(f"Se realizaron {ventas[year][1]} ventas en el año {year} que genero una ganancia de ${ventas[year][0]}.\n")
 ```
 
 Ahora simplemente mandamos a llamar a la función desde el código principal.
 
 ``` python
# Ventas por año
venta_year(ventas_anual)
 ```
 
 Ahora para imprimir la información guarda en el diccionario resumen_ventas se creó una función llamada resumen_ventas_meses que imprime los resultados de las ventas por mes, los resultados se ordenan según el valor del parámetro index. Esta función recibe por parámetro las siguientes variables:
 
*	dicc_1(dict): Almacena la información de las ventas por mes.
*	titulo(string): Es el título que se va a imprimir de los resultados.
*	columnas(list): Son el nombre de las columnas de cada resultado.
*	index(int): Indica cómo se ordenarán los resultados ya sea por ganancia, ventas o promedio de ventas al mes.

Primero se ordena el dicc_1 en base al al valor del parámetro index, el resultado se guarda en la lista resumen_ventas, después se procede a imprimir los resultados, se imprime el Mes, Ganancia, Ventas, Promedio de ventas al mes.

 ``` python
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
 ```
 
Ahora desde el archivo principal se manda a llamar la función donde se mandan los mismos parámetros excepto la columna por la cual se va ordenar, ya sea ganancia, por ventas o por promedio de ventas al mes.
 
 ``` python
 # Ventas por mes
resumen_ventas_meses(resumen_ventas, "Meses con mas ganancias:", ["Mes", "Ganancia", "Ventas", "Promedio de ventas al mes"], 0)
resumen_ventas_meses(resumen_ventas, "Meses con mas ventas:", ["Mes", "Ganancia", "Ventas", "Promedio de ventas al mes"], 1)
resumen_ventas_meses(resumen_ventas, "Ventas promedio por mes:", ["Mes", "Ganancia", "Ventas", "Promedio de ventas al mes"], 2)
 ```
 
Por ultimo tenemos el login para el sistema de ventas que básicamente es pedir el usuario y contraseña al usuario, estos datos son emtech2022 y proyecTO-01 respectivamente, si el usuario se equivoca 3 veces el código finaliza, si el login es exitoso se inicializa el código.

 ``` python
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
  ```
  
  ## RESULTADOS
