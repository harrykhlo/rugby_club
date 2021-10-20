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


@app.route("/", methods=['GET', 'POST'])
def login():
    if request.method == 'POST':

        selectmemberroute = request.form.get('selectmemberroute')
        # print(selectmemberroute)
        # print("testing selectmemberroute=====================")
        return redirect(selectmemberroute)

    else:
        cur = getCursor()
        cur.execute(
            "select MemberID, MemberFirstName, MemberLastName, MembershipStatus, AdminAccess from members;")
        memberidnamestatusaccesslist = cur.fetchall()
        # print(memberidnamestatusaccesslist)
        return render_template('login.html', memberidnamestatuslist=memberidnamestatusaccesslist)


@app.route("/member", methods=['GET'])
def member():
    memberid = request.args.get("memberid")
    # print("memberid------Testing---------")
    # print(memberid)

    cur = getCursor()
    # get the member details
    cur.execute(
        "select * from members where MemberID = %s;", (memberid,))
    # typle e.g.(5623, 23, 123, 'Beauden', 'Barrett', '34 Main Sth Rd', 'Islington', 'Christchurch', 'beauden@allblack.co.nz', '0274658254', datetime.date(1999, 6, 7), 1, 0)
    memberrecord = cur.fetchall()[0]
    # print("memberrecord------Testing---------")
    # print(memberrecord)  # for checking only

    clubid = memberrecord[1]
    cur.execute(
        "select ClubID, ClubName from clubs where ClubID = %s;", (clubid,))
    clubidname = cur.fetchall()[0]  # tuple (club id, club name)
    # print("testing-clubidname--------------------------------------------")
    # print(clubidname)
    # print(type(clubidname))
    teamid = memberrecord[2]
    cur.execute(
        "select TeamID, TeamName from teams where TeamID = %s;", (teamid,))
    teamidname = cur.fetchall()[0]  # tuple (team id, team name)
    # print("testing-teamidname--------------------------------------------")
    # print(teamidname)
    # print(type(teamidname))

    cur.execute(
        "select NewsHeader, NewsByline, NewsDate, News from clubnews where ClubID=%s order by NewsDate DESC limit 3;",
        (clubidname[0],))
    threelatestclubnews = cur.fetchall()

    today = date.today()
    cur.execute(
        "select FixtureID, FixtureDate,hteam.TeamName as HomeTeamName, \
        ateam.TeamName as AwayTeamName, HomeTeam as HomeTeamId, \
        AwayTeam as AwayTeamId FROM fixtures \
        join teams as hteam on fixtures.HomeTeam = hteam.TeamID \
        join teams as ateam on fixtures.AwayTeam = ateam.TeamID \
        where FixtureDate >= %s and (HomeTeam = %s or AwayTeam = %s) order by FixtureDate;",
        (today, teamid, teamid,))
    upcomingteamfixtures = cur.fetchall()

    return render_template('member.html', memberdetaillist=memberrecord, clubidname=clubidname, teamidname=teamidname, threelatestclubnews=threelatestclubnews, today=today, upcomingteamfixtures=upcomingteamfixtures)


@app.route("/member/update", methods=['GET', 'POST'])
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
        # print("Testing member value -------------------------------")
        # print(memberid)
        # print(firstname)
        # print(lastname)
        # print(address1)
        # print(address2)
        # print(city)
        # print(email)
        # print(phone)
        # print(birthdate)

        cur = getCursor()
        cur.execute(
            "update members set MemberFirstName = %s, MemberLastName = %s, \
            Address1 = %s, Address2 = %s, \
            City=%s, Email=%s,  \
            Phone=%s, Birthdate=%s \
            where MemberID = %s;",
            (firstname, lastname, address1, address2, city, email, phone, birthdate, memberid,))

        return(redirect(f"/member?memberid={memberid}"))

    else:
        memberid = request.args.get("memberid")
        if memberid == None:
            # print("no member id is given ------------------------------")
            return redirect("/")
        else:
            # print("test - request.args - memberid ---------------------")
            # print(request.args)
            # print(memberid)

            cur = getCursor()
            # get the member details
            cur.execute(
                "select * from members where MemberID = %s;", (memberid,))
            memberrecord = cur.fetchall()[0]

            return render_template('memberupdate.html', memberdetails=memberrecord)


@app.route("/admin", methods=['GET', 'POST'])
def admin():
    adminid = request.args.get("adminid")
    # print("adminid------Testing---------")
    # print(adminid)
    cur = getCursor()
    cur.execute(
        "select * from members where MemberID = %s;", (adminid,))
    adminrecord = cur.fetchall()[0]
    # print(adminrecord)

    clubid = adminrecord[1]
    cur.execute(
        "select * from clubs where ClubID = %s;", (clubid,))
    clubrecord = cur.fetchall()[0]
    # print(clubrecord)

    cur.execute(
        "select * from clubnews where ClubID = %s order by NewsDate desc;", (clubid,))
    clubnewsrecord = cur.fetchall()
    # print(clubnewsrecord)

    cur.execute(
        "select * from members where ClubID = %s order by MemberFirstName, MemberLastName;", (clubid,))
    memberrecord = cur.fetchall()
    # print(memberrecord)

    cur.execute(
        "select * from teams where ClubID = %s order by TeamName;", (clubid,))
    teamrecord = cur.fetchall()
    # print(teamrecord)

    cur.execute(
        "select * from teams where ClubID <> %s order by TeamName;", (clubid,))
    otherteamrecord = cur.fetchall()
    # print(otherteamrecord)

    return render_template('admin.html', adminrecord=adminrecord, clubrecord=clubrecord,
                           clubnewsrecord=clubnewsrecord, memberrecord=memberrecord,
                           teamrecord=teamrecord, otherteamrecord=otherteamrecord)


@app.route("/news/add", methods=['GET', 'POST'])
def newsadd():
    if request.method == "POST":
        adminid = request.form.get('adminid')
        clubid = request.form.get('clubid')
        newsheader = request.form.get('newsheader')
        newsbyline = request.form.get('newsbyline')
        newsdate = request.form.get('newsdate')
        news = request.form.get('news')
        # print("testing newsheader----------")
        # print(adminid)
        # print(clubid)
        # print(newsheader)
        # print(newsbyline)
        # print(newsdate)
        # print(news)
        cur = getCursor()
        cur.execute(
            "insert into ClubNews values (null, %s, %s, %s,  %s, %s);",
            (clubid, newsheader, newsbyline, newsdate, news,))

        return (redirect(f"/admin?adminid={adminid}"))
    else:
        clubid = request.args.get("clubid")
        adminid = request.args.get("adminid")
        return render_template('newsadd.html', clubid=clubid, adminid=adminid)
