-- QUERY 1: Tickets por categoría
SELECT
    c.nombre as categoria,
    COUNT(*) as total_tickets,
    ROUND(100.0 * COUNT(*) / SUM(COUNT(*)) OVER (), 2) as porcentaje,
    ROUND(AVG(EXTRACT(EPOCH FROM (t.fecha_resolucion - t.fecha_creacion))/3600)::NUMERIC, 2) as mttr_horas
FROM tickets t
JOIN categorias c ON t.categoria_id = c.id
GROUP BY c.nombre
ORDER BY total_tickets DESC;

-- QUERY 2: Desempeño de técnicos
SELECT
    tec.nombre,
    tec.nivel,
    COUNT(*) as tickets_asignados,
    COUNT(CASE WHEN t.estado = 'Resuelto' THEN 1 END) as tickets_resueltos,
    ROUND(100.0 * COUNT(CASE WHEN t.estado = 'Resuelto' THEN 1 END) / COUNT(*), 2) as tasa_resolucion,
    ROUND(AVG(EXTRACT(EPOCH FROM (t.fecha_resolucion - t.fecha_creacion))/3600)::NUMERIC, 2) as mttr_horas
FROM tickets t
JOIN tecnicos tec ON t.tecnico_id = tec.id
WHERE t.estado = 'Resuelto'
GROUP BY tec.id, tec.nombre, tec.nivel
ORDER BY tasa_resolucion DESC;

-- QUERY 3: Cumplimiento de SLA
SELECT
    c.nombre as categoria,
    COUNT(*) as total_tickets,
    COUNT(CASE WHEN EXTRACT(EPOCH FROM (t.fecha_resolucion - t.fecha_creacion))/3600 <= sp.tiempo_resolucion_horas THEN 1 END) as cumplidos,
    ROUND(100.0 * COUNT(CASE WHEN EXTRACT(EPOCH FROM (t.fecha_resolucion - t.fecha_creacion))/3600 <= sp.tiempo_resolucion_horas THEN 1 END) / COUNT(*), 2) as tasa_cumplimiento
FROM tickets t
JOIN categorias c ON t.categoria_id = c.id
JOIN sla_policies sp ON c.id = sp.categoria_id AND t.prioridad = sp.prioridad
WHERE t.estado = 'Resuelto'
GROUP BY c.nombre, c.id
ORDER BY tasa_cumplimiento DESC;

-- QUERY 4: Distribución por prioridad
SELECT
    prioridad,
    COUNT(*) as total,
    ROUND(AVG(EXTRACT(EPOCH FROM (fecha_resolucion - fecha_creacion))/3600)::NUMERIC, 2) as mttr_horas,
    COUNT(CASE WHEN estado = 'Resuelto' THEN 1 END) as resueltos
FROM tickets
GROUP BY prioridad
ORDER BY CASE prioridad WHEN 'Crítica' THEN 1 WHEN 'Alta' THEN 2 WHEN 'Media' THEN 3 WHEN 'Baja' THEN 4 END;

-- QUERY 5: Tickets por mes (análisis de tendencia)
SELECT
    DATE_TRUNC('month', fecha_creacion)::DATE as mes,
    COUNT(*) as total_tickets,
    COUNT(CASE WHEN estado = 'Resuelto' THEN 1 END) as resueltos,
    ROUND(AVG(EXTRACT(EPOCH FROM (fecha_resolucion - fecha_creacion))/3600)::NUMERIC, 2) as mttr_horas
FROM tickets
GROUP BY DATE_TRUNC('month', fecha_creacion)
ORDER BY mes DESC;
