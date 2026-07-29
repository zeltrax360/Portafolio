-- Crear base de datos
-- CREATE DATABASE service_desk;

-- Tabla de categorías
CREATE TABLE IF NOT EXISTS categorias (
    id SERIAL PRIMARY KEY,
    nombre VARCHAR(50) UNIQUE NOT NULL,
    descripcion TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Tabla de técnicos
CREATE TABLE IF NOT EXISTS tecnicos (
    id SERIAL PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE,
    nivel VARCHAR(20) CHECK (nivel IN ('Junior', 'Senior', 'Lead')),
    fecha_inicio DATE,
    estado VARCHAR(20) DEFAULT 'Activo',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Tabla de políticas SLA
CREATE TABLE IF NOT EXISTS sla_policies (
    id SERIAL PRIMARY KEY,
    categoria_id INTEGER REFERENCES categorias(id),
    prioridad VARCHAR(20) CHECK (prioridad IN ('Baja', 'Media', 'Alta', 'Crítica')),
    tiempo_respuesta_horas INTEGER,
    tiempo_resolucion_horas INTEGER,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Tabla principal de tickets
CREATE TABLE IF NOT EXISTS tickets (
    id SERIAL PRIMARY KEY,
    numero_ticket VARCHAR(20) UNIQUE NOT NULL,
    fecha_creacion TIMESTAMP NOT NULL,
    fecha_resolucion TIMESTAMP,
    categoria_id INTEGER REFERENCES categorias(id),
    tecnico_id INTEGER REFERENCES tecnicos(id),
    prioridad VARCHAR(20) CHECK (prioridad IN ('Baja', 'Media', 'Alta', 'Crítica')),
    estado VARCHAR(20) CHECK (estado IN ('Abierto', 'En Progreso', 'Resuelto', 'Cerrado')),
    descripcion TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Índices para optimización
CREATE INDEX idx_tickets_categoria ON tickets(categoria_id);
CREATE INDEX idx_tickets_tecnico ON tickets(tecnico_id);
CREATE INDEX idx_tickets_fecha ON tickets(fecha_creacion);
CREATE INDEX idx_tickets_estado ON tickets(estado);
