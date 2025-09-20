# Django REST API – Machine Test

This project is a Django REST Framework–based API for managing **Users, Clients, and Projects**.  
It demonstrates CRUD operations, relationships, authentication, and MySQL integration.

---

## 📌 Features
- Register, fetch, update, and delete **Clients**
- Create **Projects** for a client and assign multiple users
- Retrieve projects assigned to the **logged-in user**
- Uses **MySQL** as the database

---

## 🏗️ Tech Stack
- **Python 3.x**
- **Django 5.x**
- **Django REST Framework (DRF)**
- **MySQL**

---

## ⚙️ Database Design
- **User** (Django’s built-in User model)  
- **Client** → created by a User  
- **Project** → belongs to one Client, can be assigned to multiple Users  

**Relations:**
- One Client → Many Projects  
- One Project → Many Users  

---

## 🚀 How to Run the Project

### 1️⃣ Clone the repository
```bash
git clone https://github.com/<your-username>/nimap-rest-api.git
cd nimap-rest-api
