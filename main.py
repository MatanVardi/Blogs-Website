import smtplib
from datetime import date
import werkzeug
from flask import Flask, abort, render_template, redirect, url_for, flash, request
from flask_bootstrap import Bootstrap5
from flask_ckeditor import CKEditor
from flask_gravatar import Gravatar
from flask_login import UserMixin, login_user, LoginManager, current_user, logout_user
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Text
from functools import wraps
from datetime import datetime, timedelta
from werkzeug.security import generate_password_hash, check_password_hash
# from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship
# Import your forms from the forms.py
from forms import CreatePostForm, RegisterForm, LoginForm, CommentForm
import os
import time
from dotenv import load_dotenv
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

load_dotenv()


app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('FLASK_KEY')
ckeditor = CKEditor(app)
Bootstrap5(app)

login_manager = LoginManager()
login_manager.init_app(app)


gravatar = Gravatar(app,
                    size=100,
                    rating='g',
                    default='retro',
                    force_default=False,
                    force_lower=False,
                    use_ssl=False,
                    base_url=None)

@login_manager.user_loader
def load_user(user_id):
    return db.get_or_404(User, user_id)


# CREATE DATABASE
class Base(DeclarativeBase):
    pass


app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get("DB_URI", "sqlite:///posts.db")
db = SQLAlchemy(model_class=Base)
db.init_app(app)


def admin_only(f):
    @wraps(f)
    def decorator_function(*args,**kwargs):
        # If id is not 1 then return abort with 403 error
        if (current_user.is_authenticated and current_user.id != 1) or (not current_user.is_authenticated):
            return abort(403)
        # Otherwise continue with the route function
        return f(*args, **kwargs)
    return decorator_function

# CONFIGURE TABLES
class BlogPost(db.Model):
    __tablename__ = "blog_posts"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    author = relationship("User", back_populates="posts")
    author_id: Mapped[int] = mapped_column(Integer, db.ForeignKey("users.id"))
    title: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    subtitle: Mapped[str] = mapped_column(String(250), nullable=False)
    date: Mapped[str] = mapped_column(String(250), nullable=False)
    body: Mapped[str] = mapped_column(Text, nullable=False)
    #author: Mapped[str] = mapped_column(String(250), nullable=False)
    img_url: Mapped[str] = mapped_column(String(250), nullable=False)
    # Create Foreign Key, "users.id" the users refers to the tablename of User.
    # Create reference to the User object. The "posts" refers to the posts property in the User class.
    comments = relationship("Comment", back_populates="parent_post")


class Comment(db.Model):
    __tablename__ = "comments"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    text: Mapped[str] = mapped_column(Text, nullable=False)
    author_id: Mapped[int] = mapped_column(Integer, db.ForeignKey("users.id"))
    comment_author = relationship("User", back_populates="comments")

    post_id: Mapped[int] = mapped_column(Integer, db.ForeignKey("blog_posts.id"))
    parent_post = relationship("BlogPost", back_populates = "comments")




class User(UserMixin, db.Model):
    __tablename__ = "users"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    email: Mapped[str] = mapped_column(String(100), unique=True)
    password: Mapped[str] = mapped_column(String(100))
    name: Mapped[str] = mapped_column(String(100))
    posts = relationship("BlogPost", back_populates="author")
    comments = relationship("Comment", back_populates="comment_author")

    def __init__(self, email, password, name):
        self.email: str = email
        self.password = password
        self.name = name

# def initialize_app():
#     with app.app_context():
#         # Create database tables
#         db.create_all()
#         new_user = User(
#             name="Yon",
#             email="yon@email.com",
#             password=123456,
#             posts=[
#                 BlogPost(
#                     title="Life of Cactus",
#                     subtitle="So Interesting",
#                     body="blah blah"
#                 )
#             ])
#
#         db.session.add(new_user)
#         db.session.commit()


with app.app_context():
    db.create_all()


# TODO: Use Werkzeug to hash the user's password when creating a new user.
@app.route('/register', methods=["GET", "POST"])
def register():
    form = RegisterForm()
    if request.method == "POST":
        if form.validate_on_submit():
            user_email = request.form.get("email")
            result = db.session.execute(db.select(User).where(User.email == user_email))
            user = result.scalar()
            if user:
                flash("You've already signed up with that email, log in instead!")
                return redirect(url_for("login"))

            user_password = request.form.get("password")
            user_name = request.form.get("name")
            hashed_password = werkzeug.security.generate_password_hash(user_password, method='pbkdf2:sha256',
                                                                       salt_length=8)
            print(user_email, hashed_password, user_name)
            new_user = User(email=user_email, password=hashed_password, name=user_name)
            db.session.add(new_user)
            db.session.commit()

            login_user(new_user)
            return redirect(url_for("get_all_posts"))

    return render_template("register.html", form=form, not_logged_in=current_user.is_authenticated)


# TODO: Retrieve a user from the database based on their email.
@app.route('/login', methods=["GET", "POST"])
def login():
    form = LoginForm()
    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")
        name = request.form.get("name")
        result = db.session.execute(db.select(User).where(User.email == email))
        user = result.scalar()
        if user and check_password_hash(user.password, password):
            login_user(user)
            # print(current_user.is_authenticated)
            return redirect(url_for('get_all_posts'))
        elif user == None:
            flash("That email doesn't exist, please try again")
            return redirect(url_for("login"))

        else:  # check_password_hash(user.password, password) == False:
            flash("Password incorrect, try again.")
            return redirect(url_for("login"))

    return render_template("login.html", form=form, not_logged_in=current_user.is_authenticated)


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('get_all_posts'))


@app.route('/')
def get_all_posts():
    result = db.session.execute(db.select(BlogPost))
    posts = result.scalars().all()
    if current_user.is_authenticated == True:
        return render_template("index.html", all_posts=posts, logged_in=current_user.is_authenticated,
                               user_id=current_user.id)
    else:
        return render_template("index.html", all_posts=posts, logged_in=current_user.is_authenticated)


# TODO: Allow logged-in users to comment on posts
@app.route("/post/<int:post_id>", methods=["GET", "POST"])
def show_post(post_id):
    requested_post = db.get_or_404(BlogPost, post_id)
    comment_form = CommentForm()
    if request.method == "POST":
        if current_user.is_authenticated:
            comment_data = comment_form.data.get("comment_text")
            new_comment = Comment(text=comment_data, author_id=current_user.id, post_id=requested_post.id)
            db.session.add(new_comment)
            db.session.commit()
            return redirect(url_for("show_post", post_id=post_id))
        else:
            flash("You need to log in or register to comment")
            return redirect(url_for("login"))

    # Handle GET request
    result = db.session.execute(db.select(Comment).filter(Comment.post_id == post_id).order_by(Comment.id))
    all_comments = result.scalars().all()

    # Extract author IDs
    author_ids = {comment.author_id for comment in all_comments}

    # Fetch user details for those author IDs
    user_query = db.select(User).filter(User.id.in_(author_ids))
    user_result = db.session.execute(user_query)
    users = user_result.scalars().all()

    # Create a mapping of author IDs to author names
    author_name_map = {user.id: user.name for user in users}

    return render_template(
        "post.html",
        post=requested_post,
        logged_in=current_user.is_authenticated,
        user_id=current_user.id if current_user.is_authenticated else None,
        form=comment_form,
        all_comments=all_comments,
        author_name_map=author_name_map,
        gravatar = gravatar
    )



# TODO: Use a decorator so only an admin user can create a new post

# @app.route("/new-post", methods=["GET", "POST"])
# @admin_only
# def add_new_post():
#     form = CreatePostForm()
#     if form.validate_on_submit():
#         new_post = BlogPost(
#             title=form.title.data,
#             subtitle=form.subtitle.data,
#             body=form.body.data,
#             img_url=form.img_url.data,
#             author=str(current_user.name),
#             date=date.today().strftime("%B %d, %Y")
#         )
#         db.session.add(new_post)
#         db.session.commit()
#         return redirect(url_for("get_all_posts"))
#     return render_template("make-post.html", form=form, logged_in=current_user.is_authenticated)

@app.route("/new-post", methods=["GET", "POST"])
@admin_only
def add_new_post():
    form = CreatePostForm()
    if form.validate_on_submit():
        new_post = BlogPost(
            title=form.title.data,
            subtitle=form.subtitle.data,
            body=form.body.data,
            img_url=form.img_url.data,
            author=current_user,
            date=date.today().strftime("%B %d, %Y")
        )
        db.session.add(new_post)
        db.session.commit()
        return redirect(url_for("get_all_posts"))
    return render_template("make-post.html", form=form, current_user=current_user)


# TODO: Use a decorator so only an admin user can edit a post

@app.route("/edit-post/<int:post_id>", methods=["GET", "POST"])
@admin_only
def edit_post(post_id):
    post = db.get_or_404(BlogPost, post_id)
    edit_form = CreatePostForm(
        title=post.title,
        subtitle=post.subtitle,
        img_url=post.img_url,
        author=str(current_user.name),
        body=post.body
    )
    if edit_form.validate_on_submit():
        post.title = edit_form.title.data
        post.subtitle = edit_form.subtitle.data
        post.img_url = edit_form.img_url.data
        post.author = str(current_user.name)
        post.body = edit_form.body.data
        db.session.commit()
        return redirect(url_for("show_post", post_id=post.id, logged_in=current_user.is_authenticated))
    return render_template("make-post.html", form=edit_form, is_edit=True, logged_in=current_user.is_authenticated)


# TODO: Use a decorator so only an admin user can delete a post

@app.route("/delete/<int:post_id>")
@admin_only
def delete_post(post_id):
    post_to_delete = db.get_or_404(BlogPost, post_id)
    db.session.delete(post_to_delete)
    db.session.commit()
    return redirect(url_for('get_all_posts'))


@app.route("/about")
def about():
    return render_template("about.html", logged_in=current_user.is_authenticated)



MAIL_ADDRESS = os.environ.get("EMAIL_KEY")
MAIL_APP_PW = os.environ.get("PASSWORD_KEY")
email_data = {
    "count": 0,
    "last_reset": datetime.utcnow()
}

# Time interval for reset
reset_interval = timedelta(hours=2)

@app.route("/contact", methods=["GET", "POST"])
def contact():
    global email_data
    current_sended_emails = email_data['count']
    last_reset = email_data['last_reset']

    if datetime.utcnow() - last_reset > reset_interval:
        # Reset count if the interval has passed
        current_sended_emails = 0
        last_reset = datetime.utcnow()
        email_data['count'] = current_sended_emails
        email_data['last_reset'] = last_reset

    if request.method == "POST":
        data = request.form
        if current_sended_emails >= 2:
            return render_template("contact.html", failed_to_send=True, logged_in=current_user.is_authenticated)

        send_email(data["name"], data["email"], data["phone"], data["message"])
        current_sended_emails += 1
        email_data['count'] = current_sended_emails

        return render_template("contact.html", msg_sent=True)

    return render_template("contact.html", msg_sent=False, logged_in=current_user.is_authenticated)

# def send_email(name, email, phone, message):
#     email_message = f"Subject:New Message\n\nName: {name}\nEmail: {email}\nPhone: {phone}\nMessage:{message}"
#     with smtplib.SMTP("smtp.office365.com") as connection:
#         connection.starttls()
#         connection.login(MAIL_ADDRESS, MAIL_APP_PW)
#         connection.sendmail(MAIL_ADDRESS, MAIL_APP_PW, email_message)

def send_email(name, sender_email, phone, message):
    # Create the email message
    email_message = MIMEMultipart()
    email_message['From'] = MAIL_ADDRESS  # Your email address
    email_message['To'] = MAIL_ADDRESS  # Recipient's email address
    email_message['Subject'] = 'New Message from Contact Form'

    # Create the body of the email
    body = f"Name: {name}\nEmail: {sender_email}\nPhone: {phone}\nMessage: {message}"
    email_message.attach(MIMEText(body, 'plain'))

    try:
        # Set up the SMTP server connection
        with smtplib.SMTP("smtp.office365.com", 587) as connection:
            connection.starttls()  # Upgrade the connection to a secure encrypted SSL/TLS connection
            connection.login(MAIL_ADDRESS, MAIL_APP_PW)  # Authenticate with your credentials
            connection.sendmail(MAIL_ADDRESS, MAIL_ADDRESS, email_message.as_string())  # Send the email
        print("Email sent successfully!")
    except Exception as e:
        print(f"Failed to send email. Error: {e}")





if __name__ == "__main__":
    app.run(debug=True)


