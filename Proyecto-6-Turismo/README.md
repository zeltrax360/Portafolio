# Proyecto 6: Análisis de Turismo en España

## 📋 Descripción

Análisis de datos abiertos españoles sobre turismo. Demuestra capacidad de trabajar con datos públicos y crear insights de negocio.

## 🎯 Objetivos

1. Analizar tendencias de turismo en España
2. Identificar regiones con mejor desempeño
3. Segmentar por tipo de turista
4. Forecasting de ingresos turísticos
5. Benchmarking internacional

## 📊 Fuentes de Datos

- **INE (Instituto Nacional de Estadística)**
  - Llegadas de turistas
  - Gasto por turista
  - Estadía promedio

- **UNWTO (Organización Mundial de Turismo)**
  - Comparativas internacionales
  - Tendencias globales

- **Datos Abiertos Españoles**
  - Ocupación hotelera
  - Pernoctaciones
  - Ingresos por región

## 📈 Análisis

1. **Tendencias Nacionales**
   - Crecimiento anual
   - Estacionalidad
   - Segmentación por país de origen

2. **Análisis Regional**
   - Barcelona, Madrid, Málaga, etc.
   - Revenue per tourist
   - Seasonality por región

3. **Segmentación**
   - Turista de lujo
   - Turista de playa
   - Turista cultural
   - Mochilero

4. **Forecasting**
   - Proyecciones 2024-2025
   - Impacto de eventos
   - Sensibilidad a cambios

## 🛠️ Tecnologías

- Python: Pandas, Plotly
- SQL: Agregaciones complejas
- Power BI: Dashboard regional
- APIs: Web scraping de datos públicos

## 📁 Estructura

```
Proyecto-6-Turismo/
├── data/
│   ├── arrivals.csv
│   ├── spending.csv
│   ├── occupancy.csv
│   └── download_data.py
├── scripts/
│   ├── 01_eda.py
│   ├── 02_regional_analysis.py
│   ├── 03_segmentation.py
│   ├── 04_forecasting.py
│   └── utils.py
└── dashboards/
    └── turismo_espana.pbix
```

## 🚀 Ejecución

```bash
python scripts/01_eda.py
python scripts/02_regional_analysis.py
python scripts/03_segmentation.py
python scripts/04_forecasting.py
```

## 📊 Deliverables

- Dashboard con datos de 17 comunidades
- Análisis de 10+ años histórico
- Pronóstico de 12 meses
- Reporte de oportunidades turísticas
- Benchmarking vs Europa
