# Aplicación de Solicitudes de Compra

Esta aplicación, construida con **FastAPI** y **SQLAlchemy**, permite gestionar solicitudes de compra. Las funcionalidades principales incluyen:

- **Crear Solicitudes de Compra**: Los usuarios pueden crear solicitudes de compra con una descripción.
- **Leer Solicitudes**: Las solicitudes de compra pueden ser leídas y marcadas como vistas.
- **Aprobación**: Las solicitudes de compra se pueden aprobar automáticamente después de ser leídas.

## Tecnologías usadas

- **FastAPI**: Framework web moderno para la creación de APIs con Python.
- **SQLAlchemy**: ORM para la interacción con la base de datos.
- **SQLite**: Base de datos ligera usada para almacenar las solicitudes de compra.

## Requisitos previos

Asegúrate de tener **Python 3.7+** instalado en tu sistema.

## Uso de la aplicación

Puedes interactuar con la API utilizando un cliente como **Postman** o **cURL**. A continuación se describen los endpoints disponibles:

### 1. Crear una solicitud de compra

- **URL**: `POST http://127.0.0.1:8000/purchase_request/`
- **Cuerpo (JSON)**:

  {
      "description": "Descripción de la solicitud de compra"
  }

- **Respuesta (JSON)**:

  {
      "id": 1,
      "description": "Descripción de la solicitud de compra",
      "is_read": false,
      "is_approved": false
  }

### 2. Leer una solicitud de compra

- **URL**: `GET http://127.0.0.1:8000/acknowledge/read_request/?request_id=1`
- **Respuesta (JSON)**:

 {
    "message": "Request has been read"
 }

### 3. Marcar recibido una solicitud

- **URL**: `POST http://127.0.0.1:8000/acknowledge/acknowledge/?request_id=1`


- **Respuesta (JSON)**:

  {
    "request_id": 1,
    "id": 1,
    "acknowledged": true,
    "approved": false
  }
