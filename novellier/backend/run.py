from app import create_app, db
# Import models here to ensure they are known to Flask-Migrate
from app.models import User, NovelProject # Add this line

app = create_app()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
