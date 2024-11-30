import pandas as pd
import numpy as np
from scipy import stats
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score, mean_squared_error
import statsmodels.api as sm

def cargar_y_limpiar_datos(ruta_archivo):
    """
    Carga y realiza limpieza inicial de datos.
    """
    # Cargar datos
    df = pd.read_csv(ruta_archivo)
    
    # Eliminar filas con más del 50% de valores faltantes
    df = df.dropna(thresh=len(df.columns)*0.5)
    
    # Imputar valores faltantes para variables numéricas
    numeric_columns = df.select_dtypes(include=[np.number]).columns
    for col in numeric_columns:
        df[col].fillna(df[col].median(), inplace=True)
    
    # Imputar valores faltantes para variables categóricas
    categorical_columns = df.select_dtypes(include=['object']).columns
    for col in categorical_columns:
        df[col].fillna(df[col].mode()[0], inplace=True)
    
    return df

def analisis_descriptivo(df):
    """
    Realiza análisis descriptivo de los datos.
    """
    resultados = {
        'estadisticas_numericas': df.describe(),
        'distribucion_categoricas': {col: df[col].value_counts(normalize=True) 
                                   for col in df.select_dtypes(include=['object']).columns}
    }
        
    return resultados

def analisis_brecha_digital(df):
    """
    Analiza la brecha digital entre estudiantes.
    """
    # Crear índice de acceso digital
    variables_acceso = ['calidad_internet', 'dispositivos_disponibles']
    df['indice_acceso'] = df[variables_acceso].mean(axis=1)
    
    # Análisis por grupos demográficos
    resultados_brecha = {
        'por_ciclo': df.groupby('año')['indice_acceso'].mean(),
        'por_genero': df.groupby('genero')['indice_acceso'].mean(),
        'distribucion': df['indice_acceso'].describe()
    }
    
    # Visualización
    plt.figure(figsize=(10, 6))
    sns.boxplot(data=df, x='año', y='indice_acceso')
    plt.title('Distribución del Índice de Acceso Digital por Año')
    plt.show()
    
    return resultados_brecha

def analisis_competencias_digitales(df):
    """
    Analiza las competencias digitales de los estudiantes.
    """
    # Crear índice de competencias digitales
    competencias = ['comp_busqueda', 'comp_analisis', 'comp_presentacion', 
                   'comp_data', 'comp_programacion']
    
    df['indice_competencias'] = df[competencias].mean(axis=1)
    
    # Análisis de clusters
    X = df[competencias]
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)
    
    # Determinar número óptimo de clusters
    inertias = []
    for k in range(1, 6):
        kmeans = KMeans(n_clusters=k, random_state=42)
        kmeans.fit(X_scaled)
        inertias.append(kmeans.inertia_)
    
    # Aplicar clustering final
    kmeans_final = KMeans(n_clusters=3, random_state=42)
    df['cluster_competencias'] = kmeans_final.fit_predict(X_scaled)
    
    return {
        'perfiles_competencias': df.groupby('cluster_competencias')[competencias].mean(),
        'distribucion_clusters': df['cluster_competencias'].value_counts(),
        'inertias': inertias
    }

def analisis_rendimiento(df):
    """
    Analiza factores que influyen en el rendimiento académico.
    """
    # Preparar variables para el modelo
    variables_predictoras = ['indice_acceso', 'indice_competencias', 'horas_estudio',
                           'uso_plataforma', 'uso_db_academica']
    
    X = df[variables_predictoras]
    y = df['promedio_ponderado']
    
    # Dividir datos en entrenamiento y prueba
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    # Ajustar modelo
    modelo = LinearRegression()
    modelo.fit(X_train, y_train)
    
    # Evaluación del modelo
    y_pred = modelo.predict(X_test)
    r2 = r2_score(y_test, y_pred)
    rmse = np.sqrt(mean_squared_error(y_test, y_pred))
    
    # Análisis estadístico más detallado
    X_sm = sm.add_constant(X)
    modelo_sm = sm.OLS(y, X_sm).fit()
    
    return {
        'coeficientes': pd.DataFrame({
            'variable': variables_predictoras,
            'coeficiente': modelo.coef_
        }),
        'r2': r2,
        'rmse': rmse,
        'resumen_estadistico': modelo_sm.summary()
    }

def generar_reporte(df, resultados_analisis):
    """
    Genera un reporte completo del análisis.
    """
    reporte = """
    REPORTE DE ANÁLISIS DE INNOVACIÓN DIGITAL Y RENDIMIENTO ACADÉMICO
    
    1. ESTADÍSTICAS DESCRIPTIVAS
    ---------------------------
    {estadisticas}
    
    2. BRECHA DIGITAL
    ----------------
    {brecha}
    
    3. COMPETENCIAS DIGITALES
    ------------------------
    {competencias}
    
    4. ANÁLISIS DE RENDIMIENTO
    -------------------------
    {rendimiento}
    
    5. RECOMENDACIONES
    -----------------
    {recomendaciones}
    """.format(
        estadisticas=resultados_analisis['descriptivo']['estadisticas_numericas'],
        brecha=resultados_analisis['brecha'],
        competencias=resultados_analisis['competencias'],
        rendimiento=resultados_analisis['rendimiento'],
        recomendaciones=generar_recomendaciones(resultados_analisis)
    )
    
    return reporte

def generar_recomendaciones(resultados):
    """
    Genera recomendaciones basadas en los resultados del análisis.
    """
    recomendaciones = []
    
    # Analizar brecha digital
    if resultados['brecha']['distribucion']['std'] > 0.5:
        recomendaciones.append("Se recomienda implementar programas de apoyo para reducir la brecha digital")
    
    # Analizar competencias
    perfiles = resultados['competencias']['perfiles_competencias']
    areas_debiles = perfiles.min()
    recomendaciones.append(f"Fortalecer capacitación en: {areas_debiles.idxmin()}")
    
    # Analizar rendimiento
    if resultados['rendimiento']['r2'] < 0.3:
        recomendaciones.append("Investigar factores adicionales que afectan el rendimiento")
    
    return "\n".join(recomendaciones)

def ejecutar_analisis_completo(ruta_archivo):
    """
    Ejecuta el proceso completo de análisis de datos.
    """
    # Cargar y limpiar datos
    df = cargar_y_limpiar_datos(ruta_archivo)
    
    # Realizar análisis
    resultados = {
        'descriptivo': analisis_descriptivo(df),
        'brecha': analisis_brecha_digital(df),
        'competencias': analisis_competencias_digitales(df),
        'rendimiento': analisis_rendimiento(df)
    }
    
    # Generar reporte
    reporte = generar_reporte(df, resultados)
    
    return df, resultados, reporte

if __name__ == "__main__":
    pass
    # Ejemplo de uso
    # ruta_archivo = "datos_encuesta.csv"
    # df, resultados, reporte = ejecutar_analisis_completo(ruta_archivo)
    # print(reporte)