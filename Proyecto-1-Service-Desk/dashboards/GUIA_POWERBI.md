# Guía Paso a Paso: Crear Dashboard en Power BI

## 🎯 Meta
Crear dashboard profesional con 3 páginas y 15+ visualizaciones en 1-2 horas.

---

## PASO 1: Preparar Power BI (5 min)

### 1.1 Crear Medidas DAX

En Power BI Desktop, ve a:
- **Home** → **New Measure**

**Medida 1: Total Tickets**
```dax
Total Tickets = COUNTA(tickets[id])
```
- Formato: Número sin decimales
- Categoría: General

**Medida 2: MTTR Promedio**
```dax
MTTR Promedio = AVERAGE(tickets[mttr_horas])
```
- Formato: Número, 1 decimal
- Unidad: " horas"

**Medida 3: Tickets Resueltos**
```dax
Tickets Resueltos = COUNTIF(tickets[estado], "Resuelto")
```

**Medida 4: Tasa Resolución**
```dax
Tasa Resolucion = 
DIVIDE(
    COUNTIF(tickets[estado], "Resuelto"),
    COUNTA(tickets[id])
)
```
- Formato: Porcentaje, 1 decimal

**Medida 5: Cumplimiento SLA**
```dax
SLA Cumplimiento = 
DIVIDE(
    COUNTX(
        FILTER(tickets, tickets[mttr_horas] <= 8.5),
        tickets[id]
    ),
    COUNTA(tickets[id])
)
```
- Formato: Porcentaje

**Medida 6: Tickets Abiertos**
```dax
Tickets Abiertos = COUNTIF(tickets[estado], "Abierto")
```

---

## PASO 2: Crear PÁGINA 1 - Resumen Ejecutivo (30 min)

### 2.1 Crear página

- **Home** → **New Page**
- Nombra: "Resumen"
- Tamaño: 1920 x 1080

### 2.2 Crear KPI Cards (Fila 1)

Inserta 4 **Cards** (Insertar → Card):

**Card 1: Total Tickets**
1. Selecciona **Insert** → **Card**
2. Arrastra **Total Tickets** al campo Value
3. Format:
   - Background: Azul (#0078D4)
   - Font: Blanco, Talla 40
   - Title: "Total Tickets"
   - Posición: Esquina superior izquierda

**Card 2: MTTR Promedio**
1. Insert → Card
2. Arrastra **MTTR Promedio** al Value
3. Format:
   - Background: Verde (#70AD47)
   - Font: Blanco, Talla 40
   - Posición: Segunda columna

**Card 3: Cumplimiento SLA**
1. Insert → Card
2. Medida: **SLA Cumplimiento**
3. Format:
   - Background: Naranja (#F7B500)
   - Font: Negro
   - Posición: Tercera columna

**Card 4: Tickets Abiertos**
1. Insert → Card
2. Medida: **Tickets Abiertos**
3. Format:
   - Background: Rojo (#E74C3C)
   - Font: Blanco
   - Posición: Cuarta columna

---

### 2.3 Crear Gráficos (Fila 2)

**Gráfico 1: Tickets por Categoría (Barras Horizontales)**

1. **Insert** → **Stacked Bar Chart**
2. Axis (Y): `categorias[nombre]`
3. Value (X): `COUNT(tickets[id])`
4. Format:
   - Data labels: ON (valores dentro)
   - Sort: Descendente por Value
   - Show legend: No
   - Color: Azul (#0078D4)
5. Posición: Abajo izquierda, tamaño grande
6. Title: "Tickets por Categoría (Top 5)"

**Datos esperados:**
```
Network: 2,800
Hardware: 2,100
Software: 1,500
Email: 1,200
Passwords: 1,200
```

---

**Gráfico 2: Distribución por Estado (Donut)**

1. **Insert** → **Pie Chart** (change to Donut)
2. Legend (Rings): `tickets[estado]`
3. Values: `COUNT(tickets[id])`
4. Format:
   - Data labels: Percent
   - Colors:
     - Abierto: Rojo (#E74C3C)
     - En Progreso: Amarillo (#FFE662)
     - Resuelto: Verde (#70AD47)
     - Cerrado: Gris (#808080)
5. Posición: Segunda columna, fila 2
6. Title: "Estado de Tickets"

---

**Gráfico 3: Tendencia Mensual (Líneas)**

1. **Insert** → **Line Chart**
2. Axis: `tickets[fecha_creacion]` (Agrupar: Month)
3. Legend: Agrega 2 valores:
   - Value 1: `COUNT(tickets[id])` → Nombre: "Creados"
   - Value 2: `Tickets Resueltos` → Nombre: "Resueltos"
4. Format:
   - Show legend: Abajo
   - Data labels: ON
   - Line style: Suave
5. Posición: Abajo derecha, ancho 2 columnas
6. Title: "Tendencia Mensual"

---

**Gráfico 4: MTTR por Categoría (Barras)**

1. **Insert** → **Clustered Column Chart**
2. Axis: `categorias[nombre]`
3. Value: `AVERAGE(tickets[mttr_horas])`
4. Format:
   - Data labels: ON (valores encima)
   - Color: Verde (#70AD47)
   - Y-axis reference line: 8.5 (meta)
5. Posición: Abajo centro-derecha
6. Title: "MTTR por Categoría"

---

## PASO 3: Crear PÁGINA 2 - Desempeño (20 min)

### 3.1 Nueva página

- **Home** → **New Page**
- Nombre: "Técnicos"

### 3.2 Crear Tabla de Técnicos

1. **Insert** → **Table**
2. Columnas:
   - `tecnicos[nombre]` → "Técnico"
   - `tecnicos[nivel]` → "Nivel"
   - `COUNT(tickets[id])` → "Total Tickets"
   - `AVERAGE(tickets[mttr_horas])` → "MTTR (h)"
   - `Tasa Resolucion` → "Resolución %"

3. Format:
   - Tamaño de fuente: 11px
   - Alternancia de colores: ON
   - Formato condicional en MTTR:
     - < 8: Verde
     - 8-10: Amarillo
     - > 10: Rojo

4. Posición: Arriba, ancho completo

---

### 3.3 Crear Gráficos (Fila 2)

**Gráfico 1: MTTR por Técnico**
1. Insert → Clustered Column Chart
2. Axis: `tecnicos[nombre]` (Top 7)
3. Value: `AVERAGE(tickets[mttr_horas])`
4. Posición: Abajo izquierda

**Gráfico 2: Tasa de Resolución (Gauge)**
1. Insert → Gauge
2. Value: `Tasa Resolucion`
3. Target: 0.94 (94%)
4. Format:
   - Min: 0, Max: 1
   - Color: Verde si > 0.90
5. Posición: Abajo centro-izquierda

**Gráfico 3: Tickets por Nivel**
1. Insert → Clustered Column Chart
2. Axis: `tecnicos[nivel]`
3. Value: `COUNT(tickets[id])`
4. Posición: Abajo centro

**Gráfico 4: Tendencia MTTR**
1. Insert → Line Chart
2. Axis: `fecha_creacion` (Día)
3. Value: `AVERAGE(tickets[mttr_horas])`
4. Trend line: 7-day moving average
5. Posición: Abajo derecha

---

## PASO 4: Crear PÁGINA 3 - SLA y Análisis (15 min)

### 4.1 Nueva página

- **Home** → **New Page**
- Nombre: "SLA"

### 4.2 KPI - Cumplimiento SLA

1. Insert → Card
2. Value: `SLA Cumplimiento`
3. Format:
   - Background: Azul (#0078D4)
   - Font: 48px
   - Title: "SLA Cumplimiento Global"

---

### 4.3 Tabla - Cumplimiento por Categoría

1. Insert → Table
2. Columnas:
   - `categorias[nombre]`
   - `COUNT(tickets[id])` → Total
   - `SLA Cumplimiento` → % (barra de progreso)

3. Posición: Centro, ancho completo

---

### 4.4 Gráficos

**Gráfico 1: Por Prioridad**
1. Insert → Stacked Column Chart
2. Axis: `tickets[prioridad]`
3. Value: `COUNT(tickets[id])`
4. Colores:
   - Crítica: Rojo
   - Alta: Naranja
   - Media: Amarillo
   - Baja: Verde

**Gráfico 2: Tickets Pendientes**
1. Insert → Card
2. Value: `Tickets Pendientes`
3. Format: Rojo si > 100

**Gráfico 3: MTTR por Prioridad**
1. Insert → Table
2. Mostrar: Prioridad, MTTR, Total Tickets

---

## PASO 5: Aplicar Formato Visual (15 min)

### 5.1 Colores de Fondo

Para todas las páginas:
- **View** → **Theme** → Selecciona tema profesional
- O personaliza con colores corporativos

### 5.2 Agregar Filtros Globales

En cada página:
1. **Insert** → **Slicer**
2. Filtros útiles:
   - Fecha (fecha_creacion)
   - Categoría (categorias[nombre])
   - Técnico (tecnicos[nombre])

3. Posición: Arriba de las visualizaciones

---

## PASO 6: Guardar y Publicar (5 min)

### 6.1 Guardar localmente

1. **File** → **Save As**
2. Nombre: `service_desk.pbix`
3. Ubicación: `Proyecto-1-Service-Desk/dashboards/`

### 6.2 Publicar en Power BI Service (Opcional)

1. **Home** → **Publish**
2. Selecciona workspace
3. URL pública: `https://app.powerbi.com`

---

## ✅ CHECKLIST FINAL

Antes de considerar "completado":

- [ ] Página 1 - Resumen: 4 KPI cards + 4 gráficos
- [ ] Página 2 - Técnicos: 1 tabla + 4 gráficos
- [ ] Página 3 - SLA: 1 KPI + 1 tabla + 3 gráficos
- [ ] Colores consistentes en todas las páginas
- [ ] Filtros interactivos funcionando
- [ ] Datos se actualizan correctamente
- [ ] Guardado como `service_desk.pbix`
- [ ] Verificado en resolución 1920x1080

---

## 🎯 Tiempo Estimado

| Tarea | Tiempo |
|-------|--------|
| Crear Medidas DAX | 5 min |
| Página 1 - Resumen | 30 min |
| Página 2 - Técnicos | 20 min |
| Página 3 - SLA | 15 min |
| Formato y refinamiento | 15 min |
| Guardar y verificar | 5 min |
| **TOTAL** | **90 min** |

---

## 💡 Tips

1. **Usa plantillas:** Copia un gráfico y modifica (más rápido)
2. **Colores:** Define una paleta y úsala siempre
3. **Nombres:** Usa nombres descriptivos en medidas DAX
4. **Testing:** Verifica filtros cruzados entre páginas
5. **Performance:** Si es lento, reduce datos o agrupa por mes

---

## 🚨 Si Hay Errores

**Error: "Column not found"**
- Verifica que la tabla está cargada en Power Query
- Recarga datos: Data → Refresh

**Error: "DAX formula invalid"**
- Copia exactamente desde DASHBOARD_SPEC.md
- Verifica nombres de columnas coincidan

**Gráficos vacios:**
- Verifica que hay datos en PostgreSQL
- Ejecuta: `SELECT COUNT(*) FROM tickets;`

---

¿Empiezas con Paso 1? 👇
