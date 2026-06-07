# Matan's Blog

A full-stack blog application built with Flask, featuring user 
authentication, blog post creation, commenting, and contact form.

## Features
- User registration and login with hashed passwords
- Admin-only controls for creating, editing, and deleting posts
- Rich text editor powered by CKEditor
- Commenting system with Gravatar profile images
- Contact form with email sending via SMTP
- Rate limiting on contact form (max 2 emails per 2 hours)
- Responsive design using Bootstrap 5

## Tech Stack
- **Backend:** Python, Flask
- **Database:** SQLite / configurable via DB_URI
- **ORM:** SQLAlchemy
- **Auth:** Flask-Login, Werkzeug
- **Forms:** Flask-WTF, WTForms
- **Editor:** Flask-CKEditor
- **Email:** smtplib (Office365 SMTP)
- **UI:** Bootstrap 5, Font Awesome, Google Fonts

## Setup
\`\`\`bash
git clone <your-repo-url>
cd your-project
python -m venv venv
source venv/bin/activate
pip install flask flask-wtf flask-login flask-sqlalchemy \
  flask-bootstrap flask-ckeditor flask-gravatar werkzeug python-dotenv
python main.py
\`\`\`
