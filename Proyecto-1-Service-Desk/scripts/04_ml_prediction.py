"""
Machine Learning - Predicción de Carga de Tickets
Script para entrenar modelo de predicción de volumen de tickets
"""

import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestRegressor
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score, mean_absolute_error
from utils import conectar_postgres, ejecutar_query
import pickle

def preparar_datos_ml():
    """Preparar datos para ML"""

    conexion = conectar_postgres()
    if not conexion:
        print("No se pudo conectar a la base de datos")
        return None

    print("="*80)
    print("MACHINE LEARNING - PREDICCIÓN DE CARGA")
    print("="*80)

    print("\n[1] Cargando y preparando datos...")

    query = """
    SELECT
        DATE_TRUNC('day', fecha_creacion)::DATE as fecha,
        EXTRACT(DOW FROM fecha_creacion) as dia_semana,
        EXTRACT(WEEK FROM fecha_creacion) as semana_anio,
        COUNT(*) as tickets_diarios,
        COUNT(CASE WHEN prioridad = 'Crítica' THEN 1 END) as criticos,
        COUNT(CASE WHEN prioridad = 'Alta' THEN 1 END) as altos,
        COUNT(CASE WHEN prioridad = 'Media' THEN 1 END) as medios
    FROM tickets
    GROUP BY DATE_TRUNC('day', fecha_creacion), EXTRACT(DOW FROM fecha_creacion), EXTRACT(WEEK FROM fecha_creacion)
    ORDER BY fecha
    """

    df = ejecutar_query(query, conexion)
    conexion.close()

    if df is None or df.empty:
        print("No hay datos para entrenar")
        return None

    # Crear características adicionales
    df['fecha'] = pd.to_datetime(df['fecha'])
    df['es_lunes'] = (df['dia_semana'] == 1).astype(int)
    df['es_viernes'] = (df['dia_semana'] == 5).astype(int)
    df['es_fin_semana'] = (df['dia_semana'].isin([6, 0])).astype(int)

    print(f"   Registros: {len(df)}")
    print(f"   Rango: {df['fecha'].min()} a {df['fecha'].max()}")

    return df

def entrenar_modelo(df):
    """Entrenar modelo de predicción"""

    print("\n[2] Preparando features...")

    # Features para el modelo
    features = ['dia_semana', 'semana_anio', 'es_lunes', 'es_viernes', 'es_fin_semana', 'criticos', 'altos', 'medios']
    X = df[features]
    y = df['tickets_diarios']

    # Split train/test
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    print(f"   Features: {features}")
    print(f"   Train: {len(X_train)} | Test: {len(X_test)}")

    # Entrenar modelo
    print("\n[3] Entrenando modelo...")
    modelo = RandomForestRegressor(n_estimators=100, random_state=42, max_depth=10)
    modelo.fit(X_train, y_train)

    # Predicciones
    y_pred_train = modelo.predict(X_train)
    y_pred_test = modelo.predict(X_test)

    # Métricas
    print("\n[4] RESULTADOS DEL MODELO")
    print("-" * 80)
    print(f"   MAE (Train):  {mean_absolute_error(y_train, y_pred_train):.2f} tickets")
    print(f"   MAE (Test):   {mean_absolute_error(y_test, y_pred_test):.2f} tickets")
    print(f"   RMSE (Train): {np.sqrt(mean_squared_error(y_train, y_pred_train)):.2f} tickets")
    print(f"   RMSE (Test):  {np.sqrt(mean_squared_error(y_test, y_pred_test)):.2f} tickets")
    print(f"   R² (Train):   {r2_score(y_train, y_pred_train):.4f}")
    print(f"   R² (Test):    {r2_score(y_test, y_pred_test):.4f}")

    # Importancia de features
    print("\n[5] IMPORTANCIA DE FEATURES")
    print("-" * 80)
    importancia = pd.DataFrame({
        'feature': features,
        'importancia': modelo.feature_importances_
    }).sort_values('importancia', ascending=False)

    for idx, row in importancia.iterrows():
        print(f"   {row['feature']}: {row['importancia']:.4f}")

    # Predicciones de ejemplo
    print("\n[6] PREDICCIONES EJEMPLO")
    print("-" * 80)
    sample_pred = pd.DataFrame({
        'fecha': df['fecha'].tail(5),
        'actual': y.tail(5).values,
        'predicho': y_pred_test[:5]
    })
    print(sample_pred.to_string(index=False))

    print("\n✓ Modelo entrenado exitosamente")

    return modelo

if __name__ == "__main__":
    df = preparar_datos_ml()
    if df is not None:
        modelo = entrenar_modelo(df)
