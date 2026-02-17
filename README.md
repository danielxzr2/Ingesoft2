# Taller de DevOps: CI/CD con GitHub Actions

![CI Pipeline](https://github.com/danielxzr2/Ingesoft2/actions/workflows/ci.yml/badge.svg)
![Node.js](https://img.shields.io/badge/Node.js-18-green)
![Express](https://img.shields.io/badge/Express-4.18-blue)

Este proyecto es una implementación práctica de un flujo de trabajo de **Integración Continua (CI)** y **Despliegue Continuo (CD)** utilizando GitHub Actions. Consiste en una API REST básica construida con Node.js y Express, cubierta por pruebas unitarias automatizadas y desplegada automáticamente en GitHub Pages.

---

## 📸 Evidencia del Pipeline Exitoso

A continuación se muestra la ejecución correcta del flujo de trabajo en GitHub Actions.

<img width="714" height="301" alt="GithubActions" src="https://github.com/user-attachments/assets/226303ff-2829-43c5-aa94-eec269a86d83" />

Donde se evidencia la instalación de dependencias
<img width="746" height="541" alt="build" src="https://github.com/user-attachments/assets/bd285dc2-14c9-4f9f-8fd8-80e32e4b70c6" />


La ejecución de pruebas 
<img width="725" height="565" alt="test" src="https://github.com/user-attachments/assets/13500ce5-5461-465c-8bcc-515762d66963" />

Y despliegue:
<img width="734" height="423" alt="deploy" src="https://github.com/user-attachments/assets/77f98401-b475-492e-8a61-31fab2ece33d" />

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

## 💡 Desafío Técnico y Solución

Durante la implementación del pipeline de Despliegue Continuo (CD), nos enfrentamos al siguiente reto:

**El Problema:**
Al intentar realizar el push automático a la rama `gh-pages`, el pipeline fallaba con un error `403 Forbidden`.
> `remote: Permission to danielxzr2/Ingesoft2.git denied to github-actions[bot].`

**La Causa:**
Los tokens automáticos de GitHub Actions (`GITHUB_TOKEN`) tienen, por defecto, permisos de solo lectura para mayor seguridad.

**La Solución:**
Configuramos explícitamente los permisos de escritura en el repositorio:
1. Navegamos a *Settings > Actions > General*.
2. En *Workflow permissions*, habilitamos **"Read and write permissions"**.
3. Adicionalmente, agregamos el permiso `contents: write` en el archivo YAML del workflow.

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

## 🧪 Reporte de Cobertura de Código

Este proyecto utiliza **Jest** para medir qué porcentaje del código está cubierto por pruebas. Para ver el reporte detallado en HTML:

1. Ejecuta las pruebas:
   ```bash
   npm test
   
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

**Daniel** - Estudiante de Ingeniería de Sistemas y Computación

