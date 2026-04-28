# EVM Project Tracker

Aplicación full stack para gestionar proyectos y actividades usando indicadores de Earned Value Management (EVM).

El proyecto incluye:

- `backend` en Flask con API REST documentada con Swagger
- `frontend` en React + Vite
- `database` PostgreSQL
- ejecución local con Docker Compose
- pruebas unitarias e integración en backend

## Objetivo

La aplicación permite:

- crear, editar, listar y eliminar proyectos
- crear, editar, listar y eliminar actividades por proyecto
- calcular indicadores EVM por actividad y consolidados por proyecto
- visualizar KPIs y gráfica comparativa `PV vs EV vs AC`

## Stack tecnológico

### Backend

- Python 3.11
- Flask
- Flask-SQLAlchemy
- Flask-Migrate
- Flask-Smorest
- Marshmallow
- PostgreSQL
- Pytest

### Frontend

- React
- Vite
- Axios
- React Router
- Recharts

### Infraestructura

- Docker
- Docker Compose

## Estructura del proyecto

```text
PruebaTecnica/
├── backend/
│   ├── app/
│   │   ├── controllers/
│   │   ├── errors/
│   │   ├── models/
│   │   ├── repositories/
│   │   ├── schemas/
│   │   ├── services/
│   │   ├── config.py
│   │   ├── extensions.py
│   │   └── __init__.py
│   ├── tests/
│   │   ├── integration/
│   │   └── unit/
│   ├── Dockerfile
│   ├── pytest.ini
│   ├── requirements.txt
│   └── wsgi.py
├── database/
│   └── init.sql
├── frontend/
│   ├── public/
│   ├── src/
│   │   ├── api/
│   │   ├── components/
│   │   ├── constants/
│   │   ├── hooks/
│   │   ├── pages/
│   │   ├── App.jsx
│   │   └── main.jsx
│   ├── Dockerfile
│   ├── package.json
│   └── vite.config.js
├── docker-compose.yml
└── README.md
```

## Arquitectura backend

El backend sigue una separación por capas:

- `controllers`: exponen endpoints HTTP
- `schemas`: validación y serialización
- `repositories`: acceso a base de datos
- `services`: reglas de orquestación y armado de respuestas
- `evm_service.py`: cálculos puros de EVM

Esto permite mantener:

- lógica de negocio aislada
- validaciones centralizadas
- pruebas más simples
- endpoints más delgados

## Indicadores EVM implementados

### Por actividad

- `PV` Planned Value
- `EV` Earned Value
- `CV` Cost Variance
- `SV` Schedule Variance
- `CPI` Cost Performance Index
- `SPI` Schedule Performance Index
- `EAC` Estimate at Completion
- `VAC` Variance at Completion

### Por proyecto

Se calculan los mismos indicadores de forma consolidada a partir de las actividades del proyecto.

## Variables de entorno

Crea un archivo `.env` en la raíz del proyecto.

Ejemplo:

```env
POSTGRES_USER=postgres
POSTGRES_PASSWORD=postgres
POSTGRES_DB=evm_db
POSTGRES_PORT=5432

DATABASE_URL=postgresql://postgres:postgres@db:5432/evm_db
FLASK_ENV=development
SECRET_KEY=dev-secret-key

VITE_API_URL=http://localhost:5000/api/v1
```

### Variables usadas

| Variable | Descripción |
|---|---|
| `POSTGRES_USER` | Usuario de PostgreSQL |
| `POSTGRES_PASSWORD` | Contraseña de PostgreSQL |
| `POSTGRES_DB` | Nombre de la base de datos |
| `POSTGRES_PORT` | Puerto local para PostgreSQL |
| `DATABASE_URL` | URL de conexión usada por el backend |
| `FLASK_ENV` | Entorno del backend |
| `SECRET_KEY` | Clave secreta de Flask |
| `VITE_API_URL` | URL base de la API consumida por el frontend |

## Levantar el proyecto con Docker

### Requisitos

- Docker Desktop
- Docker Compose

### Comando

```powershell
docker compose up --build
```

Para ejecutarlo en segundo plano:

```powershell
docker compose up --build -d
```

### Servicios disponibles

| Servicio | URL |
|---|---|
| Frontend | `http://localhost:3000` |
| Backend API | `http://localhost:5000` |
| Swagger UI | `http://localhost:5000/api-docs` |
| PostgreSQL | `localhost:${POSTGRES_PORT}` |

### Detener servicios

```powershell
docker compose down
```

## Ejecutar sin Docker

## Backend

### Requisitos

- Python 3.11
- PostgreSQL

### Instalación

```powershell
cd backend
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
```

### Ejecución

Desde `backend/`:

```powershell
$env:FLASK_ENV="development"
python wsgi.py
```

O:

```powershell
flask run --host=0.0.0.0 --port=5000
```

## Frontend

### Requisitos

- Node.js 20+
- npm

### Instalación

```powershell
cd frontend
npm install
```

### Ejecución

```powershell
npm run dev
```

El frontend por defecto corre en:

```text
http://localhost:5173
```

## API REST

Base URL:

```text
http://localhost:5000/api/v1
```

### Endpoints de proyectos

| Método | Endpoint | Descripción |
|---|---|---|
| `GET` | `/projects/` | Listar proyectos |
| `POST` | `/projects/` | Crear proyecto |
| `GET` | `/projects/{project_id}` | Obtener detalle de proyecto |
| `PUT` | `/projects/{project_id}` | Editar proyecto |
| `DELETE` | `/projects/{project_id}` | Eliminar proyecto |

### Endpoints de actividades

| Método | Endpoint | Descripción |
|---|---|---|
| `GET` | `/projects/{project_id}/activities` | Listar actividades de un proyecto |
| `POST` | `/projects/{project_id}/activities` | Crear actividad |
| `PUT` | `/activities/{activity_id}` | Editar actividad |
| `DELETE` | `/activities/{activity_id}` | Eliminar actividad |

## Swagger

La documentación interactiva está disponible en:

```text
http://localhost:5000/api-docs
```

El documento OpenAPI queda en:

```text
http://localhost:5000/openapi.json
```

## Ejemplos de uso

### Crear proyecto

`POST /api/v1/projects/`

```json
{
  "name": "Proyecto Puente",
  "description": "Seguimiento EVM del puente principal"
}
```

### Crear actividad

`POST /api/v1/projects/{project_id}/activities`

```json
{
  "name": "Cimentacion",
  "bac": "10000",
  "planned_progress": "50",
  "actual_progress": "40",
  "actual_cost": "4500"
}
```

## Frontend: funcionalidades implementadas

### Pantalla de proyectos

- listar proyectos
- crear proyecto
- editar proyecto
- eliminar proyecto
- navegar al detalle del proyecto

### Pantalla de detalle de proyecto

- ver KPIs consolidados
- ver gráfica `PV / EV / AC`
- listar actividades
- crear actividad
- editar actividad
- eliminar actividad

## Base de datos

El archivo [database/init.sql](/C:/Users/Usuario/Documents/Prueba%20tecnica/PruebaTecnica/database/init.sql) crea:

- extensión `pgcrypto`
- tabla `projects`
- tabla `activities`
- índices para consultas por proyecto
- triggers para mantener `updated_at`

## Pruebas

## Backend

Desde Docker:

### Todas las pruebas

```powershell
docker exec evm_backend pytest -v
```

### Unitarias

```powershell
docker exec evm_backend pytest tests/unit/test_evm_service.py -v
```

### Integración

```powershell
docker exec evm_backend pytest tests/integration/ -v
```

### Cobertura

El backend está configurado con:

- cobertura sobre `app/services`
- umbral mínimo de `80%`

Configuración en [backend/pytest.ini](/C:/Users/Usuario/Documents/Prueba%20tecnica/PruebaTecnica/backend/pytest.ini).

## Frontend

### Build

```powershell
docker exec evm_frontend npm run build
```

### Lint

```powershell
docker exec evm_frontend npm run lint
```

## Decisiones de implementación

- Los valores EVM se exponen como `string` en la API para evitar pérdida de precisión con `Decimal`.
- El frontend consume la API mediante `VITE_API_URL`.
- Se habilitó CORS para `http://localhost:3000` sobre rutas `/api/*`.
- La documentación OpenAPI se genera con `flask-smorest`.

## Solución de problemas

### El frontend abre, pero no conecta con la API

Verifica:

- que el backend esté arriba en `http://localhost:5000`
- que `VITE_API_URL` apunte a `http://localhost:5000/api/v1`
- que los contenedores estén corriendo:

```powershell
docker ps
```

### Swagger carga, pero `/openapi.json` falla

Reinicia backend y revisa logs:

```powershell
docker restart evm_backend
docker logs evm_backend --tail 100
```

### El frontend queda en blanco

Revisar logs:

```powershell
docker logs evm_frontend --tail 100
```

### Reconstruir todo desde cero

```powershell
docker compose down
docker compose up --build -d
```

## Estado actual

El proyecto ya cuenta con:

- backend funcional con API REST
- Swagger operativo
- frontend funcional conectado a la API
- CRUD de proyectos
- CRUD de actividades
- cálculo y visualización de indicadores EVM
- pruebas unitarias e integración en backend

## Autor

Pablo Duarte.
Proyecto desarrollado como prueba técnica.
