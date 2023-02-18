import hashlib
import os


def create_password(password):
    salt = os.urandom(32)  # Новая соль для данного пользователя
    key = hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), salt, 390000)

    key_in_db = key + salt
    return key_in_db


def check_password(key_from_db, password_for_check):
    key = key_from_db[:32]  # Получение соли
    salt = key_from_db[32:]  # Получение правильного ключа
    password = password_for_check
    new_key = hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), salt, 390000)
    if key != new_key:  # Ключи не совпадают, следовательно, пароли не совпадают
        return False
    else:
        return True







