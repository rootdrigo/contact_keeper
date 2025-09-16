# 📇 Contact Keeper

**Contact Keeper** is a command-line (CLI) application written in **Python** that allows you to easily manage contacts.

It uses **JSON** for persistent storage and **Regex** for validating and searching information.

---

## ✨Features

- ➕ Add a new contact (name, phone, email, etc.)
- ✏️ Modify an existing contact
- 🔍 Search for contacts by name or email using regular expressions
- 📋 List all contacts
- ❌ Delete contacts
- 💾 Persistent storage in a JSON file

---

## 🛠 Requirements

- Python 3.8+

No external libraries required, only standard Python modules (`json`, `re`, `os`).

---

## 🚀 Usage

Run the program from the terminal:

> batch
> python contact_keeper.py

The current contacts will be listed and an interactive menu will appear with the available options:
A. Add contact
M. Modify contact
S. Search contact
D. Delete contact
E. Exit

---

## 📂 Project structure

📦 contact_keeper\
┣ 📜 contact_keeper.py\
┣ 📜 contacts.json\
┣ 📜 README-es.md\
┗ 📜 README-es.md

---

## 📖 Saved contact example (JSON)

{
"name": "John Doe",
"phone": "+59812345678",
"email": "john.doe@example.com"
}

---

## 🤝 Contributions

This is a personal practice project, but suggestions and improvements are welcome.

---

## 👨‍💻 Author: Rodrigo Portugal
