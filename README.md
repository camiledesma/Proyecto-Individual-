# Proyecto-Individual-
Demostración de todo lo aprendido durante mi etapa como alumna en Soy Henry
Hola mi nombre es Camila. Este proyecto tiene como objetivo realizar un análisis
de datos en el contexto de videojuegos. Se utilizan diversas fuentes de datos para
extraer información relevante y realizar diferentes análisis. 
A continuación, se describen las principales etapas del proyecto y los resultados obtenidos.

#Etapa 1: Bibliotecas necesarias
En esta etapa, instalo e importo todas las bibliotecas necesarias para llevar a cabo mi proyecto

#Etapa 2: Leer los archivos en formato json
En este punto, en el primer archivo que era el mas sencillo en cuestion de formato,
utilicé pandas para leer el archivo y pasarlo a csv; con el segundo y tercer archivo 
lo que hice fue, en una lista vacia, abro el archivo e inicio un bucle que recorre cada línea
del mismo enumerandolas y convirtiendolas en un diccionario de python y el diccionario
se agrega a dicha lista. Una vez realizado este proceso creo un df de pandas a partir de 
esa lista en donde cada fila representa un diccionario de la lista y las claves
de ese diccionario se convierte en un df.

#Etapa 3 EDA
Realizo un análisis de esos datos, viendo si hay datos anidados, que representa cada dato,
en que formato está, cuales son las columnas que voy a utilizar, etc.

#Etapa 4 ETL
Comienzo viendo si hay duplicados, nulos, conviertiendo las columnas a los tipos
de datos que corresponda, eliminando columnas innecesarias, trabajar con los datos
anidados, luego eliminar esa columna con los datos anidados y los mismos trasladarnos a 
otra columna ya limpios y en el formato que correspondan. 
Para desanidar estos datos fue crear un diccionario para almacenar los datos ya desanidados
e iterar a traves de las filas de ese df y obtener los valores de las listas en la columna
donde estaban esos datos anidados; luego los desanido y los almaceno en un diccionario, creando
un nuevo df a partir de este diccionario .
A partir que los df estan correctos, los uno con un merge a los que necesito para poder 
comenzar con las consignas.

#Consignas
1) Analisis de sentimiento: creo una funcion para realizar dicho analisis a partir del df2_reviews,
clasificando a base del sentimiento como positivo, malo y neutral (dependiendo de cada valor me 
retorna una clasificacion diferente) y luego aplico la funcion a cada reseña y creo
la nueva columna llamada 'sentiment_analysis'.

2) PlayTimeGenre: devuelve el año con mas horas jugadas para dicho genero. En esta funcion
tengo como parametro el genero, utilizando la variable global ya designada que es la union
del df 1 y el df 2. Primero filtro los juegos por el genero especifico, luego encuentro el año con mas
horas jugadas para el genero dado y que me retorne el año de lanzamiento con mas horas jugadas para dicho genero.

3) UserForGenre: devuelve el  el usuario que acumula más horas jugadas para el género dado y una lista de la acumulación
de horas jugadas por año. En esta funcion tengo como parametro el genero, utilizando la variable global ya designada que
es la union de los 3 archivos. Filtro los juegos por el genero especifico; luego encontru el usuario que acumula
mas horas jugadas; calculo la acumulacion de esas horas jugadas por año; creo una lista de años y horas jugadas
y luego creo un diccionario con los resultados.

4) UsersRecommend y UsersNotRecommend: también utilizo la variable globar con los 3 archivos unidos;
filtro para obtener solo las filas del año dado; filtro las recomendaciones positivas o neutrales; ordeno
las filas con recomendaciones positivas o neutrales; ordeno las filas por la cantidad
de recomendaciones en orden descendente; selecciono las 3 primeras filas y creo una lista con los resultados.
En ambos casos los mismo pero una funcion me devuelve el top 3 de juegos mas recomendados y la otra
el top 3 de juegos menos recomendados.

5) sentiment_analysis: según el año de lanzamiento, me devuelve una lista con la cantidad de registros de reseñas de usuarios que
se encuentren categorizados con un análisis de sentimiento. En este caso filtro las filas para el año
especificado, mapeo los valores numericos a las categorias deseadas; cuento la cantidad de registros en cada
categoria y convierto el resulado en un diccionario.

6) recomendacion_usuario: me devuelve los 5 juegos mas recomendados ingresando el id del usuario.
Creo una variable que filtra las reseñas del usuario actual; encuentro los usuarios similares crendo
otra variable y excluyendo al usuario actual; ordeno a los usuarios similares por recomendacion;
inicio una lista para almacenar las recomendaciones e itero sobre los usuarios similares encontrando juegos
recomendados por ellos; evito que el usuario ya haya revisado ese juego y detengo la busqueda cuando
se almacene el numero de recomendaciones deseadas.

#Etapa 5 Github
Subo todos mis archivos a git para poderlos conectar con render

#Etapa 6 Render
Me creo una cuenta y pongo el link de mi repositorio en donde va recorrer el archivo .py con las funciones 
y el requeriments con las librerias necesarias.
