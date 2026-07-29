# Proyecto 8: Dashboard Master Ejecutivo

## 📋 Descripción

Dashboard unificado que integra datos de los 7 proyectos anteriores. Demuestra expertise en:

- **Power BI avanzado** (DAX, Power Query)
- **Data Modeling** (Star Schema)
- **Storytelling** con datos
- **Performance Optimization**

## 🎯 Objetivos

1. Dashboard ejecutivo centralizado
2. Integración de 7+ fuentes de datos
3. KPIs en tiempo real (near real-time)
4. Interactividad y drill-down
5. Mobile-ready

## 📊 Estructura del Dashboard

### Portada Ejecutiva
**4 Tarjetas KPI principales:**
- Revenue Total (Retail)
- Predicción de Churn (HR)
- MTTR Promedio (Service Desk)
- Riesgo Crediticio (Banco)

### Pestaña 1: Operaciones
- Service Desk: MTTR, SLA, tickets por categoría
- HR: Rotación, satisfacción, headcount
- Gráficos: Tendencias mensuales

### Pestaña 2: Finanzas
- Revenue por línea de negocio
- Profitabilidad por producto
- Riesgo crediticio y cobranza

### Pestaña 3: Clientes
- Análisis de segmentación (Retail)
- Customer Lifetime Value
- Churn vs Retention

### Pestaña 4: Predicciones
- Forecasting de ventas
- Riesgo crediticio scores
- Churn predictions

### Pestaña 5: Detalles
- Drill-down a transacciones
- Tablas de referencia
- Data exploration libre

## 🛠️ Componentes Power BI

### Data Model
- **Tablas de Hechos:** 5 (ventas, tickets, empleados, préstamos, pacientes)
- **Tablas de Dimensiones:** 8 (tiempo, geografía, producto, etc.)
- **Relaciones:** Star Schema

### Medidas DAX

```dax
Total Revenue = SUM(Sales[Amount])
YoY Growth = DIVIDE([Current Year], [Prior Year]) - 1
Customer Churn Risk = CALCULATE(COUNTROWS(Employees), Employees[Churn] = 1)
Average SLA Compliance = AVERAGE(Tickets[SLA_Met])
```

### Visualizaciones (20+)
- 📊 Gráficos de líneas (tendencias)
- 📊 Barras (comparativas)
- 🥧 Donuts (proporciones)
- 🗺️ Mapas (geográfico)
- 📈 Dispersión (correlaciones)
- 📋 Tablas (detalles)
- 🎯 Indicadores (KPIs)

## 📁 Estructura

```
Proyecto-8-Dashboard/
├── powerbi/
│   ├── dashboard_master.pbix
│   ├── data_model.pptx (documentación)
│   └── dax_formulas.txt
├── data/
│   ├── connections.json
│   └── refresh_schedule.txt
└── README.md
```

## 🔄 Conexiones de Datos

```
PostgreSQL (Proyecto 1-7)
    ↓
Power BI Desktop
    ↓
Import (Refresh diario)
    ↓
Cloud (Power BI Service)
    ↓
Acceso Web/Mobile
```

## 🎨 Diseño

- **Color Scheme:** Profesional corporativo
- **Tipografía:** Clara y legible
- **Layout:** Responsive, mobile-first
- **Accesibilidad:** Contraste alto, alt text

## 📊 Ejemplos de Análisis

**Pregunta 1:** "¿Qué producto genera más ROI?"
→ Retail + Finanzas → Rentabilidad por SKU

**Pregunta 2:** "¿Quién es mi cliente de más valor?"
→ Retail + HR → Segmentación RFM + Empleado asignado

**Pregunta 3:** "¿Dónde va a estar el problema en 3 meses?"
→ Predicciones + Alertas → Churn/Carga/Riesgo

## 🚀 Interactividad

1. **Filtros Globales:**
   - Período (mes, trimestre, año)
   - Región
   - Tipo de producto

2. **Drill-Down:**
   - Región → Provincia → Ciudad
   - Trimestre → Mes → Día

3. **Bookmarks:**
   - Vista ejecutiva (3 minutos)
   - Vista análitica (30 minutos)
   - Vista operativa (exploración)

## 📱 Mobile Experience

- Versión móvil optimizada
- Menos gráficos, más tablas
- Botones grandes
- Scroll horizontal/vertical

## ⚡ Performance

- **Datos importados:** 5M registros
- **Tiempo carga:** < 3 segundos
- **Refresh:** 1 hora
- **Usuarios simultáneos:** 50+

## 📈 Resultados

Dashboard completo que permite:
- ✅ Toma de decisiones en segundos
- ✅ Identificar oportunidades
- ✅ Detectar problemas temprano
- ✅ Trackear progress de objetivos

## 🎓 Skills Demostrados

- ✅ Power BI Avanzado
- ✅ DAX Reporting
- ✅ Data Modeling
- ✅ Business Intelligence
- ✅ Design UX
- ✅ Storytelling
