# Proyecto 2: Análisis de Riesgo de Crédito (Banco)

## 📋 Descripción

Análisis predictivo de riesgo de impago en una cartera de préstamos bancarios. Este proyecto demuestra:

- **Feature Engineering** en datos financieros
- **Modelado Predictivo** con múltiples algoritmos
- **Evaluación de Modelos** (ROC, AUC, Precisión)
- **Business Intelligence** - Impacto financiero

## 🎯 Objetivos

1. Predecir clientes con riesgo de impago
2. Identificar variables más influyentes
3. Calcular probabilidad de default
4. Estimar pérdida esperada por cliente
5. Crear estrategia de cobro

## 📊 Dataset

**Fuente:** Datos simulados de cartera de préstamos

**Tamaño:** 50,000 clientes | 30 variables

**Variables principales:**
- Datos demográficos (edad, ingresos, estado civil)
- Historial crediticio (score, deuda anterior)
- Características del préstamo (monto, plazo, tasa)
- Target: Default (0/1)

## 🛠️ Tecnologías

- Python: scikit-learn, XGBoost, LightGBM
- SQL: PostgreSQL (análisis exploratorio)
- Visualización: Plotly, Matplotlib
- Power BI: Dashboard de riesgo

## 📈 Modelos Entrenados

1. **Logistic Regression** - Baseline
2. **Random Forest** - Mejor precisión
3. **XGBoost** - Mejor AUC
4. **LightGBM** - Más rápido

## 🔍 KPIs Esperados

| Métrica | Target |
|---------|--------|
| AUC Score | > 0.85 |
| Precisión | > 0.80 |
| Recall | > 0.75 |
| F1-Score | > 0.77 |

## 📁 Estructura

```
Proyecto-2-Banco/
├── data/
│   ├── loans.csv
│   └── data_prep.py
├── scripts/
│   ├── 01_eda.py
│   ├── 02_feature_engineering.py
│   ├── 03_model_training.py
│   ├── 04_evaluation.py
│   └── utils.py
├── models/
│   └── (modelos guardados)
├── dashboards/
│   └── credit_risk.pbix
├── docs/
│   └── model_card.md
└── README.md
```

## 🚀 Cómo Usar

```bash
pip install -r ../requirements.txt
python scripts/01_eda.py
python scripts/02_feature_engineering.py
python scripts/03_model_training.py
```

## 📊 Resultados Esperados

- Modelos entrenados con AUC > 0.85
- Identificación de top 5 variables de riesgo
- Segmentación de clientes por perfil de riesgo
- Dashboard interactivo en Power BI

## 👤 Autor

Sebastian Beltran | Data Scientist
