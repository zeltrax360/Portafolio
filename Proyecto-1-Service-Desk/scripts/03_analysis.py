"""
Análisis Descriptivo Detallado
Script para análisis de KPIs y métricas principales
"""

import pandas as pd
import numpy as np
from utils import conectar_postgres, ejecutar_query
import matplotlib.pyplot as plt
import seaborn as sns

def analisis_completo():
    """Realizar análisis completo y generar KPIs"""

    conexion = conectar_postgres()
    if not conexion:
        print("No se pudo conectar a la base de datos")
        return

    print("="*80)
    print("ANÁLISIS DE RENDIMIENTO - SERVICE DESK")
    print("="*80)

    # KPI 1: Métricas Generales
    print("\n[KPI 1] MÉTRICAS GENERALES")
    print("-" * 80)
    query = """
    SELECT
        COUNT(*) as total_tickets,
        COUNT(CASE WHEN estado = 'Resuelto' THEN 1 END) as resueltos,
        COUNT(CASE WHEN estado = 'Abierto' THEN 1 END) as abiertos,
        ROUND(100.0 * COUNT(CASE WHEN estado = 'Resuelto' THEN 1 END) / COUNT(*), 2) as tasa_resolucion,
        ROUND(AVG(EXTRACT(EPOCH FROM (fecha_resolucion - fecha_creacion))/3600)::NUMERIC, 2) as mttr_promedio,
        COUNT(DISTINCT tecnico_id) as total_tecnicos
    FROM tickets
    WHERE estado = 'Resuelto'
    """
    df_kpi1 = ejecutar_query(query, conexion)
    for col in df_kpi1.columns:
        print(f"   {col}: {df_kpi1[col].iloc[0]}")

    # KPI 2: Desempeño por Técnico
    print("\n[KPI 2] TOP 5 TÉCNICOS POR DESEMPEÑO")
    print("-" * 80)
    query = """
    SELECT
        tec.nombre,
        tec.nivel,
        COUNT(*) as tickets_resueltos,
        ROUND(AVG(EXTRACT(EPOCH FROM (t.fecha_resolucion - t.fecha_creacion))/3600)::NUMERIC, 2) as mttr_horas
    FROM tickets t
    JOIN tecnicos tec ON t.tecnico_id = tec.id
    WHERE t.estado = 'Resuelto'
    GROUP BY tec.id, tec.nombre, tec.nivel
    ORDER BY tickets_resueltos DESC
    LIMIT 5
    """
    df_kpi2 = ejecutar_query(query, conexion)
    print(df_kpi2.to_string(index=False))

    # KPI 3: Categorías Críticas
    print("\n[KPI 3] CATEGORÍAS POR VOLUMEN Y COMPLEJIDAD")
    print("-" * 80)
    query = """
    SELECT
        c.nombre as categoria,
        COUNT(*) as total_tickets,
        ROUND(100.0 * COUNT(*) / SUM(COUNT(*)) OVER (), 2) as porcentaje,
        ROUND(AVG(EXTRACT(EPOCH FROM (t.fecha_resolucion - t.fecha_creacion))/3600)::NUMERIC, 2) as mttr_horas
    FROM tickets t
    JOIN categorias c ON t.categoria_id = c.id
    WHERE t.estado = 'Resuelto'
    GROUP BY c.nombre
    ORDER BY total_tickets DESC
    """
    df_kpi3 = ejecutar_query(query, conexion)
    print(df_kpi3.to_string(index=False))

    # KPI 4: Cumplimiento de SLA
    print("\n[KPI 4] CUMPLIMIENTO DE SLA")
    print("-" * 80)
    query = """
    SELECT
        c.nombre as categoria,
        COUNT(*) as total,
        COUNT(CASE WHEN EXTRACT(EPOCH FROM (t.fecha_resolucion - t.fecha_creacion))/3600 <= sp.tiempo_resolucion_horas THEN 1 END) as cumplidos,
        ROUND(100.0 * COUNT(CASE WHEN EXTRACT(EPOCH FROM (t.fecha_resolucion - t.fecha_creacion))/3600 <= sp.tiempo_resolucion_horas THEN 1 END) / COUNT(*), 2) as cumplimiento
    FROM tickets t
    JOIN categorias c ON t.categoria_id = c.id
    JOIN sla_policies sp ON c.id = sp.categoria_id AND t.prioridad = sp.prioridad
    WHERE t.estado = 'Resuelto'
    GROUP BY c.nombre
    ORDER BY cumplimiento DESC
    """
    df_kpi4 = ejecutar_query(query, conexion)
    print(df_kpi4.to_string(index=False))

    # KPI 5: Tendencia Temporal
    print("\n[KPI 5] TENDENCIA MENSUAL")
    print("-" * 80)
    query = """
    SELECT
        DATE_TRUNC('month', fecha_creacion)::DATE as mes,
        COUNT(*) as tickets_creados,
        COUNT(CASE WHEN estado = 'Resuelto' THEN 1 END) as resueltos,
        ROUND(AVG(EXTRACT(EPOCH FROM (fecha_resolucion - fecha_creacion))/3600)::NUMERIC, 2) as mttr_horas
    FROM tickets
    GROUP BY DATE_TRUNC('month', fecha_creacion)
    ORDER BY mes DESC
    LIMIT 12
    """
    df_kpi5 = ejecutar_query(query, conexion)
    print(df_kpi5.to_string(index=False))

    # KPI 6: Distribución de Prioridades
    print("\n[KPI 6] ANÁLISIS POR PRIORIDAD")
    print("-" * 80)
    query = """
    SELECT
        prioridad,
        COUNT(*) as total,
        ROUND(100.0 * COUNT(*) / SUM(COUNT(*)) OVER (), 2) as porcentaje,
        COUNT(CASE WHEN estado = 'Resuelto' THEN 1 END) as resueltos,
        ROUND(AVG(EXTRACT(EPOCH FROM (fecha_resolucion - fecha_creacion))/3600)::NUMERIC, 2) as mttr_horas
    FROM tickets
    GROUP BY prioridad
    ORDER BY CASE prioridad WHEN 'Crítica' THEN 1 WHEN 'Alta' THEN 2 WHEN 'Media' THEN 3 WHEN 'Baja' THEN 4 END
    """
    df_kpi6 = ejecutar_query(query, conexion)
    print(df_kpi6.to_string(index=False))

    conexion.close()

    print("\n" + "="*80)
    print("✓ Análisis completado")

if __name__ == "__main__":
    analisis_completo()
