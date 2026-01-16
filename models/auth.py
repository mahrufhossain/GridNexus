import hashlib
import json
import os

class User:
    def __init__(self, email, password, node_id):
        self.email = email
        self.password_hash = self._hash_password(password)
        self.node_id = node_id

    def _hash_password(self, password):
        # SHA-256 converts the password into a 64-character hex string
        return hashlib.sha256(password.encode()).hexdigest()

    def to_dict(self):
        return {
            "email": self.email,
            "password_hash": self.password_hash,
            "node_id": self.node_id
        }


USER_DB = "data/users.json"

def register_user(email, password, node_id):
    """Saves a new user with a hashed password."""
    new_user = User(email, password, node_id)
    
    # Load existing or start new
    data = []
    if os.path.exists(USER_DB):
        with open(USER_DB, "r") as f:
            data = json.load(f)
    
    data.append(new_user.to_dict())
    
    with open(USER_DB, "w") as f:
        json.dump(data, f, indent=4)
    print(f"✅ User {email} registered.")

def authenticate(email, provided_password):
    """The 'Underneath' check: Hashes input and compares to database."""
    if not os.path.exists(USER_DB):
        return None
        
    with open(USER_DB, "r") as f:
        users = json.load(f)
        
    # Simple Hashing check
    attempt_hash = hashlib.sha256(provided_password.encode()).hexdigest()
    
    for user in users:
        if user['email'] == email and user['password_hash'] == attempt_hash:
            return user['node_id']  # Login success!
            
    return None  # Login failed