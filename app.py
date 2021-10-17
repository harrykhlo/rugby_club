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

                # cur.execute(
                #     "select * from fixtures;")
                # cur.execute(
                #     "select * FROM fixtures where FixtureDate >= '2021-09-21';")

                today = date.today()
                cur.execute(
                    "select FixtureID, FixtureDate,hteam.TeamName as HomeTeamName, \
                    ateam.TeamName as AwayTeamName, HomeTeam as HomeTeamId, \
                    AwayTeam as AwayTeamId FROM fixtures \
                    join teams as hteam on fixtures.HomeTeam = hteam.TeamID \
                    join teams as ateam on fixtures.AwayTeam = ateam.TeamID \
                    where FixtureDate >= %s and (HomeTeam = %s or AwayTeam = %s) order by FixtureDate;", (today, teamid, teamid,))
                upcomingteamfixtures = cur.fetchall()
                # print("testing---------------------------------------------")
                # print(upcomingteamfixtures)
                # print(type(upcomingteamfixtures))

                # print("member is logged in")
                # print(memberrecord)
                return render_template('memberindex.html', memberdetaillist=memberrecord[0], clubidname=clubidname, teamidname=teamidname, threelatestclubnews=threelatestclubnews, today=today, upcomingteamfixtures=upcomingteamfixtures)
    # if request.method == 'GET':
    else:
        cur = getCursor()
        cur.execute(
            "select MemberID, MemberFirstName, MemberLastName, MembershipStatus from members;")
        select_result = cur.fetchall()
        print(select_result)
        return render_template('login.html', membernameidlist=select_result)


@app.route("/memberupdate", methods=['GET', 'POST'])
def memberupdate():
    if request.method == "POST":
        memberid = request.form.get('memberid')
        firstname = request.form.get('firstname')
        lastname = request.form.get('lastname')
        address1 = request.form.get('address1')
        address2 = request.form.get('address2')
        city = request.form.get('city')
        email = request.form.get('email')
        phone = request.form.get('phone')
        birthdate = request.form.get('birthdate')

        cur = getCursor()
        cur.execute(
            "update members set MemberFirstName = %s, MemberLastName = %s, \
            Address1 = %s, Address2 = %s, \
            City=%s, Email=%s,  \
            Phone=%s, Birthdate=%s \
            where MemberID = %s;",
            (firstname, lastname, address1, address2, city, email, phone, birthdate, memberid,))

        cur.execute(
            "select * from members where MemberID = %s;", (memberid,))
        memberrecord = cur.fetchall()
        # memberrecorddiscription = cur.description # for checking only
        # print(memberrecorddiscription) # for checking only

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
        cur.execute(
            "select NewsHeader, NewsByline, NewsDate, News from clubnews where ClubID=%s order by NewsDate DESC limit 3;", (clubidname[0],))
        threelatestclubnews = cur.fetchall()

        today = date.today()
        cur.execute(
            "select FixtureID, FixtureDate,hteam.TeamName as HomeTeamName, \
            ateam.TeamName as AwayTeamName, HomeTeam as HomeTeamId, \
            AwayTeam as AwayTeamId FROM fixtures \
            join teams as hteam on fixtures.HomeTeam = hteam.TeamID \
            join teams as ateam on fixtures.AwayTeam = ateam.TeamID \
            where FixtureDate >= %s and (HomeTeam = %s or AwayTeam = %s) order by FixtureDate;", (today, teamid, teamid,))
        upcomingteamfixtures = cur.fetchall()
        # print("testing---------------------------------------------")
        # print(upcomingteamfixtures)
        # print(type(upcomingteamfixtures))

        # print("member is logged in")
        # print(memberrecord)
        return render_template('memberindex.html', memberdetaillist=memberrecord[0], clubidname=clubidname, teamidname=teamidname, threelatestclubnews=threelatestclubnews, today=today, upcomingteamfixtures=upcomingteamfixtures)
        # return redirect("/")
    else:
        memberid = request.args.get("memberid")
        if memberid == None:
            # print("no member id is given ------------------------------")
            return redirect("/")
        else:
            print(request.args)

            print(memberid)

            cur = getCursor()
            # get the member details
            cur.execute(
                "select * from members where MemberID = %s;", (memberid,))
            memberrecord = cur.fetchall()

            return render_template('memberupdate.html', memberdetails=memberrecord[0])
