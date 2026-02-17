# Taller de DevOps: CI/CD con GitHub Actions

![CI Pipeline](https://github.com/danielxzr2/Ingesoft2/actions/workflows/ci.yml/badge.svg)
![Node.js](https://img.shields.io/badge/Node.js-18-green)
![Express](https://img.shields.io/badge/Express-4.18-blue)

Este proyecto es una implementación práctica de un flujo de trabajo de **Integración Continua (CI)** y **Despliegue Continuo (CD)** utilizando GitHub Actions. Consiste en una API REST básica construida con Node.js y Express, cubierta por pruebas unitarias automatizadas y desplegada automáticamente en GitHub Pages.

---

## 📸 Evidencia del Pipeline Exitoso

### 1. Visión General del Workflow
Ejecución correcta del flujo de trabajo en GitHub Actions:

<div align="center">
  <img width="800" alt="GithubActions" src="https://github.com/user-attachments/assets/226303ff-2829-43c5-aa94-eec269a86d83" />
</div>

### 2. Detalle de los Pasos (Logs)
A continuación se detalla la ejecución exitosa de cada etapa crítica del pipeline:

| 📦 1. Instalación de Dependencias | 🧪 2. Ejecución de Pruebas | 🚀 3. Despliegue a Producción |
| :---: | :---: | :---: |
| <img src="https://github.com/user-attachments/assets/f1d71fcb-a30e-4f1a-8354-0a0554c69e62" width="100%"> | <img src="https://github.com/user-attachments/assets/13500ce5-5461-465c-8bcc-515762d66963" width="100%"> | <img src="https://github.com/user-attachments/assets/77f98401-b475-492e-8a61-31fab2ece33d" width="100%"> |
| *Dependencias instaladas limpiamente (`npm ci`)* | *Tests unitarios y cobertura aprobados* | *Subida exitosa a la rama `gh-pages`* |

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
   
2. Busca la carpeta generada: coverage/lcov-report/index.html

3. Abre ese archivo en tu navegador para ver línea por línea qué está testeado.
   
---

## 🔄 Arquitectura del Pipeline (CI/CD)

El flujo de trabajo automatizado está definido en `.github/workflows/ci.yml` y se divide en dos etapas secuenciales (Jobs):

### 1. 🧪 Integración Continua (Job: `test`)
Este trabajo se encarga de garantizar la integridad del código antes de cualquier intento de despliegue.

* **Disparadores (`on`):** Se activa automáticamente en cada `push` o `pull_request` dirigido a la rama `main`.
* **Entorno:** Se ejecuta sobre un contenedor virtual **Ubuntu Latest**.
* **Pasos Clave:**
    1.  **Checkout:** Utiliza `actions/checkout@v4` para clonar el repositorio en el entorno virtual.
    2.  **Environment Setup:** Configura Node.js versión 18.
    3.  **Clean Install:** Ejecuta `npm ci` (en lugar de `npm install`). Esto asegura una instalación determinista basada exactamente en el archivo `package-lock.json`, vital para entornos de CI.
    4.  **Unit Testing:** Ejecuta `npm test`. Si **una sola prueba falla**, el proceso se detiene inmediatamente y marca el commit como fallido (❌).

### 2. 🚀 Entrega Continua (Job: `deploy`)
Este trabajo se encarga de publicar la aplicación, pero tiene **candados de seguridad** estrictos.

* **Dependencia Crítica (`needs: test`):** Este job **espera** a que el job `test` termine exitosamente. Si las pruebas fallan, el despliegue nunca inicia.
* **Condición de Rama (`if`):** Verifica `github.ref == 'refs/heads/main'`. Esto asegura que los cambios en ramas de desarrollo (features) se prueben, pero no rompan el sitio público hasta que se fusionen a `main`.
* **Permisos de Escritura:** Se configuran permisos explícitos (`contents: write`) para permitir que el bot de GitHub Actions pueda hacer `git push` a la rama del repositorio.
* **Generación de Artefactos:**
    * Se crea un directorio `public` al vuelo.
    * Se inyectan variables de entorno dinámicas como `$(date)` y `$GITHUB_SHA` (el ID único del commit) en un archivo HTML para trazabilidad.
* **Despliegue:** Utiliza la acción `peaceiris/actions-gh-pages` para subir la carpeta generada a la rama `gh-pages`, lo que actualiza el sitio web en vivo.

---

## 👥 Autor

**Daniel** - Estudiante de Ingeniería de Sistemas y Computación

