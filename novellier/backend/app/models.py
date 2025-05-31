from . import db # Assuming db is the SQLAlchemy instance from app/__init__.py
from werkzeug.security import generate_password_hash, check_password_hash
import datetime

class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(256), nullable=False) # Increased length for hash
    created_at = db.Column(db.DateTime, default=datetime.datetime.utcnow)

    novel_projects = db.relationship('NovelProject', backref='author', lazy=True)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return f'<User {self.username}>'

class NovelProject(db.Model):
    __tablename__ = 'novel_projects'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(150), nullable=False)
    genre = db.Column(db.String(50), nullable=True) # Genre can be optional initially
    # Consider adding a brief description/synopsis field later
    # description = db.Column(db.Text, nullable=True)
    created_at = db.Column(db.DateTime, default=datetime.datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.datetime.utcnow, onupdate=datetime.datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    # Basic version control: Store content as JSON or Text.
    # For MVP, a simple text field for the whole novel or latest draft.
    # More complex versioning can be built on this.
    # current_content_json = db.Column(db.JSON, nullable=True) # For structured content
    # current_content_text = db.Column(db.Text, nullable=True) # For simpler text editor content

    def __repr__(self):
        return f'<NovelProject {self.title}>'

# Future models to consider:
# class Chapter(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     title = db.Column(db.String(150))
#     order = db.Column(db.Integer)
#     content = db.Column(db.Text) # Or JSON for rich text
#     project_id = db.Column(db.Integer, db.ForeignKey('novel_projects.id'))
#     created_at = db.Column(db.DateTime, default=datetime.datetime.utcnow)
#     updated_at = db.Column(db.DateTime, default=datetime.datetime.utcnow, onupdate=datetime.datetime.utcnow)

# class Scene(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     title = db.Column(db.String(150), nullable=True)
#     content = db.Column(db.Text) # Or JSON
#     order = db.Column(db.Integer)
#     chapter_id = db.Column(db.Integer, db.ForeignKey('chapters.id'))
#     # AI analysis results could be linked here or in a separate table
#     # logos_analysis = db.Column(db.JSON, nullable=True)
#     # pathos_analysis = db.Column(db.JSON, nullable=True)
#     # ethos_analysis = db.Column(db.JSON, nullable=True)

# class VersionSnapshot(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     project_id = db.Column(db.Integer, db.ForeignKey('novel_projects.id'))
#     content_snapshot = db.Column(db.Text) # Or JSON
#     created_at = db.Column(db.DateTime, default=datetime.datetime.utcnow)
#     notes = db.Column(db.String(255), nullable=True) # User notes for this version
