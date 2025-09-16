# 📇 Contact Keeper

**Contact Keeper** es una aplicación de línea de comandos (CLI) escrita en **Python** que permite gestionar contactos de forma sencilla.  
Utiliza **JSON** para almacenamiento persistente y **Regex** para validar y buscar información.  

---

## ✨ Funcionalidades

- ➕ Agregar un nuevo contacto (nombre, teléfono, email, etc.)  
- ✏️ Modificar un contacto existente  
- 🔍 Buscar contactos por nombre o email usando expresiones regulares  
- 📋 Listar todos los contactos  
- ❌ Borrar contactos  
- 💾 Almacenamiento persistente en archivo JSON  

---

## 🛠 Requisitos

- Python 3.8+  

No requiere librerías externas, solo módulos estándar de Python (`json`, `re`, `os`).  

---

## 🚀 Uso

Ejecutar el programa desde terminal:

> bash
> python contact_keeper.py

Se listarán los contactos actuales y se mostrará un menú interactivo con las opciones disponibles:
A. Agregar contacto
M. Modificar contacto
S. Buscar contacto
D. Eliminar contacto
E. Salir

---

## 📂 Estructura del proyecto

📦 contact_keeper\
 ┣ 📜 contact_keeper.py\
 ┣ 📜 contacts.json\
 ┣ 📜 README-es.md\
 ┗ 📜 README-en.md

 ---

 ## 📖 Ejemplo de contacto guardado (JSON)

{
  "name": "Juan Pérez",
  "phone": "+59812345678",
  "email": "juan.perez@example.com"
}

---

## 🤝 Contribuciones

Este es un proyecto de práctica personal, pero sugerencias y mejoras son bienvenidas.

---

## 👨‍💻 Autor : Rodrigo Portugal
