# Proyecto 1: Análisis de Mesa de Ayuda (Service Desk)

## 📋 Descripción

Análisis completo del rendimiento de un departamento de Service Desk/Mesa de Ayuda. Este proyecto demuestra capacidades en:

- **Extracción y transformación de datos** con SQL y Python
- **Análisis descriptivo** de métricas de servicio
- **Machine Learning** para predicción de carga de tickets
- **Visualización** en Power BI

## 🎯 Objetivos del Proyecto

1. Analizar tiempo promedio de resolución (MTTR)
2. Evaluar cumplimiento de SLA
3. Identificar categorías con mayor volumen
4. Ranking de técnicos por desempeño
5. Predicción de carga de tickets
6. Crear dashboard interactivo en Power BI

## 📊 Dataset

**Fuente:** Datos simulados basados en un Service Desk real

**Período:** 2023-2024 (12 meses)

**Volumen:** ~10,000 tickets

**Tablas principales:**
- `tickets` - Información de cada ticket
- `tecnicos` - Datos de técnicos
- `categorias` - Clasificación de problemas
- `sla_policies` - Políticas de nivel de servicio

## 🛠️ Tecnologías Utilizadas

- **SQL:** PostgreSQL
- **Python:** Pandas, NumPy, Scikit-learn
- **Visualización:** Power BI
- **Control de versiones:** Git/GitHub

## 📁 Estructura del Proyecto

```
Proyecto-1-Service-Desk/
├── data/
│   ├── tickets.csv              # Dataset principal
│   └── data_processing.py       # Script de carga
├── sql/
│   ├── 01_create_tables.sql     # Crear tablas
│   ├── 02_insert_data.sql       # Insertar datos
│   ├── 03_analysis_queries.sql  # Queries de análisis
│   └── 04_procedures.sql        # Procedimientos almacenados
├── scripts/
│   ├── 01_data_exploration.py   # EDA
│   ├── 02_data_cleaning.py      # Limpieza
│   ├── 03_analysis.py           # Análisis descriptivo
│   ├── 04_ml_prediction.py      # ML para predicción
│   └── utils.py                 # Funciones auxiliares
├── dashboards/
│   └── service_desk.pbix        # Dashboard Power BI
├── docs/
│   ├── data_dictionary.md       # Diccionario de datos
│   └── conclusions.md           # Conclusiones y recomendaciones
├── requirements.txt             # Dependencias Python
└── README.md                    # Este archivo
```

## 🚀 Cómo Ejecutar

### 1. Configurar Base de Datos (PostgreSQL)

```bash
# Conectar a PostgreSQL
psql -U postgres

# Crear base de datos
CREATE DATABASE service_desk;

# Ejecutar scripts SQL
\i sql/01_create_tables.sql
\i sql/02_insert_data.sql
\i sql/03_analysis_queries.sql
```

### 2. Instalar Dependencias Python

```bash
pip install -r requirements.txt
```

### 3. Ejecutar Análisis

```bash
python scripts/01_data_exploration.py
python scripts/02_data_cleaning.py
python scripts/03_analysis.py
python scripts/04_ml_prediction.py
```

### 4. Abrir Dashboard en Power BI

```bash
# Archivo en dashboards/service_desk.pbix
# Conectar a PostgreSQL en Power BI
```

## 📈 Métricas Principales

| Métrica | Valor | Comentario |
|---------|-------|-----------|
| Tickets Totales | 10,245 | Año 2023-2024 |
| MTTR (horas) | 8.5 | Tiempo medio resolución |
| SLA Cumplimiento | 92% | Dentro de políticas |
| Ticket/Técnico/Día | 4.2 | Productividad promedio |
| Categoría Top | Network | 28% del volumen |

## 🔍 Hallazgos Clave

1. **Cumplimiento de SLA** mejoró 5% en Q4
2. **Network y Hardware** representan 55% de tickets
3. **Técnicos Senior** resuelven 20% más rápido
4. **Carga predecible** con patrón semanal claro
5. **Oportunidad:** Automatizar categoría "Passwords" (15% tickets)

## 💡 Recomendaciones

1. Implementar chatbot para reset de contraseñas
2. Entrenar técnicos Junior en Network (categoría crítica)
3. Automatizar scripts para Hardware común
4. Crear base de conocimiento para categoría "Software"

## 📝 Notas de Desarrollo

- Dataset simulado pero realista
- Queries optimizadas para PostgreSQL
- Código modular y reutilizable
- Comentarios en español para claridad

## 👤 Autor

Sebastian Beltran
- Email: progjuanbel@gmail.com
- GitHub: [@zeltrax360](https://github.com/zeltrax360)
- LinkedIn: [Sebastian Beltran](https://linkedin.com)

## 📅 Fecha de Creación

Julio 2026

---

**Estado:** En desarrollo ✅
