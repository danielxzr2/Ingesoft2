# Lab JWT + SSH — Ingeniería de Software 2
# Daniel Alberto Garzon Fraile

## Descripción
Laboratorio de autenticación con JWT usando Node.js, validación de endpoints REST
y consumo remoto de la API mediante SSH.

---

## Requisitos previos
- Node.js instalado
- jq instalado (`sudo apt install jq`)

---

## 1. Configuración inicial

### Arrancar el servidor
```bash
node server.js
```

[CAPTURA: terminal mostrando "Server running on port 3000"]

---

## 2. Registro y Login

### Registrar usuario
```bash
curl -s -X POST http://localhost:3000/auth/register \
  -H "Content-Type: application/json" \
  -d '{"username":"carlos","email":"carlos@test.com","password":"1234"}'
```

[CAPTURA: respuesta del register con el JSON de confirmación]

### Guardar token
```bash
TOKEN=$(curl -s -X POST http://localhost:3000/auth/login \
  -H "Content-Type: application/json" \
  -d '{"email":"carlos@test.com","password":"1234"}' | jq -r '.token')

echo $TOKEN
```

[CAPTURA: el token JWT impreso en pantalla]

---

## 3. Operaciones CRUD sobre tareas

### Crear tarea
```bash
TAREA=$(curl -s -X POST http://localhost:3000/tasks \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $TOKEN" \
  -d '{"title":"Tarea de prueba","description":"Para probar PUT y DELETE"}')

echo $TAREA
TAREA_ID=$(echo $TAREA | jq -r '.id')
```

[CAPTURA: respuesta con el JSON de la tarea creada, incluyendo su id]

### Listar tareas
```bash
curl -s http://localhost:3000/tasks \
  -H "Authorization: Bearer $TOKEN"
```

[CAPTURA: respuesta mostrando el arreglo de tareas]

### Actualizar tarea (PUT)
```bash
curl -s -X PUT http://localhost:3000/tasks/$TAREA_ID \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $TOKEN" \
  -d '{"status":"completed"}'
```

[CAPTURA: respuesta con la tarea actualizada mostrando "status":"completed"]

### Eliminar tarea (DELETE)
```bash
curl -s -X DELETE http://localhost:3000/tasks/$TAREA_ID \
  -H "Authorization: Bearer $TOKEN"
```

[CAPTURA: terminal sin respuesta — comportamiento esperado del status 204]

### Verificar que fue eliminada
```bash
curl -s http://localhost:3000/tasks \
  -H "Authorization: Bearer $TOKEN"
```

[CAPTURA: respuesta mostrando "tasks": [] — lista vacía]

---

## 4. Conexión SSH desde otro equipo

### Conectarse por SSH
```bash
ssh danielxzr@192.168.10.8
```

[CAPTURA: terminal del otro PC mostrando el prompt de Ubuntu después de conectarse]

### Consumir la API desde la sesión SSH
```bash
curl -s http://localhost:3000/tasks \
  -H "Authorization: Bearer $TOKEN"
```

[CAPTURA: respuesta de la API vista desde la sesión SSH — debe mostrar el prompt
 con el nombre del equipo Ubuntu para evidenciar que es una conexión remota]

---

## 5. Implementación de PUT y DELETE

Los endpoints fueron implementados en `server.js` completando los TODOs:

- **PUT** `/tasks/:id` — busca la tarea, verifica permisos y actualiza los campos recibidos
- **DELETE** `/tasks/:id` — busca la tarea, verifica permisos y la elimina del arreglo

[CAPTURA: fragmento del código implementado en server.js]
