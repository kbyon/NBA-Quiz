import base64
from cryptography.fernet import Fernet

class EncryptionManager:
    def __init__(self):
        """
        [Encryption and Decryption] Initialize encryption manager
        Generate a key for symmetric encryption
        """
        # [Functions] Encryption methods
        self.key = Fernet.generate_key()
        self.cipher_suite = Fernet(self.key)

    def encrypt_message(self, message):
        """
        [Encryption and Decryption] Encrypt a message
        
        Args:
            message (str): Message to encrypt
        
        Returns:
            bytes: Encrypted message
        """
        # Ensure message is in bytes
        if isinstance(message, str):
            message = message.encode('utf-8')
        
        return self.cipher_suite.encrypt(message)

    def decrypt_message(self, encrypted_message):
        """
        [Encryption and Decryption] Decrypt an encrypted message
        
        Args:
            encrypted_message (bytes): Message to decrypt
        
        Returns:
            str: Decrypted message
        """
        return self.cipher_suite.decrypt(encrypted_message).decode('utf-8')
