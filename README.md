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
  * id_ventas: Una lista que guarda los ID de los productos que fueron vendidos (no cuentan las devueltos).
  * id_busquedas: Una lista que guarda los ID de los productos que fueron buscados.

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
 * id_sin_ventas: Un diccionario que guarda como llave los ID de los productos que no han tenido ninguna venta y su valor es una lista que almacena el nombre y categoría del producto además de que se agrega un 0 indicando que no tuvo ninguna venta.
 * id_sin_busquedas: Un diccionario que guarda como llave los ID de los productos que no han sido buscados ninguna vez y su valor es una lista que almacena el nombre y * categoría del producto además de que se agrega un 0 indicando que no ha tenido ninguna búsqueda.
 * categorías: Una lista con todas las categorías de los productos, primero se extraen todas las categorías encontradas en la lista lifestore_products, después se usa la función set para tener valores únicos.

