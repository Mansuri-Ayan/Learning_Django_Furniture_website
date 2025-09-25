# Django Furniture Website

A Django-based furniture store web application built as a learning project.  
This repository contains the `feature` branch version of the project.  

## Table of Contents

- [Features](#features)  
- [Tech Stack](#tech-stack)  
- [Project Structure](#project-structure)  
- [Setup & Installation](#setup--installation)  
- [Running the Project](#running-the-project)  
- [Database & Migrations](#database--migrations)  
- [Static Files & Templates](#static-files--templates)  
- [Contributing](#contributing)  
- [License](#license)  

---

## Features

- Display furniture catalog  
- Add, edit, delete products (CRUD operations)  
- Categories, filtering, and search  
- Basic user interface with static pages  
- Template inheritance and reusable components  

(Add or remove features as per your implementation.)

---

## Tech Stack

- **Backend:** Python, Django  
- **Frontend:** HTML, CSS (you may use frameworks like Bootstrap if included)  
- **Database:** SQLite (default for Django)  
- **Others:** Django Templates, static files handling  

---

## Project Structure

```

MyProject/
├── Myapp/
│   ├── migrations/
│   ├── templates/
│   ├── static/
│   └── views, models, etc.
├── static/
├── template/
├── manage.py
└── .gitignore

````

- `Myapp/` — The main Django app with models, views, urls, templates, etc.  
- `static/` — Global static files  
- `template/` — Shared templates  
- `manage.py` — Django’s command-line utility  
- `.gitignore` — Files and directories excluded from version control  

---

## Setup & Installation

1. **Clone the repository (feature branch):**  
   ```bash
   git clone -b feature https://github.com/Mansuri-Ayan/Learning_Django_Furniture_website.git
   cd Learning_Django_Furniture_website
````

2. **Create a virtual environment & activate it:**

   ```bash
   python -m venv venv
   # On Windows
   venv\Scripts\activate
   # On macOS / Linux
   source venv/bin/activate
   ```

3. **Install dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

   > *If you don’t have a `requirements.txt`, generate one:*
   >
   > ```bash
   > pip freeze > requirements.txt
   > ```

---

## Running the Project

```bash
python manage.py runserver
```

Then open your browser and go to `http://127.0.0.1:8000/` (or the port Django prints).

---

## Database & Migrations

1. **Make migrations:**

   ```bash
   python manage.py makemigrations
   ```

2. **Apply migrations:**

   ```bash
   python manage.py migrate
   ```

3. **Create a superuser (for admin panel):**

   ```bash
   python manage.py createsuperuser
   ```

---

## Static Files & Templates

* Add your CSS, JavaScript, images in the `static/` folder of your app or global static directory.
* Use `{% load static %}` in templates to reference static files.
* Templates are organized (e.g. base templates, pages inside `template/` or `Myapp/templates/`).

---

## Contributing

Feel free to contribute!

1. Fork the repository
2. Create a new branch (e.g. `feature/add-cart`)
3. Make your changes & commit
4. Push to your fork
5. Open a Pull Request

Please follow code style, write clear commit messages, and ensure things work before submitting.

---

## License

This project is released under the **MIT License**.
(You can choose a different license, e.g. Apache 2.0, if you prefer.)

---

## Contact

If you have any questions or suggestions, feel free to open an issue or reach out.

---

> *“Learning by building”* — This project is a work in progress, welcomes improvements and feature additions 😀

```
