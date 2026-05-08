**Estudiante:** Daniel Garzón  
**API Seleccionada:** [Rick and Morty API](https://rickandmortyapi.com/)  

---

## 1. Selección de la API
**¿Qué API elegiste y por qué?**
He seleccionado la **Rick and Morty API**. La elección se basa en que, a diferencia de otras herramientas básicas como JSONPlaceholder, esta API ofrece:
* **Estructura del mundo real:** Datos anidados y relaciones entre personajes, locaciones y episodios.
* **Documentación clara:** Facilita la construcción de consultas complejas mediante filtros.

---

## 2. Análisis de Datos
**¿Qué datos devuelve?**
La API entrega información estructurada en formato JSON sobre tres recursos principales:
1.  **Characters:** Atributos como `name`, `status`, `species`, `type`, `gender`, e imágenes.
2.  **Locations:** Detalles de planetas y dimensiones (`name`, `type`, `dimension`).
3.  **Episodes:** Información cronológica de la serie.

---

## 3. Autenticación y Seguridad
**¿Usa token o no? ¿Qué tipo?**
**No usa token.** Es una API de consulta abierta. Esto permite centrarse puramente en la lógica de las peticiones `GET` y en la validación de los datos recibidos sin la capa adicional de gestión de sesiones o tokens de portador (Bearer Tokens).

---

## 4. Registro de Solicitudes (Requests)
Se configuraron 3 solicitudes clave para cubrir los requerimientos de la tarea:

| Solicitud | Método | Endpoint / Query Params | Código de Estado |
| :--- | :--- | :--- | :--- |
| **Obtener todo** | `GET` | `/` | `200 OK` |
| **Búsqueda por ID** | `GET` | `/character/2` (Morty Smith) | `200 OK` |
| **Filtro Combinado** | `GET` | `/character/?status=alive&name=Rick` | `200 OK` |

---

## 5. Diferencias con JSONPlaceholder
**¿Qué aprendiste diferente a JSONPlaceholder?**
1.  **Filtros Avanzados:** Aprendí a usar múltiples *Query Parameters* en una sola URL para realizar búsquedas granulares (ej: filtrar por estado y especie al mismo tiempo).
2.  **Validación de Objetos Anidados:** En JSONPlaceholder los datos suelen ser planos. Aquí tuve que aprender a validar propiedades dentro de objetos (como `origin.name`).
3.  **Eficiencia con Tests de Colección:** Implementé los tests a nivel de carpeta, lo que permite que una sola lógica de validación se ejecute para todas las peticiones automáticamente, optimizando el flujo de trabajo.

---

## 6. Tests Automáticos Implementados
Se añadieron los siguientes scripts en la pestaña **Tests** para automatizar la validación:

```javascript
// Validar código de estado exitoso
pm.test("Status code is 200", function () {
    pm.response.to.have.status(200);
});

// Validar que la respuesta es un objeto JSON válido
pm.test("Estructura JSON correcta", function () {
    var jsonData = pm.response.json();
    pm.expect(jsonData).to.be.an('object');
});

// Validar tiempo de respuesta (Performance)
pm.test("Tiempo de respuesta aceptable (<500ms)", function () {
    pm.expect(pm.response.responseTime).to.be.below(500);
});
