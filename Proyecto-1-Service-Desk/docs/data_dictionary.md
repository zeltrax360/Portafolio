# Diccionario de Datos - Service Desk

## Tabla: tickets

| Campo | Tipo | Descripción |
|-------|------|-------------|
| id | SERIAL | Identificador único |
| numero_ticket | VARCHAR(20) | Número de ticket único |
| fecha_creacion | TIMESTAMP | Fecha y hora de creación |
| fecha_resolucion | TIMESTAMP | Fecha y hora de resolución |
| categoria_id | INTEGER | Referencia a tabla categorias |
| tecnico_id | INTEGER | Referencia a tabla tecnicos |
| prioridad | VARCHAR(20) | Baja, Media, Alta, Crítica |
| estado | VARCHAR(20) | Abierto, En Progreso, Resuelto, Cerrado |
| descripcion | TEXT | Descripción del problema |
| created_at | TIMESTAMP | Timestamp de creación del registro |
| updated_at | TIMESTAMP | Timestamp de última actualización |

## Tabla: categorias

| Campo | Tipo | Descripción |
|-------|------|-------------|
| id | SERIAL | Identificador único |
| nombre | VARCHAR(50) | Nombre de la categoría (único) |
| descripcion | TEXT | Descripción detallada |
| created_at | TIMESTAMP | Timestamp de creación |

### Valores de Categoría:
- Network
- Hardware
- Software
- Email
- Passwords
- Acceso
- Impresoras
- VPN
- Antivirus
- Otros

## Tabla: tecnicos

| Campo | Tipo | Descripción |
|-------|------|-------------|
| id | SERIAL | Identificador único |
| nombre | VARCHAR(100) | Nombre del técnico |
| email | VARCHAR(100) | Email corporativo (único) |
| nivel | VARCHAR(20) | Junior, Senior, Lead |
| fecha_inicio | DATE | Fecha de inicio en empresa |
| estado | VARCHAR(20) | Activo, Inactivo |
| created_at | TIMESTAMP | Timestamp de creación |

## Tabla: sla_policies

| Campo | Tipo | Descripción |
|-------|------|-------------|
| id | SERIAL | Identificador único |
| categoria_id | INTEGER | Referencia a tabla categorias |
| prioridad | VARCHAR(20) | Baja, Media, Alta, Crítica |
| tiempo_respuesta_horas | INTEGER | Horas para primera respuesta |
| tiempo_resolucion_horas | INTEGER | Horas para resolución |
| created_at | TIMESTAMP | Timestamp de creación |

## Métricas Calculadas

### MTTR (Mean Time To Resolution)
**Fórmula:** `(fecha_resolucion - fecha_creacion) / 3600`
**Unidad:** Horas
**Descripción:** Tiempo promedio para resolver un ticket

### Cumplimiento de SLA
**Fórmula:** `MTTR <= tiempo_resolucion_horas`
**Valor:** Booleano
**Descripción:** Indica si un ticket cumple con el SLA establecido

### Tasa de Resolución
**Fórmula:** `(tickets_resueltos / tickets_totales) * 100`
**Unidad:** Porcentaje
**Descripción:** Porcentaje de tickets resueltos sobre el total
