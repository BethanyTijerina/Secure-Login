import bcrypt
import json
import os

def hash_password(password):
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

def save_user(username, hased_password):
    users= {}
    if os.path.exists("users.json"):
        with open("users.json", "r") as file:
            users = json.load(file)
    users[username] = hash_password.decode('utf-8')
    with open("users.json", "w") as file:
        json.dump(users, file)

def signup():
    username = input("Create a username: ")
    password = input("Creat a password: ")
    hash_pass = hash_password(password)
    save_user(username, hash_pass)
    print("User registered successfully.")
    