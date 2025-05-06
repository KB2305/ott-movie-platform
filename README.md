# ott-movie-platform
# 🎬 BingeBox

**BingeBox** is a Django-based OTT (Over-The-Top) streaming platform that allows users to browse, search, and stream movies. It includes features like genre and language-based filtering, dynamic movie rendering, user authentication with OTP, and personal features like a "Watch Later" list and a suggestion form.

## 🚀 Features

- 🔍 **Search Movies** by title
- 🎭 **Filter by Genre** and 🌐 **Language**
- 📽️ **Dynamic Movie Rendering**
- 🔐 **User Authentication** (Login & Registration with OTP)
- 🕒 **Watch Later List**
- 📝 **"You Ask, We Provide"** movie request form *(feature in development)*
- 🧑‍💼 Admin panel for managing movies and content
- 📱 Responsive frontend design

## 📁 Project Structure

ottproject/
├── manage.py
├── bingebox/ # Project settings
├── movies/ # Main app: models, views, forms, URLs
├── templates/ # HTML templates
├── static/ # posters,movies
└── requirements.txt


---

## ⚙️ Installation & Setup

Follow these steps to set up the project locally:

### 1. Clone the repository
```bash
[https://github.com/KB2305/ott-movie-platform)]
cd bingebox

### 2. Create & Active Virtual Environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

### 3. Install Dependencies

pip install -r requirements.txt


### 4. Apply migrations
python manage.py makemigrations
python manage.py migrate


### 5. Create a superuser (optional, for admin access)
python manage.py createsuperuser

### 6. Run the development server
python manage.py runserver


🧪 Known Issues / To Do
❌ "Watch Later" not saving to DB — under development

❌ "You Ask, We Provide" form backend logic not implemented yet

✅ OTP-based authentication using session tokens is implemented


🛠 Tech Stack
Backend: Django (Python)

Frontend: HTML, CSS, Bootstrap

Database: SQLite (default) or PostgreSQL (recommended for production)

📜 License
This project is licensed under the MIT License.



🙌 Acknowledgements
Django — Python Web Framework

Bootstrap — UI Components

Open-source tools and communities that inspired this project
