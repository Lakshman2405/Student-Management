# 🎓 Student Management System

A full-featured, Django-based web application designed to streamline the management of student records, administrative data, and user interactions. This project demonstrates core web development principles and a practical implementation of the Django framework.

![Django](https://img.shields.io/badge/Django-5.2.1-092E20?style=for-the-badge&logo=django)
![Python](https://img.shields.io/badge/Python-3.13-3776AB?style=for-the-badge&logo=python)
![SQLite](https://img.shields.io/badge/SQLite-07405E?style=for-the-badge&logo=sqlite&logoColor=white)
![Git](https://img.shields.io/badge/Git-F05032?style=for-the-badge&logo=git&logoColor=white)

![Student Management System](https://img.shields.io/badge/Student-Management%20System-blue?style=for-the-badge)
![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)

## ✨ Features

- **📝 CRUD Operations**: Fully Create, Read, Update, and Delete student records through an intuitive interface.
- **👨‍💻 Admin Dashboard**: Leverage Django's powerful built-in admin site for advanced data management.
- **🎨 Responsive UI**: Clean and functional templates for a seamless user experience.
- **🗄️ Database Management**: Utilizes Django ORM with SQLite for robust data handling and queries.
- **🔐 Secure Architecture**: Built on Django's secure, out-of-the-box framework.

## 🛠️ Tech Stack

- **Backend Framework:** Django 5.2.1
- **Programming Language:** Python 3.13
- **Database:** SQLite
- **Frontend:** HTML, CSS (Django Templates)
- **Version Control:** Git & GitHub

## 📦 Installation & Setup

Follow these steps to get the project running on your local machine.

### Prerequisites
Make sure you have the following installed:
- Python (3.8 or higher)
- pip (Python package installer)
- Git

### 1. Clone the Repository
```bash
git clone https://github.com/Lakshman2405/Student-Management.git
cd Student-Management
```
### 2. Create a Virtual Environment (Recommended)
```bash
python -m venv venv
# Activate the virtual environment
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```
### 4. Apply Database Migrations
```bash
python manage.py migrate
```
### 5. Create a Superuser (To access the Admin Panel)
```bash
python manage.py createsuperuser
```
Follow the prompts to create an admin account.
### 6. Run the Development Server
```bash
python manage.py runserver
```
### 7. Open Your Browser
Navigate to
```bash
http://127.0.0.1:8000/
```
to view the application.
Access the admin panel at
```bash
http://127.0.0.1:8000/admin/
```
and log in with your superuser credentials.

## 📖 Usage
- **View Students:** Navigate to the homepage to see a list of all students.
- **Add a New Student:** Use the provided form to add new student records to the system.
- **Edit/Delete Records:** Update existing information or remove records as needed.
- **Admin Access:** Use the /admin endpoint for a powerful backend interface to manage all data.

## 🗂️ Project Structure
```text
Student-Management/
├── AdminOfficer/                 # Main Django project directory (settings, configs)
│   ├── __init__.py
│   ├── settings.py              # Project settings
│   ├── urls.py                  # Main URL router
│   ├── asgi.py
│   └── wsgi.py
├── MedicalStudent/              # Django application for core functionality
│   ├── migrations/              # Database migration files
│   ├── templates/               # HTML templates
│   │   ├── manage.html
│   │   ├── edit.html
│   │   └── delete.html
│   ├── __init__.py
│   ├── admin.py                 # Admin site configuration
│   ├── apps.py
│   ├── forms.py                 # Django forms for data input
│   ├── models.py                # Database models (e.g., Student model)
│   ├── tests.py
│   ├── urls.py                  # App-specific URLs
│   └── views.py                 # Application logic and view functions
├── .gitignore                   # Files to be ignored by Git
├── manage.py                    # Django's command-line utility
└── requirements.txt             # Project dependencies
```

# HOW TO CLEAN YOUR DJANGO PROJECT BEFORE PUSHING TO GITHUB

## 🚨 CRITICAL: Never upload these files to GitHub:

- **db.sqlite3** (Contains all your sensitive data)
- ***.pyc files** (Temporary compiled files)
- __pycache__/ folders (Cache directories)
- Secret Keys(In **settings.py**)

### Step-by-Step Cleaning Procedure:
1.**Create/Update your .gitignore file** in your project's root folder (where manage.py is) with the following content:
  ```bash
  # Django
  *.sqlite3
  *.pyc
  __pycache__/
  db.sqlite3
  
  # Environment variables (where secrets are stored)
  .env
  .env.local
  env/
  
  # IDE
  .vscode/
  .idea/
  
  # OS
  Thumbs.db
  .DS_Store
  
  # Django secret key (if in separate file)
  secret_key.txt
  ```

2. **Remove existing tracked files** from Git's staging area:
  ```bash
  git rm -r --cached .
  ```

3. **Re-add all files** (.gitignore will now work correctly):
  ```bash
  git add .
  ```
4. **Check status** to confirm unwanted files are gone:
  ```bash
   git status
  ```
5. **Commit and push** your clean project:
  ```bash
  git commit -m "Initial commit: Clean project setup"
  git push origin main
  ```

### FINAL STEPS TO COMPLETE YOUR GITHUB SETUP
1.  **Create the `requirements.txt` file** (if you haven't):
    ```bash
    pip freeze > requirements.txt
    ```

2.  **Add, commit, and push** the README and all changes:
    ```bash
    git add README.md
    git add requirements.txt
    git commit -m "Add professional README and requirements file"
    git push origin main
    ```

Your GitHub repository now has a clean codebase and a professional presentation that will impress anyone who sees it! This is perfect for your internship applications.


