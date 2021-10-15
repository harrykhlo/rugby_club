# Student Name: Harry
# Student Id: 1149599

# python -m flask run

from flask import Flask
from flask import render_template
from flask import request
from flask import redirect
from flask import url_for
import mysql.connector
import connect
import uuid
connection = None
dbconn = None

app = Flask(__name__)

# return database cursor. And also create database connection if no connection


def getCursor():
    global dbconn
    global connection
    if dbconn == None:
        connection = mysql.connector.connect(user=connect.dbuser,
                                             password=connect.dbpass, host=connect.dbhost,
                                             database=connect.dbname, autocommit=True)
        dbconn = connection.cursor()
        return dbconn
    else:
        return dbconn


def getID():
    return uuid.uuid4().fields[1]


@app.route("/")
def home():
    # cur = getCursor()
    # # cur.execute("select id, company, last_name from customers;")
    # cur.execute("select MemberID, MemberFirstName, MemberLastName from members;")
    # select_result = cur.fetchall()
    # column_name = [decs[0] for decs in cur.description]
    # print(f"{column_name}")
    # return render_template('customerresult.html', dbresult=select_result, dbcols=column_name)
    return render_template('login.html')
