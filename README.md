# Taller de DevOps: CI/CD con GitHub Actions

![CI Pipeline](https://github.com/danielxzr2/Ingesoft2/actions/workflows/ci.yml/badge.svg)
![Node.js](https://img.shields.io/badge/Node.js-18-green)
![Express](https://img.shields.io/badge/Express-4.18-blue)

Este proyecto es una implementación práctica de un flujo de trabajo de **Integración Continua (CI)** y **Despliegue Continuo (CD)** utilizando GitHub Actions. Consiste en una API REST básica construida con Node.js y Express, cubierta por pruebas unitarias y automatizada para desplegar una página de estado en GitHub Pages.

## 🚀 Despliegue en Vivo (CD)

El pipeline despliega automáticamente una página de estado cada vez que se aprueban los cambios en la rama `main`.

🔗 **Ver Estado del Despliegue:** [https://danielxzr2.github.io/Ingesoft2/](https://danielxzr2.github.io/Ingesoft2/)

> **Resultado esperado en la web:**
> - **Last deploy:** Tue Feb 17 01:45:35 UTC 2026
> - **Commit:** 89819433d5691a65b8300bee6a7b3454588abc9a

---

## 🛠️ Tecnologías Utilizadas

* **Runtime:** Node.js
* **Framework:** Express.js
* **Testing:** Jest + Supertest
* **CI/CD:** GitHub Actions
* **Hosting (Static):** GitHub Pages

---

## 📂 Estructura del Proyecto

El proyecto sigue una arquitectura modular para facilitar las pruebas y el mantenimiento:

```text
mi-proyecto/
├── src/
│   └── app.js           # Lógica de la aplicación y endpoints
├── tests/
│   └── app.test.js      # Pruebas unitarias e integración
├── .github/
│   └── workflows/
│       └── ci.yml       # Definición del Pipeline CI/CD
├── package.json         # Dependencias y scripts
└── README.md            # Documentación
