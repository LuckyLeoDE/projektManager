import sqlite3
import hashlib
import random as ran


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

def int_to_string(value: int, x: int) -> str:
    binary = bin(value)[2:]

    # Auf ein Vielfaches von 8 auffüllen
    binary += "0" * ((8 - len(binary) % 8) % 8)

    # Binär in ASCII-Zeichen umwandeln
    string = ''.join(
        chr(int(binary[i:i+8], 2))
        for i in range(0, len(binary), 8)
    )

    # Auf genau x Zeichen auffüllen
    string = string.ljust(x, "\x00")

    return string[:x]


def session_id_gen(seed:int)->str:
    ran.seed(seed)
    
    return ran.randint(1,256**32)




# admin account
# add(username="Admin",rights=0,dataLastAdded="0.0.0.0",password="1234",session_id="e",email="leon@familie-brauer.net")

if __name__ == "__main__":
    print(verify(1,"1234"))
    print(verify_And_Session(1,"1234","e"))
    #print(session_id_gen(3))
    x = int_to_string(session_id_gen(3),32)
    print(len(x))
    print(x)


db.close()

