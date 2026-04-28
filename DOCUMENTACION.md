# Documentación Técnica - EVM Project Tracker

## 📋 Descripción General

**EVM Project Tracker** es una aplicación web para gestionar y monitorear proyectos usando la metodología **Earned Value Management (EVM)**, estándar de Project Management Institute (PMI).

La aplicación permite:
- Crear proyectos y sus actividades
- Registrar avance planificado vs actual
- Calcular automáticamente indicadores EVM
- Visualizar el desempeño del proyecto en tiempo real

---

## 🏗️ Arquitectura General

```
┌─────────────────────────────────────────────────────────────────┐
│                         NAVEGADOR (React)                       │
│  (Frontend - Vite + React 19 + React Router)                    │
└─────────────────────────────────────────────────────────────────┘
                                 ↕ HTTP/API
┌─────────────────────────────────────────────────────────────────┐
│                    SERVIDOR (Flask + Python)                    │
│  (Backend - Flask-smorest + SQLAlchemy + PostgreSQL)            │
└─────────────────────────────────────────────────────────────────┘
                                 ↕ SQL
┌─────────────────────────────────────────────────────────────────┐
│                    BASE DE DATOS (PostgreSQL)                   │
│  (Tablas: projects, activities)                                 │
└─────────────────────────────────────────────────────────────────┘
```

---

## 🔙 BACKEND - Descripción Detallada

### Stack Tecnológico

```
Flask 2.3.3                    - Framework web
Flask-SQLAlchemy 3.1.1         - ORM para base de datos
Flask-Migrate 4.0.5            - Migraciones de base de datos
Flask-smorest 0.42.1           - API REST automática + OpenAPI
Flask-CORS 5.0.1               - Soporte CORS
PostgreSQL (psycopg2)          - Base de datos
Marshmallow 3.20.1             - Serialización/Validación
pytest 7.4.3                   - Testing
```

### Estructura de Carpetas

```
backend/
├── app/
│   ├── __init__.py             - Factory de aplicación Flask
│   ├── config.py               - Configuración (dev, test, prod)
│   ├── extensions.py           - Inicialización de extensiones
│   ├── controllers/            - Endpoints API (blueprints)
│   │   ├── project_blueprint.py   - Rutas: GET, POST, PUT, DELETE proyectos
│   │   └── activity_blueprint.py  - Rutas: GET, POST, PUT, DELETE actividades
│   ├── models/                 - Modelos ORM SQLAlchemy
│   │   ├── project.py          - Modelo Project con relación a actividades
│   │   └── activity.py         - Modelo Activity con foreign key a proyectos
│   ├── repositories/           - Acceso a datos (patrón Repository)
│   │   ├── project_repo.py     - Queries a tabla projects
│   │   └── activity_repo.py    - Queries a tabla activities
│   ├── services/               - Lógica de negocio
│   │   ├── evm_service.py      - Cálculos EVM (PV, EV, CPI, SPI, etc)
│   │   ├── project_service.py  - Operaciones de proyectos con EVM
│   │   └── activity_service.py - Operaciones de actividades
│   ├── schemas/                - Validación/Serialización (Marshmallow)
│   │   ├── project_schema.py   - Esquemas para proyectos
│   │   └── activity_schema.py  - Esquemas para actividades
│   └── errors/
│       └── handlers.py         - Manejo de excepciones
├── tests/
│   ├── conftest.py             - Configuración pytest (fixtures)
│   ├── unit/
│   │   └── test_evm_service.py - Tests de cálculos EVM
│   └── integration/
│       ├── test_projects_endpoint.py  - Tests endpoints proyectos
│       └── test_activities_endpoint.py - Tests endpoints actividades
├── migrations/                 - Migraciones de base de datos (Alembic)
├── Dockerfile                  - Contenedor para producción
├── requirements.txt            - Dependencias Python
├── wsgi.py                     - Punto de entrada WSGI
└── pytest.ini                  - Configuración de tests
```

### 📊 Modelos de Datos

#### Modelo: Project (Proyecto)

```python
# Tabla: projects
id              UUID (PK)           - Identificador único
name            String(255)         - Nombre del proyecto
description     Text (nullable)     - Descripción
created_at      DateTime            - Fecha de creación
updated_at      DateTime            - Última actualización

# Relación
activities      → List[Activity]    - Actividades del proyecto (1:N)
```

#### Modelo: Activity (Actividad)

```python
# Tabla: activities
id              UUID (PK)           - Identificador único
project_id      UUID (FK)           - Referencia al proyecto
name            String(255)         - Nombre de la actividad
bac             Decimal(15,2)       - Budget at Completion (presupuesto)
planned_progress Decimal(5,2)       - Progreso planificado (0-100%)
actual_progress  Decimal(5,2)       - Progreso real (0-100%)
actual_cost      Decimal(15,2)      - Costo incurrido
created_at      DateTime            - Fecha de creación
updated_at      DateTime            - Última actualización

# Relación
project         → Project           - Proyecto padre
```

### 🔄 Flujo de Solicitudes API

#### 1️⃣ Obtener Proyectos (GET /api/v1/projects/)

```
Cliente (React)
    ↓
GET /api/v1/projects/
    ↓
project_blueprint.py (ProjectList.get())
    ↓
project_service.list_projects_service()
    ↓
project_repo.fetch_all_projects()
    ↓
SELECT * FROM projects;  (PostgreSQL)
    ↓
Para cada proyecto:
  - Obtener actividades
  - Calcular EVM consolidado (total_bac, total_pv, total_ev, total_ac, cpi, spi, etc)
    ↓
Retornar JSON con proyectos + EVM
    ↓
Cliente renderiza lista
```

#### 2️⃣ Obtener Detalle de Proyecto (GET /api/v1/projects/<project_id>)

```
Cliente (React)
    ↓
GET /api/v1/projects/{uuid}
    ↓
project_blueprint.py (ProjectDetail.get())
    ↓
project_service.get_project_detail_service(project_id)
    ↓
1. Obtener proyecto: SELECT * FROM projects WHERE id = ?
2. Obtener actividades: SELECT * FROM activities WHERE project_id = ?
3. Para cada actividad:
   - Calcular EVM individual (pv, ev, cv, sv, cpi, spi, eac, vac)
4. Calcular EVM consolidado del proyecto
    ↓
Retornar JSON:
{
  id, name, description, created_at, updated_at,
  evm: { total_bac, total_pv, total_ev, total_ac, cv, sv, cpi, spi, eac, vac, ... },
  activities: [
    { id, name, bac, planned_progress, actual_progress, actual_cost, evm: {...} },
    ...
  ]
}
    ↓
Cliente renderiza detalle con KPIs y gráficos
```

#### 3️⃣ Crear Proyecto (POST /api/v1/projects/)

```
Cliente (React)
    ↓
POST /api/v1/projects/
Body: { "name": "Mi Proyecto", "description": "..." }
    ↓
project_blueprint.py (ProjectList.post())
    ↓
ProjectCreateSchema valida y parsea datos
    ↓
project_service.create_project_service(name, description)
    ↓
project_repo.save_project(name, description)
    ↓
INSERT INTO projects (id, name, description, created_at, updated_at)
VALUES (uuid(), 'Mi Proyecto', '...', now(), now());
    ↓
Retornar proyecto creado (201 Created)
```

#### 4️⃣ Agregar Actividad a Proyecto (POST /api/v1/projects/<project_id>/activities)

```
Cliente (React)
    ↓
POST /api/v1/projects/{uuid}/activities
Body: {
  "name": "Diseño",
  "bac": 5000,
  "planned_progress": 50,
  "actual_progress": 30,
  "actual_cost": 1200
}
    ↓
activity_blueprint.py (ActivityList.post())
    ↓
ActivityCreateSchema valida datos
    ↓
activity_service.create_activity_service(project_id, fields)
    ↓
Verificar que proyecto existe
    ↓
activity_repo.save_activity(project_id, fields)
    ↓
INSERT INTO activities (...)
    ↓
Retornar actividad con EVM calculado (201 Created)
```

### 🎯 Cálculos EVM (Earned Value Management)

**Ubicación:** `app/services/evm_service.py`

Metodología estándar del PMI para medir desempeño de proyectos.

#### Fórmulas Básicas

```
PV (Planned Value) = (planned_progress / 100) × BAC
   └─ Valor planeado según cronograma
   └─ Ejemplo: BAC=1000, planned=50% → PV=500

EV (Earned Value) = (actual_progress / 100) × BAC
   └─ Valor ganado según progreso real
   └─ Ejemplo: BAC=1000, actual=30% → EV=300

CV (Cost Variance) = EV - AC
   └─ Diferencia entre valor ganado y costo incurrido
   └─ > 0: Bajo presupuesto ✅
   └─ < 0: Sobre presupuesto ❌
   └─ Ejemplo: EV=300, AC=1200 → CV=-900 (muy sobre presupuesto)

SV (Schedule Variance) = EV - PV
   └─ Diferencia entre valor ganado y valor planeado
   └─ > 0: Adelantado en cronograma ✅
   └─ < 0: Atrasado en cronograma ❌
   └─ Ejemplo: EV=300, PV=500 → SV=-200 (200 atrás)
```

#### Índices de Desempeño

```
CPI (Cost Performance Index) = EV / AC
   └─ Eficiencia de costos
   └─ > 1.0: Eficiente (ganar más con menos) ✅
   └─ < 1.0: Ineficiente (gastar más para ganar menos) ❌
   └─ NULL: Si AC=0 (sin gastos aún)
   └─ Ejemplo: EV=300, AC=1200 → CPI=0.25 (muy ineficiente)

SPI (Schedule Performance Index) = EV / PV
   └─ Eficiencia de cronograma
   └─ > 1.0: Adelantado ✅
   └─ < 1.0: Atrasado ❌
   └─ NULL: Si PV=0 (no iniciado)
   └─ Ejemplo: EV=300, PV=500 → SPI=0.6 (muy atrasado)
```

#### Proyecciones

```
EAC (Estimate at Completion) = AC + (BAC - EV) / CPI
   └─ Estimación del costo final del proyecto
   └─ Asume que el desempeño continuará igual
   └─ NULL: Si CPI=0 (división por cero)
   └─ Ejemplo: AC=1200, BAC=1000, CPI=0.25
              → EAC = 1200 + (1000-300)/0.25 = 1200 + 2800 = 4000

VAC (Variance at Completion) = BAC - EAC
   └─ Variación esperada al completar
   └─ > 0: Espera gastar menos de lo presupuestado ✅
   └─ < 0: Espera gastar más de lo presupuestado ❌
   └─ Ejemplo: BAC=1000, EAC=4000 → VAC=-3000 (muy sobre presupuesto)
```

#### Cálculos EVM por Actividad vs por Proyecto

**Por Actividad:**
- Calcula PV, EV, CV, SV, CPI, SPI, EAC, VAC para una sola actividad
- Se usa para analizar desempeño individual

**Por Proyecto (Consolidado):**
```python
total_bac = Sum(BAC de todas las actividades)
total_pv = Sum(PV de todas las actividades)
total_ev = Sum(EV de todas las actividades)
total_ac = Sum(AC de todas las actividades)

# Luego se calculan índices con los totales
cpi = total_ev / total_ac
spi = total_ev / total_pv
```

---

## 🎨 FRONTEND - Descripción Detallada

### Stack Tecnológico

```
React 19.2.0               - Librería UI
Vite 8.0.10                - Build tool (muy rápido)
React Router 7.0.0         - Enrutamiento SPA
Recharts 2.14.0            - Gráficos (para visualizar EVM)
Axios 1.7.0                - Cliente HTTP
ESLint 9.39.1              - Análisis de código
```

### Estructura de Carpetas

```
frontend/
├── src/
│   ├── main.jsx            - Punto de entrada (renderiza App en #root)
│   ├── App.jsx             - Componente raíz con rutas
│   ├── index.css           - Estilos globales
│   ├── api/
│   │   └── evmApi.js       - Funciones HTTP con Axios
│   │                          (getAllProjects, getProjectById, createActivity, etc)
│   ├── components/
│   │   ├── evm/            - Componentes de dominio EVM
│   │   │   ├── ConsolidatedKPIs.jsx - Muestra KPIs consolidados del proyecto
│   │   │   ├── EVMChart.jsx         - Gráfico PV vs EV vs AC
│   │   │   ├── ActivityForm.jsx     - Formulario crear/editar actividad
│   │   │   └── ActivityTable.jsx    - Tabla de actividades
│   │   └── ui/             - Componentes reutilizables
│   │       ├── Button.jsx  - Botón personalizado
│   │       ├── LoadingSpinner.jsx - Indicador de carga
│   │       └── StatusBadge.jsx - Badge con estado (efficient/inefficient)
│   ├── hooks/
│   │   ├── useProjects.js  - Hook para listar y crear proyectos
│   │   └── useProject.js   - Hook para detalle de proyecto + actividades
│   ├── pages/
│   │   ├── ProjectsPage.jsx      - Página listado de proyectos
│   │   └── ProjectDetailPage.jsx - Página detalle de proyecto
│   ├── constants/
│   │   └── evm.js          - Constantes de la app (interpretaciones, colores, etc)
│   └── assets/             - Recursos estáticos
├── public/
│   └── index.html          - HTML plantilla
├── index.html              - HTML plantilla (Vite)
├── package.json            - Dependencias y scripts
├── vite.config.js          - Configuración Vite
├── eslint.config.js        - Configuración ESLint
└── Dockerfile              - Contenedor para producción
```

### 🔄 Flujo de la Aplicación Frontend

#### Página 1: Proyectos (ProjectsPage.jsx)

```
┌─────────────────────────────────┐
│   Página: Listado de Proyectos  │
└─────────────────────────────────┘
         ↓
1. Al montar componente:
   - Hook useProjects() se ejecuta
   - Se llama API GET /api/v1/projects/
   - Se obtiene lista de proyectos con EVM consolidado

2. Estado local:
   - projects: lista de proyectos
   - isLoading: boolean (cargando)
   - error: string (mensaje de error)
   - showForm: boolean (mostrar formulario)
   - name, description: datos del formulario

3. Interfaz:
   ┌─────────────────────────────────────┐
   │ ⬅ [Proyectos]    [+ Nuevo proyecto] │
   └─────────────────────────────────────┘
   
   ┌─────────────────────────────────────┐
   │ [Si showForm=true]                  │
   │                                     │
   │ Nuevo proyecto                      │
   │ Nombre: [_____________]             │
   │ Descripción: [___________]          │
   │ [Crear]  [Cancelar]                 │
   └─────────────────────────────────────┘
   
   ┌──────────┬────────────┬──────────────┐
   │ Nombre   │ Desc.      │ Creado       │
   ├──────────┼────────────┼──────────────┤
   │ Proyecto │ Descripción│ 2024-04-28  │
   │ A        │ ...        │              │
   └──────────┴────────────┴──────────────┘

4. Al crear proyecto:
   - handleCreate valida name (no vacío)
   - Llama createProject(name, description)
   - POST /api/v1/projects/ { name, description }
   - Reinicia estado del formulario
   - Lista se actualiza automáticamente

5. Al hacer click en fila:
   - Navigate a /projects/{projectId}
   - Va a ProjectDetailPage
```

#### Página 2: Detalle de Proyecto (ProjectDetailPage.jsx)

```
┌────────────────────────────────────────────┐
│ Detalle de Proyecto: "Mi Proyecto"         │
│ Descripción: "Construcción de sitio web"   │
└────────────────────────────────────────────┘
         ↓
1. Al montar componente:
   - Hook useProject(projectId) se ejecuta
   - GET /api/v1/projects/{id}
   - Se obtiene proyecto con:
     * evm: { total_bac, total_pv, total_ev, total_ac, cpi, spi, cv, sv, eac, vac }
     * activities: [ {...evm...}, {...evm...}, ... ]

2. Secciones de UI:

   ┌─────────────────────────────────────────────┐
   │ 🎯 KPIs del Proyecto (ConsolidatedKPIs)     │
   ├─────────────────────────────────────────────┤
   │ [BAC Total]  [PV Total]  [EV Total] [AC T.] │
   │ 10000        5000        3000       1200    │
   │                                             │
   │ [CPI] [SPI] [CV]      [SV]       [EAC] [VAC]
   │ 2.50  0.60  1800      -2000      4000  6000 │
   └─────────────────────────────────────────────┘

   ┌──────────────────────────────────────────────┐
   │ 📈 PV vs EV vs AC por Actividad (EVMChart)   │
   ├──────────────────────────────────────────────┤
   │                                              │
   │  $  ┃                                        │
   │     ┃    ┌─────┐                            │
   │     ┃    │  EV │                            │
   │     ┃  ┌─┴─────┴─┐                          │
   │     ┃  │   PV    │                          │
   │     ┃  │  ┌──┐   │                          │
   │     ┃  │  │AC│   │                          │
   │     ┃  └──┴──┴───┘                          │
   │     ┗━━━━━━━━━━━━━━━━━━━━                   │
   │        Actividad1  Actividad2  Actividad3   │
   └──────────────────────────────────────────────┘

   ┌──────────────────────────────────────────────┐
   │ 📋 Actividades (ActivityTable)               │
   │ [+ Agregar actividad]                        │
   ├──────────────────────────────────────────────┤
   │ Nombre   │ BAC  │ Plan│ Real│ AC   │ Acc.   │
   ├──────────┼──────┼─────┼─────┼──────┼────────┤
   │ Diseño   │5000  │ 50% │ 30% │ 1200 │ Editar │
   │ Desarrollo
5000  │ 50% │ 60% │ 4000 │ Editar │
   │ Testing  │ 0    │ 0%  │ 0%  │ 0    │ Editar │
   └──────────────────────────────────────────────┘

3. Interacciones:
   - "Agregar actividad": Abre formulario (ActivityForm)
   - "Editar": Abre formulario con datos precargados
   - "Eliminar": Confirmación y DELETE /api/v1/activities/{id}

4. Formulario Actividad (ActivityForm):
   ┌──────────────────────────────────────────┐
   │ Nueva Actividad                          │
   ├──────────────────────────────────────────┤
   │ Nombre:              [Diseño ________]   │
   │ BAC:                 [5000 ________]     │
   │ Progreso Planeado:   [50 ________] %    │
   │ Progreso Real:       [30 ________] %    │
   │ Costo Incurrido:     [1200 _____]       │
   ├──────────────────────────────────────────┤
   │ [Guardar]  [Cancelar]                    │
   └──────────────────────────────────────────┘

5. Flujos de Actividades:

   📝 Crear Nueva Actividad:
     handleAddClick()
       └─ setShowForm(true), setEditingActivity(null)
     Usuario completa formulario
       └─ handleAddSubmit(data)
     data validado y completo
       └─ addActivity(data)  [Hook useProject]
     POST /api/v1/projects/{projectId}/activities
       └─ Actividad creada en BD
     refetch() automático
       └─ GET /api/v1/projects/{projectId} nuevamente
     UI se actualiza con nueva actividad

   ✏️  Editar Actividad Existente:
     handleEditClick(activity)
       └─ setEditingActivity(activity), setShowForm(true)
     Usuario modifica datos en formulario
       └─ handleEditSubmit(data)
     PUT /api/v1/activities/{activityId}
       └─ Actividad actualizada
     refetch() automático
       └─ UI se actualiza

   🗑️  Eliminar Actividad:
     Usuario hace click en Eliminar
       └─ removeActivity(activityId)
     DELETE /api/v1/activities/{activityId}
       └─ Actividad eliminada
     refetch() automático
       └─ UI se actualiza sin esa actividad
```

### 🪝 Hooks Personalizados

#### useProjects() - Listar y Crear Proyectos

```javascript
export const useProjects = () => {
  const [projects, setProjects] = useState([])      // Lista de proyectos
  const [isLoading, setIsLoading] = useState(false) // Cargando
  const [error, setError] = useState(null)          // Error

  const refetch = useCallback(async () => {
    // GET /api/v1/projects/
    // Obtiene lista completa de proyectos
  }, [])

  const createProject = async (name, description) => {
    // POST /api/v1/projects/
    // Crea nuevo proyecto
    // Luego refetch() para actualizar lista
  }

  useEffect(() => {
    // Al montar: ejecuta refetch()
    refetch()
  }, [])

  return { projects, isLoading, error, createProject, refetch }
}
```

#### useProject(projectId) - Detalle + Actividades

```javascript
export const useProject = (projectId) => {
  const [project, setProject] = useState(null)      // Proyecto completo
  const [isLoading, setIsLoading] = useState(false) // Cargando
  const [error, setError] = useState(null)          // Error
  const [isMutating, setIsMutating] = useState(false) // Modificando

  const refetch = useCallback(async () => {
    // GET /api/v1/projects/{projectId}
    // Obtiene proyecto + actividades + EVM
  }, [projectId])

  const addActivity = async (data) => {
    // POST /api/v1/projects/{projectId}/activities
    // Crea actividad
    // Luego refetch()
  }

  const editActivity = async (activityId, fields) => {
    // PUT /api/v1/activities/{activityId}
    // Actualiza actividad
    // Luego refetch()
  }

  const removeActivity = async (activityId) => {
    // DELETE /api/v1/activities/{activityId}
    // Elimina actividad
    // Luego refetch()
  }

  useEffect(() => {
    // Al montar o cambiar projectId: refetch()
    refetch()
  }, [projectId])

  return {
    project, isLoading, error, isMutating,
    addActivity, editActivity, removeActivity, refetch
  }
}
```

---

## 🧪 Testing

### Backend - pytest

**Ubicación:** `backend/tests/`

```
tests/
├── conftest.py                           - Configuración compartida
│   └─ Fixtures: client (Flask test client), db (BD de prueba)
├── unit/
│   └─ test_evm_service.py               - Tests de cálculos EVM
│      ├─ test_calculate_pv()
│      ├─ test_calculate_ev()
│      ├─ test_calculate_cpi()
│      ├─ test_calculate_spi()
│      └─ test casos edge (división por cero, etc)
└── integration/
    ├─ test_projects_endpoint.py         - Tests API proyectos
    │  ├─ test_list_projects()
    │  ├─ test_create_project()
    │  ├─ test_get_project_detail()
    │  └─ test_delete_project()
    └─ test_activities_endpoint.py       - Tests API actividades
       ├─ test_create_activity()
       ├─ test_update_activity()
       └─ test_delete_activity()

Ejecutar:
  $ pytest                    # Todos los tests
  $ pytest -v                 # Verbose
  $ pytest --cov              # Con cobertura
```

---

## 🚀 Deployment

### Docker Compose

```yaml
services:
  backend:
    build: ./backend
    ports: 5000:5000
    env: DATABASE_URL=postgresql://user:password@db:5432/evm_db

  frontend:
    build: ./frontend
    ports: 3000:3000
    environment:
      VITE_API_URL: http://localhost:5000/api/v1

  db:
    image: postgres:15
    volumes:
      - ./database/init.sql:/docker-entrypoint-initdb.d/init.sql
    ports: 5432:5432
```

**Para iniciar:**
```bash
docker-compose up
```

---

## 📝 Ejemplos de Flujos

### Ejemplo 1: Crear Proyecto y Agregar Actividades

1. Usuario accede a http://localhost:3000
2. Ve página de proyectos vacía: "No hay proyectos"
3. Click en "+ Nuevo proyecto"
4. Completa:
   - Nombre: "Construcción Sitio Web"
   - Descripción: "Sitio corporativo responsivo"
5. Click en "Crear"
   - Frontend: POST /api/v1/projects/
   - Backend: INSERT INTO projects VALUES (...)
   - Response: { id: "uuid-123", name: "Construcción...", ... }
6. Frontend navega a /projects/uuid-123
7. Usuario ve página detalle vacía: "Agrega actividades..."
8. Click en "+ Agregar actividad"
9. Completa:
   - Nombre: "Diseño UI/UX"
   - BAC: 5000
   - Progreso Planeado: 30%
   - Progreso Real: 20%
   - Costo Incurrido: 800
10. Click en "Guardar"
    - Frontend: POST /api/v1/projects/uuid-123/activities
    - Backend: INSERT INTO activities (...)
    - EVM calculado automáticamente:
      * PV = 30% × 5000 = 1500
      * EV = 20% × 5000 = 1000
      * CV = 1000 - 800 = 200 ✅ (bajo presupuesto)
      * SV = 1000 - 1500 = -500 ❌ (atrasado)
      * CPI = 1000 / 800 = 1.25 ✅ (eficiente)
      * SPI = 1000 / 1500 = 0.67 ❌ (atrasado)
11. Frontend refetch() automático
12. UI actualiza con:
    - KPIs: muestra CPI=1.25 (verde, eficiente), SPI=0.67 (rojo, atrasado)
    - Gráfico: barra con PV (1500), EV (1000), AC (800)
    - Tabla: fila con actividad

### Ejemplo 2: Monitorear Progreso de Proyecto

1. Usuario en detalle del proyecto
2. Ve 3 actividades:
   - Diseño: 30% planificado, 20% real
   - Desarrollo: 50% planificado, 60% real
   - Testing: 0% planificado, 0% real

3. KPIs consolidados:
   - total_bac = 15000
   - total_pv = 6000 (promedio 40%)
   - total_ev = 4000 (promedio 26.7%)
   - total_ac = 5000
   - cv = -1000 ❌ (sobre presupuesto)
   - sv = -2000 ❌ (muy atrasado)
   - cpi = 0.8 ❌ (gastar más para ganar menos)
   - spi = 0.67 ❌ (progreso lento)

4. Gráfico EVMChart muestra:
   ```
   PV (naranja)  |────────|
   EV (azul)     |───────|
   AC (rojo)     |─────────|
                 Diseño Desarrollo Testing
   ```

5. Manager analiza:
   - Proyecto está 2000 atrás de cronograma
   - Presupuesto casi agotado (AC 5000 de 15000)
   - Eficiencia baja (gastar 1.25 para ganar 1.0)
   - Acción: Necesita más recursos en Desarrollo

---

## 🔗 Endpoints API

### Proyectos
```
GET    /api/v1/projects/              - Listar todos
POST   /api/v1/projects/              - Crear nuevo
GET    /api/v1/projects/{id}          - Obtener detalle
PUT    /api/v1/projects/{id}          - Actualizar
DELETE /api/v1/projects/{id}          - Eliminar
```

### Actividades
```
POST   /api/v1/projects/{id}/activities  - Crear
PUT    /api/v1/activities/{id}           - Actualizar
DELETE /api/v1/activities/{id}           - Eliminar
```

---

## 📚 Referencias

- **EVM (Earned Value Management):** https://www.pmi.org/
- **Flask-smorest:** https://flask-smorest.readthedocs.io/
- **React Hooks:** https://react.dev/reference/react/hooks
- **Recharts:** https://recharts.org/

---

**Última actualización:** 28/04/2026
**Versión:** v1.0
