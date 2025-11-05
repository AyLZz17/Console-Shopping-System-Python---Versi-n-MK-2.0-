# 🛒 MK-2.01 — Sistema de Compras en Consola (Python)

Un **prototipo funcional** de sistema de compras ejecutado desde consola, desarrollado en **Python 3.10+**.  
Permite **gestionar inventarios**, **procesar compras**, **emitir recibos automáticos**, y **generar reportes de ventas**, todo con persistencia de datos local en `.json`.

---

## 📚 Índice

1. [Características principales](#-características-principales)  
2. [Notas de versión](#-notas-de-versión)  
3. [Instalación y ejecución](#-instalación-y-ejecución)  
4. [Estructura del proyecto](#-estructura-del-proyecto)  
5. [Limitaciones del prototipo](#-limitaciones-del-prototipo)  
6. [Versión](#-versión)  
7. [Bugs conocidos](#-bugs-conocidos)  
8. [Contribución](#-contribución)  
9. [Agradecimientos](#-agradecimientos)  
10. [Licencia](#-licencia)

---

## ✨ Características principales

### 🛒 Módulo de Compras
- Visualiza productos disponibles y precios.  
- Permite agregar al carrito, vaciarlo o pagar.  
- Calcula el total, descuenta inventario y genera un recibo automático.

### 💳 Procesamiento de Pagos
- Simula pagos con tarjetas virtuales.  
- Valida saldo y confirma transacciones.  
- Registra ventas exitosas y emite recibos.

### 🧾 Generación de Recibos
- Crea archivos `.txt` con el detalle completo de la compra.  
- Muestra el recibo en consola y lo guarda en `/Data/Recibos`.

### 📈 Sistema de Reportes
- Registra y consolida todas las ventas.  
- Genera estadísticas (producto más vendido, total de compras, ingresos acumulados).  
- Guarda los reportes en `/Data/Reportes`.

### 🏪 Panel de Trabajador
- Acceso restringido mediante autenticación.  
- Permite añadir o eliminar productos y generar reportes.  

### 💾 Persistencia de Datos
- Toda la información se conserva entre ejecuciones gracias a archivos `.json`.

---

## 📣 Notas de Versión — MK 2.01

- Requiere **Python 3.10 o superior** (uso de `match-case`).  
- Se añadió un **inicio de sesión** al ejecutar el codigo
- Se añadió un **panel exclusivo para trabajadores**.  
- **Reportes y recibos automáticos** con persistencia local.  
- **Gestión segura de credenciales** mediante `bcrypt`.  
- Archivos principales:
  - `/Data/Productos.json`  
  - `/Data/CredencialesTrabajadores.json`  
  - `/Data/DatosTarjetasPago.py`
- Se añadió un **inicio de sesión al ejecutar el programa**
- Se corrigió bug con rutas (ANTES: RUTAS ABSOLUTAS -> AHORA: RUTAS RELATIVAS)

---

## ⚙️ Instalación y ejecución

### 1️⃣ Requisitos previos
- Python **3.10 o superior**

### 2️⃣ Clonar el repositorio
```bash
git clone git clone https://github.com/AyLZz17/Console-Shopping-System-Python---Versi-n-MK-2.0-.git
cd Console-Shopping-System-Python---Versi-n-MK-2.0-/Sistem

```

### 3️⃣ Instalar dependencias
```bash
pip install bcrypt
pip install datetime
```

> Librerías como `os`, `sys`, `time` y `json` son estándar de Python.

### 4️⃣ Ejecutar el sistema
```bash
python main.py
```

---

## 📂 Estructura del proyecto

📦 MK-2.0  
 ┣ 📂 Sistem  
 ┃ ┣ 📂 Data  
 ┃ ┃ ┣ 📂 Recibos  
 ┃ ┃ ┣ 📂 Reportes  
 ┃ ┃ ┣ 📜 CredencialesTrabajadores.json  
 ┃ ┃ ┣ 📜 DatosTarjetasPago.py  
 ┃ ┃ ┗ 📜 Productos.json  
 ┃ ┣ 📂 functions  
 ┃ ┃ ┣ 📜 GestionProductos.py  
 ┃ ┃ ┣ 📜 mainPagos.py  
 ┃ ┃ ┣ 📜 MenuCompra.py  
 ┃ ┃ ┣ 📜 RecibosVenta.py  
 ┃ ┃ ┣ 📜 reportes.py  
 ┃ ┃ ┗ 📜 ValidacionesTrabajadores.py  
 ┃ ┣ 📂 interfaz  
 ┃ ┃ ┣ 📜 interfazMain.py  
 ┃ ┃ ┗ 📜 utilidades.py  
 ┃ ┗ 📜 main.py  

---

## ⚠️ Limitaciones del prototipo

- Persistencia solo en archivos locales (`.json` y `.txt`).  
- Sin integración con bases de datos o APIs externas.  
- Recibos y reportes solo en formato `.txt`.  
- Interfaz únicamente por consola.  
- Validaciones básicas y sin soporte multihilo.  
- No escalado para grandes volúmenes de datos.

---

## 📌 Versión

**MK-2.0** — Versión prototipo funcional del sistema de compras en consola.  
Incluye gestión de usuarios, inventario, ventas, reportes y recibos automáticos.

---

## 🪲 Bugs conocidos

- No se han identificado errores críticos.  
- En observación: persistencia en rutas personalizadas y compatibilidad entre sistemas operativos.

---

## 🤝 Contribución

¡Las contribuciones son bienvenidas!  
Si deseas mejorar el sistema o proponer nuevas funciones:

1. Realiza un **fork** del repositorio.  
2. Crea una rama con tu mejora (`git checkout -b feature/nueva-funcion`).  
3. Realiza los cambios y haz commit (`git commit -m 'Agrega nueva función'`).  
4. Sube los cambios (`git push origin feature/nueva-funcion`).  
5. Crea un **Pull Request** explicando tu aporte.

> Antes de enviar cambios mayores, abre un **issue** para discutir lo que te gustaría modificar.

---

## 🙌 Agradecimientos

Agradecimientos especiales a:
- **AYLZ**, creador y desarrollador principal del sistema.  
- La comunidad de desarrolladores de Python por las librerías y documentación.  
- GitHub por ofrecer una plataforma gratuita para alojar y compartir proyectos educativos.

---

## 🧾 Licencia

Este proyecto está bajo la **licencia MIT**.  
Puedes usar, modificar y redistribuir este software libremente, siempre que se mantenga la **atribución al autor original (AYLZ)**.
