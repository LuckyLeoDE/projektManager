import sqlite3
import hashlib



db = sqlite3.connect("data/user.db")
cursor = db.cursor()


def add(username,rights,dataLastAdded,password:str,session_id,email):

    cursor.execute("""
        INSERT INTO users
        (username, rights, dataLastAdded, password, session_id, email)
        VALUES (?, ?, ?, ?, ?, ?)
    """, (
        username,
        rights,
        dataLastAdded,
        hashlib.sha256(password.encode()).hexdigest(),
        session_id,
        email
    ))

    db.commit()

def read(id):
    cursor.execute(
    "SELECT * FROM users WHERE id = ?",
    (id,)
)
    # (username, rights, dataLastAdded, password, session_id, email)

    return cursor.fetchone()


def verify(id,password:str):

    if read(id)[4] == hashlib.sha256(password.encode()).hexdigest():
        return True
    else:
        return False


def verify_And_Session(id,password,session_id):
    if verify(id,password) and read(id)[5] == session_id:
        return True
    else: 
        return False





# admin account
# add(username="Admin",rights=0,dataLastAdded="0.0.0.0",password="1234",session_id="e",email="leon@familie-brauer.net")

if __name__ == "__main__":
    print(verify(1,"1234"))
    print(verify_And_Session(1,"1234","e"))


db.close()

