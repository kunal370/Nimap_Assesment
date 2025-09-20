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
```
2️⃣ Create and activate virtual environment
```bash
python -m venv venv
# Activate (Windows)
venv\Scripts\activate
# Activate (Mac/Linux)
source venv/bin/activate
```
3️⃣ Install dependencies
```bash
pip install -r requirements.txt
```
4️⃣ Configure MySQL Database
```bash
Edit settings.py and update your DB settings:

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'nimap_db',
        'USER': 'root',
        'PASSWORD': 'your_password',
        'HOST': '127.0.0.1',
        'PORT': '3306',
    }
}
```
5️⃣ Run migrations
```bash
python manage.py makemigrations
python manage.py migrate
```
6️⃣ Create a superuser
```bash
python manage.py createsuperuser
```
7️⃣ Start development server
```bash
python manage.py runserver
```

Server runs at → http://127.0.0.1:8000/

🔑 API Endpoints
Clients

- GET /api/clients/ → List all clients

- POST /api/clients/ → Create a client

- GET /api/clients/{id}/ → Retrieve a client (with projects)

- PUT /api/clients/{id}/ → Update client

- DELETE /api/clients/{id}/ → Delete client

Projects

- POST /api/clients/{id}/projects/ → Create a project for a client & assign users

- GET /api/projects/ → List projects assigned to logged-in user

🧪 Example Requests
Create a Client
```bash
POST /api/clients/
{
  "client_name": "Company A"
}
```
Create a Project
```bash
POST /api/clients/17/projects/
{
  "project_name": "Project A",
  "users": [13, 14]
}
```
Get My Projects
```bash
GET /api/projects/
```
# 👨‍💻 Users in this test

- Ganesh → id = 14
- Neha → id = 15
- Rohit → id = 13
