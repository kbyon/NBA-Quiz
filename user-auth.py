import json
import os
import hashlib

class UserAuthentication:
    def __init__(self, user_file='users.json'):
        """
        [Authentication] Initialize user authentication system
        
        Args:
            user_file (str): Path to the JSON file storing user credentials
        """
        # [Files] Using file for user storage
        # [Lists and Dictionaries] Using dictionary to store user credentials
        self.user_file = user_file
        self.users = self.load_users()

    def load_users(self):
        """
        [Authentication] Load existing users from file
        [Files] Reading user data from JSON file
        
        Returns:
            dict: Dictionary of users
        """
        # [Loops] Potentially using loops in file reading
        if not os.path.exists(self.user_file):
            return {}
        
        with open(self.user_file, 'r') as f:
            return json.load(f)

    def authenticate_user(self, username, password):
        """
        [Authentication] Authenticate a user
        
        Args:
            username (str): Username
            password (str): Password
        
        Returns:
            bool: True if authentication successful, False otherwise
        """
        # [Loops] Implicit loops in dictionary checking
        if username not in self.users:
            return False
        
        return self.users[username] == self.hash_password(password)
