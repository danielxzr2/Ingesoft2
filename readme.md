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

---

## 2. Registro y Login

### Registrar usuario
```bash
curl -s -X POST http://localhost:3000/auth/register \
  -H "Content-Type: application/json" \
  -d '{"username":"carlos","email":"carlos@test.com","password":"1234"}'
```

<img width="1526" height="185" alt="Screenshot from 2026-05-07 19-52-53" src="https://github.com/user-attachments/assets/8a4d14bf-7b7c-4162-9f1b-bbdef4949b7f" />


### Guardar token
```bash
TOKEN=$(curl -s -X POST http://localhost:3000/auth/login \
  -H "Content-Type: application/json" \
  -d '{"email":"carlos@test.com","password":"1234"}' | jq -r '.token')

echo $TOKEN
```

<img width="1850" height="150" alt="Screenshot from 2026-05-07 19-54-03" src="https://github.com/user-attachments/assets/ac142b33-562b-4564-8d7e-abc295398c96" />

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

<img width="1856" height="298" alt="Screenshot from 2026-05-08 00-39-57" src="https://github.com/user-attachments/assets/d83e43c5-595f-4639-9da9-0e71d72fb887" />


### Listar tareas
```bash
curl -s http://localhost:3000/tasks \
  -H "Authorization: Bearer $TOKEN"
```

<img width="1857" height="319" alt="Screenshot from 2026-05-08 00-40-10" src="https://github.com/user-attachments/assets/aaa0bb02-184c-49b1-b9c8-68e8193c724b" />


### Actualizar tarea (PUT)
```bash
curl -s -X PUT http://localhost:3000/tasks/$TAREA_ID \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $TOKEN" \
  -d '{"status":"completed"}'
```

<img width="1834" height="556" alt="Screenshot from 2026-05-08 00-40-55" src="https://github.com/user-attachments/assets/fea73f62-0ec8-423b-923e-d5964c6107d9" />


### Eliminar tarea (DELETE)
```bash
curl -s -X DELETE http://localhost:3000/tasks/$TAREA_ID \
  -H "Authorization: Bearer $TOKEN"
```

### Verificar que fue eliminada
```bash
curl -s http://localhost:3000/tasks \
  -H "Authorization: Bearer $TOKEN"
```

<img width="1792" height="127" alt="Screenshot from 2026-05-08 00-41-11" src="https://github.com/user-attachments/assets/f26cc5cf-375c-480a-8a11-161bdc4c1e9c" />

---

## 4. Conexión SSH desde otro equipo

### Conectarse por SSH
```bash
ssh danielxzr@192.168.10.8
```

<img width="929" height="437" alt="image" src="https://github.com/user-attachments/assets/d4ef6c44-569c-4b25-9dcf-88c7993d794a" />


### Consumir la API desde la sesión SSH
```bash
curl -s http://localhost:3000/tasks \
  -H "Authorization: Bearer $TOKEN"
```

<img width="957" height="534" alt="image" src="https://github.com/user-attachments/assets/1e3033cf-ee47-4c3b-94e3-010e210bb162" />
<img width="956" height="723" alt="image" src="https://github.com/user-attachments/assets/02046e77-309d-4f35-8e61-2d8148d21eda" />
<img width="952" height="135" alt="image" src="https://github.com/user-attachments/assets/33df7fc1-5310-4086-bc12-e8c63ce84e08" />

---

## 5. Implementación de PUT y DELETE

Los endpoints fueron implementados en `server.js` completando los TODOs:

- **PUT** `/tasks/:id` — busca la tarea, verifica permisos y actualiza los campos recibidos

<img width="834" height="542" alt="Screenshot from 2026-05-08 00-52-42" src="https://github.com/user-attachments/assets/5d045325-cccd-4a3f-bf4a-4488d0e14578" />


- **DELETE** `/tasks/:id` — busca la tarea, verifica permisos y la elimina del arreglo

<img width="843" height="501" alt="Screenshot from 2026-05-08 00-52-56" src="https://github.com/user-attachments/assets/b3de7388-2db1-42b9-a41a-dacc167f61f6" />



