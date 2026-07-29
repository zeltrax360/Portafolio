import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import psycopg2
from psycopg2.extras import RealDictCursor
from dotenv import load_dotenv
import os

load_dotenv()

def conectar_postgres():
    """Conectar a PostgreSQL"""
    try:
        conexion = psycopg2.connect(
            host=os.getenv('DB_HOST', 'localhost'),
            port=os.getenv('DB_PORT', '5432'),
            database=os.getenv('DB_NAME', 'service_desk'),
            user=os.getenv('DB_USER', 'postgres'),
            password=os.getenv('DB_PASSWORD', '')
        )
        return conexion
    except Exception as e:
        print(f"Error de conexión: {e}")
        return None

def ejecutar_query(query, conexion):
    """Ejecutar query y retornar DataFrame"""
    try:
        cursor = conexion.cursor(cursor_factory=RealDictCursor)
        cursor.execute(query)
        resultados = cursor.fetchall()
        cursor.close()
        return pd.DataFrame(resultados)
    except Exception as e:
        print(f"Error al ejecutar query: {e}")
        return None

def calcular_mttr(fecha_creacion, fecha_resolucion):
    """Calcular MTTR en horas"""
    if pd.isna(fecha_resolucion):
        return np.nan
    delta = fecha_resolucion - fecha_creacion
    return delta.total_seconds() / 3600

def calcular_cumplimiento_sla(mttr, sla_horas):
    """Verificar si cumple SLA"""
    if pd.isna(mttr):
        return False
    return mttr <= sla_horas

def guardar_csv(df, ruta):
    """Guardar DataFrame como CSV"""
    df.to_csv(ruta, index=False, encoding='utf-8')
    print(f"Datos guardados en: {ruta}")

def cargar_csv(ruta):
    """Cargar CSV como DataFrame"""
    return pd.read_csv(ruta)
