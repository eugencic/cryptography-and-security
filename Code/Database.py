import sqlite3

tokens = {}

con = sqlite3.connect('../users.db', check_same_thread=False)
cur = con.cursor()


def create_initial_db_resources():
    cur.execute(
        "CREATE TABLE IF NOT EXISTS Users(email varchar unique, password varchar, user_type varchar, totp varchar)")
    cur.execute("SELECT * FROM Users")
    print(cur.fetchall())


def create_user(email, password, user_type, totp):
    cur.execute("INSERT INTO Users(email, password, user_type, totp) values(:email, :password, :user_type, :totp)", {
        'email': email,
        'password': password,
        'user_type': user_type,
        'totp': totp
    })
    print("Created user successfully")
    con.commit()


def get_user(email):
    try:
        cur.execute("SELECT email, password, user_type, totp FROM Users WHERE email = :email", {
            'email': email
        })
        print("User found successfully")
        return cur.fetchall()
    except Exception as e:
        print("Exception occurred while checking for the user")
        raise e
