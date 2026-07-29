# Proyecto 5: Predicción de Riesgo de Enfermedades - Salud

## 📋 Descripción

Modelo de machine learning para predicción de diabetes y enfermedades cardiacas usando datos públicos UCI.

## 🎯 Objetivos

1. Predecir riesgo de diabetes (AUC > 0.85)
2. Predecir enfermedad cardiaca (AUC > 0.82)
3. Identificar factores de riesgo clave
4. Crear score de riesgo por paciente
5. Generar recomendaciones de prevención

## 📊 Datasets

### Diabetes
- 768 pacientes, 8 variables
- Objetivo: Diagnóstico (0/1)
- Variables: Glucosa, presión, BMI, etc.

### Enfermedad Cardiaca
- 303 pacientes, 13 variables
- Objetivo: Presencia de enfermedad (0/1)
- Variables: Edad, colesterol, ECG, etc.

## 📈 Modelos

| Modelo | Diabetes | Cardiacas | Time |
|--------|----------|-----------|------|
| Logistic | 0.78 | 0.75 | <1s |
| Random Forest | 0.82 | 0.84 | 5s |
| XGBoost | 0.84 | 0.86 | 8s |
| **LightGBM** | **0.85** | **0.87** | 3s |

## 🛠️ Análisis

1. **EDA y Visualización**
   - Distribución de variables
   - Correlaciones
   - Imbalance analysis

2. **Feature Engineering**
   - Interaction terms
   - Polynomial features
   - Scaling y normalization

3. **Model Comparison**
   - Cross-validation
   - Hyperparameter tuning
   - Ensemble methods

4. **Interpretability**
   - Feature importance
   - SHAP values
   - Decision rules

## 📁 Estructura

```
Proyecto-5-Salud/
├── data/
│   ├── diabetes.csv
│   └── heart.csv
├── scripts/
│   ├── 01_eda.py
│   ├── 02_preprocessing.py
│   ├── 03_modeling.py
│   ├── 04_evaluation.py
│   └── utils.py
└── models/
    └── (modelos guardados)
```

## 🚀 Ejecución

```bash
python scripts/01_eda.py
python scripts/02_preprocessing.py
python scripts/03_modeling.py
python scripts/04_evaluation.py
```

## 📊 Deliverables

- 2 modelos de predicción (AUC > 0.85)
- Comparativa de algoritmos
- Feature importance ranking
- ROC curves y matrices de confusión
- Recomendaciones clínicas
