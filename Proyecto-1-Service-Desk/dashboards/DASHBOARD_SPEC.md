# Dashboard Specifications - Service Desk

## 📋 Configuración del Dashboard

**Nombre archivo:** `service_desk.pbix`  
**Páginas:** 3  
**Formato:** 1920x1080 (Desktop)  

---

## 📄 PÁGINA 1: RESUMEN EJECUTIVO

### Layout: 2 Filas x 4 Columnas

#### ROW 1: KPI Cards (4 tarjetas grandes)

**Tarjeta 1: Total Tickets**
- Valor: `COUNTA(tickets[id])`
- Formato: Número sin decimales
- Color fondo: Azul
- Tamaño: Grande

**Tarjeta 2: MTTR Promedio (horas)**
- Valor: `AVERAGE(tickets[mttr_horas])`
- Formato: 1 decimal
- Unidad: " horas"
- Color fondo: Verde

**Tarjeta 3: Cumplimiento SLA**
- Valor: Porcentaje de tickets cumplidos
- Formato: 0%
- Color fondo: Naranja
- Meta: 92%

**Tarjeta 4: Tickets Abiertos**
- Valor: `COUNTIF(tickets[estado] = "Abierto")`
- Formato: Número
- Color fondo: Rojo
- Alerta si > 5%

---

#### ROW 2: Gráficos Principales (2x2)

**Gráfico 1: Tickets por Categoría (Top 5)**
- Tipo: Gráfico de barras horizontal
- Eje X: COUNT(tickets)
- Eje Y: categorias[nombre]
- Filtro: Top 5 categorías
- Ordenar por: Descendente
- Tamaño: Grande

**Query SQL:**
```sql
SELECT
    c.nombre as Categoria,
    COUNT(*) as Total_Tickets
FROM tickets t
JOIN categorias c ON t.categoria_id = c.id
GROUP BY c.nombre
ORDER BY Total_Tickets DESC
LIMIT 5;
```

---

**Gráfico 2: Distribución por Estado**
- Tipo: Gráfico de donut
- Valores: COUNT(tickets)
- Leyenda: estado
- Colores: Abierto=Rojo, En Progreso=Amarillo, Resuelto=Verde, Cerrado=Gris
- Tamaño: Medio

**Query SQL:**
```sql
SELECT
    estado as Estado,
    COUNT(*) as Total
FROM tickets
GROUP BY estado;
```

---

**Gráfico 3: Trend Mensual**
- Tipo: Gráfico de líneas
- Eje X: Mes (fecha_creacion)
- Eje Y: COUNT(tickets)
- Línea 2: COUNT si estado='Resuelto'
- Período: Últimos 12 meses
- Tamaño: Grande (2 columnas)

**Query SQL:**
```sql
SELECT
    DATE_TRUNC('month', fecha_creacion)::DATE as Mes,
    COUNT(*) as Total_Creados,
    COUNT(CASE WHEN estado = 'Resuelto' THEN 1 END) as Total_Resueltos
FROM tickets
GROUP BY DATE_TRUNC('month', fecha_creacion)
ORDER BY Mes DESC
LIMIT 12;
```

---

**Gráfico 4: MTTR por Categoría**
- Tipo: Gráfico de barras vertical
- Eje X: categorias[nombre]
- Eje Y: AVG(mttr_horas)
- Línea de meta: 8.5 horas
- Tamaño: Medio

**Query SQL:**
```sql
SELECT
    c.nombre as Categoria,
    ROUND(AVG(EXTRACT(EPOCH FROM (t.fecha_resolucion - t.fecha_creacion))/3600)::NUMERIC, 2) as MTTR_Horas
FROM tickets t
JOIN categorias c ON t.categoria_id = c.id
WHERE t.estado = 'Resuelto'
GROUP BY c.nombre
ORDER BY MTTR_Horas DESC;
```

---

## 📄 PÁGINA 2: DESEMPEÑO DE TÉCNICOS

### Layout: 2 Filas

#### ROW 1: Tabla de Técnicos (Ancho completo)

**Visualización: Tabla Interactiva**
- Columnas:
  1. Nombre (tecnico[nombre])
  2. Nivel (tecnico[nivel])
  3. Tickets Resueltos (COUNTIF estado='Resuelto')
  4. MTTR Promedio (AVERAGE mttr_horas)
  5. Tasa Resolución (%)
  6. Tickets Pendientes (COUNTIF estado='En Progreso')

- Ordenar por: Tickets Resueltos DESC
- Formato condicional: Columna MTTR (Verde < 8, Amarillo 8-10, Rojo > 10)
- Tamaño: Grande

**Query SQL:**
```sql
SELECT
    tec.nombre as Tecnico,
    tec.nivel as Nivel,
    COUNT(CASE WHEN t.estado = 'Resuelto' THEN 1 END) as Tickets_Resueltos,
    ROUND(AVG(EXTRACT(EPOCH FROM (t.fecha_resolucion - t.fecha_creacion))/3600)::NUMERIC, 2) as MTTR_Horas,
    ROUND(100.0 * COUNT(CASE WHEN t.estado = 'Resuelto' THEN 1 END) / COUNT(*), 2) as Tasa_Resolucion,
    COUNT(CASE WHEN t.estado = 'En Progreso' THEN 1 END) as Tickets_Pendientes
FROM tickets t
LEFT JOIN tecnicos tec ON t.tecnico_id = tec.id
GROUP BY tec.id, tec.nombre, tec.nivel
ORDER BY Tickets_Resueltos DESC;
```

---

#### ROW 2: Gráficos de Desempeño (2x2)

**Gráfico 1: MTTR por Técnico (Top 7)**
- Tipo: Gráfico de barras
- Eje X: Técnico
- Eje Y: MTTR (horas)
- Ordenar por: MTTR DESC
- Tamaño: Medio

**Gráfico 2: Tasa de Resolución**
- Tipo: Indicador (gauge)
- Valor: Promedio de Tasa_Resolucion
- Min: 0%, Max: 100%
- Meta: 94%
- Tamaño: Pequeño

**Gráfico 3: Tickets por Nivel**
- Tipo: Gráfico de barras
- Eje X: tecnico[nivel]
- Eje Y: COUNT(tickets)
- Colores distintos por nivel
- Tamaño: Medio

**Gráfico 4: Tiempo de Respuesta**
- Tipo: Gráfico de líneas
- Eje X: Fecha
- Eje Y: MTTR (promedio móvil 7 días)
- Tamaño: Medio

---

## 📄 PÁGINA 3: SLA Y ANÁLISIS DETALLADO

### Layout: 2 Filas

#### ROW 1: Cumplimiento de SLA

**Tarjeta: SLA Overall**
- Valor: % cumplimiento global
- Meta: 92%
- Color: Verde si > 90%, Amarillo si 80-90%, Rojo si < 80%

**Gráfico: Cumplimiento por Categoría**
- Tipo: Tabla
- Columnas:
  1. Categoría
  2. Total Tickets
  3. Cumplidos
  4. % Cumplimiento (barra de progreso)
- Ordenar: % Cumplimiento DESC
- Tamaño: Grande (ancho completo)

**Query SQL:**
```sql
SELECT
    c.nombre as Categoria,
    COUNT(*) as Total,
    COUNT(CASE WHEN EXTRACT(EPOCH FROM (t.fecha_resolucion - t.fecha_creacion))/3600 <= sp.tiempo_resolucion_horas THEN 1 END) as Cumplidos,
    ROUND(100.0 * COUNT(CASE WHEN EXTRACT(EPOCH FROM (t.fecha_resolucion - t.fecha_creacion))/3600 <= sp.tiempo_resolucion_horas THEN 1 END) / COUNT(*), 2) as Porcentaje
FROM tickets t
JOIN categorias c ON t.categoria_id = c.id
JOIN sla_policies sp ON c.id = sp.categoria_id AND t.prioridad = sp.prioridad
WHERE t.estado = 'Resuelto'
GROUP BY c.nombre
ORDER BY Porcentaje DESC;
```

---

#### ROW 2: Análisis Complementario

**Gráfico 1: Distribución por Prioridad**
- Tipo: Gráfico de barras
- Eje X: prioridad
- Eje Y: COUNT(tickets)
- Colores: Crítica=Rojo, Alta=Naranja, Media=Amarillo, Baja=Verde
- Tamaño: Medio

**Gráfico 2: Tickets sin Resolver**
- Tipo: Indicador
- Valor: COUNT(estado != 'Resuelto')
- Subtext: "pendientes de resolver"
- Color: Rojo si > 100
- Tamaño: Pequeño

**Gráfico 3: Tiempo Promedio por Prioridad**
- Tipo: Tabla
- Columnas: Prioridad, MTTR, # Tickets
- Tamaño: Medio

**Query SQL:**
```sql
SELECT
    prioridad as Prioridad,
    ROUND(AVG(EXTRACT(EPOCH FROM (fecha_resolucion - fecha_creacion))/3600)::NUMERIC, 2) as MTTR_Horas,
    COUNT(*) as Total_Tickets
FROM tickets
WHERE estado = 'Resuelto'
GROUP BY prioridad;
```

---

## 🎨 Colores Consistentes

| Elemento | Color | Hex |
|----------|-------|-----|
| Crítica | Rojo Oscuro | #C5504A |
| Alta | Naranja | #F7B500 |
| Media | Amarillo | #FFE662 |
| Baja | Verde Claro | #70AD47 |
| Positivo | Verde | #00B050 |
| Negativo | Rojo | #E74C3C |
| Neutral | Gris | #808080 |

---

## 📊 Medidas DAX Necesarias

```dax
// Medida 1: Total Tickets
Total Tickets = COUNTA(tickets[id])

// Medida 2: MTTR Promedio
MTTR Promedio = AVERAGE(tickets[mttr_horas])

// Medida 3: SLA Cumplimiento
SLA Cumplimiento = 
DIVIDE(
    COUNTIF(tickets[mttr_horas] <= RELATED(sla_policies[tiempo_resolucion_horas])),
    COUNTA(tickets[id]),
    0
)

// Medida 4: Tickets Abiertos
Tickets Abiertos = COUNTIF(tickets[estado], "Abierto")

// Medida 5: Tasa Resolución
Tasa Resolucion = 
DIVIDE(
    COUNTIF(tickets[estado], "Resuelto"),
    COUNTA(tickets[id]),
    0
)

// Medida 6: Tickets Pendientes
Tickets Pendientes = COUNTIF(tickets[estado], <> "Resuelto")
```

---

## 🔄 Refresh Schedule

- **Tipo:** Automático
- **Frecuencia:** Cada hora
- **Hora punta:** 8-18 (cada 15 min)
- **Hora valle:** 19-7 (cada 4 horas)

---

## ✅ Checklist Final

- [ ] 3 páginas creadas
- [ ] 15+ visualizaciones
- [ ] Colores consistentes
- [ ] Filtros interactivos
- [ ] Medidas DAX funcionando
- [ ] Conexión PostgreSQL activa
- [ ] Datos se refrescan correctamente
- [ ] Mobile preview funciona
- [ ] Guardado como `service_desk.pbix`
