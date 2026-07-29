-- Insertar categorías
INSERT INTO categorias (nombre, descripcion) VALUES
('Network', 'Problemas de conectividad y red'),
('Hardware', 'Problemas de equipos físicos'),
('Software', 'Instalación y configuración de software'),
('Email', 'Problemas de correo electrónico'),
('Passwords', 'Reset y cambio de contraseñas'),
('Acceso', 'Permisos y acceso a recursos'),
('Impresoras', 'Problemas de impresoras'),
('VPN', 'Problemas de VPN'),
('Antivirus', 'Problemas de antivirus'),
('Otros', 'Otros problemas');

-- Insertar técnicos
INSERT INTO tecnicos (nombre, email, nivel, fecha_inicio) VALUES
('Juan García', 'juan.garcia@company.com', 'Senior', '2018-03-15'),
('María López', 'maria.lopez@company.com', 'Senior', '2019-06-01'),
('Carlos Rodríguez', 'carlos.rodriguez@company.com', 'Lead', '2017-01-10'),
('Ana Martínez', 'ana.martinez@company.com', 'Junior', '2022-09-01'),
('Pedro Sánchez', 'pedro.sanchez@company.com', 'Junior', '2023-01-15'),
('Laura Fernández', 'laura.fernandez@company.com', 'Senior', '2020-02-20'),
('Diego Gómez', 'diego.gomez@company.com', 'Junior', '2023-06-01');

-- Insertar políticas SLA
INSERT INTO sla_policies (categoria_id, prioridad, tiempo_respuesta_horas, tiempo_resolucion_horas) VALUES
(1, 'Crítica', 1, 4),
(1, 'Alta', 2, 8),
(1, 'Media', 4, 24),
(2, 'Alta', 2, 8),
(2, 'Media', 4, 24),
(3, 'Media', 4, 24),
(4, 'Alta', 2, 8),
(5, 'Media', 8, 24),
(6, 'Alta', 2, 8);
