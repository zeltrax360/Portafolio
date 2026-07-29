"""
Limpieza y Transformación de Datos
Script para preparar datos para análisis
"""

import pandas as pd
import numpy as np
from utils import conectar_postgres, ejecutar_query, calcular_mttr

def limpiar_datos():
    """Limpieza completa del dataset"""

    conexion = conectar_postgres()
    if not conexion:
        print("No se pudo conectar a la base de datos")
        return

    print("="*80)
    print("LIMPIEZA Y TRANSFORMACIÓN DE DATOS")
    print("="*80)

    # 1. Cargar todos los tickets
    print("\n[1] Cargando datos...")
    query = """
    SELECT
        t.id,
        t.numero_ticket,
        t.fecha_creacion,
        t.fecha_resolucion,
        t.prioridad,
        t.estado,
        c.nombre as categoria,
        tec.nombre as tecnico,
        tec.nivel as nivel_tecnico
    FROM tickets t
    LEFT JOIN categorias c ON t.categoria_id = c.id
    LEFT JOIN tecnicos tec ON t.tecnico_id = tec.id
    ORDER BY t.fecha_creacion
    """
    df = ejecutar_query(query, conexion)
    conexion.close()

    if df is None or df.empty:
        print("No hay datos para procesar")
        return

    print(f"Registros cargados: {len(df)}")

    # 2. Conversión de tipos
    print("\n[2] Convirtiendo tipos de datos...")
    df['fecha_creacion'] = pd.to_datetime(df['fecha_creacion'])
    df['fecha_resolucion'] = pd.to_datetime(df['fecha_resolucion'])

    # 3. Cálculo de MTTR
    print("[3] Calculando MTTR...")
    df['mttr_horas'] = df.apply(
        lambda row: calcular_mttr(row['fecha_creacion'], row['fecha_resolucion']),
        axis=1
    )

    # 4. Extracción de características temporales
    print("[4] Extrayendo características temporales...")
    df['mes'] = df['fecha_creacion'].dt.to_period('M')
    df['semana'] = df['fecha_creacion'].dt.isocalendar().week
    df['dia_semana'] = df['fecha_creacion'].dt.day_name()
    df['hora'] = df['fecha_creacion'].dt.hour

    # 5. Verificación de datos faltantes
    print("\n[5] Análisis de datos faltantes:")
    valores_faltantes = df.isnull().sum()
    for columna, cantidad in valores_faltantes[valores_faltantes > 0].items():
        print(f"   {columna}: {cantidad} ({100*cantidad/len(df):.2f}%)")

    # 6. Estadísticas descriptivas
    print("\n[6] Estadísticas de MTTR (horas):")
    print(df['mttr_horas'].describe())

    # 7. Detección de outliers (MTTR > 72 horas)
    print("\n[7] Detección de outliers:")
    outliers = len(df[df['mttr_horas'] > 72])
    print(f"   Tickets con MTTR > 72 horas: {outliers} ({100*outliers/len(df):.2f}%)")

    # 8. Resumen por categoría
    print("\n[8] Resumen por Categoría:")
    resumen_cat = df.groupby('categoria').agg({
        'numero_ticket': 'count',
        'mttr_horas': ['mean', 'min', 'max']
    }).round(2)
    print(resumen_cat)

    print("\n✓ Limpieza completada")

    return df

if __name__ == "__main__":
    df_limpio = limpiar_datos()
