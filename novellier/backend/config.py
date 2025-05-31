import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    # Expected environment variable: DATABASE_URL
    # Example: postgresql://postgres:postgres@db:5432/novellier_db
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'postgresql://postgres:postgres@db:5432/novellier_db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
