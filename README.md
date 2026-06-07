A full-stack blog application built with Flask, featuring user authentication, blog post creation, commenting, and contact form functionality.

Features

User registration and login with hashed passwords
Admin-only controls for creating, editing, and deleting posts
Rich text blog post editor powered by CKEditor
Commenting system with Gravatar profile images
Contact form with email sending via SMTP
Rate limiting on contact form (max 2 emails per 2 hours)
Responsive design using Bootstrap 5


Tech Stack

Backend: Python, Flask
Database: SQLite (development) / configurable via environment variable
ORM: SQLAlchemy
Auth: Flask-Login, Werkzeug password hashing
Forms: Flask-WTF, WTForms
Editor: Flask-CKEditor
Email: smtplib (Office365 SMTP)
UI: Bootstrap 5, Font Awesome, Google Fonts


Project Structure
├── main.py               # Main Flask app, routes, and models
├── forms.py              # WTForms form definitions
├── templates/
│   ├── header.html       # Navbar and head section
│   ├── footer.html       # Footer and scripts
│   ├── index.html        # Homepage - lists all posts
│   ├── post.html         # Individual post with comments
│   ├── make-post.html    # Create / edit post form
│   ├── register.html     # User registration page
│   ├── login.html        # User login page
│   ├── about.html        # About page
│   └── contact.html      # Contact form page
├── static/
│   ├── css/styles.css    # Custom styles
│   ├── js/scripts.js     # Custom scripts
│   └── assets/           # Images and favicon
└── .env                  # Environment variables (not committed)
