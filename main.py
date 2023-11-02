import pandas as pd
from fastapi import FastAPI

app = FastAPI()

# Definición de rutas y funciones de manejo aquí


# Carga el DataFrame desde el archivo CSV
df123 = pd.read_csv('df123.csv')
df13 = pd.read_csv('df13.csv')

@app.get("/playtime_genre/{genero}")
def PlayTimeGenre(genero):
    global df13  # Acceso a la variable global df13
    try:
        # Filtrar juegos por el género específico en el DataFrame unido
        filtered_games = df13[df13['genres'] == genero]

        if not filtered_games.empty:
            # Encontrar el año con más horas jugadas para el género dado
            year_with_most_hours_played = filtered_games.groupby('release_year')['playtime_forever'].sum().idxmax()

            return {"Año de lanzamiento con más horas jugadas para " + genero: int(year_with_most_hours_played)}
        else:
            return {"Error": "No se encontraron juegos para el género especificado."}
    except Exception as e:
        # Manejo de errores
        return {"Error": str(e)}




    
        

@app.get("/user_for_genre/{genero}")
def UserForGenre(genero):
    global df123  # Acceso a la variable global df123
    try:
        # Filtrar juegos por el género específico
        filtered_df = df123[df123['genres'] == genero]

        if not filtered_df.empty:
            # Encontrar al usuario que acumula más horas jugadas
            max_playtime_user = filtered_df.groupby('user_id')['playtime_forever'].sum().idxmax()

            # Calcular la acumulación de horas jugadas por año
            hours_played_by_year = filtered_df.groupby('release_year')['playtime_forever'].sum().reset_index()

            # Crear la lista de años y horas jugadas
            years = hours_played_by_year['release_year'].tolist()
            hours = hours_played_by_year['playtime_forever'].tolist()

            # Crear el diccionario de resultados
            result = {
                "Usuario con más horas jugadas para " + genero: max_playtime_user,
                "Horas jugadas": [{"Año": year, "Horas": hour} for year, hour in zip(years, hours)]
            }
            return result
        else:
            return {"Error": "No se encontraron juegos para el género especificado."}
    except Exception as e:
        return {"Error": str(e)}

    

        



            

    
@app.get("/users_recommend/{año}")    
def UsersRecommend(anio: int):
    global df123  # Acceso a la variable global df123
    try:
        # Filtra el DataFrame para obtener solo las filas del año dado
        df_filtered = df123[df123['release_year'] == anio]

        if not df_filtered.empty:
            # Filtra las filas con recomendaciones positivas o neutrales
            df_filtered = df_filtered[df_filtered['recommend'] == 1.0]

            if not df_filtered.empty:
                # Ordena las filas por la cantidad de recomendaciones en orden descendente
                df_filtered = df_filtered.sort_values(by='recommend', ascending=False)

                # Selecciona las 3 primeras filas (los juegos más recomendados)
                top_3_recommendations = df_filtered.head(3)

                # Crea una lista con los resultados
                result = [{"Puesto " + str(i + 1): row['title']} for i, (_, row) in enumerate(top_3_recommendations.iterrows())]

                return result

        return {"Error": "No se encontraron juegos recomendados para el año especificado."}
    except Exception as e:
        return {"Error": str(e)}

            








@app.get("/users_not_recommend/{año}")        
def UsersNotRecommend(anio: int):
    global df123  # Acceso a la variable global df123
    try:
        # Filtra el DataFrame para obtener solo las filas del año dado
        df_filtered = df123[df123['release_year'] == anio]

        if not df_filtered.empty:
            # Filtra las filas con recomendaciones negativas
            df_filtered = df_filtered[df_filtered['recommend'] == 0.0]

            if not df_filtered.empty:
                # Ordena las filas por la cantidad de recomendaciones en orden descendente
                df_filtered = df_filtered.sort_values(by='recommend', ascending=True)

                # Selecciona las 3 primeras filas (los juegos menos recomendados)
                top_3_not_recommendations = df_filtered.head(3)

                # Crea una lista con los resultados
                result = [{"Puesto " + str(i + 1): row['title']} for i, (_, row) in enumerate(top_3_not_recommendations.iterrows())]

                return result

        return {"Error": "No se encontraron juegos menos recomendados para el año especificado."}
    except Exception as e:
        return {"Error": str(e)}








    




@app.get("/sentiment_analysis/{año}")
def sentiment_analysis(anio):
    try:
        # Filtra las filas del DataFrame para el año especificado
        filtered_data = df123[df123['release_year'] == anio]
        
        # Mapea los valores numéricos a las categorías deseadas
        sentiment_map = {0.0: 'Negative', 1.0: 'Neutral', 2.0: 'Positive'}
        filtered_data.loc[:, 'sentiment_analysis'] = filtered_data['sentiment_analysis'].map(sentiment_map)
        
        # Cuenta la cantidad de registros en cada categoría de análisis de sentimiento
        sentiment_counts = filtered_data['sentiment_analysis'].value_counts()
        
        # Convierte el resultado en un diccionario
        sentiment_dict = sentiment_counts.to_dict()
        
        return str(sentiment_dict)
    except Exception as e:
        # Manejo de errores
        return {"Error": str(e)}
    













@app.get("/recomendacion_usuario/{usuario_id}")
def recomendacion_usuario(usuario_id):
    global df123  # Acceso a la variable global df123

    # Filtrar las reseñas del usuario actual
    reseñas_usuario = df123[df123['user_id'] == usuario_id]

    # Encontrar usuarios similares
    usuarios_similares = df123[df123['user_id'] != usuario_id]  # Excluir al usuario actual
    usuarios_similares = usuarios_similares.groupby('user_id')['recommend'].mean().reset_index()

    # Ordenar usuarios similares por su similitud (recomendación promedio)
    usuarios_similares = usuarios_similares.sort_values(by='recommend', ascending=False)

    # Inicializar una lista para almacenar las recomendaciones
    recomendaciones_usuario = []  # Usamos una variable diferente para las recomendaciones de usuario

    # Iterar sobre los usuarios similares y encontrar juegos recomendados por ellos
    for i, row in usuarios_similares.iterrows():
        usuario_similar_id = row['user_id']
        juegos_recomendados = df123[(df123['user_id'] == usuario_similar_id) & (df123['recommend'] == 1)]['title'].tolist()

        # Evitar juegos que el usuario ya haya revisado
        juegos_recomendados = [juego for juego in juegos_recomendados if juego not in reseñas_usuario['title'].tolist()]

        recomendaciones_usuario.extend(juegos_recomendados)

        # Detener la búsqueda cuando se alcance el número deseado de recomendaciones
        if len(recomendaciones_usuario) >= 5:
            break

    return str(recomendaciones_usuario[:5])


