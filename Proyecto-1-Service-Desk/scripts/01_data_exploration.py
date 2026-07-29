"""
Exploración Inicial de Datos (EDA)
Script para analizar la estructura y características del dataset
"""

import pandas as pd
import numpy as np
from utils import conectar_postgres, ejecutar_query

def exploracion_inicial():
    """Realizar EDA completo"""

    conexion = conectar_postgres()
    if not conexion:
        print("No se pudo conectar a la base de datos")
        return

    # 1. Información general de tickets
    print("="*80)
    print("EXPLORACIÓN DE DATOS - SERVICE DESK")
    print("="*80)

    query = "SELECT COUNT(*) as total, COUNT(DISTINCT tecnico_id) as tecnicos FROM tickets"
    df_info = ejecutar_query(query, conexion)
    print("\n[1] INFORMACIÓN GENERAL")
    print(df_info.to_string(index=False))

    # 2. Distribución de tickets por estado
    print("\n[2] TICKETS POR ESTADO")
    query = "SELECT estado, COUNT(*) as cantidad FROM tickets GROUP BY estado ORDER BY cantidad DESC"
    df_estado = ejecutar_query(query, conexion)
    print(df_estado.to_string(index=False))

    # 3. Distribución por prioridad
    print("\n[3] TICKETS POR PRIORIDAD")
    query = "SELECT prioridad, COUNT(*) as cantidad FROM tickets GROUP BY prioridad ORDER BY cantidad DESC"
    df_prioridad = ejecutar_query(query, conexion)
    print(df_prioridad.to_string(index=False))

    # 4. Categorías con más tickets
    print("\n[4] TOP 10 CATEGORÍAS")
    query = """
    SELECT c.nombre, COUNT(*) as cantidad
    FROM tickets t
    JOIN categorias c ON t.categoria_id = c.id
    GROUP BY c.nombre
    ORDER BY cantidad DESC
    LIMIT 10
    """
    df_categorias = ejecutar_query(query, conexion)
    print(df_categorias.to_string(index=False))

    # 5. Rango de fechas
    print("\n[5] RANGO TEMPORAL DE DATOS")
    query = """
    SELECT
        MIN(fecha_creacion) as fecha_inicio,
        MAX(fecha_creacion) as fecha_fin,
        MAX(fecha_creacion) - MIN(fecha_creacion) as dias_cobertura
    FROM tickets
    """
    df_fechas = ejecutar_query(query, conexion)
    print(df_fechas.to_string(index=False))

    # 6. Datos faltantes
    print("\n[6] ANÁLISIS DE COMPLETITUD")
    query = """
    SELECT
        COUNT(*) as total_tickets,
        COUNT(fecha_resolucion) as con_resolucion,
        COUNT(*) - COUNT(fecha_resolucion) as sin_resolucion
    FROM tickets
    """
    df_completitud = ejecutar_query(query, conexion)
    print(df_completitud.to_string(index=False))

    conexion.close()
    print("\n✓ Exploración completada")

if __name__ == "__main__":
    exploracion_inicial()
