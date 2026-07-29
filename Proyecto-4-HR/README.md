# Proyecto 4: Análisis de Rotación de Empleados - RRHH

## 📋 Descripción

Análisis predictivo de rotación de empleados. Identifica qué colaboradores tienen mayor riesgo de renuncia y por qué.

## 🎯 Objetivos

1. Predecir empleados con riesgo de rotación
2. Identificar factores clave de renuncia
3. Segmentar por perfil de riesgo
4. Calcular impacto económico
5. Proponer estrategias de retención

## 📊 Dataset

- **Tamaño:** 1,000 empleados histórico
- **Período:** 5 años
- **Variables:** Edad, salario, departamento, desempeño, satisfacción
- **Target:** Churn (renunció sí/no)

## 📈 KPIs

| Métrica | Valor | Impact |
|---------|-------|--------|
| Tasa Rotación | 15% | $2.5M/año |
| Predicción AUC | 0.82 | - |
| Costo por renuncia | $25K | - |

## 🛠️ Análisis

1. **Exploratory Analysis**
   - Distribución demográfica
   - Salario vs rotación
   - Departamento más afectado

2. **Predictive Modeling**
   - Logistic Regression
   - Random Forest
   - Gradient Boosting

3. **Segmentación**
   - High Risk (> 80%)
   - Medium Risk (40-80%)
   - Low Risk (< 40%)

4. **Business Impact**
   - ROI de retención
   - Costo-beneficio de incentivos

## 📁 Estructura

```
Proyecto-4-HR/
├── data/
│   ├── employees.csv
│   └── performance.csv
├── scripts/
│   ├── 01_eda.py
│   ├── 02_churn_modeling.py
│   ├── 03_segmentation.py
│   └── utils.py
└── dashboards/
    └── hr_churn.pbix
```

## 🚀 Ejecución

```bash
python scripts/01_eda.py
python scripts/02_churn_modeling.py
python scripts/03_segmentation.py
```

## 📊 Deliverables

- Modelo con 82%+ AUC
- Lista de empleados de alto riesgo
- Dashboard con drill-down por departamento
- Recomendaciones de retención
