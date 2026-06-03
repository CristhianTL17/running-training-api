# Running Backend API

Backend desarrollado con FastAPI para la gestión de atletas, planes de entrenamiento y sesiones de running.

## Características

- Registro de usuarios
- Autenticación JWT
- Rutas protegidas
- Gestión de atletas
- Gestión de planes de entrenamiento
- Gestión de sesiones de entrenamiento
- Base de datos PostgreSQL
- SQLAlchemy ORM
- Validación con Pydantic

## Tecnologías

- Python
- FastAPI
- PostgreSQL
- SQLAlchemy
- JWT Authentication
- Pydantic
- Bcrypt

## Instalación

Clonar repositorio:

```bash
git clone <url-del-repositorio>
```

Crear entorno virtual:

```bash
python -m venv venv
```

Activar entorno:

```bash
venv\Scripts\activate
```

Instalar dependencias:

```bash
pip install -r requirements.txt
```

Crear archivo `.env` usando `.env.example`.

Ejecutar servidor:

```bash
uvicorn app.main:app --reload
```

## Endpoints

### Usuarios

- GET /users
- POST /register
- PUT /users/{id}
- DELETE /users/{id}

### Autenticación

- POST /login
- GET /profile

### Planes

- POST /plans
- GET /plans

### Sesiones

- POST /sessions
- GET /sessions
- PUT /sessions/{id}
- DELETE /sessions/{id}

## Autor

Cristhian Torres