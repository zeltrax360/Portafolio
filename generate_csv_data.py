import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import random

# Seed para reproducibilidad
np.random.seed(42)
random.seed(42)

print("Generando datos de ejemplo...")

# ============= DATOS BASICOS =============

# Técnicos
tecnicos_data = {
    'id': [1, 2, 3, 4, 5, 6, 7],
    'nombre': ['Juan García', 'María López', 'Carlos Rodríguez', 'Ana Martínez',
               'Pedro Sánchez', 'Laura Fernández', 'Diego Gómez'],
    'email': ['juan.garcia@company.com', 'maria.lopez@company.com', 'carlos.rodriguez@company.com',
              'ana.martinez@company.com', 'pedro.sanchez@company.com', 'laura.fernandez@company.com',
              'diego.gomez@company.com'],
    'nivel': ['Senior', 'Senior', 'Lead', 'Junior', 'Junior', 'Senior', 'Junior']
}
tecnicos = pd.DataFrame(tecnicos_data)

# Categorías
categorias_data = {
    'id': range(1, 11),
    'nombre': ['Network', 'Hardware', 'Software', 'Email', 'Passwords',
               'Acceso', 'Impresoras', 'VPN', 'Antivirus', 'Otros'],
    'descripcion': [
        'Problemas de conectividad y red',
        'Problemas de equipos físicos',
        'Instalación y configuración de software',
        'Problemas de correo electrónico',
        'Reset y cambio de contraseñas',
        'Permisos y acceso a recursos',
        'Problemas de impresoras',
        'Problemas de VPN',
        'Problemas de antivirus',
        'Otros problemas'
    ]
}
categorias = pd.DataFrame(categorias_data)

# ============= GENERAR TICKETS =============

n_tickets = 10000
start_date = datetime(2023, 1, 1)
end_date = datetime(2024, 12, 31)

tickets_list = []

for i in range(n_tickets):
    # Fecha aleatoria
    delta = end_date - start_date
    random_days = random.randint(0, delta.days)
    random_hours = random.randint(0, 23)
    random_minutes = random.randint(0, 59)
    fecha_creacion = start_date + timedelta(days=random_days, hours=random_hours, minutes=random_minutes)

    # Duración aleatoria (1 a 120 horas)
    duracion_horas = random.randint(1, 120)
    fecha_resolucion = fecha_creacion + timedelta(hours=duracion_horas)

    ticket = {
        'id': i + 1,
        'numero_ticket': f'TKT-{i+1:06d}',
        'fecha_creacion': fecha_creacion.isoformat(),
        'fecha_resolucion': fecha_resolucion.isoformat(),
        'categoria_id': random.randint(1, 10),
        'tecnico_id': random.randint(1, 7),
        'prioridad': random.choice(['Baja', 'Media', 'Alta', 'Crítica']),
        'estado': 'Resuelto',
        'descripcion': f'Ticket de prueba #{i+1}',
        'mttr_horas': duracion_horas
    }
    tickets_list.append(ticket)

tickets = pd.DataFrame(tickets_list)

# ============= GUARDAR ARCHIVOS =============

# Guardar en Proyecto 1
output_path = "Proyecto-1-Service-Desk/data/"

tecnicos.to_csv(f"{output_path}tecnicos.csv", index=False, encoding='utf-8')
print(f"✓ {output_path}tecnicos.csv")

categorias.to_csv(f"{output_path}categorias.csv", index=False, encoding='utf-8')
print(f"✓ {output_path}categorias.csv")

tickets.to_csv(f"{output_path}tickets.csv", index=False, encoding='utf-8')
print(f"✓ {output_path}tickets.csv ({len(tickets)} registros)")

# ============= RESUMEN =============

print("\nRESUMEN DE DATOS:")
print(f"Total Tickets: {len(tickets)}")
print(f"MTTR Promedio: {tickets['mttr_horas'].mean():.2f} horas")
print(f"Tickets por Categoría:")
for cat_id in range(1, 11):
    count = len(tickets[tickets['categoria_id'] == cat_id])
    cat_name = categorias[categorias['id'] == cat_id]['nombre'].values[0]
    print(f"  - {cat_name}: {count}")

print(f"\nTécnicos: {len(tecnicos)}")
print(f"Categorías: {len(categorias)}")

print("\n✓ Archivos CSV generados exitosamente")
print(f"  Ubicación: {output_path}")
