-- Script para generar 10,000 tickets de ejemplo
-- Ejecutar DESPUÉS de cargar los scripts 01, 02 y 03

-- Generar tickets de ejemplo (función para insertar en bucles)
DO $$
DECLARE
    v_fecha_inicio DATE := '2023-01-01';
    v_fecha_fin DATE := '2024-12-31';
    v_contador INTEGER := 0;
    v_fecha_creacion TIMESTAMP;
    v_fecha_resolucion TIMESTAMP;
    v_dias_aleatorio INTEGER;
    v_horas_aleatorias INTEGER;
BEGIN
    WHILE v_contador < 10000 LOOP
        -- Generar fecha aleatoria entre inicio y fin
        v_fecha_creacion := v_fecha_inicio + (RANDOM() * (v_fecha_fin - v_fecha_inicio));

        -- Generar duración aleatoria (1 a 120 horas)
        v_horas_aleatorias := FLOOR(RANDOM() * 119) + 1;
        v_fecha_resolucion := v_fecha_creacion + (v_horas_aleatorias || ' hours')::INTERVAL;

        INSERT INTO tickets (
            numero_ticket,
            fecha_creacion,
            fecha_resolucion,
            categoria_id,
            tecnico_id,
            prioridad,
            estado,
            descripcion
        ) VALUES (
            'TKT-' || LPAD(v_contador::TEXT, 6, '0'),
            v_fecha_creacion,
            v_fecha_resolucion,
            FLOOR(RANDOM() * 10) + 1,  -- categoria_id 1-10
            FLOOR(RANDOM() * 7) + 1,   -- tecnico_id 1-7
            (ARRAY['Baja', 'Media', 'Alta', 'Crítica'])[FLOOR(RANDOM() * 4) + 1],
            'Resuelto',
            'Descripción de ticket de prueba ' || v_contador
        );

        v_contador := v_contador + 1;

        -- Mostrar progreso cada 1000 registros
        IF v_contador % 1000 = 0 THEN
            RAISE NOTICE 'Insertados % tickets', v_contador;
        END IF;
    END LOOP;
END $$;

-- Actualizar el updated_at para todos los registros
UPDATE tickets SET updated_at = CURRENT_TIMESTAMP;

-- Verificar el resultado
SELECT
    COUNT(*) as total_tickets,
    MIN(fecha_creacion) as fecha_inicio,
    MAX(fecha_creacion) as fecha_fin,
    COUNT(DISTINCT categoria_id) as categorias,
    COUNT(DISTINCT tecnico_id) as tecnicos
FROM tickets;
