from flask import Flask, request, jsonify
import os

app = Flask(__name__)

# In-memory database
users = []

# Generate a unique ID
def get_next_id():
    return max([user['id'] for user in users], default=0) + 1

# Create a User
@app.route('/users', methods=['POST'])
def create_user():
    data = request.get_json()
    if not data or 'name' not in data or 'email' not in data or 'age' not in data:
        return jsonify({'error': 'Missing required fields'}), 400
    user = {'id': get_next_id(), 'name': data['name'], 'email': data['email'], 'age': data['age']}
    users.append(user)
    return jsonify(user), 201

# Retrieve All Users
@app.route('/users', methods=['GET'])
def get_users():
    return jsonify(users)

# Retrieve a Single User
@app.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = next((u for u in users if u['id'] == user_id), None)
    if user is None:
        return jsonify({'error': 'User not found'}), 404
    return jsonify(user)

# Update a User
@app.route('/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    user = next((u for u in users if u['id'] == user_id), None)
    if user is None:
        return jsonify({'error': 'User not found'}), 404
    data = request.get_json()
    user.update({key: data[key] for key in data if key in user})
    return jsonify(user)

# Delete a User
@app.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    global users
    users = [u for u in users if u['id'] != user_id]
    return jsonify({'message': 'User deleted'}), 200

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))  # Use PORT from environment, default to 5000
    app.run(host='0.0.0.0', port=port)
