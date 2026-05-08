## Reflexión sobre GraphQL vs REST

### 1. ¿Qué diferencia encontraste vs REST?

La diferencia fundamental es el **control**.

- **Overfetching (Exceso de datos):** En REST (como con Rick y Morty), si solo quisiera el nombre del personaje, la API de todos modos me obligaba a descargar la especie, el género, la imagen y el origen. En GraphQL, solo se define el "molde" y la API solo llena esos campos.

- **Endpoints:** En REST tenía una URL para cada cosa (`/character`, `/location`). En GraphQL, todo sucede en una única URL (`/`). El servidor no decide qué dar por la URL, sino por el contenido de la `query`.

- **Tipado y Autocompletado:** Al configurar Postman para GraphQL, note que "entiende" los campos disponibles. Eso es porque GraphQL tiene un **Esquema (Schema)** que sirve como contrato estricto entre el cliente y el servidor.

---

### 2. ¿Cuántos requests REST necesitarías para reemplazar tu query más compleja?

Tomando como ejemplo la query de Países de Sudamérica (`GetSouthAmericanCountries`):

```graphql
query {
  continent(code: "SA") {
    name
    countries {
      name
      capital
    }
  }
}
```

Para obtener esto mismo en una API REST convencional, normalmente necesitaria:

1. **1 request** a `/continents/SA` para obtener la información del continente. Este mw devolvería una lista de IDs o códigos de países.
2. **$n$ requests** (uno por cada país) a `/countries/{code}` para obtener el nombre y la capital de cada uno.

Considerando que Sudamérica tiene 12 países, necesitaria realizar **13 peticiones** (1 + 12) para obtener la misma información que GraphQL me dio en una sola. A esto en programación se le conoce como el **problema de $n+1$ consultas**, y GraphQL lo resuelve de raíz.

---

### 3. ¿En qué proyecto real usarías GraphQL?

GraphQL brilla en proyectos donde los datos están muy relacionados y el ancho de banda es importante. Un ejemplo perfecto sería una **Red Social** (tipo Facebook o Instagram):

- **Por qué:** Por ejemplo, para el Feed se necesitaria el nombre del usuario, su foto de perfil, el contenido del post, los últimos 3 comentarios y el nombre de quien dio "like".
- **En REST:** Tendria que llamar al endpoint de `/posts`, luego por cada post llamar a `/users/{id}`, luego a `/comments?post_id={id}`, etc. Sería un caos de red.
- **En GraphQL:** Solo se envia una query anidada y se construye toda la pantalla de una vez.

También es ideal para **Aplicaciones Móviles**, ya que al pedir solo los datos necesarios, ahorras batería y datos móviles del usuario.
