# 🎬 BingeBox - OTT Streaming Platform

**BingeBox** is a Django-based OTT (Over-The-Top) streaming platform that allows users to browse, search, and stream movies. It includes features like genre and language-based filtering, dynamic movie rendering, user authentication with OTP, and personal features like a "Watch Later" list and a suggestion form.

---

## 🚀 Features

- 🔍 Search movies by title  
- 🎭 Filter by **genre** and 🌐 **language**  
- 📽️ Dynamic movie rendering  
- 🔐 OTP-based registration and login system  
- 📌 "Watch Later" feature  
- 📝 "You Ask, We Provide" movie request form (frontend only, backend not functional)  
- 🧑‍💼 Django admin panel for managing content  
- 📱 Responsive UI  

---

## 📁 Project Structure

```
ott-movie-platform/
├── manage.py
├── requirements.txt
├── db.sqlite3
├── ottProject/                 # Main Django project folder
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── asgi.py
├── home/                       # Django app
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   └── migrations/
├── templates/                  # HTML templates
│   ├── account.html
│   ├── ask_provide.html
│   ├── base.html
│   ├── genre_list.html
│   ├── home.html
│   ├── index.html
│   ├── moviepage.html
│   ├── movies.html
│   ├── otp.html
│   ├── watchlater.html
│   └── register.html
├── static/                     # Static files
│   ├── movies/                 # JavaScript, thumbnails, or support files related to movies
│   └── posters/                # Movie poster images
```

> ⚠️ **Important:** Make sure the `static/` folder includes both the `movies/` and `posters/` subfolders. These are used for displaying movie images and related assets.

---

## ⚙️ Installation & Setup

### 1. Clone the Repository

```bash
git clone https://github.com/KB2305/ott-movie-platform.git
cd ott-movie-platform
```

### 2. Create a Virtual Environment

- **Windows:**
  ```bash
  python -m venv venv
  venv\Scripts\activate
  ```

- **macOS/Linux:**
  ```bash
  python3 -m venv venv
  source venv/bin/activate
  ```

### 3. Install Dependencies

If a `requirements.txt` file exists:
```bash
pip install -r requirements.txt
```

Otherwise:
```bash
pip install django
pip install django-otp
```

### 4. Apply Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### 5. Create a Superuser

```bash
python manage.py createsuperuser
```

### 6. Run the Development Server

```bash
python manage.py runserver
```

Visit: [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

---

## 🔑 Admin Panel

Visit: [http://127.0.0.1:8000/admin](http://127.0.0.1:8000/admin)  
Use the superuser credentials created earlier.

---

## ⚠️ Known Issues / To-Do

- 🚧 "Watch Later" not connected to backend  
- 🚧 "You Ask, We Provide" form not functional  
- ✅ Movie filtering, streaming, and OTP login functional
-   Add two folders in static folder 1) Movies 2) poster and store accordingly
---

## 🧰 Tech Stack

- **Backend:** Django (Python)  
- **Frontend:** HTML, Bootstrap  
- **Database:** SQLite  

---

## 📄 License

This project is released under the **MIT License**. You can add a `LICENSE` file to reflect this.

---

## 🤝 Contributing

Contributions are welcome! Fork the repository and open a pull request to suggest improvements.

---

## 🙏 Acknowledgments

- Django Documentation  
- Bootstrap  
- Open Source Communities  
