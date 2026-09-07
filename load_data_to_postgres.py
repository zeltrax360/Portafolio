import pandas as pd
import psycopg2
from psycopg2.extras import execute_values

# Conexión a PostgreSQL
conn = psycopg2.connect(
    host="127.0.0.1",
    database="service_desk",
    user="postgres",
    password=""
)
cursor = conn.cursor()

print("Cargando datos en PostgreSQL...")

# 1. Cargar categorías
print("  1. Categorías...")
df_cat = pd.read_csv("Proyecto-1-Service-Desk/data/categorias.csv")
for _, row in df_cat.iterrows():
    cursor.execute(
        "INSERT INTO categorias (id, nombre, descripcion) VALUES (%s, %s, %s)",
        (row['id'], row['nombre'], row['descripcion'])
    )
conn.commit()
print(f"     ✓ {len(df_cat)} categorías")

# 2. Cargar técnicos
print("  2. Técnicos...")
df_tec = pd.read_csv("Proyecto-1-Service-Desk/data/tecnicos.csv")
for _, row in df_tec.iterrows():
    cursor.execute(
        "INSERT INTO tecnicos (id, nombre, email, nivel) VALUES (%s, %s, %s, %s)",
        (row['id'], row['nombre'], row['email'], row['nivel'])
    )
conn.commit()
print(f"     ✓ {len(df_tec)} técnicos")

# 3. Cargar tickets
print("  3. Tickets (esto toma un momento)...")
df_tkt = pd.read_csv("Proyecto-1-Service-Desk/data/tickets.csv")

# Insertar en lotes para más velocidad
batch_size = 1000
for i in range(0, len(df_tkt), batch_size):
    batch = df_tkt.iloc[i:i+batch_size]
    for _, row in batch.iterrows():
        cursor.execute(
            """INSERT INTO tickets
               (id, numero_ticket, fecha_creacion, fecha_resolucion,
                categoria_id, tecnico_id, prioridad, estado, descripcion, mttr_horas)
               VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)""",
            (row['id'], row['numero_ticket'], row['fecha_creacion'], row['fecha_resolucion'],
             row['categoria_id'], row['tecnico_id'], row['prioridad'], row['estado'],
             row['descripcion'], row['mttr_horas'])
        )
    conn.commit()
    print(f"     Insertados {min(i+batch_size, len(df_tkt))}/{len(df_tkt)}")

print(f"     ✓ {len(df_tkt)} tickets")

# Verificar
cursor.execute("SELECT COUNT(*) FROM tickets")
total = cursor.fetchone()[0]
print(f"\n✓ Total tickets en BD: {total}")

cursor.close()
conn.close()

print("\n✓ Datos cargados exitosamente en PostgreSQL")
