from flask import Blueprint, jsonify, request
from .models import User, db # Assuming User and db are in models.py
from werkzeug.security import check_password_hash # Already in User model but good for direct use if needed

bp = Blueprint('main', __name__, url_prefix='/api')

@bp.route('/')
def index():
    return jsonify(message="Welcome to Novellier API!")

@bp.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    if not data or not data.get('username') or not data.get('email') or not data.get('password'):
        return jsonify(message="Username, email, and password are required."), 400

    if User.query.filter_by(username=data['username']).first():
        return jsonify(message="Username already exists."), 409 # 409 Conflict

    if User.query.filter_by(email=data['email']).first():
        return jsonify(message="Email address already registered."), 409 # 409 Conflict

    user = User(username=data['username'], email=data['email'])
    user.set_password(data['password'])
    db.session.add(user)
    db.session.commit()

    return jsonify(message="User registered successfully."), 201

@bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    if not data or not data.get('username') or not data.get('password'):
        return jsonify(message="Username and password are required."), 400

    user = User.query.filter_by(username=data['username']).first()

    if user is None or not user.check_password(data['password']):
        return jsonify(message="Invalid username or password."), 401 # 401 Unauthorized

    # Here you would typically generate a token (e.g., JWT) and return it.
    # For now, just a success message.
    # token = generate_auth_token(user.id) # Placeholder for token generation
    return jsonify(message="Login successful.", user_id=user.id), 200

# Placeholder for a protected route - to be implemented with token auth
# @bp.route('/protected')
# @token_required # Placeholder for a decorator that checks the token
# def protected_route(current_user):
#     return jsonify(message=f"Hello, {current_user.username}! This is a protected area.")
