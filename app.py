# Student Name: Harry
# Student Id: 1149599


# python -m venv env

# python -m pip install --upgrade pip

# python -m pip install flask

# pip install mysql-connector-python

# python -m flask run

from flask import Flask
from flask import render_template
from flask import request
from flask import redirect
from flask import url_for
from datetime import date
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


@app.route("/membernamelist")
def membernamelist():
    cur = getCursor()
    # cur.execute("select id, company, last_name from customers;")
    cur.execute("select MemberID, MemberFirstName, MemberLastName from members;")
    select_result = cur.fetchall()
    column_name = [decs[0] for decs in cur.description]
    print(f"{column_name}")
    return render_template('listmembernames.html', dbresult=select_result, dbcols=column_name)


@app.route("/", methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # print(request.form) # for checing only

        # get member ID from the login from in login.html
        memberid = request.form.get('selectedmember')
        # print(memberid) # for checing only

        if memberid == "None":  # if no member is selected from the login from in login.html
            print("Not member is given")
            cur = getCursor()
            cur.execute(
                "select MemberID, MemberFirstName, MemberLastName, MembershipStatus from members;")
            select_result = cur.fetchall()
            return render_template('login.html', membernameidlist=select_result)
        else:  # if a member is selected from the login from in login.html
            cur = getCursor()
            # get the member details
            cur.execute(
                "select * from members where MemberID = %s;", (memberid,))
            memberrecord = cur.fetchall()
            # memberrecorddiscription = cur.description # for checking only
            # print(memberrecorddiscription) # for checking only

            # get the member's AdminAccess which is an integer (1 = admin member; 0 = general member)
            adminaccess = memberrecord[0][12]
            clubid = memberrecord[0][1]
            cur.execute(
                "select ClubID, ClubName from clubs where ClubID = %s;", (clubid,))
            clubidname = cur.fetchall()[0]  # tuple (club id, club name)
            # print("testing---------------------------------------------")
            # print(clubidname)
            # print(type(clubidname))
            teamid = memberrecord[0][2]
            cur.execute(
                "select TeamID, TeamName from teams where TeamID = %s;", (teamid,))
            teamidname = cur.fetchall()[0]  # tuple (team id, team name)
            # print("testing---------------------------------------------")
            # print(teamidname)
            # print(type(teamidname))

            if adminaccess:  # check if the memeber is admin or not
                # route to admin's page
                print("admin is logged in")
                print(memberrecord)
                return render_template('adminindex.html', admindetaillist=memberrecord[0])
            else:  # if the memeber is not an admin
                # route to member's page

                cur.execute(
                    "select NewsHeader, NewsByline, NewsDate, News from clubnews where ClubID=%s order by NewsDate DESC limit 3;", (clubidname[0],))
                threelatestclubnews = cur.fetchall()

                today = date.today()
                # cur.execute(
                #     "select * from fixtures;")
                # cur.execute(
                #     "select * FROM fixtures where FixtureDate >= '2021-09-21';")
                cur.execute(
                    "select * from fixtures where FixtureDate >= %s;", (today,))
                upcomingfixtures = cur.fetchall()
                print("Test----------------------------------------")
                print(upcomingfixtures)

                print("member is logged in")
                print(memberrecord)
                return render_template('memberindex.html', memberdetaillist=memberrecord[0], clubidname=clubidname, teamidname=teamidname, threelatestclubnews=threelatestclubnews, today=today)
    # if request.method == 'GET':
    else:
        cur = getCursor()
        cur.execute(
            "select MemberID, MemberFirstName, MemberLastName, MembershipStatus from members;")
        select_result = cur.fetchall()
        print(select_result)
        return render_template('login.html', membernameidlist=select_result)
