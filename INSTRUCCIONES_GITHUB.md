# 📘 Instrucciones: Subir Proyecto a GitHub

## Paso 1: Crear Repositorio en GitHub

1. Ve a **https://github.com/new**
2. Rellena los campos:
   - **Repository name:** `Portafolio` (o el nombre que prefieras)
   - **Description:** "Portfolio de proyectos de ciencia de datos y análisis"
   - **Public:** ✓ (así se ve en el portafolio)
   - **Add .gitignore:** No (ya lo tenemos)
   - **Add a README:** No (ya lo tenemos)

3. Haz clic en **"Create repository"**

## Paso 2: Configurar Remote en Git Local

Después de crear el repositorio, GitHub te mostrará comandos. Copia los comandos para "push an existing repository from the command line".

En VS Code Terminal (o PowerShell), ejecuta:

```bash
git remote add origin https://github.com/tu-usuario/Portafolio.git
git branch -M main
git push -u origin main
```

**Reemplaza `tu-usuario` con tu usuario de GitHub actual**

O desde VS Code:
1. Abre la **Paleta de Comandos** (Ctrl+Shift+P)
2. Busca "Git: Add Remote"
3. Pega: `https://github.com/tu-usuario/Portafolio.git`
4. En el **Source Control panel**, haz clic en "Push"

## Paso 3: Verificar en GitHub

- Ve a https://github.com/tu-usuario/Portafolio
- Verifica que aparezcan todos los archivos
- Busca la carpeta `Proyecto-1-Service-Desk`

## Siguiente: Configurar PostgreSQL y Cargar Datos

### Instalar PostgreSQL (si no lo has hecho)

```bash
# Si usas Windows, descargalo de: https://www.postgresql.org/download/windows/
# Instala con contraseña que recuerdes para usuario 'postgres'
```

### Crear Base de Datos

```bash
# Conectar a PostgreSQL
psql -U postgres

# Crear database
CREATE DATABASE service_desk;

# Salir
\q
```

### Cargar Esquema SQL

```bash
# Desde la carpeta del proyecto
cd "C:\Users\Sebastian Beltran\Documents\Portafolio\Proyecto-1-Service-Desk"

# Cargar scripts en orden
psql -U postgres -d service_desk -f sql/01_create_tables.sql
psql -U postgres -d service_desk -f sql/02_insert_data.sql
psql -U postgres -d service_desk -f sql/03_analysis_queries.sql
psql -U postgres -d service_desk -f sql/04_generate_sample_data.sql
```

### Configurar .env

```bash
# Copiar el archivo de ejemplo
Copy-Item ".\.env.example" ".\.env"

# Editar .env con tus credenciales PostgreSQL
# (si usas contraseña en postgres, agrega: DB_PASSWORD=tu_password)
```

## Siguiente: Ejecutar Scripts de Análisis

```bash
# Instalar dependencias
pip install -r requirements.txt

# Ejecutar exploración de datos
python scripts/01_data_exploration.py

# Ejecutar análisis
python scripts/03_analysis.py

# Ejecutar predicción ML
python scripts/04_ml_prediction.py
```

---

**¿Listo para empezar?** 

1. ✅ Repositorio creado en GitHub
2. ✅ Git push hecho desde tu máquina
3. ⏳ Ahora configurar PostgreSQL
4. ⏳ Cargar datos SQL
5. ⏳ Ejecutar scripts Python
6. ⏳ Crear dashboard en Power BI

Confirma cuando hayas subido a GitHub y te ayudaré con el siguiente paso.
