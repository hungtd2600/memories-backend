from flask import Blueprint, request, jsonify
from app.models.models import DatabaseManager
from app.auth.auth import generate_token, verify_login, verify_token

main = Blueprint('main', __name__)

db = DatabaseManager(db_path='database/memories.db')

@main.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')
    if not username or not password:
        return jsonify({'message': 'Missing username or password'}), 400
    if verify_login(username, password):
        token = generate_token(username)
        return jsonify({'message': 'Login successful', 'token': token}), 200
@main.route('/memories', methods=['GET'])
def get_memories():
    token = request.headers.get('Authorization')
    if not token:
        return jsonify({'message': 'Token is missing'}), 401
    if token.startswith('Bearer '):
        token = token.split(' ')[1]
    username = verify_token(token)
    if not username:
        return jsonify({'message': 'Invalid or expired token'}), 401
    memories = db.get_all_memories()
    return jsonify({'memories': memories}), 200

@main.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')
    if not username or not password:
        return jsonify({'message': 'Missing username or password'}), 400
    if db.add_user(username, password):
        return jsonify({'message': 'User registered successfully'}), 201