# Taller de DevOps: CI/CD con GitHub Actions

![CI Pipeline](https://github.com/danielxzr2/Ingesoft2/actions/workflows/ci.yml/badge.svg)
![Node.js](https://img.shields.io/badge/Node.js-18-green)
![Express](https://img.shields.io/badge/Express-4.18-blue)

Este proyecto es una implementación práctica de un flujo de trabajo de **Integración Continua (CI)** y **Despliegue Continuo (CD)** utilizando GitHub Actions. Consiste en una API REST básica construida con Node.js y Express, cubierta por pruebas unitarias automatizadas y desplegada automáticamente en GitHub Pages.

---

## 🚀 Despliegue en Vivo (CD)

El pipeline despliega automáticamente una página de estado cada vez que se aprueban los cambios y pasan las pruebas en la rama `main`.

🔗 **Ver Estado del Despliegue:** [https://danielxzr2.github.io/Ingesoft2/](https://danielxzr2.github.io/Ingesoft2/)

> **Resultado esperado en la web (Ejemplo real):**
> 
> **Deploy Status**
> * **Last deploy:** Tue Feb 17 01:45:35 UTC 2026
> * **Commit:** 89819433d5691a65b8300bee6a7b3454588abc9a

---

## 🛠️ Tecnologías Utilizadas

* **Runtime:** Node.js (v18)
* **Framework:** Express.js
* **Testing:** Jest + Supertest
* **CI/CD:** GitHub Actions
* **Hosting (Static):** GitHub Pages
* **Control de Versiones:** Git & GitHub

---

## 📂 Estructura del Proyecto

El proyecto sigue una arquitectura modular para facilitar las pruebas y el mantenimiento:

```text
mi-proyecto/
├── src/
│   └── app.js           # Lógica de la aplicación y endpoints
├── tests/
│   └── app.test.js      # Pruebas unitarias e integración (Jest)
├── .github/
│   └── workflows/
│       └── ci.yml       # Definición del Pipeline CI/CD
├── package.json         # Dependencias y scripts
└── README.md            # Documentación del proyecto
```

---

## ⚙️ Instalación y Uso Local

Para ejecutar este proyecto en tu máquina local:

1.  **Clonar el repositorio:**
    ```bash
    git clone [https://github.com/danielxzr2/Ingesoft2.git](https://github.com/danielxzr2/Ingesoft2.git)
    cd Ingesoft2
    ```

2.  **Instalar dependencias:**
    ```bash
    npm install
    ```

3.  **Ejecutar el servidor:**
    ```bash
    npm start
    ```
    El servidor correrá en `http://localhost:3000`.

4.  **Ejecutar pruebas:**
    ```bash
    npm test
    ```

---

## 📡 API Endpoints

La aplicación expone los siguientes endpoints REST:

| Método | Endpoint | Descripción | Respuesta Ejemplo |
| :--- | :--- | :--- | :--- |
| `GET` | `/` | Mensaje de bienvenida | `{ "message": "Hola, DevOps!" }` |
| `GET` | `/health` | Chequeo de salud del servicio | `{ "status": "OK", "timestamp": "..." }` |
| `GET` | `/version` | Versión actual de la API | `{ "version": "1.0.0" }` |

---

## 🔄 Arquitectura del Pipeline (CI/CD)

El archivo `.github/workflows/ci.yml` orquesta todo el proceso automático:

### 1. Integración Continua (CI) - Job: `test`
Se ejecuta en cada `push` o `pull_request` hacia la rama `main`.
1.  **Checkout:** Descarga el código del repositorio.
2.  **Setup Node:** Configura el entorno con Node.js v18.
3.  **Install:** Instala las dependencias limpias (`npm ci`).
4.  **Test:** Ejecuta la suite de pruebas con Jest y genera reporte de cobertura.

### 2. Entrega Continua (CD) - Job: `deploy`
Se ejecuta **solo si los tests pasan** y estamos en la rama `main`.
1.  **Build:** Genera un archivo `index.html` dinámico que incluye:
    * Fecha del despliegue.
    * Hash del último commit (SHA).
2.  **Deploy:** Sube el archivo generado a la rama `gh-pages` utilizando la acción `peaceiris/actions-gh-pages`, actualizando el sitio web automáticamente.

---

## 👥 Autor

**Daniel** - Estudiante de Ingeniería de Software
