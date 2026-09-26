from flask import Flask ,render_template 

import sqlite3 

app = Flask(__name__)






@app.route("/")
def main():
    return "klappt"




app.run(host="0.0.0.0",port=5000)