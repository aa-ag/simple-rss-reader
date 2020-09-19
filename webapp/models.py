from webapp import app, db, login
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime
from flask_login import UserMixin

@login.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(db.Model, UserMixin):
    # user information
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), nullable=False, unique=True)
    email = db.Column(db.String(150), nullable=False, unique=True)
    password = db.Column(db.String(10), nullable=False)

    # user's feed(s) / data
    # feed = db.relationship('Post', backref='subscribed', lazy=True)

    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = self.hash_password(password)
        # self.feed = feed

    def hash_password(self, password):
        self.pw_hash = generate_password_hash(password)
        return self.pw_hash

class Feed(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(300))
    link = db.Column(db.String(300))
    date_created = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    # TO DO: if not linking feeds to users, a user needs to be linked to their feeds

    def __init__(self, title, link, date_created):
        self.title = title
        self.link = link
        self.date_created = datetime
