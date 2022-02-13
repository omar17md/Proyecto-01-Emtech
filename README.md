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
