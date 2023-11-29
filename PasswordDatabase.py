
import hashlib
import os
class PasswordDatabase:
    def __init__(self):
     self.data = dict()

    def hash_password(self, password):
     pwd_bytes = password.encode("utf-8")
     salt = os.urandom(32)
     hashed_password = hashlib.pbkdf2_hmac('sha512', pwd_bytes, salt, 100000)
     self.store_hashed_password(hashed_password, salt, password)
     return salt, hashed_password
    
    def store_hashed_password(self, hashed_password, salt, password):
     if password not in self.data:
        self.data[password] = (salt,hashed_password)
     
    
    
