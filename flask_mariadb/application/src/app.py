import os
import pymysql.cursors
from flask import Flask
from flask import jsonify

connection = pymysql.connect(host='database',
                             user=os.getenv('MYSQL_USER'),
                             password=os.getenv('MYSQL_PASSWORD'),
                             db='application_db',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)

app = Flask(__name__)


@app.route('/')
def hello():
    cur2 = connection.cursor()

    return f'Application /'

@app.route('/quadrado/<int:x>')
def quadrado(x):
   cur3 = connection.cursor()
   r = x**2
   return jsonify (r)


@app.route('/db')
def db():
    cur = connection.cursor()
    cur.execute("SELECT VERSION() AS db_version")

    version = cur.fetchone()

    return (f'Database /db<br />\n'
            f'Version of database: {version["db_version"]}')

