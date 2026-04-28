# Documento del proceso

## Herramientas IA
------

ChatGPT
Cloud
Gemini
Copilot

------

Se eligieron estas por su desempeño en el codigo y por el uso de capa gratuita

------

## Prmpts
------

qué es el Valor Ganado y cómo funciona

------
explicame como se toman las medidas BAC    Av. Planif.    Av. Real    AC    PV    EV    CV    SV    CPI    SPI    EAC    VAC

------

Actúa como un Software Architect senior encargado de analizar requerimientos y definir soluciones técnicas completas.
### CONTEXTO ###
Se te proporcionarán documentos de requerimientos (pueden ser funcionales, técnicos o descripciones de negocio, generalmente en formato PDF). Debes analizarlos completamente antes de proponer una solución.
El objetivo es definir una arquitectura clara, consistente y ejecutable por un equipo de desarrollo.
---
### REGLAS DE TECNOLOGÍA ###
- Prioriza el uso de:
  - PostgreSQL (base de datos)
  - Python con Flask (backend/API)
  - React (frontend)
- Si el documento propone tecnologías diferentes:
  - Evalúalas
  - Decide si mantenerlas o reemplazarlas
  - Justifica claramente la decisión
---
### REQUERIMIENTO ###
1. Analiza el problema y resume:
   - Objetivos del sistema
   - Problemas que resuelve
   - Alcance funcional
---
2. Propón una solución técnica que incluya:
   - Arquitectura general (alto nivel)
   - Componentes principales
   - Flujo de datos entre componentes
---
3. Define tecnologías:
   - Backend
   - Frontend
   - Base de datos
   - Integraciones
   - Herramientas adicionales
Justifica cada elección técnica.
---
4. Divide la solución por capas:
   - Base de datos
   - Backend
   - Frontend
   - Integraciones
   - Testing
---
5. Para cada capa:
   - Responsabilidades
   - Patrones de diseño recomendados (con justificación)
   - Funcionalidades principales (nivel backlog técnico, no demasiado abstracto ni demasiado bajo)
---
6. Plan de trabajo:
   - Orden de implementación basado en:
     - Dependencias técnicas
     - Riesgo
     - Valor de negocio
   - Definir fases del proyecto
---
7. Cronograma:
   - Organizado por fases
   - Estimado en horas
   - Incluir entregables claros por fase
---
### FORMATO ###
- Usar Markdown
- Estructura clara con títulos y subtítulos
- Listas numeradas
- Tablas para cronograma
---
### RESTRICCIONES ###
- Evitar contenido genérico
- Justificar decisiones técnicas
- No asumir componentes que no existan en el requerimiento
- Mantener equilibrio entre arquitectura y ejecución
---
### VALIDACIÓN ###
Si falta información crítica (por ejemplo: volumen de datos, usuarios esperados, tipo de despliegue, integraciones externas):
- Realiza preguntas primero
- NO generes la solución hasta tener claridad suficiente


------

P: ¿Cuántos usuarios concurrentes se esperan usar la herramienta?
R: 1–10 usuarios (equipo pequeño)

P: ¿Cuál es el tipo de despliegue esperado?
R: docker

P: ¿El sistema requiere autenticación/multitenancy (múltiples organizaciones con datos aislados)?
R: No, es una herramienta interna de un solo equipo

------
### CONTEXTO ###
Se te proporcionarán documentos de requerimientos (pueden ser funcionales, técnicos o descripciones de negocio, generalmente en formato PDF). Debes analizarlos completamente antes de proponer una solución.

El objetivo es definir una arquitectura clara, consistente y ejecutable por un equipo de desarrollo.

---

### REGLAS DE TECNOLOGÍA ###
- Prioriza el uso de:
  - PostgreSQL (base de datos)
  - Python con Flask (backend/API)
  - React (frontend)
- Si el documento propone tecnologías diferentes:
  - Evalúalas
  - Decide si mantenerlas o reemplazarlas
  - Justifica claramente la decisión

---

### REQUERIMIENTO ###

1. Analiza el problema y resume:
   - Objetivos del sistema
   - Problemas que resuelve
   - Alcance funcional

---

2. Propón una solución técnica que incluya:
   - Arquitectura general (alto nivel)
   - Componentes principales
   - Flujo de datos entre componentes

---

3. Define tecnologías:
   - Backend
   - Frontend
   - Base de datos
   - Integraciones
   - Herramientas adicionales

Justifica cada elección técnica.

---

4. Divide la solución por capas:
   - Base de datos
   - Backend
   - Frontend
   - Integraciones
   - Testing

---

5. Para cada capa:
   - Responsabilidades
   - Patrones de diseño recomendados (con justificación)
   - Funcionalidades principales (nivel backlog técnico, no demasiado abstracto ni demasiado bajo)

---

6. Plan de trabajo:
   - Orden de implementación basado en:
     - Dependencias técnicas
     - Riesgo
     - Valor de negocio
   - Definir fases del proyecto

---

7. Cronograma:
   - Organizado por fases
   - Estimado en horas
   - Incluir entregables claros por fase

---

### FORMATO ###
- Usar Markdown
- Estructura clara con títulos y subtítulos
- Listas numeradas
- Tablas para cronograma

---

### RESTRICCIONES ###
- Evitar contenido genérico
- Justificar decisiones técnicas
- No asumir componentes que no existan en el requerimiento
- Mantener equilibrio entre arquitectura y ejecución

---

### VALIDACIÓN ###
Si falta información crítica (por ejemplo: volumen de datos, usuarios esperados, tipo de despliegue, integraciones externas):
- Realiza preguntas primero
- NO generes la solución hasta tener claridad suficiente

------
### CONTEXTO ###
Se cuenta con un sistema previamente definido (arquitectura y cronograma). A partir de ese contexto, debes diseñar el modelo de base de datos.

El objetivo es crear un esquema eficiente, mantenible y optimizado para almacenamiento y consultas.

---

### REQUERIMIENTO ###

1. Diseña las tablas necesarias considerando:
   - Normalización (mínimo 3FN, salvo justificación)
   - Relaciones entre entidades
   - Integridad referencial

2. Define para cada tabla:
   - Tipos de datos óptimos (evitar sobreuso de TEXT o VARCHAR innecesario)
   - Claves primarias
   - Claves foráneas
   - Restricciones (NOT NULL, UNIQUE, CHECK)
   - Valores por defecto

3. Define índices cuando:
   - Mejoren consultas frecuentes
   - Sean necesarios para claves foráneas o búsquedas

4. Define triggers SOLO si aplican, por ejemplo:
   - Auditoría (updated_at)
   - Validaciones complejas
   - Automatización de lógica de negocio simple

5. Considera buenas prácticas:
   - Nombres en snake_case
   - Uso consistente de timestamps (created_at, updated_at)
   - Evitar redundancia innecesaria
   - Balance entre normalización y performance

---

### SALIDA ###

## 1. Script SQL
- Código en PostgreSQL listo para ejecutar
- Incluir:
  - CREATE TABLE
  - ALTER TABLE (si aplica)
  - CREATE INDEX
  - CREATE TRIGGER (si aplica)
- Orden correcto de ejecución (respetando dependencias)
- SIN explicaciones dentro del bloque SQL

## 2. Documentación técnica
Para cada tabla, explicar:
- Propósito
- Justificación de los campos
- Decisiones de diseño (tipos de datos, relaciones, índices)
- Razón de uso de triggers (si existen)

---

### FORMATO ###
- Usar Markdown
- Separar claramente:
  - Bloque de código SQL
  - Documentación
- El SQL debe poder copiarse y ejecutarse directamente

---

### VALIDACIÓN ###
Si no hay suficiente información sobre:
- Entidades
- Relaciones
- Volumen de datos
- Casos de uso

Debes hacer preguntas primero y NO generar el modelo hasta tener claridad.

------

### CONTEXTO ###
con el contexto del proyecto que ya tienes,voy a crear un monorepo para subirlo en git, pero quiero que la Bd, el front y el back tengan sus propios contenedores en docker

### REQUERIMIENTO ###
Dame el sistema de carpetas desde la raíz, ejemplo:
evm-system/
│
├── backend/
│   ├── app/
│   ├── Dockerfile
│   └── requirements.txt
│
├── frontend/
│   ├── src/
│   ├── Dockerfile
│   └── package.json
│
├── database/
│   └── init.sql   # opcional
│
├── docker-compose.yml
├── .env
├── README.md
└── .gitignore

------
crea el archivo yml para levantar los dockers, crea el readme y el gitgnore

### SALIDA ESPERADA ###
espero el sistema de carpetas en orden anidado, los archivos mencionas para que solo sea copiar y pegar, 

------

### CONTEXTO ###
Voy a crear un monorepo para un sistema compuesto por:
- Backend en Python con Flask
- Frontend en React
- Base de datos PostgreSQL

Cada componente debe ejecutarse en su propio contenedor Docker y orquestarse con docker-compose.

El objetivo es tener un entorno listo para desarrollo local, funcional con un solo comando.

---

### REQUERIMIENTO ###

1. Define la estructura completa de carpetas desde la raíz del proyecto.

2. Incluye:
   - backend (Flask)
   - frontend (React)
   - database (PostgreSQL)
   - docker-compose.yml
   - archivo .env
   - README.md
   - .gitignore

3. Genera los siguientes archivos completos (listos para copiar y pegar):
   - docker-compose.yml (con servicios para backend, frontend y database)
   - Dockerfile para backend
   - Dockerfile para frontend
   - init.sql (opcional, si aplica)
   - .env
   - .gitignore
   - README.md

4. Configura correctamente:
   - Conexión del backend a PostgreSQL mediante variables de entorno
   - Puertos expuestos (backend, frontend, db)
   - Red interna de Docker
   - Volúmenes básicos si son necesarios

---

### SALIDA ###

## 1. Estructura del proyecto
- Mostrar árbol de carpetas en formato texto (tipo árbol)

## 2. Archivos
- Cada archivo en bloque de código separado
- Listos para copiar y ejecutar
- Sin placeholders incompletos

Archivos mínimos:
- docker-compose.yml
- backend/Dockerfile
- frontend/Dockerfile
- database/init.sql (si aplica)
- .env
- .gitignore
- README.md

---

### RESTRICCIONES ###
- Usar buenas prácticas de Docker
- Evitar configuraciones innecesarias
- Todo debe funcionar en entorno local sin cambios adicionales
- Mantener configuración simple y clara

---

### NOTAS ###
- El archivo docker-compose.yml debe permitir levantar todo el sistema con un solo comando: `docker-compose up`
- El README debe incluir:
  - Requisitos
  - Cómo levantar el entorno
  - Explicación breve de cada servicio

------

### CONTEXTO ###
Se te proporcionará una imagen con la estructura de carpetas actual del proyecto.


El objetivo es validar si la estructura es correcta y proponer mejoras alineadas a buenas prácticas y mantenibilidad.

---

### REQUERIMIENTO ###

1. Analiza la estructura de carpetas mostrada en la imagen.

2. Evalúa la estructura considerando:
   - Separación de responsabilidades
   - Escalabilidad
   - Legibilidad
   - Mantenibilidad
   - Buenas prácticas en proyectos Flask y React

3. Indica claramente:
   - Qué está bien
   - Qué está mal
   - Qué puede mejorar

---

4. Si la estructura NO es adecuada:
   - Propón una nueva estructura de carpetas para:
     - Backend 
     - Frontend 
   - Mostrar ambas estructuras en formato árbol

---

5. Define patrones de diseño recomendados:

### Backend
- Proponer un patrón adecuado (ej: Clean Architecture, Layered Architecture, etc.)
- Explicar por qué es el más adecuado considerando:
  - Múltiples APIs
  - Escalabilidad
  - Separación de lógica de negocio

### Frontend 
- Proponer un patrón (ej: Feature-based, Atomic Design, etc.)
- Explicar por qué es adecuado para consumir múltiples APIs

---

### SALIDA ###

1. Evaluación de la estructura actual (clara y directa)

2. Estructura propuesta:
   - Backend (formato árbol)
   - Frontend (formato árbol)

3. Patrones de diseño:
   - Backend → nombre + explicación + beneficios
   - Frontend → nombre + explicación + beneficios

---

### RESTRICCIONES ###
- No asumir información que no esté en la imagen
- Si falta contexto sobre APIs, indicarlo explícitamente
- Evitar respuestas genéricas
- Mantener enfoque práctico (usable en un equipo real)

------

### CONTEXTO ###
Ya se conoce el proyecto previamente. Considera las siguientes restricciones:

- No hay autenticación ni manejo de roles
- Es un sistema tipo CRUD
- La complejidad principal está en la lógica de consulta (validaciones, procesamiento de datos)
- No hay integraciones con sistemas externos
- No existen estados en las entidades (no flujos tipo aprobado/rechazado)

El objetivo es definir los casos de uso necesarios para diseñar:
- APIs del backend
- Funcionalidades del frontend

---

### REQUERIMIENTO ###

1. Define los casos de uso separándolos en:

### 1.1 Casos de uso de negocio (usuario)
- Acciones directas que realiza el usuario en el sistema

### 1.2 Casos de uso técnicos (sistema)
- Procesos internos necesarios para soportar la lógica, especialmente en consultas

---

2. Para cada caso de uso, incluye:

- Nombre del caso de uso
- Descripción clara
- Actor (usuario o sistema)
- Flujo principal (pasos numerados)
- Resultado esperado

---

3. Relaciona cada caso de uso con:

- API(s) necesarias (ej: POST /documentos, GET /consultas)
- Funcionalidad en frontend (pantalla, acción o componente)

---

4. Ordena los casos de uso según:

- Flujo lógico del sistema (de inicio a consulta)
- Dependencias entre funcionalidades

---

### SALIDA ###

- Formato Markdown
- Secciones claras:
  - Casos de uso de negocio
  - Casos de uso técnicos
- Cada caso de uso bien detallado (no solo títulos)
- Listas organizadas y numeradas

---

### RESTRICCIONES ###
- No incluir autenticación ni roles
- No inventar integraciones externas
- Evitar casos de uso innecesarios
- Mantener enfoque práctico para construir APIs y frontend
- Priorizar claridad sobre volumen

------
### CONTEXTO ###
Ya existe un plan de trabajo definido y la Fase 1 fue completada.

Ahora se debe ejecutar la Fase 2, tomando en cuenta también los casos de uso ya definidos previamente.

### OBJETIVO DE LA FASE 2 ###
Dejar el archivo `evm_service.py` 100% implementado, probado y listo para merge.

Incluye:

- Implementar `evm_service.py`
- Implementar las 8 fórmulas EVM necesarias
- Implementar interpretaciones de resultados
- Implementar `interpret_performance_index()`
- Implementar constantes `EVM_CONSTANTS`
- Crear unit tests completos
- Cubrir edge cases
- Validar cobertura mínima de 80% con pytest --cov
- Preparar PR `feature/evm-service` hacia `develop`

---

### REQUERIMIENTO ###

Genera una guía detallada paso a paso para que una persona nueva en el proyecto pueda implementar esta fase sin depender de conocimiento previo.

Debe incluir:

## 1. Contexto inicial
- Qué es `evm_service.py`
- Qué responsabilidad tiene dentro del sistema
- Cómo se relaciona con otros módulos

## 2. Orden recomendado de implementación
Explica qué hacer primero, segundo, tercero, etc.

## 3. Desarrollo técnico detallado

Para cada tarea:

### A. Fórmulas EVM
- Qué fórmulas implementar
- Qué reciben
- Qué retornan
- Validaciones necesarias
- Casos borde comunes

### B. Interpretaciones
- Cómo interpretar métricas
- Reglas sugeridas

### C. Constantes
- Cómo estructurar `EVM_CONSTANTS`

### D. Tests
- Qué probar
- Casos normales
- Casos edge
- Errores esperados

### E. Cobertura
- Cómo ejecutar pytest --cov
- Cómo validar mínimo 80%

### F. Pull Request
- Qué revisar antes de abrir PR
- Checklist de calidad

---

## 4. Validaciones finales
Checklist para saber si la fase quedó terminada correctamente.

---

## 5. Riesgos comunes
Errores típicos que puede cometer alguien nuevo y cómo evitarlos.

---

### SALIDA ESPERADA ###

- Formato Markdown limpio
- Títulos y subtítulos claros
- Listas numeradas
- Lenguaje sencillo pero profesional
- Debe parecer una guía interna descargable del proyecto
- Enfoque práctico, no teórico

------

Actúa como un Senior Python Developer especializado en backend, testing, Clean Code y arquitectura por capas.

### CONTEXTO GENERAL ###
Este chat NO tiene contexto previo del proyecto. Todo el trabajo se enfocará únicamente en escribir código correcto, limpio y profesional.

Trabajarás sobre el proyecto:

- Objetivo principal: Implementar completamente `evm_service.py`
- Cobertura mínima requerida: 80% sobre `app/services/`

---

# Guía de Implementación — Sprint 2: `evm_service.py`

**Proyecto:** EVM Project Tracker  
**Sprint:** 2 — Núcleo de negocio EVM  
**Rama de trabajo:** `feature/evm-service`  
**Rama destino del PR:** `develop`  
**Responsable de revisión:** Tech Lead  
**Cobertura mínima requerida:** 80% sobre `app/services/`

---

## Tabla de contenidos

1. [Contexto inicial](#1-contexto-inicial)
2. [Orden de implementación](#2-orden-de-implementación)
3. [Desarrollo técnico detallado](#3-desarrollo-técnico-detallado)
   - [A. Constantes EVM_CONSTANTS](#a-constantes-evm_constants)
   - [B. Fórmulas EVM](#b-fórmulas-evm)
   - [C. Interpretaciones](#c-interpretaciones)
   - [D. Funciones orquestadoras](#d-funciones-orquestadoras)
   - [E. Tests unitarios](#e-tests-unitarios)
   - [F. Cobertura con pytest --cov](#f-cobertura-con-pytest---cov)


---

## 1. Contexto inicial

### ¿Qué es `evm_service.py`?

`evm_service.py` es el módulo que contiene toda la lógica de negocio del sistema. Implementa la metodología **Earned Value Management (EVM)**, un estándar del PMI para medir si un proyecto está bien o mal en términos de cronograma y presupuesto.

Este archivo **no sabe nada de HTTP, Flask ni base de datos**. Recibe números, hace cálculos y devuelve resultados. Esa es su única responsabilidad.

### ¿Qué calcula?

A partir de cinco datos que el usuario ingresa por actividad:

| Campo | Nombre técnico | Descripción |
|---|---|---|
| Presupuesto total planificado | `bac` | Budget at Completion |
| Avance planificado a hoy | `planned_progress` | % entre 0 y 100 |
| Avance real completado | `actual_progress` | % entre 0 y 100 |
| Costo real incurrido | `actual_cost` | AC — Actual Cost |

El servicio calcula 8 indicadores:

| Indicador | Nombre completo | Lo que mide |
|---|---|---|
| PV | Planned Value | Cuánto trabajo debería estar hecho según el plan |
| EV | Earned Value | Cuánto trabajo está realmente hecho (en términos de costo) |
| CV | Cost Variance | Si se está gastando más o menos de lo que se avanza |
| SV | Schedule Variance | Si se va adelantado o atrasado respecto al plan |
| CPI | Cost Performance Index | Eficiencia en el uso del presupuesto |
| SPI | Schedule Performance Index | Eficiencia en el cumplimiento del cronograma |
| EAC | Estimate at Completion | Estimado de cuánto costará el proyecto al terminar |
| VAC | Variance at Completion | Diferencia entre el presupuesto original y el estimado final |

### ¿Cómo se relaciona con otros módulos?

```
HTTP Request
     ↓
Controller (project_blueprint.py / activity_blueprint.py)
     ↓
Service (project_service.py / activity_service.py)
     ↓  ← aquí se invoca evm_service.py
Repository (project_repo.py / activity_repo.py)
     ↓
Base de datos (PostgreSQL)
```

`evm_service.py` es invocado por `project_service.py` y `activity_service.py`. Nunca es invocado directamente desde un controller ni desde un repositorio. Nunca toca la base de datos.

### ¿Por qué es lo primero que se implementa?

Porque todos los endpoints del sistema dependen de él. Sin los cálculos EVM, ninguna respuesta del API puede construirse correctamente. Al implementarlo primero y cubrirlo con tests, se garantiza que la base matemática del sistema es correcta antes de agregar capas de HTTP y base de datos.

---

## 2. Orden de implementación

Sigue este orden estrictamente. Cada paso habilita el siguiente.

```

Paso 1 → Crear el archivo evm_service.py con las constantes
Paso 2 → Implementar las funciones primitivas (PV, EV, CV, SV)
Paso 3 → Implementar las funciones con edge cases (CPI, SPI, EAC, VAC)
Paso 4 → Implementar interpret_performance_index()
Paso 5 → Implementar los dataclasses de retorno
Paso 6 → Implementar calculate_activity_evm() (orquestadora por actividad)
Paso 7 → Implementar calculate_project_evm() (orquestadora por proyecto)
Paso 8 → Escribir todos los tests unitarios

```

---

## 3. Desarrollo técnico detallado

### A. Constantes `EVM_CONSTANTS`

#### ¿Por qué usar constantes?

El requerimiento exige **cero magic numbers**. Un número como `100` o `1` disperso en el código no explica qué representa. Si el criterio de eficiencia cambia en el futuro, habría que buscarlo en múltiples funciones. Las constantes resuelven ambos problemas.

#### Estructura recomendada

Crea una clase de solo atributos de clase (no instancias). No uses un diccionario: los atributos de clase permiten autocompletado en el IDE y son más seguros.

```python
from decimal import Decimal

class EVM_CONSTANTS:
    # Divisor para convertir porcentaje a decimal (50% → 0.50)
    PERCENT_DIVISOR = Decimal("100")

    # Umbral que define si un índice es eficiente o no
    PERFORMANCE_THRESHOLD = Decimal("1")

    # Interpretaciones de resultado — evitar strings literales dispersos
    INTERPRETATION_EFFICIENT = "efficient"
    INTERPRETATION_INEFFICIENT = "inefficient"
    INTERPRETATION_ON_TRACK = "on_track"
    INTERPRETATION_INSUFFICIENT_DATA = "insufficient_data"
```

**Regla:** Toda comparación contra `1` o toda división entre `100` en el archivo debe usar estas constantes, no los literales.

---

### B. Fórmulas EVM

#### Antes de implementar: tipos de datos

Usa `Decimal` de la librería estándar de Python para todos los cálculos. **Nunca uses `float`**.

```python
#  MAL — float introduce error de representación binaria
pv = (50 / 100) * 1000  # puede dar 499.99999999998

#  BIEN — Decimal garantiza precisión exacta
from decimal import Decimal
pv = (Decimal("50") / Decimal("100")) * Decimal("1000")  # da exactamente 500
```

Las funciones reciben `Decimal` y retornan `Decimal` o `Optional[Decimal]`. La conversión desde `float` o `str` a `Decimal` ocurre en la capa de servicio que invoca estas funciones, no aquí.

---

#### Función 1 — `calculate_pv`

**Fórmula:** `PV = (planned_progress / 100) × BAC`

**¿Qué mide?** El valor del trabajo que debería estar terminado a la fecha de corte, según el plan original.

**Firma:**
```python
def calculate_pv(bac: Decimal, planned_progress: Decimal) -> Decimal:
```

**Parámetros:**
- `bac`: presupuesto total de la actividad. Siempre ≥ 0.
- `planned_progress`: porcentaje planificado entre 0 y 100.

**Retorna:** `Decimal` — el valor planificado.

**Edge cases:**
- `planned_progress = 0` → retorna `Decimal("0")`. Válido, significa que nada debería estar hecho aún.
- `planned_progress = 100` → retorna el valor completo del `bac`.
- `bac = 0` → retorna `Decimal("0")`. Válido también.

**No lanzar excepciones** en ninguno de estos casos. Son estados válidos de una actividad.

---

#### Función 2 — `calculate_ev`

**Fórmula:** `EV = (actual_progress / 100) × BAC`

**¿Qué mide?** El valor del trabajo que realmente está terminado, expresado en términos del presupuesto.

**Firma:**
```python
def calculate_ev(bac: Decimal, actual_progress: Decimal) -> Decimal:
```

**Edge cases:** Mismos que `calculate_pv`. Si `actual_progress = 0`, el proyecto no ha avanzado nada y `EV = 0`.

---

#### Función 3 — `calculate_cv`

**Fórmula:** `CV = EV − AC`

**¿Qué mide?** La variación de costo. Positivo significa que se está gastando menos de lo que se avanza (bueno). Negativo indica sobrecosto.

**Firma:**
```python
def calculate_cv(ev: Decimal, actual_cost: Decimal) -> Decimal:
```

**Edge cases:**
- `ev = 0` y `actual_cost > 0` → resultado negativo. El proyecto gastó dinero sin avanzar.
- `actual_cost = 0` → `CV = EV`. Situación rara pero matemáticamente válida.

**No retorna `None`** nunca. La resta siempre es posible.

---

#### Función 4 — `calculate_sv`

**Fórmula:** `SV = EV − PV`

**¿Qué mide?** La variación de cronograma. Negativo significa atraso. Positivo significa adelanto.

**Firma:**
```python
def calculate_sv(ev: Decimal, pv: Decimal) -> Decimal:
```

**Edge cases:** Mismos patrones que `calculate_cv`. Nunca retorna `None`.

---

#### Función 5 — `calculate_cpi`  Contiene el edge case más importante

**Fórmula:** `CPI = EV / AC`

**¿Qué mide?** Por cada peso gastado, cuántos pesos de valor se obtienen. CPI > 1 es eficiente. CPI < 1 significa que se gasta más de lo que se avanza.

**Firma:**
```python
def calculate_cpi(ev: Decimal, actual_cost: Decimal) -> Optional[Decimal]:
```

**Edge case crítico:** Si `actual_cost = 0`, **no se puede calcular CPI** (división por cero). Este caso ocurre cuando una actividad está planificada pero aún no se ha incurrido en ningún costo. No es un error del usuario — es un estado válido de la actividad.

**Regla:** Si `actual_cost == 0`, retorna `None`. No lanzar `ZeroDivisionError`.

```python
#  Correcto
if actual_cost == Decimal("0"):
    return None
return ev / actual_cost
```

**Edge case secundario:** `ev = 0` y `actual_cost > 0` → retorna `Decimal("0")`. Se gastó dinero pero no hay avance. Es un CPI válido (y muy malo).

---

#### Función 6 — `calculate_spi`  Mismo patrón que CPI

**Fórmula:** `SPI = EV / PV`

**¿Qué mide?** Por cada unidad de trabajo planificada, cuánta se completó realmente. SPI > 1 es adelanto. SPI < 1 es atraso.

**Firma:**
```python
def calculate_spi(ev: Decimal, pv: Decimal) -> Optional[Decimal]:
```

**Edge case crítico:** Si `pv = 0`, retorna `None`. Ocurre cuando `planned_progress = 0`, es decir, la actividad aún no debería haber comenzado según el plan. Calcular un SPI en ese estado no tiene sentido.

---

#### Función 7 — `calculate_eac`

**Fórmula:** `EAC = BAC / CPI`

**¿Qué mide?** Si el proyecto continúa al ritmo actual de eficiencia, ¿cuánto costará en total al terminar?

**Firma:**
```python
def calculate_eac(bac: Decimal, cpi: Optional[Decimal]) -> Optional[Decimal]:
```

**Edge cases:**
- Si `cpi` es `None` → retorna `None`. No se puede estimar si no hay CPI.
- Si `cpi == 0` → retorna `None`. División por cero.
- `cpi > 0` → retorna `bac / cpi`.

---

#### Función 8 — `calculate_vac`

**Fórmula:** `VAC = BAC − EAC`

**¿Qué mide?** La diferencia entre el presupuesto original y el costo estimado final. Negativo significa que se prevé gastar más de lo presupuestado.

**Firma:**
```python
def calculate_vac(bac: Decimal, eac: Optional[Decimal]) -> Optional[Decimal]:
```

**Edge cases:**
- Si `eac` es `None` → retorna `None`. Sin EAC no hay VAC.

---

### C. Interpretaciones

#### `interpret_performance_index`

Esta función recibe el valor numérico de CPI o SPI y retorna un string que describe el estado. Es la función que el frontend usa para determinar el color del `StatusBadge`.

**Firma:**
```python
def interpret_performance_index(value: Optional[Decimal]) -> str:
```

**Reglas de interpretación:**

| Condición | Retorno | Significado |
|---|---|---|
| `value is None` | `"insufficient_data"` | No hay datos suficientes para calcular |
| `value > 1` | `"efficient"` | Por debajo del presupuesto / adelantado |
| `value == 1` | `"on_track"` | Exactamente en línea con el plan |
| `value < 1` | `"inefficient"` | Sobre presupuesto / atrasado |

**Importante:** Usa las constantes definidas en `EVM_CONSTANTS`, no strings literales.

```python
#  Correcto
return EVM_CONSTANTS.INTERPRETATION_EFFICIENT

#  Incorrecto — magic string
return "efficient"
```

---

### D. Funciones orquestadoras

Estas dos funciones coordinan las funciones primitivas y producen los objetos de resultado completos.

#### Dataclasses de retorno

Declara estos dataclasses **antes** de las funciones orquestadoras en el mismo archivo. Son los contratos de datos que los servicios de nivel superior esperan recibir.

```python
from dataclasses import dataclass
from decimal import Decimal
from typing import Optional

@dataclass
class ActivityEVMResult:
    pv: Decimal
    ev: Decimal
    cv: Decimal
    sv: Decimal
    cpi: Optional[Decimal]
    spi: Optional[Decimal]
    eac: Optional[Decimal]
    vac: Optional[Decimal]
    cpi_interpretation: str
    spi_interpretation: str

@dataclass
class ProjectEVMResult:
    total_bac: Decimal
    total_pv: Decimal
    total_ev: Decimal
    total_ac: Decimal
    cv: Decimal
    sv: Decimal
    cpi: Optional[Decimal]
    spi: Optional[Decimal]
    eac: Optional[Decimal]
    vac: Optional[Decimal]
    cpi_interpretation: str
    spi_interpretation: str
```

---

#### `calculate_activity_evm`

Recibe los cuatro valores crudos de una actividad y retorna un `ActivityEVMResult` completo.

**Firma:**
```python
def calculate_activity_evm(
    bac: Decimal,
    planned_progress: Decimal,
    actual_progress: Decimal,
    actual_cost: Decimal,
) -> ActivityEVMResult:
```

**Flujo interno:**
1. Llama `calculate_pv(bac, planned_progress)` → `pv`
2. Llama `calculate_ev(bac, actual_progress)` → `ev`
3. Llama `calculate_cv(ev, actual_cost)` → `cv`
4. Llama `calculate_sv(ev, pv)` → `sv`
5. Llama `calculate_cpi(ev, actual_cost)` → `cpi`
6. Llama `calculate_spi(ev, pv)` → `spi`
7. Llama `calculate_eac(bac, cpi)` → `eac`
8. Llama `calculate_vac(bac, eac)` → `vac`
9. Llama `interpret_performance_index(cpi)` → `cpi_interpretation`
10. Llama `interpret_performance_index(spi)` → `spi_interpretation`
11. Retorna `ActivityEVMResult(...)` con todos los valores.

**Regla:** Esta función no hace ningún cálculo directo. Solo coordina las funciones primitivas.

---

#### `calculate_project_evm`

Recibe la lista de objetos `Activity` de un proyecto y retorna un `ProjectEVMResult` con los indicadores consolidados.

**Firma:**
```python
def calculate_project_evm(activities: list) -> ProjectEVMResult:
```

**Edge case crítico — lista vacía:**
Si `activities` está vacío, retorna un `ProjectEVMResult` con todos los valores en `Decimal("0")` y los índices en `None`. No lanzar excepciones.

**Por qué la agregación es por suma y no por promedio:**
Si una actividad tiene BAC de $50,000 y otra de $1,000, promediar sus CPI individuales daría el mismo peso a ambas. La suma de valores absolutos garantiza que actividades con mayor presupuesto tengan mayor impacto en el indicador consolidado. Eso refleja la realidad del proyecto.

**Flujo interno:**
1. Si `activities` está vacío → retornar `ProjectEVMResult` con ceros y `None`.
2. Sumar los `bac` de todas las actividades → `total_bac`.
3. Sumar los PV individuales calculados → `total_pv`.
4. Sumar los EV individuales calculados → `total_ev`.
5. Sumar los `actual_cost` → `total_ac`.
6. Calcular CV, SV, CPI, SPI, EAC, VAC sobre los totales usando las funciones primitivas.
7. Retornar `ProjectEVMResult(...)`.

**Nota de implementación:** Los atributos del modelo `Activity` son numéricos de la BD (pueden venir como `Decimal` o `str` según el driver). Convierte explícitamente con `Decimal(str(activity.bac))` para evitar pérdida de precisión.

---

### E. Tests unitarios

Los tests van en `tests/unit/test_evm_service.py`. Usa `pytest` con clases para agrupar los casos de cada función.

#### Estructura base del archivo

```python
from decimal import Decimal
import pytest
from app.services.evm_service import (
    calculate_pv,
    calculate_ev,
    calculate_cv,
    calculate_sv,
    calculate_cpi,
    calculate_spi,
    calculate_eac,
    calculate_vac,
    interpret_performance_index,
    calculate_activity_evm,
    calculate_project_evm,
    EVM_CONSTANTS,
)
```

#### Casos obligatorios por función

**`TestCalculatePV`**
```
 caso estándar: bac=1000, planned_progress=50 → 500
 progreso cero: bac=1000, planned_progress=0 → 0
 progreso completo: bac=1000, planned_progress=100 → 1000
 bac cero: bac=0, planned_progress=50 → 0
 progreso parcial con decimales: bac=3000, planned_progress=33.33 → 999.90
```

**`TestCalculateEV`**
```
 caso estándar: bac=1000, actual_progress=40 → 400
 progreso cero: ev=0
 completado al 100%: ev=bac
```

**`TestCalculateCV`**
```
 eficiente: ev=800, ac=600 → 200 (positivo)
 ineficiente: ev=400, ac=600 → -200 (negativo)
 ac cero: ev=500, ac=0 → 500
 ev cero, ac positivo: ev=0, ac=200 → -200
```

**`TestCalculateSV`**
```
 adelantado: ev=800, pv=600 → 200
 atrasado: ev=400, pv=600 → -200
 pv cero: ev=500, pv=0 → 500
```

**`TestCalculateCPI`** — Este es el más importante
```
 eficiente: ev=800, ac=600 → Decimal > 1
 ineficiente: ev=400, ac=600 → Decimal < 1
 ac=0 → None  (edge case crítico — sin excepción)
 ev=0, ac positivo → Decimal("0")
 ev=1000, ac=1000 → Decimal("1")
```

**`TestCalculateSPI`**
```
 adelantado: ev=800, pv=600 → Decimal > 1
 atrasado: ev=400, pv=600 → Decimal < 1
 pv=0 → None  (edge case crítico — sin excepción)
 ev=0, pv positivo → Decimal("0")
```

**`TestCalculateEAC`**
```
 cpi normal: bac=1000, cpi=0.8 → 1250
 cpi=None → None
 cpi=0 → None
 cpi=1 → bac
```

**`TestCalculateVAC`**
```
 caso normal: bac=1000, eac=1250 → -250
 eac=None → None
 eac=bac → 0
```

**`TestInterpretPerformanceIndex`**
```
 value > 1 → "efficient"
 value == 1 → "on_track"
 value < 1 → "inefficient"
 value = None → "insufficient_data"
```

**`TestCalculateActivityEVM`** — Tests de integración interna
```
 actividad estándar con todos los campos (verificar los 10 campos del resultado)
 ac=0 → cpi=None, eac=None, vac=None, cpi_interpretation="insufficient_data"
 actual_progress=0 → ev=0, cv=-ac, sv=-pv
 completada al 100% en presupuesto → ev=bac, cv=0, cpi=1, interpretation="on_track"
 proyecto adelantado y bajo presupuesto → cpi>1, spi>1, ambos "efficient"
 proyecto atrasado y sobre presupuesto → cpi<1, spi<1, ambos "inefficient"
```

**`TestCalculateProjectEVM`** — Edge cases de consolidación
```
 lista vacía → total_bac=0, cpi=None, interpretation="insufficient_data"
 una sola actividad → coincide con calculate_activity_evm
 múltiples actividades → verificar que la suma es correcta
 actividad con ac=0 junto a otra con ac>0 → cpi se calcula sobre el total_ac
```

#### Ejemplo de test bien escrito

```python
class TestCalculateCPI:
    def test_returns_none_when_actual_cost_is_zero(self):
        result = calculate_cpi(ev=Decimal("500"), actual_cost=Decimal("0"))
        assert result is None

    def test_returns_decimal_less_than_one_when_inefficient(self):
        result = calculate_cpi(ev=Decimal("400"), actual_cost=Decimal("600"))
        assert result is not None
        assert result < EVM_CONSTANTS.PERFORMANCE_THRESHOLD

    def test_does_not_raise_when_ev_is_zero_and_ac_is_positive(self):
        result = calculate_cpi(ev=Decimal("0"), actual_cost=Decimal("200"))
        assert result == Decimal("0")
```

---

### F. Cobertura con pytest --cov

#### Configuración en `pytest.ini`

Verifica que el archivo `pytest.ini` en la raíz del backend tenga esta configuración:

```ini
[pytest]
testpaths = tests
addopts = --cov=app/services --cov-report=term-missing --cov-fail-under=80
```

- `--cov=app/services`: solo mide cobertura sobre la capa de servicios.
- `--cov-report=term-missing`: muestra en consola qué líneas no tienen cobertura.
- `--cov-fail-under=80`: falla el comando si la cobertura baja del 80%.
---

------

### CONTEXTO DEL PROYECTO ###
Existe un proyecto backend en Flask ya avanzado.

Las Fases 1 y 2 ya fueron completadas exitosamente.

Ahora se debe ejecutar la Fase 3.

### ALCANCE DE FASE 3 ###
1. Implementar Application Factory
2. Crear Blueprint de proyectos con CRUD completo
3. Crear Blueprint de actividades con CRUD completo
4. Integrar actividades con evm_service
5. Crear Schemas Marshmallow request/response
6. Manejo centralizado de errores:
   - 404
   - 422
   - 500
7. Configurar flask-smorest
8. Habilitar Swagger UI en /api-docs
9. Crear mínimo 1 test de integración por endpoint
10. Flujo Git:
   PR feature/api -> develop

### OBJETIVO ###
Generar una guía paso a paso para un desarrollador nuevo que no conoce el proyecto, para que pueda implementar toda la Fase 3 correctamente.

### FORMATO DE SALIDA ###
- Markdown limpio
- Estructura profesional
- Orden cronológico real de ejecución
- Títulos y subtítulos claros
- Checklist por cada etapa
- Archivos/carpetas sugeridas
- Buenas prácticas recomendadas
- Riesgos comunes a evitar
- Lenguaje práctico, no teórico
- Debe parecer documentación interna descargable

### IMPORTANTE ###
No asumir conocimiento previo del proyecto.
Si falta contexto técnico, indicar supuestos razonables.

------

### CONTEXTO DEL PROYECTO ###
Existe un proyecto backend en Flask ya avanzado.
Las Fases 1 2 y 3 ya fueron completadas exitosamente.
Ahora se debe ejecutar la Fase 4.

### ALCANCE DE FASE 4 ###
1. Scaffolding Vite + React, configurar eslint, instalar dependencias
2. evmApi.js: Axios instance + funciones para proyectos y actividades
3. useProject custom hook
4. ActivityTable con colores semánticos por CPI/SPI
5. ActivityForm con validación de campos
6. ConsolidatedKPIs + StatusBadge
7. EVMChart con Recharts (PV vs EV vs AC por actividad)
8. ProjectDetailPage integrando todos los componentes
9. ProjectsPage (lista + crear proyecto)
10. PR feature/frontend-dashboard → develop

### OBJETIVO ###
Generar una guía paso a paso para un desarrollador nuevo que no conoce el proyecto, para que pueda implementar toda la Fase 4 correctamente, no es necesario generar código, solo indicar que se debe hacer y como, si ves pertinente agregar los nombres de métodos y archivos junto con su lugar 

### FORMATO DE SALIDA ###
- Markdown limpio
- Estructura profesional
- Orden cronológico real de ejecución
- Títulos y subtítulos claros
- Checklist por cada etapa
- Archivos/carpetas sugeridas
- Buenas prácticas recomendadas
- Riesgos comunes a evitar
- Lenguaje práctico, no teórico
- Debe parecer documentación interna descargable

### IMPORTANTE ###
No asumir conocimiento previo del proyecto.
Si falta contexto técnico, indicar supuestos razonables.

------
### ROL ###
Actúa como un Tech Lead Frontend Senior especializado en React, Vite y dashboards empresariales.

### CONTEXTO DEL PROYECTO ###
Existe un sistema backend en Flask ya avanzado.
Las Fases 1, 2 y 3 fueron completadas exitosamente.

Ahora corresponde ejecutar la Fase 4, enfocada en frontend dashboard.


### PERFIL DEL DESARROLLADOR ###
El desarrollador sabe programar, pero no conoce este proyecto ni su estructura interna.

### ALCANCE DE FASE 4 ###
1. Scaffolding Vite + React
2. Configurar ESLint
3. Instalar dependencias
4. Crear evmApi.js:
   - Axios instance
   - métodos proyectos
   - métodos actividades
5. Crear custom hook useProject
6. Crear ActivityTable con colores por CPI/SPI
7. Crear ActivityForm con validaciones
8. Crear ConsolidatedKPIs
9. Crear StatusBadge
10. Crear EVMChart con Recharts
11. Crear ProjectDetailPage integrando componentes
12. Crear ProjectsPage (listar + crear proyecto)
13. PR feature/frontend-dashboard → develop

### OBJETIVO ###
Generar una guía paso a paso para implementar toda la Fase 4.

No generar código.
Solo indicar:
- Qué hacer
- Cómo hacerlo
- Orden correcto
- Archivos sugeridos
- Métodos sugeridos
- Validaciones necesarias
- indicaciones de como se llama el api y como consumirlas

### FORMATO DE SALIDA ###
- Markdown limpio
- Orden cronológico real
- Checklist por etapa
- Estructura de carpetas sugerida
- Buenas prácticas React
- Riesgos comunes
- Cómo probar cada módulo
- Lenguaje práctico
- Debe parecer documentación interna profesional

### IMPORTANTE ###
No asumir conocimiento previo del proyecto.
Si falta información, usar supuestos razonables e indicarlos.
Priorizar mantenibilidad y escalabilidad.

------

# Guía de Implementación — Fase 3: API REST Completa

 
**Fase:** 3 — API REST, Blueprints, Schemas y Swagger  
**Rama de trabajo:** `feature/api`  
**Rama destino del PR:** `develop`   
**Cobertura mínima requerida:** Al menos 1 test de integración por endpoint

---

## Tabla de contenidos

1. [Antes de empezar](#1-antes-de-empezar)
2. [Orden de implementación](#2-orden-de-implementación)
3. [Paso 1 — Application Factory](#paso-2--application-factory)
4. [Paso 2 — Schemas Marshmallow](#paso-3--schemas-marshmallow)
5. [Paso 3 — Repositorios](#paso-4--repositorios)
7. [Paso 4 — Services de orquestación](#paso-5--services-de-orquestación)
8. [Paso 5 — Manejo centralizado de errores](#paso-6--manejo-centralizado-de-errores)
9. [Paso 6 — Blueprint de Proyectos](#paso-7--blueprint-de-proyectos)
10. [Paso 7 — Blueprint de Actividades](#paso-8--blueprint-de-actividades)
11. [Paso 8 — Swagger UI con flask-smorest](#paso-9--swagger-ui-con-flask-smorest)
12. [Paso 9 — Tests de integración](#paso-10--tests-de-integración)

---

## 1. Antes de empezar

### ¿Qué se construye en esta fase?

La Fase 3 convierte el proyecto en una API REST funcional y documentada. Al terminar, existirán 9 endpoints HTTP que permiten gestionar proyectos y actividades, cada uno retornando automáticamente los indicadores EVM calculados.

### ¿Qué ya existe y no debes tocar?

De las fases anteriores ya están implementados y testeados:

| Archivo | Qué contiene | Estado |
|---|---|---|
| `app/services/evm_service.py` | 8 fórmulas EVM, funciones orquestadoras | ✅ Completo |
| `app/models/project.py` | Modelo SQLAlchemy `Project` | ✅ Completo |
| `app/models/activity.py` | Modelo SQLAlchemy `Activity` | ✅ Completo |
| `app/extensions.py` | Instancias `db`, `migrate`, `api` | ✅ Completo |
| `app/config.py` | `Config` y `TestingConfig` | ✅ Completo |
| `database/init.sql` | Script de inicialización PostgreSQL | ✅ Completo |

**Regla:** No modificar ninguno de estos archivos salvo que encuentres un bug real. Si dudas, consulta al Tech Lead antes de cambiar algo de fases anteriores.

### Endpoints que vas a construir

| Método | Endpoint | Descripción |
|---|---|---|
| `GET` | `/api/v1/projects/` | Listar todos los proyectos |
| `POST` | `/api/v1/projects/` | Crear un proyecto |
| `GET` | `/api/v1/projects/{id}` | Obtener detalle de un proyecto |
| `PUT` | `/api/v1/projects/{id}` | Actualizar un proyecto |
| `DELETE` | `/api/v1/projects/{id}` | Eliminar un proyecto |
| `GET` | `/api/v1/projects/{id}/activities` | Listar actividades de un proyecto |
| `POST` | `/api/v1/projects/{id}/activities` | Crear actividad en un proyecto |
| `PUT` | `/api/v1/activities/{id}` | Actualizar una actividad |
| `DELETE` | `/api/v1/activities/{id}` | Eliminar una actividad |

### Estructura final de archivos que debes crear

```
backend/
└── app/
    ├── schemas/
    │   ├── __init__.py
    │   ├── project_schema.py       ← NUEVO
    │   └── activity_schema.py      ← NUEVO
    ├── repositories/
    │   ├── __init__.py
    │   ├── project_repo.py         ← NUEVO
    │   └── activity_repo.py        ← NUEVO
    ├── services/
    │   ├── project_service.py      ← NUEVO
    │   └── activity_service.py     ← NUEVO
    ├── controllers/
    │   ├── __init__.py
    │   ├── project_blueprint.py    ← NUEVO
    │   └── activity_blueprint.py   ← NUEVO
    ├── errors/
    │   ├── __init__.py
    │   └── handlers.py             ← NUEVO
    └── __init__.py                 ← MODIFICAR (registrar blueprints)

tests/
└── integration/
    ├── __init__.py
    ├── test_projects_endpoint.py   ← NUEVO
    └── test_activities_endpoint.py ← NUEVO
```

---

## 2. Orden de implementación

```

Paso 1  → Application Factory (app/__init__.py)
Paso 2  → Schemas Marshmallow (validación y serialización)
Paso 3  → Repositorios (acceso a datos)
Paso 4  → Services de orquestación (coordinan repo + evm_service)
Paso 5  → Manejo centralizado de errores
Paso 6  → Blueprint de Proyectos
Paso 7  → Blueprint de Actividades
Paso 8  → Swagger UI con flask-smorest
Paso 9 → Tests de integración
```

**¿Por qué este orden?**  
Los schemas se necesitan antes que los controllers (los controllers los invocan). Los repositorios se necesitan antes que los services (los services los llaman). Los services se necesitan antes que los controllers (los controllers los llaman). Los errores van antes que los controllers para que desde el primer endpoint el manejo sea consistente.

---

## Paso 1 — Application Factory

### 1.1 Modificar `app/__init__.py`

Este archivo ya puede tener una versión básica de fases anteriores. La versión final debe quedar así:

```python
from flask import Flask
from app.extensions import db, migrate, api
from app.config import Config


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    # Inicializar extensiones con la app
    db.init_app(app)
    migrate.init_app(app, db)
    api.init_app(app)

    # Registrar manejadores de error
    from app.errors.handlers import register_error_handlers
    register_error_handlers(app)

    # Registrar blueprints
    from app.controllers.project_blueprint import blp as project_blp
    from app.controllers.activity_blueprint import blp as activity_blp

    api.register_blueprint(project_blp)
    api.register_blueprint(activity_blp)

    return app
```

**¿Por qué los imports de blueprints van dentro de la función?**  
Para evitar imports circulares. Si los blueprints se importan al nivel del módulo, se ejecutan antes de que `db` y `api` estén configurados, lo que causa errores de inicialización.

### 1.2 Verificar `app/config.py`

Confirma que tiene esta estructura. No modificar si ya existe:

```python
import os


class Config:
    SECRET_KEY = os.environ.get("SECRET_KEY", "fallback-dev-key")
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # flask-smorest / OpenAPI
    API_TITLE = "EVM Project Tracker API"
    API_VERSION = "v1"
    OPENAPI_VERSION = "3.0.3"
    OPENAPI_URL_PREFIX = "/"
    OPENAPI_SWAGGER_UI_PATH = "/api-docs"
    OPENAPI_SWAGGER_UI_URL = "https://cdn.jsdelivr.net/npm/swagger-ui-dist/"


class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = "sqlite:///:memory:"
```

---

## Paso 2 — Schemas Marshmallow

### ¿Qué son los schemas?

Los schemas tienen dos responsabilidades:

1. **Validar el input:** Cuando el usuario envía un `POST` o `PUT`, el schema verifica que los datos tienen el formato correcto antes de que lleguen al service. Si algo falla, retorna automáticamente HTTP 422 con el detalle del error.

2. **Serializar el output:** Cuando el sistema retorna datos, el schema los convierte a diccionario JSON con los campos correctos.

**Regla crítica:** La validación de negocio (rangos, tipos) vive en los schemas. Los controllers nunca validan manualmente el input.

### 2.1 Crear `app/schemas/__init__.py`

```python
# Vacío — solo marca el directorio como paquete Python
```

### 2.2 Crear `app/schemas/project_schema.py`

```python
import marshmallow as ma
from marshmallow import validate


class ProjectCreateSchema(ma.Schema):
    """Valida el body de POST /projects/"""
    name = ma.fields.String(
        required=True,
        validate=validate.Length(min=1, max=255),
        metadata={"description": "Nombre del proyecto"}
    )
    description = ma.fields.String(
        load_default=None,
        metadata={"description": "Descripción opcional del proyecto"}
    )


class ProjectUpdateSchema(ma.Schema):
    """Valida el body de PUT /projects/{id}"""
    name = ma.fields.String(
        validate=validate.Length(min=1, max=255),
        metadata={"description": "Nuevo nombre del proyecto"}
    )
    description = ma.fields.String(
        load_default=None,
        metadata={"description": "Nueva descripción del proyecto"}
    )


class EVMProjectSchema(ma.Schema):
    """Serializa los indicadores EVM consolidados del proyecto"""
    total_bac = ma.fields.String()
    total_pv = ma.fields.String()
    total_ev = ma.fields.String()
    total_ac = ma.fields.String()
    cv = ma.fields.String()
    sv = ma.fields.String()
    cpi = ma.fields.String(allow_none=True)
    spi = ma.fields.String(allow_none=True)
    eac = ma.fields.String(allow_none=True)
    vac = ma.fields.String(allow_none=True)
    cpi_interpretation = ma.fields.String()
    spi_interpretation = ma.fields.String()


class ProjectResponseSchema(ma.Schema):
    """Serializa la respuesta de cualquier endpoint de proyecto"""
    id = ma.fields.String()
    name = ma.fields.String()
    description = ma.fields.String(allow_none=True)
    created_at = ma.fields.String()
    updated_at = ma.fields.String()
    activities = ma.fields.List(ma.fields.Dict(), load_default=[])
    evm = ma.fields.Nested(EVMProjectSchema)
```

### 2.3 Crear `app/schemas/activity_schema.py`

```python
import marshmallow as ma
from marshmallow import validate


class ActivityCreateSchema(ma.Schema):
    """Valida el body de POST /projects/{id}/activities"""
    name = ma.fields.String(
        required=True,
        validate=validate.Length(min=1, max=255),
        metadata={"description": "Nombre de la actividad"}
    )
    bac = ma.fields.Decimal(
        required=True,
        validate=validate.Range(min=0),
        metadata={"description": "Budget at Completion — presupuesto total de la actividad"}
    )
    planned_progress = ma.fields.Decimal(
        required=True,
        validate=validate.Range(min=0, max=100),
        metadata={"description": "Porcentaje de avance planificado a la fecha de corte (0-100)"}
    )
    actual_progress = ma.fields.Decimal(
        required=True,
        validate=validate.Range(min=0, max=100),
        metadata={"description": "Porcentaje de avance real completado (0-100)"}
    )
    actual_cost = ma.fields.Decimal(
        required=True,
        validate=validate.Range(min=0),
        metadata={"description": "Costo real incurrido hasta la fecha (AC)"}
    )


class ActivityUpdateSchema(ma.Schema):
    """Valida el body de PUT /activities/{id} — todos los campos son opcionales"""
    name = ma.fields.String(validate=validate.Length(min=1, max=255))
    bac = ma.fields.Decimal(validate=validate.Range(min=0))
    planned_progress = ma.fields.Decimal(validate=validate.Range(min=0, max=100))
    actual_progress = ma.fields.Decimal(validate=validate.Range(min=0, max=100))
    actual_cost = ma.fields.Decimal(validate=validate.Range(min=0))


class EVMActivitySchema(ma.Schema):
    """Serializa los 10 campos EVM calculados por actividad"""
    pv = ma.fields.String()
    ev = ma.fields.String()
    cv = ma.fields.String()
    sv = ma.fields.String()
    cpi = ma.fields.String(allow_none=True)
    spi = ma.fields.String(allow_none=True)
    eac = ma.fields.String(allow_none=True)
    vac = ma.fields.String(allow_none=True)
    cpi_interpretation = ma.fields.String()
    spi_interpretation = ma.fields.String()


class ActivityResponseSchema(ma.Schema):
    """Serializa la respuesta de cualquier endpoint de actividad"""
    id = ma.fields.String()
    project_id = ma.fields.String()
    name = ma.fields.String()
    bac = ma.fields.String()
    planned_progress = ma.fields.String()
    actual_progress = ma.fields.String()
    actual_cost = ma.fields.String()
    created_at = ma.fields.String()
    updated_at = ma.fields.String()
    evm = ma.fields.Nested(EVMActivitySchema)
```

**¿Por qué los valores numéricos se serializan como `String` en la respuesta?**  
Los tipos `Decimal` de Python no se serializan nativamente a JSON. Convertirlos a `String` evita pérdida de precisión (un `float` en JSON puede producir `1000.0000000001`). El frontend recibe el string `"1000.00"` y lo puede mostrar o parsear con precisión.

---

## Paso 3 — Repositorios

### ¿Qué son los repositorios?

Los repositorios encapsulan todo el acceso a la base de datos. Su única responsabilidad es ejecutar queries SQLAlchemy y retornar objetos del modelo. No contienen lógica de negocio ni cálculos EVM.

**Regla crítica:** Si en un repositorio ves un `if` que toma decisiones de negocio, ese código está en el lugar equivocado. Los `if` de negocio van en los services.

### 3.1 Crear `app/repositories/__init__.py`

```python
# Vacío
```

### 3.2 Crear `app/repositories/project_repo.py`

```python
from app.extensions import db
from app.models.project import Project


class ProjectRepository:

    def fetch_all_projects(self) -> list[Project]:
        return (
            db.session.execute(
                db.select(Project).order_by(Project.created_at.desc())
            )
            .scalars()
            .all()
        )

    def fetch_project_by_id(self, project_id) -> Project | None:
        return db.session.get(Project, project_id)

    def save_project(self, name: str, description: str | None) -> Project:
        project = Project(name=name, description=description)
        db.session.add(project)
        db.session.commit()
        db.session.refresh(project)
        return project

    def update_project_fields(self, project: Project, fields: dict) -> Project:
        for field, value in fields.items():
            setattr(project, field, value)
        db.session.commit()
        db.session.refresh(project)
        return project

    def remove_project(self, project: Project) -> None:
        db.session.delete(project)
        db.session.commit()
```

### 3.3 Crear `app/repositories/activity_repo.py`

```python
from app.extensions import db
from app.models.activity import Activity


class ActivityRepository:

    def fetch_activities_by_project(self, project_id) -> list[Activity]:
        return (
            db.session.execute(
                db.select(Activity)
                .where(Activity.project_id == project_id)
                .order_by(Activity.created_at.desc())
            )
            .scalars()
            .all()
        )

    def fetch_activity_by_id(self, activity_id) -> Activity | None:
        return db.session.get(Activity, activity_id)

    def save_activity(self, project_id, data: dict) -> Activity:
        activity = Activity(project_id=project_id, **data)
        db.session.add(activity)
        db.session.commit()
        db.session.refresh(activity)
        return activity

    def update_activity_fields(self, activity: Activity, fields: dict) -> Activity:
        for field, value in fields.items():
            setattr(activity, field, value)
        db.session.commit()
        db.session.refresh(activity)
        return activity

    def remove_activity(self, activity: Activity) -> None:
        db.session.delete(activity)
        db.session.commit()
```

**¿Por qué `db.session.refresh()` después de `commit()`?**  
Después de un `commit()`, SQLAlchemy expira los atributos del objeto para forzar una recarga desde la BD en el siguiente acceso. Si intentas retornar el objeto sin `refresh()`, el acceso a sus atributos dispara una query adicional que puede fallar si la sesión ya está cerrada. `refresh()` carga explícitamente los datos actualizados antes de retornar.


---

## Paso 4 — Services de orquestación

### ¿Qué hacen estos services?

Son la capa que coordina repositorios y el servicio EVM. Cada función de service:

1. Llama al repositorio para obtener o persistir datos
2. Invoca `evm_service` para calcular indicadores
3. Ensambla el diccionario de respuesta que el controller retornará

**Regla crítica:** Los services nunca retornan objetos SQLAlchemy directamente. Retornan diccionarios serializables que los controllers pueden devolver como JSON.

### 4.1 Crear `app/services/project_service.py`

```python
from decimal import Decimal
from app.repositories.project_repo import ProjectRepository
from app.repositories.activity_repo import ActivityRepository
from app.services.evm_service import calculate_activity_evm, calculate_project_evm

project_repo = ProjectRepository()
activity_repo = ActivityRepository()


def _serialize_evm_activity(evm_result) -> dict:
    """Convierte un ActivityEVMResult en diccionario serializable."""
    return {
        "pv": str(evm_result.pv),
        "ev": str(evm_result.ev),
        "cv": str(evm_result.cv),
        "sv": str(evm_result.sv),
        "cpi": str(evm_result.cpi) if evm_result.cpi is not None else None,
        "spi": str(evm_result.spi) if evm_result.spi is not None else None,
        "eac": str(evm_result.eac) if evm_result.eac is not None else None,
        "vac": str(evm_result.vac) if evm_result.vac is not None else None,
        "cpi_interpretation": evm_result.cpi_interpretation,
        "spi_interpretation": evm_result.spi_interpretation,
    }


def _serialize_evm_project(evm_result) -> dict:
    """Convierte un ProjectEVMResult en diccionario serializable."""
    return {
        "total_bac": str(evm_result.total_bac),
        "total_pv": str(evm_result.total_pv),
        "total_ev": str(evm_result.total_ev),
        "total_ac": str(evm_result.total_ac),
        "cv": str(evm_result.cv),
        "sv": str(evm_result.sv),
        "cpi": str(evm_result.cpi) if evm_result.cpi is not None else None,
        "spi": str(evm_result.spi) if evm_result.spi is not None else None,
        "eac": str(evm_result.eac) if evm_result.eac is not None else None,
        "vac": str(evm_result.vac) if evm_result.vac is not None else None,
        "cpi_interpretation": evm_result.cpi_interpretation,
        "spi_interpretation": evm_result.spi_interpretation,
    }


def _build_activity_dict(activity) -> dict:
    """Construye el diccionario completo de una actividad con su EVM."""
    evm = calculate_activity_evm(
        bac=Decimal(str(activity.bac)),
        planned_progress=Decimal(str(activity.planned_progress)),
        actual_progress=Decimal(str(activity.actual_progress)),
        actual_cost=Decimal(str(activity.actual_cost)),
    )
    return {
        "id": str(activity.id),
        "project_id": str(activity.project_id),
        "name": activity.name,
        "bac": str(activity.bac),
        "planned_progress": str(activity.planned_progress),
        "actual_progress": str(activity.actual_progress),
        "actual_cost": str(activity.actual_cost),
        "created_at": activity.created_at.isoformat() if activity.created_at else None,
        "updated_at": activity.updated_at.isoformat() if activity.updated_at else None,
        "evm": _serialize_evm_activity(evm),
    }


def _build_project_dict(project, include_activities: bool = True) -> dict:
    """Construye el diccionario completo de un proyecto con EVM consolidado."""
    activities = activity_repo.fetch_activities_by_project(project.id)
    project_evm = calculate_project_evm(activities)

    result = {
        "id": str(project.id),
        "name": project.name,
        "description": project.description,
        "created_at": project.created_at.isoformat() if project.created_at else None,
        "updated_at": project.updated_at.isoformat() if project.updated_at else None,
        "evm": _serialize_evm_project(project_evm),
    }

    if include_activities:
        result["activities"] = [_build_activity_dict(a) for a in activities]

    return result


# ─── Funciones públicas del service ───────────────────────────────────────────

def list_projects_service() -> list[dict]:
    projects = project_repo.fetch_all_projects()
    return [_build_project_dict(p, include_activities=False) for p in projects]


def create_project_service(name: str, description: str | None) -> dict:
    project = project_repo.save_project(name=name, description=description)
    return _build_project_dict(project)


def get_project_detail_service(project_id) -> dict | None:
    project = project_repo.fetch_project_by_id(project_id)
    if project is None:
        return None
    return _build_project_dict(project)


def update_project_service(project_id, fields: dict) -> dict | None:
    project = project_repo.fetch_project_by_id(project_id)
    if project is None:
        return None
    updated_project = project_repo.update_project_fields(project, fields)
    return _build_project_dict(updated_project)


def delete_project_service(project_id) -> bool:
    project = project_repo.fetch_project_by_id(project_id)
    if project is None:
        return False
    project_repo.remove_project(project)
    return True
```

### 4.2 Crear `app/services/activity_service.py`

```python
from app.repositories.project_repo import ProjectRepository
from app.repositories.activity_repo import ActivityRepository
from app.services.project_service import _build_activity_dict

project_repo = ProjectRepository()
activity_repo = ActivityRepository()


def list_activities_service(project_id) -> list[dict] | None:
    project = project_repo.fetch_project_by_id(project_id)
    if project is None:
        return None
    activities = activity_repo.fetch_activities_by_project(project_id)
    return [_build_activity_dict(a) for a in activities]


def create_activity_service(project_id, data: dict) -> dict | None:
    project = project_repo.fetch_project_by_id(project_id)
    if project is None:
        return None
    activity = activity_repo.save_activity(project_id=project_id, data=data)
    return _build_activity_dict(activity)


def update_activity_service(activity_id, fields: dict) -> dict | None:
    activity = activity_repo.fetch_activity_by_id(activity_id)
    if activity is None:
        return None
    updated = activity_repo.update_activity_fields(activity, fields)
    return _build_activity_dict(updated)


def delete_activity_service(activity_id) -> bool:
    activity = activity_repo.fetch_activity_by_id(activity_id)
    if activity is None:
        return False
    activity_repo.remove_activity(activity)
    return True
```

---

## Paso 5 — Manejo centralizado de errores

### ¿Por qué centralizar los errores?

Sin esto, un endpoint que no encuentra un recurso puede retornar HTML de error de Flask en lugar de JSON, lo que rompe el cliente. El manejo centralizado garantiza que todos los errores siguen el mismo formato JSON.

### 5.1 Crear `app/errors/__init__.py`

```python
# Vacío
```

### 5.2 Crear `app/errors/handlers.py`

```python
from flask import jsonify


def register_error_handlers(app):
    """Registra todos los manejadores de error en la aplicación Flask."""

    @app.errorhandler(404)
    def not_found(error):
        return jsonify({
            "error": "not_found",
            "message": str(error.description) if hasattr(error, 'description') else "Resource not found"
        }), 404

    @app.errorhandler(405)
    def method_not_allowed(error):
        return jsonify({
            "error": "method_not_allowed",
            "message": "HTTP method not allowed for this endpoint"
        }), 405

    @app.errorhandler(422)
    def unprocessable_entity(error):
        messages = error.data.get("messages", {}) if hasattr(error, 'data') else {}
        return jsonify({
            "error": "validation_error",
            "message": "Invalid input data",
            "details": messages
        }), 422

    @app.errorhandler(500)
    def internal_server_error(error):
        return jsonify({
            "error": "internal_server_error",
            "message": "An unexpected error occurred"
        }), 500
```

**¿Por qué el 422 incluye `details`?**  
Marshmallow retorna un diccionario de errores por campo cuando falla la validación. Al incluirlo en `details`, el frontend puede mostrar el error exactamente en el campo que falló, en lugar de un mensaje genérico.

Ejemplo de respuesta 422:
```json
{
  "error": "validation_error",
  "message": "Invalid input data",
  "details": {
    "json": {
      "planned_progress": ["Must be greater than or equal to 0 and less than or equal to 100."]
    }
  }
}
```

---

## Paso 6 — Blueprint de Proyectos

### ¿Qué es un Blueprint en Flask?

Un Blueprint agrupa rutas relacionadas. En lugar de tener todos los endpoints en un solo archivo, se dividen por recurso. El Blueprint de proyectos contiene las 5 rutas de proyectos; el de actividades, las 4 rutas de actividades.

### 6.1 Crear `app/controllers/__init__.py`

```python
# Vacío
```

### 6.2 Crear `app/controllers/project_blueprint.py`

```python
from flask import abort
from flask_smorest import Blueprint
from app.schemas.project_schema import ProjectCreateSchema, ProjectUpdateSchema
from app.services.project_service import (
    list_projects_service,
    create_project_service,
    get_project_detail_service,
    update_project_service,
    delete_project_service,
)

blp = Blueprint(
    "projects",
    __name__,
    url_prefix="/api/v1/projects",
    description="Gestión de proyectos y sus indicadores EVM consolidados"
)


@blp.route("/")
class ProjectList(blp.MethodView):

    def get(self):
        """
        Listar todos los proyectos con indicadores EVM consolidados.

        Retorna la lista completa de proyectos ordenados por fecha de creación
        descendente. Cada proyecto incluye sus indicadores EVM calculados a partir
        de las actividades registradas.
        """
        projects = list_projects_service()
        return projects, 200

    @blp.arguments(ProjectCreateSchema)
    def post(self, payload):
        """
        Crear un nuevo proyecto.

        Registra un proyecto con nombre y descripción opcional. Los indicadores EVM
        consolidados se retornan en cero porque el proyecto no tiene actividades aún.
        """
        project = create_project_service(
            name=payload["name"],
            description=payload.get("description"),
        )
        return project, 201


@blp.route("/<uuid:project_id>")
class ProjectDetail(blp.MethodView):

    def get(self, project_id):
        """
        Obtener el detalle completo de un proyecto.

        Incluye todas las actividades del proyecto con sus indicadores EVM individuales,
        y los indicadores EVM consolidados del proyecto completo.
        """
        project = get_project_detail_service(project_id)
        if project is None:
            abort(404, description="Project not found")
        return project, 200

    @blp.arguments(ProjectUpdateSchema)
    def put(self, payload, project_id):
        """
        Actualizar los campos de un proyecto.

        Solo los campos enviados en el body son actualizados. Los indicadores EVM
        no cambian porque dependen de las actividades, no de los campos del proyecto.
        """
        project = update_project_service(project_id, payload)
        if project is None:
            abort(404, description="Project not found")
        return project, 200

    def delete(self, project_id):
        """
        Eliminar un proyecto y todas sus actividades.

        Esta operación es irreversible. Al eliminar el proyecto, todas las actividades
        asociadas se eliminan automáticamente (CASCADE en base de datos).
        """
        deleted = delete_project_service(project_id)
        if not deleted:
            abort(404, description="Project not found")
        return "", 204
```
---

## Paso 7 — Blueprint de Actividades

### 7.1 Crear `app/controllers/activity_blueprint.py`

```python
from flask import abort
from flask_smorest import Blueprint
from app.schemas.activity_schema import ActivityCreateSchema, ActivityUpdateSchema
from app.services.activity_service import (
    list_activities_service,
    create_activity_service,
    update_activity_service,
    delete_activity_service,
)

blp = Blueprint(
    "activities",
    __name__,
    url_prefix="/api/v1",
    description="Gestión de actividades y sus indicadores EVM individuales"
)


@blp.route("/projects/<uuid:project_id>/activities")
class ActivityList(blp.MethodView):

    def get(self, project_id):
        """
        Listar todas las actividades de un proyecto.

        Cada actividad incluye sus 8 indicadores EVM calculados en tiempo real
        a partir de los datos registrados.
        """
        activities = list_activities_service(project_id)
        if activities is None:
            abort(404, description="Project not found")
        return activities, 200

    @blp.arguments(ActivityCreateSchema)
    def post(self, payload, project_id):
        """
        Crear una nueva actividad en un proyecto.

        Registra la actividad con sus 5 datos crudos y retorna inmediatamente
        los 8 indicadores EVM calculados. Si el proyecto no existe, retorna 403.
        Los valores de progreso deben estar entre 0 y 100.
        """
        activity = create_activity_service(project_id=project_id, data=payload)
        if activity is None:
            abort(404, description="Project not found")
        return activity, 201


@blp.route("/activities/<uuid:activity_id>")
class ActivityDetail(blp.MethodView):

    @blp.arguments(ActivityUpdateSchema)
    def put(self, payload, activity_id):
        """
        Actualizar una actividad existente.

        Solo los campos enviados son actualizados. Los indicadores EVM se
        recalculan automáticamente con los nuevos valores.
        """
        activity = update_activity_service(activity_id=activity_id, fields=payload)
        if activity is None:
            abort(404, description="Activity not found")
        return activity, 200

    def delete(self, activity_id):
        """
        Eliminar una actividad.

        Los indicadores EVM consolidados del proyecto se recalcularán en la
        próxima consulta, excluyendo esta actividad.
        """
        deleted = delete_activity_service(activity_id)
        if not deleted:
            abort(404, description="Activity not found")
        return "", 204
```

---

## Paso 8 — Swagger UI con flask-smorest

### ¿Qué es flask-smorest?

Es una extensión de Flask que genera automáticamente la especificación OpenAPI 3.0 a partir de los blueprints, schemas y docstrings. La especificación se sirve en `/api-docs` como Swagger UI interactivo.

### 8.1 Verificar configuración en `app/config.py`

Confirma que existen estas claves (ya deberían estar de fases anteriores):

```python
API_TITLE = "EVM Project Tracker API"
API_VERSION = "v1"
OPENAPI_VERSION = "3.0.3"
OPENAPI_URL_PREFIX = "/"
OPENAPI_SWAGGER_UI_PATH = "/api-docs"
OPENAPI_SWAGGER_UI_URL = "https://cdn.jsdelivr.net/npm/swagger-ui-dist/"
```

### 8.2 Verificar `app/extensions.py`

```python
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_smorest import Api

db = SQLAlchemy()
migrate = Migrate()
api = Api()
```

### 8.3 Verificar que Swagger funciona

Con Docker corriendo:

```bash
# El contenedor backend debe estar levantado
docker compose up -d

# Abrir en el navegador
http://localhost:5000/api-docs
```

Debes ver la interfaz Swagger con todos los endpoints listados. Si la página no carga:

```bash
# Revisar logs del backend
docker logs evm_backend --tail 50

# Verificar que Flask está corriendo en el puerto correcto
docker exec -it evm_backend flask routes
```

### 8.4 Criterios de calidad del Swagger

Cada endpoint debe tener en Swagger:

| Elemento | Origen | ¿Dónde configurarlo? |
|---|---|---|
| Descripción del endpoint | Docstring del método | En el MethodView |
| Schema del request body | `@blp.arguments(Schema)` | Decorador |
| Códigos de respuesta | flask-smorest los infiere | Automático |
| Descripción del tag | `description=` del Blueprint | Constructor del Blueprint |

---

## Paso 9 — Tests de integración

### ¿Qué prueban los tests de integración?

A diferencia de los tests unitarios (que prueban funciones aisladas), los tests de integración prueban el endpoint completo: desde el request HTTP hasta la respuesta JSON. Verifican que el contrato del API es correcto: código HTTP, estructura del body, campos presentes, tipos de datos.

### 9.1 Verificar `tests/conftest.py`

Este archivo debe estar creado desde fases anteriores. Verificar que tiene esta estructura:

```python
import pytest
from app import create_app
from app.extensions import db as _db
from app.config import TestingConfig


@pytest.fixture(scope="session")
def app():
    application = create_app(TestingConfig)
    with application.app_context():
        _db.create_all()
        yield application
        _db.drop_all()


@pytest.fixture(scope="function")
def client(app):
    return app.test_client()


@pytest.fixture(scope="function", autouse=True)
def clean_db(app):
    """Limpia todas las tablas entre tests para garantizar aislamiento."""
    yield
    with app.app_context():
        for table in reversed(_db.metadata.sorted_tables):
            _db.session.execute(table.delete())
        _db.session.commit()
```

**Puntos críticos:**
- `scope="session"` en `app`: la app se crea una sola vez por sesión de tests.
- `scope="function"` en `client` y `clean_db`: cada test recibe un cliente limpio.
- `autouse=True` en `clean_db`: se ejecuta automáticamente sin necesidad de incluirlo en cada test.
- `TestingConfig` usa SQLite en memoria: no necesita PostgreSQL para correr los tests.

### 9.2 Crear `tests/integration/__init__.py`

```python
# Vacío
```

### 9.3 Crear `tests/integration/test_projects_endpoint.py`

```python
import json


# ─── Helpers ──────────────────────────────────────────────────────────────────

def create_project(client, name="Test Project", description=None):
    """Helper para crear un proyecto en tests."""
    payload = {"name": name}
    if description:
        payload["description"] = description
    return client.post(
        "/api/v1/projects/",
        data=json.dumps(payload),
        content_type="application/json",
    )


# ─── POST /api/v1/projects/ ───────────────────────────────────────────────────

class TestCreateProject:

    def test_returns_201_with_valid_payload(self, client):
        response = create_project(client, name="Bridge Construction")
        assert response.status_code == 201

    def test_response_contains_required_fields(self, client):
        response = create_project(client, name="Bridge Construction")
        data = response.get_json()
        assert "id" in data
        assert "name" in data
        assert "evm" in data
        assert data["name"] == "Bridge Construction"

    def test_evm_fields_are_zero_for_new_project(self, client):
        response = create_project(client, name="Empty Project")
        evm = response.get_json()["evm"]
        assert evm["total_bac"] == "0"
        assert evm["cpi"] is None
        assert evm["cpi_interpretation"] == "insufficient_data"

    def test_returns_422_when_name_is_missing(self, client):
        response = client.post(
            "/api/v1/projects/",
            data=json.dumps({"description": "No name"}),
            content_type="application/json",
        )
        assert response.status_code == 422

    def test_returns_422_when_name_is_empty_string(self, client):
        response = client.post(
            "/api/v1/projects/",
            data=json.dumps({"name": ""}),
            content_type="application/json",
        )
        assert response.status_code == 422


# ─── GET /api/v1/projects/ ────────────────────────────────────────────────────

class TestListProjects:

    def test_returns_200_with_empty_list(self, client):
        response = client.get("/api/v1/projects/")
        assert response.status_code == 200
        assert response.get_json() == []

    def test_returns_created_projects(self, client):
        create_project(client, name="Project Alpha")
        create_project(client, name="Project Beta")
        response = client.get("/api/v1/projects/")
        data = response.get_json()
        assert len(data) == 2

    def test_each_project_has_evm_field(self, client):
        create_project(client, name="Project Alpha")
        projects = client.get("/api/v1/projects/").get_json()
        assert "evm" in projects[0]


# ─── GET /api/v1/projects/{id} ────────────────────────────────────────────────

class TestGetProjectDetail:

    def test_returns_200_for_existing_project(self, client):
        project_id = create_project(client).get_json()["id"]
        response = client.get(f"/api/v1/projects/{project_id}")
        assert response.status_code == 200

    def test_response_includes_activities_list(self, client):
        project_id = create_project(client).get_json()["id"]
        data = client.get(f"/api/v1/projects/{project_id}").get_json()
        assert "activities" in data
        assert isinstance(data["activities"], list)

    def test_returns_404_for_nonexistent_project(self, client):
        response = client.get("/api/v1/projects/00000000-0000-0000-0000-000000000000")
        assert response.status_code == 404

    def test_404_response_is_json(self, client):
        response = client.get("/api/v1/projects/00000000-0000-0000-0000-000000000000")
        data = response.get_json()
        assert "error" in data
        assert "message" in data


# ─── PUT /api/v1/projects/{id} ────────────────────────────────────────────────

class TestUpdateProject:

    def test_returns_200_with_updated_name(self, client):
        project_id = create_project(client, name="Original").get_json()["id"]
        response = client.put(
            f"/api/v1/projects/{project_id}",
            data=json.dumps({"name": "Updated Name"}),
            content_type="application/json",
        )
        assert response.status_code == 200
        assert response.get_json()["name"] == "Updated Name"

    def test_returns_404_for_nonexistent_project(self, client):
        response = client.put(
            "/api/v1/projects/00000000-0000-0000-0000-000000000000",
            data=json.dumps({"name": "Updated"}),
            content_type="application/json",
        )
        assert response.status_code == 404


# ─── DELETE /api/v1/projects/{id} ─────────────────────────────────────────────

class TestDeleteProject:

    def test_returns_204_for_existing_project(self, client):
        project_id = create_project(client).get_json()["id"]
        response = client.delete(f"/api/v1/projects/{project_id}")
        assert response.status_code == 204

    def test_project_is_gone_after_delete(self, client):
        project_id = create_project(client).get_json()["id"]
        client.delete(f"/api/v1/projects/{project_id}")
        get_response = client.get(f"/api/v1/projects/{project_id}")
        assert get_response.status_code == 404

    def test_returns_404_for_nonexistent_project(self, client):
        response = client.delete("/api/v1/projects/00000000-0000-0000-0000-000000000000")
        assert response.status_code == 404
```

### 9.4 Crear `tests/integration/test_activities_endpoint.py`

```python
import json


# ─── Helpers ──────────────────────────────────────────────────────────────────

def create_project(client, name="Test Project"):
    return client.post(
        "/api/v1/projects/",
        data=json.dumps({"name": name}),
        content_type="application/json",
    ).get_json()


def create_activity(client, project_id, overrides=None):
    payload = {
        "name": "Foundation Work",
        "bac": "10000",
        "planned_progress": "50",
        "actual_progress": "40",
        "actual_cost": "4500",
    }
    if overrides:
        payload.update(overrides)
    return client.post(
        f"/api/v1/projects/{project_id}/activities",
        data=json.dumps(payload),
        content_type="application/json",
    )


# ─── POST /api/v1/projects/{id}/activities ────────────────────────────────────

class TestCreateActivity:

    def test_returns_201_with_valid_payload(self, client):
        project_id = create_project(client)["id"]
        response = create_activity(client, project_id)
        assert response.status_code == 201

    def test_response_contains_evm_indicators(self, client):
        project_id = create_project(client)["id"]
        data = create_activity(client, project_id).get_json()
        assert "evm" in data
        evm = data["evm"]
        assert evm["pv"] == "5000.00"
        assert evm["ev"] == "4000.00"
        assert "cpi" in evm
        assert "cpi_interpretation" in evm

    def test_returns_404_when_project_does_not_exist(self, client):
        response = create_activity(client, "00000000-0000-0000-0000-000000000000")
        assert response.status_code == 404

    def test_returns_422_when_progress_exceeds_100(self, client):
        project_id = create_project(client)["id"]
        response = create_activity(client, project_id, overrides={"planned_progress": "150"})
        assert response.status_code == 422

    def test_returns_422_when_bac_is_negative(self, client):
        project_id = create_project(client)["id"]
        response = create_activity(client, project_id, overrides={"bac": "-500"})
        assert response.status_code == 422

    def test_cpi_is_null_when_actual_cost_is_zero(self, client):
        project_id = create_project(client)["id"]
        data = create_activity(client, project_id, overrides={"actual_cost": "0"}).get_json()
        assert data["evm"]["cpi"] is None
        assert data["evm"]["cpi_interpretation"] == "insufficient_data"


# ─── GET /api/v1/projects/{id}/activities ─────────────────────────────────────

class TestListActivities:

    def test_returns_200_with_empty_list(self, client):
        project_id = create_project(client)["id"]
        response = client.get(f"/api/v1/projects/{project_id}/activities")
        assert response.status_code == 200
        assert response.get_json() == []

    def test_returns_created_activities(self, client):
        project_id = create_project(client)["id"]
        create_activity(client, project_id)
        create_activity(client, project_id, overrides={"name": "Second Activity"})
        activities = client.get(f"/api/v1/projects/{project_id}/activities").get_json()
        assert len(activities) == 2

    def test_returns_404_when_project_does_not_exist(self, client):
        response = client.get("/api/v1/projects/00000000-0000-0000-0000-000000000000/activities")
        assert response.status_code == 404


# ─── PUT /api/v1/activities/{id} ──────────────────────────────────────────────

class TestUpdateActivity:

    def test_returns_200_with_recalculated_evm(self, client):
        project_id = create_project(client)["id"]
        activity_id = create_activity(client, project_id).get_json()["id"]

        response = client.put(
            f"/api/v1/activities/{activity_id}",
            data=json.dumps({"actual_progress": "80", "actual_cost": "7000"}),
            content_type="application/json",
        )
        assert response.status_code == 200
        evm = response.get_json()["evm"]
        assert evm["ev"] == "8000.00"

    def test_returns_404_for_nonexistent_activity(self, client):
        response = client.put(
            "/api/v1/activities/00000000-0000-0000-0000-000000000000",
            data=json.dumps({"actual_progress": "50"}),
            content_type="application/json",
        )
        assert response.status_code == 404

    def test_returns_422_when_progress_is_invalid(self, client):
        project_id = create_project(client)["id"]
        activity_id = create_activity(client, project_id).get_json()["id"]
        response = client.put(
            f"/api/v1/activities/{activity_id}",
            data=json.dumps({"actual_progress": "200"}),
            content_type="application/json",
        )
        assert response.status_code == 422


# ─── DELETE /api/v1/activities/{id} ───────────────────────────────────────────

class TestDeleteActivity:

    def test_returns_204_for_existing_activity(self, client):
        project_id = create_project(client)["id"]
        activity_id = create_activity(client, project_id).get_json()["id"]
        response = client.delete(f"/api/v1/activities/{activity_id}")
        assert response.status_code == 204

    def test_activity_is_gone_after_delete(self, client):
        project_id = create_project(client)["id"]
        activity_id = create_activity(client, project_id).get_json()["id"]
        client.delete(f"/api/v1/activities/{activity_id}")
        activities = client.get(f"/api/v1/projects/{project_id}/activities").get_json()
        assert len(activities) == 0

    def test_returns_404_for_nonexistent_activity(self, client):
        response = client.delete("/api/v1/activities/00000000-0000-0000-0000-000000000000")
        assert response.status_code == 404
```

---

------


---

## 1. Antes de empezar

### ¿Qué se construye en esta fase?

Un dashboard web donde el líder de proyecto puede:

- Ver la lista de todos sus proyectos con su estado EVM consolidado
- Crear nuevos proyectos
- Ver el detalle de un proyecto: tabla de actividades con indicadores EVM, KPIs consolidados y gráfica comparativa
- Agregar, editar y eliminar actividades desde la misma pantalla

### ¿Qué ya existe?

El backend expone una API REST completamente funcional. El frontend que se construye aquí la consume. No debes tocar ningún archivo fuera de la carpeta `frontend/`.

### URL base del backend

El backend corre en `http://localhost:5000`. Todos los endpoints del API empiezan con `/api/v1/`.

La variable de entorno `VITE_API_URL` en el archivo `.env` de la raíz del proyecto ya tiene este valor configurado:

```
VITE_API_URL=http://localhost:5000/api/v1
```

Confirma que el archivo `.env` existe en la raíz del proyecto antes de continuar.

---

## 2. Orden de implementación

```

→ Definir estructura de carpetas
→ evmApi.js — capa de comunicación con el backend
→ Hooks: useProjects y useProject
→ StatusBadge — componente base de indicadores visuales
→ ActivityForm — formulario con validaciones
→ ActivityTable — tabla con colores por CPI/SPI
→ ConsolidatedKPIs — KPIs globales del proyecto
→ EVMChart — gráfica de barras PV vs EV vs AC
→ ProjectDetailPage — página de detalle
→ ProjectsPage — página de lista
→ Ensamblaje, routing y pruebas
```

**¿Por qué este orden?**

Los componentes `StatusBadge` y `ActivityForm` no dependen de nada del proyecto: se pueden construir y probar en aislamiento. `ActivityTable` y `ConsolidatedKPIs` los usan. Las páginas ensamblan los componentes y usan los hooks. Los hooks dependen de `evmApi.js`. Construir en este orden garantiza que cada pieza está lista cuando la siguiente la necesita.

---

## Paso 1 — scaffolding


```

### 1.2 Verificar si el scaffolding ya existe

La carpeta `frontend/` puede tener una estructura básica de fases anteriores. Revisa su contenido:

```bash
ls frontend/
```

**Si la carpeta está vacía o solo tiene un Dockerfile**, procede a crear el proyecto con Vite:

```bash
cd frontend

# Elimina el contenido si hay archivos de placeholder
# Crea el proyecto Vite con React
npm create vite@latest . -- --template react

# Cuando pregunte si sobreescribir: confirmar con Y
```

**Si ya tiene estructura de Vite** (tiene `vite.config.js`, `src/`, `package.json`), salta al Paso 2.

### 1.3 Verificar la estructura generada por Vite

Después de ejecutar el scaffolding, la estructura debe ser:

```
frontend/
├── public/
│   └── vite.svg
├── src/
│   ├── assets/
│   ├── App.css
│   ├── App.jsx
│   ├── index.css
│   └── main.jsx
├── .gitignore
├── index.html
├── package.json
└── vite.config.js
```

**Elimina los archivos de ejemplo que no se usarán:**

- `src/App.css` → eliminar
- `src/assets/react.svg` → eliminar
- `src/App.jsx` → vaciar y reescribir (no eliminar, lo usarás para el Router)
- `public/vite.svg` → eliminar

### 1.4 Instalar las dependencias base de Vite

```bash
# Desde la carpeta frontend/
npm install
```

### 1.5 Verificar que Vite levanta

```bash
npm run dev
# Debe mostrar: Local: http://localhost:5173/
```

Abre el navegador en `http://localhost:5173`. Debe aparecer la página de bienvenida de Vite. Esto confirma que el scaffolding funciona.

### Checklist Paso 1


- [ ] `npm create vite@latest` ejecutado con template `react`
- [ ] `npm install` ejecutado sin errores
- [ ] `npm run dev` levanta en `http://localhost:5173`
- [ ] Archivos de ejemplo eliminados (`App.css`, `react.svg`, `vite.svg`)

---

## Paso 2 — Configurar ESLint

El requerimiento del proyecto exige que la configuración de ESLint esté incluida en el repositorio. Vite ya genera una configuración básica; aquí se ajusta para el proyecto.

### 2.1 Verificar el archivo generado

Vite genera `eslint.config.js` (versión nueva de flat config). Verifica que existe:

### 2.2 Ajustar la configuración

Abre `eslint.config.js` y confirma que incluye estas reglas mínimas. Si el archivo no las tiene, agrégalas:

```
Reglas que deben estar activas:
- no-unused-vars: error         → detecta variables declaradas y no usadas
- no-console: warn              → advierte sobre console.log olvidados
- react/prop-types: off         → desactivar (el proyecto no usa TypeScript ni PropTypes)
- react-hooks/rules-of-hooks    → asegura que los hooks se usan correctamente
- react-hooks/exhaustive-deps   → advierte si faltan dependencias en useEffect
```

### 2.3 Agregar script de linting al package.json

Verifica que `package.json` tiene este script. Si no está, agrégalo:

```
"lint": "eslint src/"
"lint:fix": "eslint src/ --fix"
```

### 2.4 Ejecutar ESLint para verificar

```bash
# No debe haber errores en este punto (src/ está casi vacío)
```

### Checklist Paso 2

- [ ] `eslint.config.js` existe y tiene las reglas mínimas
- [ ] `npm run lint` ejecuta sin errores
- [ ] Script `lint` y `lint:fix` están en `package.json`

---

## Paso 3 — Instalar dependencias

### 3.1 Dependencias de producción

```bash
cd frontend

# Router para navegación entre páginas
npm install react-router-dom

# Cliente HTTP para llamadas al backend
npm install axios

# Gráficas para el EVMChart
npm install recharts
```

### 3.2 Verificar el package.json

Después de instalar, verifica que `package.json` tiene en `dependencies`:

```
react-router-dom    → navegación (ProjectsPage ↔ ProjectDetailPage)
axios               → llamadas HTTP al backend Flask
recharts            → BarChart para comparar PV, EV y AC
```

### 3.3 Verificar que no hay conflictos

```bash
npm run dev
# Debe seguir funcionando sin errores de módulo
```

### Checklist Paso 3

- [ ] `react-router-dom` instalado
- [ ] `axios` instalado
- [ ] `recharts` instalado
- [ ] `npm run dev` funciona después de instalar

---

## Paso 4 — Estructura de carpetas

Antes de escribir código, crea toda la estructura de carpetas. Esto evita confusión sobre dónde va cada archivo.

### 4.1 Estructura final objetivo

```
frontend/src/
├── api/
│   └── evmApi.js               ← Todas las llamadas HTTP al backend
│
├── hooks/
│   ├── useProjects.js          ← Lista de proyectos + crear proyecto
│   └── useProject.js           ← Detalle de proyecto + CRUD actividades
│
├── components/
│   ├── ui/
│   │   ├── StatusBadge.jsx     ← Indicador visual verde/amarillo/rojo
│   │   └── LoadingSpinner.jsx  ← Estado de carga
│   │
│   └── evm/
│       ├── ActivityForm.jsx    ← Formulario crear/editar actividad
│       ├── ActivityTable.jsx   ← Tabla de actividades con indicadores EVM
│       ├── ConsolidatedKPIs.jsx← KPIs globales del proyecto
│       └── EVMChart.jsx        ← Gráfica de barras PV vs EV vs AC
│
├── pages/
│   ├── ProjectsPage.jsx        ← Lista de proyectos + crear proyecto
│   └── ProjectDetailPage.jsx  ← Dashboard completo de un proyecto
│
├── constants/
│   └── evm.js                  ← Colores, textos de interpretación, umbrales
│
├── App.jsx                     ← Router raíz
├── main.jsx                    ← Punto de entrada Vite
└── index.css                   ← Estilos globales mínimos
```

### 4.2 Crear las carpetas

```bash
cd frontend/src
mkdir -p api hooks components/ui components/evm pages constants
```

### 4.3 Regla de arquitectura que debes seguir

**Un hook nunca retorna JSX. Un componente nunca hace fetch directo.**

```
Página
  └── usa hooks   → lógica + estado + llamadas API
  └── usa componentes → solo presentación

Hook
  └── llama evmApi.js  → HTTP
  └── retorna { data, isLoading, error, mutate }
  └── NUNCA retorna JSX

Componente
  └── recibe props → renderiza
  └── NUNCA llama a axios directamente
```

Si te encuentras escribiendo `axios.get(...)` dentro de un componente JSX, estás en el lugar equivocado.

### Checklist Paso 4

- [ ] Todas las carpetas creadas: `api/`, `hooks/`, `components/ui/`, `components/evm/`, `pages/`, `constants/`
- [ ] La estructura está clara antes de empezar a codificar

---

## Paso 5 — Capa de API (evmApi.js)

### ¿Qué es este archivo?

`evmApi.js` es el único punto de comunicación entre el frontend y el backend. Contiene:

1. Una instancia de Axios configurada con la URL base
2. Funciones organizadas por recurso (proyectos y actividades)

Ningún otro archivo del proyecto hace llamadas HTTP directas. Si mañana el backend cambia de puerto o agrega autenticación, solo se modifica este archivo.

### 5.1 Crear `src/api/evmApi.js`

El archivo debe contener:

**Sección 1 — Instancia de Axios:**

Crea una instancia con `axios.create()`. La `baseURL` debe leer la variable de entorno `VITE_API_URL`. En Vite, las variables de entorno se acceden con `import.meta.env.VITE_NOMBRE_VARIABLE`.

Configura también:
- `timeout: 10000` — abortar si el backend no responde en 10 segundos
- `headers: { 'Content-Type': 'application/json' }` — todas las requests son JSON

**Sección 2 — Funciones de proyectos:**

| Nombre de función | Método HTTP | Endpoint | Parámetros |
|---|---|---|---|
| `getAllProjects` | GET | `/projects/` | ninguno |
| `getProjectById` | GET | `/projects/{id}` | `projectId` |
| `createProject` | POST | `/projects/` | `{ name, description }` |
| `updateProject` | PUT | `/projects/{id}` | `projectId`, `{ name?, description? }` |
| `deleteProject` | DELETE | `/projects/{id}` | `projectId` |

**Sección 3 — Funciones de actividades:**

| Nombre de función | Método HTTP | Endpoint | Parámetros |
|---|---|---|---|
| `getActivitiesByProject` | GET | `/projects/{id}/activities` | `projectId` |
| `createActivity` | POST | `/projects/{id}/activities` | `projectId`, `{ name, bac, planned_progress, actual_progress, actual_cost }` |
| `updateActivity` | PUT | `/activities/{id}` | `activityId`, campos parciales |
| `deleteActivity` | DELETE | `/activities/{id}` | `activityId` |

**Estructura de exports:**

Exporta todas las funciones individualmente (named exports), no como objeto default. Esto permite hacer imports específicos y facilita el tree-shaking.

```
// Correcto
export const getAllProjects = () => axiosInstance.get('/projects/');

// Evitar
export default { getAllProjects, createProject, ... }
```

### 5.2 Qué retornan las funciones del backend

Las funciones deben retornar directamente `response.data` para que los hooks trabajen con el dato limpio, no con el objeto de respuesta de Axios.

**Estructura de respuesta de un proyecto:**

```json
{
  "id": "uuid-string",
  "name": "Nombre del proyecto",
  "description": "Descripción opcional",
  "created_at": "2024-01-15T10:30:00",
  "updated_at": "2024-01-15T10:30:00",
  "activities": [...],
  "evm": {
    "total_bac": "50000.00",
    "total_pv": "25000.00",
    "total_ev": "20000.00",
    "total_ac": "22000.00",
    "cv": "-2000.00",
    "sv": "-5000.00",
    "cpi": "0.909090",
    "spi": "0.800000",
    "eac": "55000.00",
    "vac": "-5000.00",
    "cpi_interpretation": "inefficient",
    "spi_interpretation": "inefficient"
  }
}
```

**Estructura de respuesta de una actividad:**

```json
{
  "id": "uuid-string",
  "project_id": "uuid-string",
  "name": "Excavación de cimientos",
  "bac": "10000.00",
  "planned_progress": "50.00",
  "actual_progress": "40.00",
  "actual_cost": "4500.00",
  "created_at": "2024-01-15T10:30:00",
  "updated_at": "2024-01-15T10:30:00",
  "evm": {
    "pv": "5000.00",
    "ev": "4000.00",
    "cv": "-500.00",
    "sv": "-1000.00",
    "cpi": "0.888888",
    "spi": "0.800000",
    "eac": "11250.00",
    "vac": "-1250.00",
    "cpi_interpretation": "inefficient",
    "spi_interpretation": "inefficient"
  }
}
```

**Nota importante:** Todos los valores numéricos llegan como **strings**, no como números. Esto es intencional para preservar precisión decimal. Si necesitas hacer comparaciones numéricas en el frontend (para colores, por ejemplo), conviértelos con `parseFloat(value)`.

### 5.3 Cómo probar evmApi.js

Agrega temporalmente una llamada en `App.jsx` para verificar que la conexión funciona:

```
Importa getAllProjects desde evmApi.js
Llámala dentro de un useEffect al montar el componente
Muestra el resultado en console.log
Abre el navegador, revisa la consola de DevTools
Debe aparecer el array de proyectos (vacío si no hay datos aún)
```

Después de verificar, **elimina el código de prueba** de `App.jsx`.

### Checklist Paso 5

- [ ] Instancia de Axios creada con `baseURL` desde `import.meta.env.VITE_API_URL`
- [ ] 5 funciones de proyectos implementadas
- [ ] 4 funciones de actividades implementadas
- [ ] Todas las funciones retornan `response.data`, no el objeto response completo
- [ ] Named exports (no default export)
- [ ] Conexión verificada con prueba en consola

---

## Paso 6 — Custom Hooks: useProjects y useProject

### ¿Qué son y para qué sirven?

Los custom hooks encapsulan la lógica de estado y las llamadas a la API. Las páginas los usan para obtener datos y ejecutar acciones sin conocer los detalles de cómo se hace el fetch.

**Regla de oro:** Un hook retorna datos y funciones, nunca JSX.

### 6.1 Crear `src/hooks/useProjects.js`

Este hook maneja la lista de proyectos y la creación de nuevos proyectos. Lo usa `ProjectsPage`.

**Estado interno que debe manejar:**

| Variable | Tipo | Descripción |
|---|---|---|
| `projects` | `array` | Lista de proyectos. Inicial: `[]` |
| `isLoading` | `boolean` | True mientras hay una petición en curso |
| `error` | `string \| null` | Mensaje de error si algo falla |

**Lógica interna:**

- Al montarse el componente que usa el hook, llama a `getAllProjects()` y carga los proyectos
- Mientras carga, `isLoading` es `true`
- Si la llamada falla, guarda el mensaje de error en `error`
- Usa `useEffect` con array de dependencias vacío `[]` para cargar una sola vez

**Funciones que expone el hook:**

| Función | Qué hace |
|---|---|
| `fetchProjects()` | Recarga la lista de proyectos desde el backend |
| `createProject(name, description)` | Crea un proyecto y recarga la lista |

**Qué retorna el hook:**

```javascript
return {
  projects,       // array de proyectos
  isLoading,      // boolean
  error,          // string | null
  fetchProjects,  // función para recargar
  createProject,  // función para crear
}
```

### 6.2 Crear `src/hooks/useProject.js`

Este hook maneja el detalle de un proyecto específico: sus datos, sus actividades y todas las operaciones CRUD sobre actividades. Lo usa `ProjectDetailPage`.

**Parámetro de entrada:** `projectId` — el ID del proyecto a cargar.

**Estado interno que debe manejar:**

| Variable | Tipo | Descripción |
|---|---|---|
| `project` | `object \| null` | Datos del proyecto con su EVM consolidado |
| `isLoading` | `boolean` | Estado de carga inicial |
| `error` | `string \| null` | Error si la carga falla |
| `isMutating` | `boolean` | True durante creación/edición/eliminación de actividades |

**Lógica de carga:**

- Al montarse, llama a `getProjectById(projectId)`
- Si el proyecto no existe (404), guarda un mensaje de error
- El `projectId` va en el array de dependencias del `useEffect`

**Funciones que expone el hook:**

| Función | Parámetros | Qué hace |
|---|---|---|
| `refetch()` | ninguno | Recarga el proyecto completo |
| `addActivity(activityData)` | objeto con los 5 campos | Crea actividad y recarga el proyecto |
| `editActivity(activityId, fields)` | id + campos a actualizar | Actualiza actividad y recarga |
| `removeActivity(activityId)` | id | Elimina actividad y recarga |

**Patrón de mutación:** Después de cada operación de escritura (create, update, delete), llama a `refetch()` para recargar el proyecto completo. Esto garantiza que los indicadores EVM consolidados siempre estén actualizados sin necesidad de calcularlos en el frontend.

**Qué retorna el hook:**

```javascript
return {
  project,       // objeto del proyecto con activities[] y evm
  isLoading,     // boolean — carga inicial
  error,         // string | null
  isMutating,    // boolean — operaciones de escritura
  refetch,       // función
  addActivity,   // función
  editActivity,  // función
  removeActivity // función
}
```

### 6.3 Manejo de errores en los hooks

Para el manejo de errores de Axios, detecta el código HTTP de la respuesta:

```
Si el error tiene error.response:
  → Es un error HTTP del servidor (404, 422, 500)
  → Usa error.response.data.message para el mensaje

Si el error NO tiene error.response:
  → Es un error de red (backend no disponible)
  → Usa el mensaje genérico: "No se puede conectar con el servidor"
```

### Checklist Paso 6

- [ ] `useProjects` maneja `projects`, `isLoading`, `error`
- [ ] `useProjects` expone `fetchProjects` y `createProject`
- [ ] `useProject` recibe `projectId` como parámetro
- [ ] `useProject` maneja `project`, `isLoading`, `error`, `isMutating`
- [ ] `useProject` expone `refetch`, `addActivity`, `editActivity`, `removeActivity`
- [ ] Después de cada mutación se llama `refetch()`
- [ ] Los errores de red y HTTP se manejan por separado

---

## Paso 7 — Componente StatusBadge

### ¿Qué hace?

Es el componente visual más simple pero más importante del sistema. Muestra un badge de color según el valor de CPI o SPI. El usuario ve de un vistazo si un proyecto o actividad va bien o mal.

### 7.1 Lógica de colores

Antes de crear el componente, crea primero `src/constants/evm.js` con los colores y textos centralizados:

| Valor de interpretación | Color del badge | Texto a mostrar | Significado |
|---|---|---|---|
| `"efficient"` | Verde | "Eficiente" | CPI/SPI > 1 |
| `"on_track"` | Amarillo | "En línea" | CPI/SPI = 1 |
| `"inefficient"` | Rojo | "Ineficiente" | CPI/SPI < 1 |
| `"insufficient_data"` | Gris | "Sin datos" | CPI/SPI es null |

Centraliza esta lógica en `evm.js` como un objeto o función, no como lógica dispersa dentro del componente.

### 7.2 Crear `src/components/ui/StatusBadge.jsx`

**Props que recibe:**

| Prop | Tipo | Descripción |
|---|---|---|
| `interpretation` | `string` | Uno de los 4 valores: `"efficient"`, `"on_track"`, `"inefficient"`, `"insufficient_data"` |
| `label` | `string` | Texto adicional opcional, ej: "CPI" o "SPI" |
| `value` | `string` | El valor numérico a mostrar, ej: `"0.89"` |

**Comportamiento:**

- Si recibe `label` y `value`, muestra: `"CPI: 0.89"` con el color correspondiente
- Si solo recibe `interpretation`, muestra el texto del estado (ej: "Eficiente")
- El color de fondo y texto se determina únicamente por `interpretation`

### 7.3 Crear `src/components/ui/LoadingSpinner.jsx`

Un componente simple que muestra un indicador de carga. No recibe props. Solo muestra texto o un spinner CSS mientras el hook tiene `isLoading: true`.

### 7.4 Cómo probar StatusBadge

Agrega temporalmente en `App.jsx`:

```
Renderiza 4 instancias de StatusBadge con cada valor de interpretation
Verifica que los colores son correctos en el navegador
Elimina el código de prueba después
```

### Checklist Paso 7

- [ ] `evm.js` tiene los 4 estados con color y texto
- [ ] `StatusBadge` recibe `interpretation`, `label`, `value`
- [ ] Los colores se obtienen de `evm.js`, no hardcodeados en el componente
- [ ] `LoadingSpinner` existe y es reutilizable
- [ ] Verificado visualmente en el navegador con los 4 estados

---

## Paso 8 — Componente ActivityForm

### ¿Qué hace?

Es el formulario para crear y editar actividades. Tiene 5 campos con validaciones específicas. Es el componente con más lógica de validación del frontend.

### 8.1 Crear `src/components/evm/ActivityForm.jsx`

**Props que recibe:**

| Prop | Tipo | Descripción |
|---|---|---|
| `onSubmit` | `function` | Función que recibe los datos del formulario al confirmar |
| `onCancel` | `function` | Función que se llama al cancelar |
| `initialValues` | `object \| null` | Si viene con valores, el form es de "editar". Si es `null`, es de "crear" |
| `isLoading` | `boolean` | Deshabilita el botón mientras se procesa |

**Campos del formulario:**

| Campo | Label en UI | Tipo HTML | Validaciones |
|---|---|---|---|
| `name` | Nombre de la actividad | `text` | Requerido, mínimo 1 carácter, máximo 255 |
| `bac` | Presupuesto total (BAC) | `number` | Requerido, mayor o igual a 0 |
| `planned_progress` | Avance planificado (%) | `number` | Requerido, entre 0 y 100 |
| `actual_progress` | Avance real (%) | `number` | Requerido, entre 0 y 100 |
| `actual_cost` | Costo real (AC) | `number` | Requerido, mayor o igual a 0 |

**Lógica de estado interno del formulario:**

- Cada campo tiene su propio estado de error
- La validación ocurre al intentar hacer submit (no en tiempo real mientras escribe)
- Si `initialValues` viene con datos, los campos se precargan con esos valores
- Al hacer submit exitoso, el formulario debe resetearse si es de "crear"

**Mensajes de error por campo:**

| Campo | Mensaje cuando falla |
|---|---|
| `name` vacío | "El nombre es requerido" |
| `bac` negativo | "El presupuesto debe ser mayor o igual a 0" |
| `planned_progress` fuera de rango | "El avance planificado debe estar entre 0 y 100" |
| `actual_progress` fuera de rango | "El avance real debe estar entre 0 y 100" |
| `actual_cost` negativo | "El costo real debe ser mayor o igual a 0" |

**Comportamiento de submit:**

1. Valida todos los campos
2. Si hay errores, los muestra y NO llama a `onSubmit`
3. Si no hay errores, llama a `onSubmit` con un objeto con los 5 campos como strings o números según lo que espera el backend
4. El backend espera los valores como strings numéricos (ej: `"10000"`, `"50"`)

**Distinción crear vs editar:**

- Si `initialValues` es `null` → título: "Agregar actividad", botón: "Agregar"
- Si `initialValues` tiene datos → título: "Editar actividad", botón: "Guardar cambios"

### 8.2 Cómo probar ActivityForm

Agrega temporalmente en `App.jsx`:

```
Renderiza ActivityForm con onSubmit={console.log} y onCancel={() => {}}
Intenta hacer submit sin llenar campos → deben aparecer los mensajes de error
Llena el formulario con datos válidos y envía → console.log debe mostrar el objeto
Renderiza de nuevo con initialValues cargados → los campos deben estar precargados
```

### Checklist Paso 8

- [ ] Los 5 campos están presentes con sus labels correctos
- [ ] Validación ocurre en submit, no en cada keystroke
- [ ] Cada campo muestra su mensaje de error específico debajo
- [ ] `initialValues` precarga los campos correctamente
- [ ] El botón de submit se deshabilita cuando `isLoading` es `true`
- [ ] `onCancel` se llama correctamente al hacer clic en cancelar

---

## Paso 9 — Componente ActivityTable

### ¿Qué hace?

Muestra la lista de actividades de un proyecto en una tabla. Cada fila tiene los datos de la actividad más sus indicadores EVM. Las celdas de CPI y SPI tienen color según el estado (verde, amarillo, rojo).

### 9.1 Crear `src/components/evm/ActivityTable.jsx`

**Props que recibe:**

| Prop | Tipo | Descripción |
|---|---|---|
| `activities` | `array` | Lista de actividades con sus datos y campo `evm` |
| `onEdit` | `function` | Recibe la actividad completa al hacer clic en editar |
| `onDelete` | `function` | Recibe el `id` de la actividad al hacer clic en eliminar |

**Columnas de la tabla:**

| Columna | Dato fuente | Notas |
|---|---|---|
| Nombre | `activity.name` | |
| BAC | `activity.bac` | Mostrar con formato de moneda o 2 decimales |
| Av. Planificado | `activity.planned_progress` | Mostrar como porcentaje: "50%" |
| Av. Real | `activity.actual_progress` | Mostrar como porcentaje: "40%" |
| Costo Real (AC) | `activity.actual_cost` | Mostrar con 2 decimales |
| PV | `activity.evm.pv` | |
| EV | `activity.evm.ev` | |
| CV | `activity.evm.cv` | Negativo = rojo, positivo = verde |
| SV | `activity.evm.sv` | Negativo = rojo, positivo = verde |
| CPI | `activity.evm.cpi` | Usar `StatusBadge` con `interpretation` |
| SPI | `activity.evm.spi` | Usar `StatusBadge` con `interpretation` |
| EAC | `activity.evm.eac` | Puede ser null — mostrar "N/A" |
| VAC | `activity.evm.vac` | Puede ser null — mostrar "N/A" |
| Acciones | — | Botones editar y eliminar |

**Colores de las filas:**

Opcionalmente, aplica un color de fondo suave a toda la fila según el estado del CPI:
- CPI `"inefficient"` → fondo rojo muy claro
- CPI `"efficient"` → fondo verde muy claro
- CPI `"on_track"` o `"insufficient_data"` → sin color especial

**Comportamiento cuando no hay actividades:**

Si `activities` está vacío, muestra una fila que diga: "No hay actividades registradas. Agrega la primera actividad."

**Confirmación antes de eliminar:**

Al hacer clic en el botón de eliminar, muestra una confirmación con `window.confirm()` antes de llamar a `onDelete`. El mensaje debe incluir el nombre de la actividad.

### Checklist Paso 9

- [ ] Tabla con todas las columnas definidas
- [ ] CPI y SPI usan `StatusBadge` con el valor de `interpretation`
- [ ] CV y SV con color rojo/verde según positivo/negativo
- [ ] EAC y VAC muestran "N/A" cuando son `null`
- [ ] Estado vacío con mensaje descriptivo
- [ ] Confirmación antes de eliminar
- [ ] Botones editar y eliminar en cada fila

---

## Paso 10 — Componente ConsolidatedKPIs

### ¿Qué hace?

Muestra los indicadores EVM consolidados del proyecto completo en tarjetas visuales. Es la primera cosa que el líder de proyecto ve al entrar al dashboard de un proyecto.

### 10.1 Crear `src/components/evm/ConsolidatedKPIs.jsx`

**Props que recibe:**

| Prop | Tipo | Descripción |
|---|---|---|
| `evm` | `object` | El objeto `evm` del proyecto (con los totales y los índices consolidados) |

**Campos del objeto `evm` que recibirá:**

```
evm.total_bac            → Presupuesto total del proyecto
evm.total_pv             → Valor planificado total
evm.total_ev             → Valor ganado total
evm.total_ac             → Costo real total
evm.cv                   → Variación de costo (puede ser negativo)
evm.sv                   → Variación de cronograma (puede ser negativo)
evm.cpi                  → Índice de desempeño de costo (puede ser null)
evm.spi                  → Índice de desempeño de cronograma (puede ser null)
evm.eac                  → Estimado al término (puede ser null)
evm.vac                  → Variación al término (puede ser null)
evm.cpi_interpretation   → "efficient" | "inefficient" | "on_track" | "insufficient_data"
evm.spi_interpretation   → igual que cpi_interpretation
```

**Distribución visual sugerida:**

Organiza los indicadores en dos grupos de tarjetas:

*Grupo 1 — Valores absolutos (fila superior):*
- BAC Total
- PV Total
- EV Total
- AC Total

*Grupo 2 — Índices de desempeño (fila inferior):*
- CPI con `StatusBadge`
- SPI con `StatusBadge`
- EAC
- VAC

**Reglas de presentación:**

- Los valores que pueden ser `null` (CPI, SPI, EAC, VAC) muestran "N/A" si son null
- Los valores negativos de CV y SV se muestran en rojo
- Los valores positivos de CV y SV se muestran en verde
- Los valores numéricos se muestran con 2 decimales

**Comportamiento cuando el proyecto no tiene actividades:**

Si `evm.total_bac === "0"`, muestra un mensaje contextual: "Agrega actividades para ver los indicadores del proyecto."

### Checklist Paso 10

- [ ] Muestra los 12 campos del objeto `evm`
- [ ] CPI y SPI usan `StatusBadge`
- [ ] Valores null muestran "N/A"
- [ ] CV y SV negativos en rojo, positivos en verde
- [ ] Mensaje cuando no hay actividades aún
- [ ] Valores con 2 decimales

---

## Paso 11 — Componente EVMChart

### ¿Qué hace?

Muestra una gráfica de barras agrupadas comparando PV, EV y AC por actividad. Es la visualización que permite ver de un vistazo qué actividades están más desviadas del plan.

### 11.1 Crear `src/components/evm/EVMChart.jsx`

**Props que recibe:**

| Prop | Tipo | Descripción |
|---|---|---|
| `activities` | `array` | Lista de actividades con sus datos y campo `evm` |

**Transformación de datos necesaria antes de renderizar:**

Recharts necesita los datos en un formato específico. Transforma el array de actividades a este formato dentro del componente antes de pasarlo al chart:

```
Cada elemento del array debe tener:
  - name: el nombre de la actividad (truncado a 20 caracteres si es muy largo)
  - pv: parseFloat(activity.evm.pv)
  - ev: parseFloat(activity.evm.ev)
  - ac: parseFloat(activity.actual_cost)
```

**Nota:** los valores de `evm` son strings, necesitas `parseFloat()` para que Recharts los trate como números.

**Configuración del gráfico con Recharts:**

Usa `BarChart` de Recharts con estas tres barras:

| Barra | Datos | Color sugerido |
|---|---|---|
| PV (Valor Planificado) | `pv` | Azul — `#3b82f6` |
| EV (Valor Ganado) | `ev` | Verde — `#22c55e` |
| AC (Costo Real) | `ac` | Naranja — `#f97316` |

**Elementos obligatorios del chart:**

- `CartesianGrid` con `strokeDasharray="3 3"` — líneas de guía
- `XAxis` con el nombre de cada actividad
- `YAxis` con los valores
- `Tooltip` — muestra valores exactos al hacer hover
- `Legend` — muestra qué color es PV, EV y AC
- `ResponsiveContainer` — hace el chart responsive al ancho del contenedor

**Comportamiento cuando no hay actividades:**

Si `activities` está vacío, muestra un mensaje: "Agrega actividades para ver la gráfica." No renderices el chart vacío.

**Supuesto de diseño:** El chart no necesita estilos elaborados. Debe ser funcional y legible.

### Checklist Paso 11

- [ ] `BarChart` con tres barras (PV, EV, AC)
- [ ] Los datos se transforman con `parseFloat()` antes de pasarlos al chart
- [ ] Nombres de actividades en el eje X (truncados si son largos)
- [ ] `Tooltip` y `Legend` configurados
- [ ] `ResponsiveContainer` para que sea responsive
- [ ] Mensaje cuando no hay actividades

---

## Paso 12 — Página ProjectDetailPage

### ¿Qué hace?

Es el dashboard completo de un proyecto. Integra todos los componentes anteriores en una sola pantalla. El líder de proyecto pasa la mayor parte del tiempo en esta página.

### 12.1 Crear `src/pages/ProjectDetailPage.jsx`

**Cómo obtiene el projectId:**

Usa `useParams()` de React Router para leer el ID desde la URL. La URL de esta página será `/projects/:projectId`.

```
import { useParams } from 'react-router-dom'
const { projectId } = useParams()
```

**Hook que usa:**

`useProject(projectId)` — retorna `{ project, isLoading, error, isMutating, addActivity, editActivity, removeActivity }`

**Estado local que maneja la página:**

| Estado | Tipo | Descripción |
|---|---|---|
| `showForm` | `boolean` | Controla si el formulario de crear actividad está visible |
| `editingActivity` | `object \| null` | La actividad que se está editando. Si es null, el form es de crear |

**Layout de la página:**

```
┌─────────────────────────────────────────────────┐
│ Nombre del proyecto              [Volver a lista]│
│ Descripción del proyecto                         │
├─────────────────────────────────────────────────┤
│           ConsolidatedKPIs                       │
├─────────────────────────────────────────────────┤
│              EVMChart                            │
├─────────────────────────────────────────────────┤
│ Actividades           [+ Agregar actividad]      │
│                                                  │
│  [ActivityForm — visible solo si showForm=true]  │
│                                                  │
│              ActivityTable                       │
└─────────────────────────────────────────────────┘
```

**Flujo de interacciones:**

*Agregar actividad:*
1. Usuario hace clic en "Agregar actividad"
2. `showForm` pasa a `true`
3. Se renderiza `ActivityForm` con `initialValues={null}`
4. Usuario llena el form y confirma
5. Se llama a `addActivity(data)` del hook
6. El hook hace POST al backend y llama `refetch()`
7. `showForm` pasa a `false`
8. La tabla y los KPIs se actualizan con los nuevos datos

*Editar actividad:*
1. Usuario hace clic en editar en una fila de `ActivityTable`
2. `editingActivity` se establece con la actividad completa
3. `showForm` pasa a `true`
4. Se renderiza `ActivityForm` con `initialValues={editingActivity}`
5. Usuario modifica y confirma
6. Se llama a `editActivity(activityId, data)` del hook
7. `editingActivity` vuelve a `null` y `showForm` a `false`

*Eliminar actividad:*
1. Usuario hace clic en eliminar en `ActivityTable`
2. `ActivityTable` muestra confirmación con `window.confirm()`
3. Si confirma, `ActivityTable` llama a `onDelete(activityId)`
4. La página llama a `removeActivity(activityId)` del hook

**Botón "Volver a lista":**

Usa `useNavigate()` de React Router para ir a la raíz `/`.

**Estados de carga y error:**

- Si `isLoading` es `true`: mostrar `LoadingSpinner`
- Si `error` tiene mensaje: mostrar el error con opción de reintentar
- Mientras `isMutating` es `true`: deshabilitar el botón de agregar actividad

### Checklist Paso 12

- [ ] `useParams()` obtiene el `projectId` de la URL
- [ ] `useProject(projectId)` provee todos los datos y funciones
- [ ] `ConsolidatedKPIs`, `EVMChart` y `ActivityTable` están integrados
- [ ] `ActivityForm` aparece/desaparece según `showForm`
- [ ] El form distingue correctamente crear vs editar según `editingActivity`
- [ ] Botón "Volver a lista" navega a `/`
- [ ] Estado de carga con `LoadingSpinner`
- [ ] Estado de error con mensaje

---

## Paso 13 — Página ProjectsPage

### ¿Qué hace?

Es la página de entrada al sistema. Muestra la lista de proyectos con su estado EVM resumido y permite crear nuevos proyectos.

### 13.1 Crear `src/pages/ProjectsPage.jsx`

**Hook que usa:**

`useProjects()` — retorna `{ projects, isLoading, error, createProject }`

**Estado local:**

| Estado | Tipo | Descripción |
|---|---|---|
| `showCreateForm` | `boolean` | Controla si el formulario de crear proyecto está visible |
| `newProjectName` | `string` | Campo de nombre del nuevo proyecto |
| `newProjectDescription` | `string` | Campo de descripción del nuevo proyecto |
| `createError` | `string \| null` | Error si la creación falla |

**Layout de la página:**

```
┌─────────────────────────────────────────────────┐
│ EVM Project Tracker        [+ Nuevo proyecto]    │
├─────────────────────────────────────────────────┤
│ [Formulario de crear — visible solo si showForm] │
├─────────────────────────────────────────────────┤
│ ┌─────────────────────────────────────────────┐ │
│ │ Proyecto Alpha                              │ │
│ │ CPI: [StatusBadge]   SPI: [StatusBadge]    │ │
│ └─────────────────────────────────────────────┘ │
│ ┌─────────────────────────────────────────────┐ │
│ │ Proyecto Beta                               │ │
│ │ CPI: [StatusBadge]   SPI: [StatusBadge]    │ │
│ └─────────────────────────────────────────────┘ │
└─────────────────────────────────────────────────┘
```

**Tarjeta de proyecto:**

Cada proyecto en la lista muestra:
- Nombre del proyecto
- Descripción (si tiene)
- `StatusBadge` con CPI y su interpretación
- `StatusBadge` con SPI y su interpretación
- El botón o área completa de la tarjeta es clickeable y navega a `/projects/{id}`

**Flujo de crear proyecto:**

1. Usuario hace clic en "+ Nuevo proyecto"
2. Aparece un formulario simple con campo "Nombre" (requerido) y "Descripción" (opcional)
3. Usuario llena el nombre y confirma
4. Se llama a `createProject(name, description)` del hook
5. La lista se recarga automáticamente
6. El formulario se cierra

**Validación mínima del formulario:**

- El nombre no puede estar vacío
- El nombre no puede tener más de 255 caracteres

**Estado vacío:**

Si `projects` es un array vacío y `isLoading` es `false`, muestra:  
"No tienes proyectos aún. Crea el primero con el botón de arriba."

**Navegación al detalle:**

Al hacer clic en una tarjeta de proyecto, navega a `/projects/{project.id}` usando `useNavigate()` o un componente `<Link>` de React Router.

### Checklist Paso 13

- [ ] Lista de proyectos con tarjetas
- [ ] Cada tarjeta muestra CPI y SPI con `StatusBadge`
- [ ] Clic en tarjeta navega a `/projects/:id`
- [ ] Formulario de crear proyecto (nombre + descripción)
- [ ] Validación de nombre requerido
- [ ] Estado vacío con mensaje
- [ ] Estado de carga con `LoadingSpinner`

---

## Paso 14 — Ensamblaje final y pruebas

### 14.1 Configurar el Router en App.jsx

`App.jsx` es el componente raíz. Su única responsabilidad es configurar las rutas:

```
Importa BrowserRouter, Routes y Route de react-router-dom
Importa ProjectsPage y ProjectDetailPage

Define estas rutas:
  /                          → ProjectsPage
  /projects/:projectId       → ProjectDetailPage
```

No pongas lógica de negocio ni estado en `App.jsx`. Solo routing.

### 14.2 Verificar Vite para el routing

React Router con `BrowserRouter` requiere que el servidor web redirija todas las rutas al `index.html`. En desarrollo, Vite lo maneja automáticamente. Si en algún momento navegas manualmente a `/projects/algún-id` y obtienes un 404 en el navegador, agrega esto a `vite.config.js`:

```
En el objeto server, agrega:
  historyApiFallback: true
```

### 14.3 Verificar la variable de entorno

Crea o verifica que existe el archivo `frontend/.env.local` (para desarrollo local):

```
VITE_API_URL=http://localhost:5000/api/v1
```

**Nota:** Vite carga automáticamente `.env.local` en desarrollo. Este archivo no debe commitearse (agrégalo al `.gitignore` si no está).

### 14.4 Prueba de flujo completo

Con Docker corriendo (`docker compose up -d`), ejecuta el frontend en modo desarrollo:

```bash
cd frontend
npm run dev
```

Realiza este flujo completo en el navegador:

```
1. Abrir http://localhost:5173
   → Debe mostrar ProjectsPage con estado vacío

2. Crear un proyecto
   → Clic en "+ Nuevo proyecto"
   → Ingresar nombre: "Construcción Puente"
   → Confirmar
   → La tarjeta del proyecto debe aparecer en la lista
   → CPI y SPI deben mostrar badge gris "Sin datos" (no hay actividades)

3. Abrir el detalle del proyecto
   → Clic en la tarjeta
   → Debe navegar a /projects/{id}
   → ConsolidatedKPIs debe mostrar todos los valores en 0 o N/A
   → EVMChart debe mostrar mensaje "Agrega actividades..."
   → ActivityTable debe mostrar mensaje "No hay actividades registradas"

4. Agregar una actividad
   → Clic en "Agregar actividad"
   → Llenar los 5 campos con datos válidos, por ejemplo:
     Nombre: "Excavación de cimientos"
     BAC: 10000
     Avance planificado: 50
     Avance real: 40
     Costo real: 4500
   → Confirmar
   → La actividad debe aparecer en la tabla
   → Los indicadores EVM deben calcularse y mostrarse

5. Verificar los indicadores
   → PV debe ser 5000 (50% de 10000)
   → EV debe ser 4000 (40% de 10000)
   → CPI debe ser ~0.89 con badge rojo "Ineficiente"
   → El EVMChart debe mostrar las barras de PV, EV y AC

6. Editar la actividad
   → Clic en editar en la fila
   → El formulario debe precargarse con los valores actuales
   → Cambiar el avance real a 60
   → Confirmar
   → Los indicadores deben recalcularse (EV ahora es 6000)

7. Eliminar la actividad
   → Clic en eliminar
   → Debe aparecer confirmación con el nombre de la actividad
   → Confirmar eliminación
   → La tabla vuelve al estado vacío

8. Volver a la lista
   → Clic en "Volver a lista"
   → Debe navegar a /
   → El proyecto debe seguir apareciendo en la lista
```

### 14.5 Probar estados de error

```
1. Detener el backend: docker stop evm_backend
2. Intentar cargar un proyecto
   → Debe mostrar un mensaje de error, no una pantalla en blanco
3. Reiniciar el backend: docker start evm_backend
```

### 14.6 Verificar ESLint

```bash
cd frontend
npm run lint
# No debe haber errores
```

### Checklist Paso 14

- [ ] `App.jsx` solo tiene routing, sin lógica de negocio
- [ ] Las dos rutas funcionan: `/` y `/projects/:projectId`
- [ ] Flujo completo de crear proyecto → agregar actividad → editar → eliminar funciona
- [ ] Los indicadores EVM se actualizan después de cada operación
- [ ] Los colores de CPI y SPI son correctos en la tabla y en los KPIs
- [ ] La gráfica muestra las barras de PV, EV y AC
- [ ] Los estados de error muestran mensajes, no pantallas en blanco
- [ ] `npm run lint` sin errores

---

## Paso 15 — PR y entrega

### 15.1 Hacer commits por módulo

```bash
git add src/api/evmApi.js
git commit -m "Add Axios instance and API functions for projects and activities"

git add src/hooks/
git commit -m "Add useProjects and useProject custom hooks"

git add src/constants/evm.js src/components/ui/
git commit -m "Add EVM constants and StatusBadge and LoadingSpinner components"

git add src/components/evm/ActivityForm.jsx
git commit -m "Add ActivityForm component with field validation"

git add src/components/evm/ActivityTable.jsx
git commit -m "Add ActivityTable component with EVM indicators and color coding"

git add src/components/evm/ConsolidatedKPIs.jsx
git commit -m "Add ConsolidatedKPIs component for project-level EVM summary"

git add src/components/evm/EVMChart.jsx
git commit -m "Add EVMChart bar chart comparing PV, EV and AC per activity"

git add src/pages/
git commit -m "Add ProjectsPage and ProjectDetailPage integrating all components"

git add src/App.jsx src/main.jsx src/index.css
git commit -m "Configure React Router with project list and detail routes"
```

### 15.2 Push y PR

```bash
git push origin feature/frontend-dashboard
```

**Descripción del PR:**

```markdown
## ¿Qué hace este PR?

Implementa la Fase 4 completa: dashboard frontend con React + Vite que consume 
la API REST del backend y visualiza los indicadores EVM en tiempo real.

## Funcionalidades implementadas

- Lista de proyectos con estado EVM consolidado (CPI/SPI con color)
- Crear nuevos proyectos
- Dashboard de proyecto con KPIs consolidados, tabla de actividades y gráfica
- CRUD completo de actividades desde el dashboard
- Indicadores EVM calculados automáticamente en cada operación

## Cómo probar

docker compose up -d
cd frontend && npm run dev
Abrir http://localhost:5173

## Checklist

- [ ] Scaffolding Vite + React funcional
- [ ] ESLint configurado y sin errores
- [ ] evmApi.js con todas las funciones del API
- [ ] Hooks useProjects y useProject implementados
- [ ] StatusBadge con 4 estados de color
- [ ] ActivityForm con validaciones por campo
- [ ] ActivityTable con colores por CPI/SPI
- [ ] ConsolidatedKPIs con todos los indicadores
- [ ] EVMChart con barras PV/EV/AC
- [ ] ProjectDetailPage integrando todo
- [ ] ProjectsPage con lista y creación
- [ ] Flujo completo probado manualmente
- [ ] npm run lint sin errores
```

---

## Referencia de la API del backend

Esta sección es la referencia que necesitas para implementar `evmApi.js` correctamente.

### Proyectos

```
GET    /api/v1/projects/
       Response 200: array de ProjectObject

POST   /api/v1/projects/
       Body: { "name": string (requerido), "description": string (opcional) }
       Response 201: ProjectObject

GET    /api/v1/projects/{id}
       Response 200: ProjectObject con activities[]
       Response 404: { "error": "not_found", "message": "Project not found" }

PUT    /api/v1/projects/{id}
       Body: { "name"?: string, "description"?: string }
       Response 200: ProjectObject actualizado
       Response 404: { "error": "not_found", ... }

DELETE /api/v1/projects/{id}
       Response 204: sin body
       Response 404: { "error": "not_found", ... }
```

### Actividades

```
GET    /api/v1/projects/{id}/activities
       Response 200: array de ActivityObject
       Response 404: Project not found

POST   /api/v1/projects/{id}/activities
       Body: {
         "name": string (requerido),
         "bac": string numérico (requerido, >= 0),
         "planned_progress": string numérico (requerido, 0-100),
         "actual_progress": string numérico (requerido, 0-100),
         "actual_cost": string numérico (requerido, >= 0)
       }
       Response 201: ActivityObject con evm calculado
       Response 404: Project not found
       Response 422: { "error": "validation_error", "details": {...} }

PUT    /api/v1/activities/{id}
       Body: cualquier subconjunto de los campos de ActivityCreateSchema
       Response 200: ActivityObject actualizado con evm recalculado
       Response 404: Activity not found

DELETE /api/v1/activities/{id}
       Response 204: sin body
       Response 404: Activity not found
```

### Errores comunes del backend

| Código | Cuándo ocurre | Qué mostrar al usuario |
|---|---|---|
| 404 | Recurso no existe | "El recurso solicitado no fue encontrado" |
| 422 | Datos inválidos | Mostrar el detalle del campo que falló |
| 500 | Error interno | "Ocurrió un error inesperado. Intenta de nuevo." |
| Sin respuesta | Backend no disponible | "No se puede conectar con el servidor" |

---
## Checklist de entrega

### Archivos creados

- [ ] `src/api/evmApi.js`
- [ ] `src/hooks/useProjects.js`
- [ ] `src/hooks/useProject.js`
- [ ] `src/constants/evm.js`
- [ ] `src/components/ui/StatusBadge.jsx`
- [ ] `src/components/ui/LoadingSpinner.jsx`
- [ ] `src/components/evm/ActivityForm.jsx`
- [ ] `src/components/evm/ActivityTable.jsx`
- [ ] `src/components/evm/ConsolidatedKPIs.jsx`
- [ ] `src/components/evm/EVMChart.jsx`
- [ ] `src/pages/ProjectsPage.jsx`
- [ ] `src/pages/ProjectDetailPage.jsx`
- [ ] `src/App.jsx` (solo routing)

### Funcionalidad

- [ ] Crear proyecto desde ProjectsPage
- [ ] Listar proyectos con CPI/SPI visible
- [ ] Navegar al detalle del proyecto
- [ ] Ver ConsolidatedKPIs con todos los indicadores
- [ ] Ver EVMChart con barras PV/EV/AC
- [ ] Agregar actividad con validación de campos
- [ ] Editar actividad con formulario precargado
- [ ] Eliminar actividad con confirmación
- [ ] Indicadores EVM se actualizan después de cada operación
- [ ] Volver a la lista desde el detalle

### Calidad

- [ ] `npm run lint` sin errores ni warnings de error
- [ ] No hay `console.log` olvidados en el código
- [ ] No hay variables declaradas y no usadas
- [ ] Los valores null del EVM muestran "N/A", no "null" ni "NaN"
- [ ] Los estados de carga muestran `LoadingSpinner`
- [ ] Los estados de error muestran mensajes descriptivos
- [ ] Los valores numéricos del EVM se parsean con `parseFloat()` antes de comparar

------

## Entendimiento EVM 

Le pregunte a geminis y cloude, para entender como funciona use un ejemplo real con las siguientes formulas que me dio la IA:

PV = (planned_progress / 100) * BAC
EV = (actual_progress / 100) * BAC
CV = EV - AC
SV = EV - PV
CPI = EV / AC
SPI = EV / PV
EAC = BAC / CPI
VAC = BAC - EAC

para coroborar que todo funcionara me ayude de excel con el fin de solo pasar las formulas y evitar estar calculando, todo con casos simples, posterior a esto valide confirme con pruebas unitarias

## Dos desiciones que yo tome

al principio como inicial me dio un diseño de carpetas que no convenia para el proyecto, con las pruebas iba a usar la Bd de posgress, para un mejor uso opte por slqLite ya que no deberia mentarner los datos y asi las pruebas se pueden repetir facilmente sin necesidad de afecta la BD

## Desicion de arquitectura

El front desacoplado al backend, usando axios, para separar claramente responsabilidades

## Reflexion honesta

Ya teniendo mas contexto de como funciona el modelo y haberlo trabajado y testado cambiaria ciertos criterios de UI para mejorar la experiencia de usuario, haciendolo mas amigable
