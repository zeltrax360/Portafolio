# Proyecto 7: Pipeline ETL - Ingeniería de Datos

## 📋 Descripción

Pipeline de datos automatizado end-to-end. Extrae datos de múltiples fuentes, los transforma y carga en PostgreSQL. Demuestra expertise en data engineering.

## 🎯 Objetivos

1. Construir pipeline ETL robusto
2. Integrar múltiples fuentes de datos
3. Validar calidad de datos
4. Automatizar carga diaria
5. Crear data warehouse

## 📊 Flujo de Datos

```
APIs (3 fuentes)
    ↓
Python (Extracción)
    ↓
Transformación (Pandas)
    ↓
Validación (Great Expectations)
    ↓
PostgreSQL (Carga)
    ↓
Power BI (Visualización)
```

## 🛠️ Componentes

### 1. Extracción (Extract)
```python
# API 1: Weather Data (OpenWeather)
# API 2: Stock Prices (Yahoo Finance)
# API 3: Exchange Rates (Fixer.io)
```

### 2. Transformación (Transform)
- Normalización de tipos
- Manejo de nulls
- Deduplicación
- Agregaciones

### 3. Carga (Load)
- Inserción en PostgreSQL
- Upserts y deletes
- Logging y auditoría

### 4. Orquestación
- Schedule diario (7 AM)
- Manejo de errores
- Reintentos automáticos
- Alertas

## 📁 Estructura

```
Proyecto-7-ETL/
├── config/
│   ├── settings.yaml
│   └── database.ini
├── extractors/
│   ├── weather_api.py
│   ├── stocks_api.py
│   └── forex_api.py
├── transformers/
│   ├── data_cleaner.py
│   ├── validator.py
│   └── aggregator.py
├── loaders/
│   ├── postgres_loader.py
│   └── error_handler.py
├── orchestration/
│   ├── scheduler.py
│   └── pipeline.py
└── tests/
    └── test_pipeline.py
```

## 🛠️ Tecnologías

- **Extracción:** requests, pandas
- **Transformación:** pandas, dask
- **Validación:** great-expectations
- **Orquestación:** schedule (o Apache Airflow)
- **Base de Datos:** PostgreSQL
- **Logging:** Python logging

## ⚙️ Características

1. **Idempotencia:** Los datos pueden procesarse múltiples veces sin problemas
2. **Fault Tolerance:** Reintentos automáticos en caso de error
3. **Logging:** Auditoría completa de cada ejecución
4. **Validación:** Checks de calidad antes de cargar
5. **Alertas:** Notificaciones en caso de fallos

## 🚀 Ejecución

### Modo Manual
```bash
python orchestration/pipeline.py
```

### Modo Automático (Diario)
```bash
# El pipeline se ejecuta automáticamente cada día a las 7 AM
# Verificar logs: orchestration/logs/
```

## 📊 Deliverables

- Pipeline completamente funcional
- 3 fuentes de datos integradas
- Base de datos PostgreSQL con 3 tablas
- Sistema de logging y alertas
- Documentación técnica
- Tests unitarios

## 🔍 Ejemplo de Datos

**Tabla: weather_data** (200K registros)
- Ciudad, temperatura, humedad, fecha

**Tabla: stock_prices** (500K registros)
- Símbolo, precio, volumen, fecha

**Tabla: exchange_rates** (300K registros)
- Par de monedas, tasa, fecha

## 💡 Conceptos Clave Demostra dos

- Scraping y APIs REST
- Transformación de datos a escala
- Validación y calidad
- Orquestación de workflows
- Manejo de errores en producción
- DevOps básico
