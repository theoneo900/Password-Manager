import sqlite3
import os


def connect_to_database():
    if not os.path.exists('password-manager.db'):
        create_database()
    return sqlite3.connect('password-manager.db')


def create_database():
    # creates the two tables
    conn = sqlite3.connect('password-manager.db')
    cursor = conn.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        master_id INTEGER PRIMARY KEY AUTOINCREMENT,
        master_user TEXT NOT NULL UNIQUE,
        master_password TEXT NOT NULL
    )
    ''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS passwords (
        pass_id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER NOT NULL,
        website TEXT NOT NULL,
        website_url TEXT NOT NULL,
        username TEXT NOT NULL,
        password TEXT NOT NULL,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY (user_id) REFERENCES users(master_id)
    )
    ''')
    conn.commit()
    conn.close()


def add_new_user(master_user, master_password):
    # cursor.execute("INSERT INTO users (master_user, master_password) VALUES (?, ?)", (master_user, master_password))
    # this is sensitive to sql injection attacks use the line below instead
    conn = sqlite3.connect('password-manager.db')
    cursor = conn.cursor()
    cursor.execute("INSERT INTO users (master_user, master_password) VALUES (?, ?)", (master_user, master_password))
    conn.commit()
    conn.close()


def add_password(user_id, website, website_url, username, password):
    # adds a password with the according information to the accounts table
    conn = sqlite3.connect('password-manager.db')
    cursor = conn.cursor()
    cursor.execute('''INSERT INTO passwords (user_id, website, website_url, username, password) VALUES (?, ?, ?, ?, ?)
    ''', (user_id, website, website_url, username, password))
    conn.commit()
    conn.close()


def read_user(master_user):
    # finds a master user from the users table
    conn = sqlite3.connect('password-manager.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE master_user = ?", (master_user,))
    user_return_test = cursor.fetchone()
    conn.close()
    return user_return_test


def read_password(user_id, website):
    # finds a password for a specific website that you want to log into
    conn = sqlite3.connect('password-manager.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM passwords WHERE user_id = ? AND website = ?", (user_id, website))
    password_return_test = cursor.fetchone()
    conn.close()
    return password_return_test


def user_delete(master_user):
    conn = sqlite3.connect('password-manager.db')
    cursor = conn.cursor()
    cursor.execute("DELETE FROM users WHERE master_user = ? ", (master_user,))
    conn.commit()
    conn.close()


def password_delete(user_id, website):
    conn = sqlite3.connect('password-manager.db')
    cursor = conn.cursor()
    cursor.execute("DELETE FROM passwords WHERE user_id = ? AND website = ?", (user_id, website))
    conn.commit()
    conn.close()


def get_user_id(master_user, master_password):
    conn = connect_to_database()
    cursor = conn.cursor()

    cursor.execute('''
    SELECT master_id FROM users WHERE master_user = ? AND master_password = ?
    ''', (master_user, master_password))

    user_id = cursor.fetchone()
    conn.close()

    if user_id:
        return user_id[0]
    else:
        return None


def authenticate_user(master_user, master_password):
    user_id = get_user_id(master_user, master_password)
    if user_id:
        return user_id
    else:
        return None


# establish the connection with the database
# conn = sqlite3.connect('password-manager.db')
# cursor = conn.cursor()

# check if database file exists and if not creates one
# if not os.path.exists('password-manager.db'):
#     create_database()
# create_database()

# first test adding a user
# add_new_user("test2", "password2")
# answer = read_user("test2")

# second test adding a password (the functions handle the connection comment out the establish connection with the database)
# add_password(1, "test", "www.test.com", "Mars", 'pass')
# answer = read_password(4, "google")

# third test get user id (the functions handle the connection comment out the establish connection with the database)
# answer = get_user_id('test3', 'password')

# fourth test authenticate a user (the functions handle the connection comment out the establish connection with the database)
# answer = authenticate_user("test2", "password2")

# fifth test removing a password
# password_delete(3, "test")
# answer = read_password("3", "test")

# sixth test user delete
# user_delete("test2")
# answer = read_user("test2")

# print(answer)

# close the connection with the database
# conn.commit()
# conn.close()
