# Proyecto 3: Análisis de Ventas - Retail

## 📋 Descripción

Dashboard de ventas con análisis de rentabilidad, segmentación de productos y pronóstico. Demuestra expertise en:

- **Analytics BI** - Dashboards ejecutivos
- **Análisis de cohortes** - Comportamiento de clientes
- **ABC Analysis** - Segmentación de productos
- **Forecasting** - Pronóstico de demanda

## 🎯 Objetivos

1. Analizar ventas por categoría, región, período
2. Identificar productos TOP (Pareto 80/20)
3. Calcular rentabilidad neta por SKU
4. Segmentar clientes (RFM)
5. Forecasting de demanda Q3-Q4

## 📊 KPIs Principales

| KPI | Valor | Target |
|-----|-------|--------|
| Revenue Total | $50M | - |
| Margin Promedio | 35% | > 33% |
| Conversion Rate | 3.2% | > 3.5% |
| AOV (Average Order Value) | $125 | > $120 |
| Customer Lifetime Value | $2,500 | > $2,000 |

## 📁 Estructura

```
Proyecto-3-Retail/
├── data/
│   ├── sales.csv (500K transacciones)
│   ├── products.csv
│   ├── customers.csv
│   └── regions.csv
├── scripts/
│   ├── 01_eda.py
│   ├── 02_rfm_analysis.py
│   ├── 03_profitability.py
│   ├── 04_forecasting.py
│   └── utils.py
├── dashboards/
│   └── retail_dashboard.pbix
└── README.md
```

## 🛠️ Tecnologías

- Python: Pandas, NumPy, Scikit-learn
- SQL: PostgreSQL (agregaciones)
- Visualización: Power BI
- Forecasting: ARIMA, Prophet

## 📈 Análisis Incluidos

1. **Revenue Analysis**
   - Total y por categoría
   - Tendencia mensual
   - Top productos

2. **Customer Segmentation**
   - RFM Scoring
   - Lifetime Value
   - Churn Risk

3. **Product Performance**
   - ABC Classification
   - Margin Analysis
   - Stock Efficiency

4. **Forecasting**
   - ARIMA para demanda
   - Seasonality detection
   - Confidence intervals

## 🚀 Ejecución

```bash
python scripts/01_eda.py
python scripts/02_rfm_analysis.py
python scripts/03_profitability.py
python scripts/04_forecasting.py
```

## 📊 Salidas Esperadas

- Dashboard con 15+ visualizaciones
- Segmentación de clientes en 4 clusters
- Pronóstico de 6 meses
- Top 20 productos por rentabilidad
- Recomendaciones de acción
