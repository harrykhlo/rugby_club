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
from datetime import datetime
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


# route of login page


@app.route("/", methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        selectmemberroute = request.form.get('selectmemberroute')
        return redirect(selectmemberroute)
    else:
        cur = getCursor()
        cur.execute(
            "select MemberID, MemberFirstName, MemberLastName, MembershipStatus, AdminAccess from members;")
        memberidnamestatusaccesslist = cur.fetchall()
        return render_template('login.html', memberidnamestatuslist=memberidnamestatusaccesslist)


# route of member page


@app.route("/member", methods=['GET'])
def member():
    memberid = request.args.get("memberid")
    cur = getCursor()
    # get the member details
    cur.execute(
        "select * from members where MemberID = %s;", (memberid,))
    # typle e.g.(5623, 23, 123, 'Beauden', 'Barrett', '34 Main Sth Rd', 'Islington', 'Christchurch', 'beauden@allblack.co.nz', '0274658254', datetime.date(1999, 6, 7), 1, 0)
    memberrecord = cur.fetchall()[0]
    clubid = memberrecord[1]
    cur.execute(
        "select ClubID, ClubName from clubs where ClubID = %s;", (clubid,))
    clubidname = cur.fetchall()[0]  # tuple (club id, club name)
    teamid = memberrecord[2]
    cur.execute(
        "select TeamID, TeamName from teams where TeamID = %s;", (teamid,))
    teamidname = cur.fetchall()[0]  # tuple (team id, team name)
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


# route of updating member details


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
            return redirect("/")
        else:
            cur = getCursor()
            # get the member details
            cur.execute(
                "select * from members where MemberID = %s;", (memberid,))
            memberrecord = cur.fetchall()[0]

            return render_template('memberupdate.html', memberdetails=memberrecord)


# route of admin page


@app.route("/admin", methods=['GET', 'POST'])
def admin():
    adminid = request.args.get("adminid")
    today = date.today()
    cur = getCursor()
    cur.execute(
        "select * from members where MemberID = %s;", (adminid,))
    adminrecord = cur.fetchall()[0]
    clubid = adminrecord[1]
    cur.execute(
        "select * from clubs where ClubID = %s;", (clubid,))
    clubrecord = cur.fetchall()[0]
    cur.execute(
        "select * from clubnews where ClubID = %s order by NewsDate desc;", (clubid,))
    clubnewsrecord = cur.fetchall()
    cur.execute(
        "select * from members join teams on members.TeamID = teams.TeamID where members.ClubID = %s order by MemberFirstName, MemberLastName;", (clubid,))
    memberrecord = cur.fetchall()
    cur.execute(
        "select * from teams join \
        grades on teams.TeamGrade = grades.GradeID join \
        clubs on teams.ClubID = clubs.ClubID where clubs.ClubID = %s order by GradeMinimumAge;", (clubid,))
    teamrecord = cur.fetchall()
    cur.execute(
        "select * from teams join \
        grades on teams.TeamGrade = grades.GradeID join \
        clubs on teams.ClubID = clubs.ClubID where clubs.ClubID <> %s order by GradeMinimumAge, clubs.ClubName;", (clubid,))
    otherteamrecord = cur.fetchall()
    cur.execute(
        "select * from fixtures \
            join teams as hteam on fixtures.HomeTeam = hteam.TeamID \
            join teams as ateam on fixtures.AwayTeam = ateam.TeamID \
            order by FixtureDate desc;")
    fixturerecord = cur.fetchall()
    return render_template('admin.html', adminrecord=adminrecord, clubrecord=clubrecord,
                           clubnewsrecord=clubnewsrecord, memberrecord=memberrecord,
                           teamrecord=teamrecord, otherteamrecord=otherteamrecord,
                           fixturerecord=fixturerecord, today=today)


# route of admin adding club news


@app.route("/admin/news/add", methods=['GET', 'POST'])
def newsadd():
    if request.method == "POST":
        adminid = request.form.get('adminid')
        clubid = request.form.get('clubid')
        newsheader = request.form.get('newsheader')
        newsbyline = request.form.get('newsbyline')
        newsdate = request.form.get('newsdate')
        news = request.form.get('news')
        cur = getCursor()
        cur.execute(
            "insert into clubnews values (null, %s, %s, %s,  %s, %s);",
            (clubid, newsheader, newsbyline, newsdate, news,))
        return (redirect(f"/admin?adminid={adminid}"))
    else:
        clubid = request.args.get("clubid")
        adminid = request.args.get("adminid")
        return render_template('adminnewsadd.html', clubid=clubid, adminid=adminid)


# route of admin updating member details


@app.route("/admin/member/update", methods=['GET', 'POST'])
def adminmemberupdate():
    if request.method == "POST":
        adminid = request.form.get('adminid')
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
        return(redirect(f"/admin?adminid={adminid}"))
    else:
        memberid = request.args.get("memberid")
        adminid = request.args.get("adminid")
        cur = getCursor()
        cur.execute(
            "select * from members where MemberID = %s;", (memberid,))
        memberrecord = cur.fetchall()[0]
        return render_template('adminmemberupdate.html', memberdetails=memberrecord, adminid=adminid)


# route of admin adding member


@app.route("/admin/member/add", methods=['GET', 'POST'])
def adminmemberadd():
    if request.method == "POST":
        adminid = request.form.get('adminid')
        memberid = request.form.get('memberid')
        clubid = request.form.get('clubid')
        teamid = request.form.get('teamid')
        firstname = request.form.get('firstname')
        lastname = request.form.get('lastname')
        address1 = request.form.get('address1')
        address2 = request.form.get('address2')
        city = request.form.get('city')
        email = request.form.get('email')
        phone = request.form.get('phone')
        birthdate = request.form.get('birthdate')
        membershipstatus = request.form.get('membershipstatus')
        adminaccess = request.form.get('adminaccess')
        cur = getCursor()
        cur.execute(
            "INSERT INTO members VALUES (null, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s); ",
            (clubid, teamid, firstname, lastname, address1, address2, city, email, phone, birthdate,
             membershipstatus, adminaccess,))
        return(redirect(f"/admin?adminid={adminid}"))
    else:
        adminid = request.args.get("adminid")
        cur = getCursor()
        cur.execute(
            "select * from members where MemberID = %s;", (adminid,))
        adminrecord = cur.fetchall()[0]
        cur.execute(
            "select ClubID, ClubName from clubs where ClubID = %s;", (adminrecord[1],))
        clubidname = cur.fetchall()[0]
        cur.execute(
            "select * from teams join \
        grades on teams.TeamGrade = grades.GradeID join \
        clubs on teams.ClubID = clubs.ClubID where clubs.ClubID = %s order by GradeMinimumAge;", (adminrecord[1],))
        teamrecord = cur.fetchall()
        return render_template('adminmemberadd.html', adminrecord=adminrecord, clubidname=clubidname, teamrecord=teamrecord)


# route of admin activating member


@app.route("/admin/member/activate", methods=['GET', 'POST'])
def adminmemberactivate():
    if request.method == "POST":

        adminid = request.form.get('adminid')
        memberid = request.form.get('memberid')
        membershipstatus = request.form.get('membershipstatus')
        cur = getCursor()
        cur.execute(
            "update members set MembershipStatus = %s where MemberID = %s;",
            (membershipstatus, memberid,))
        return(redirect(f"/admin?adminid={adminid}"))
    else:
        memberid = request.args.get("memberid")
        membershipstatus = int(request.args.get("membershipstatus"))
        adminid = request.args.get("adminid")
        cur = getCursor()
        cur.execute(
            "select MemberFirstName, MemberLastName from members where MemberID = %s;", (memberid,))
        membername = cur.fetchall()[0]
        return render_template('adminmemberactivate.html', adminid=adminid, memberid=memberid, membershipstatus=membershipstatus, membername=membername)


# route of admin adding club teams


@app.route("/admin/clubteam/add", methods=['GET', 'POST'])
def adminclubteamadd():
    if request.method == "POST":
        adminid = request.form.get("adminid")
        gradeid = request.form.get("gradeid")
        clubid = request.form.get("clubid")
        teamname = request.form.get("teamname")
        cur = getCursor()
        cur.execute(
            "insert into teams values (null, %s, %s, %s); ",
            (clubid, teamname, gradeid,))
        return(redirect(f"/admin?adminid={adminid}"))
    else:
        adminid = request.args.get("adminid")
        clubid = request.args.get("clubid")
        cur = getCursor()
        cur.execute(
            "select * from grades;")
        graderecord = cur.fetchall()
        return render_template('adminclubteamadd.html', graderecord=graderecord, adminid=adminid, clubid=clubid)


# route of admin adding opposition teams


@app.route("/admin/oppositionteam/add", methods=['GET', 'POST'])
def adminoppositionteamadd():
    if request.method == "POST":
        adminid = request.form.get("adminid")
        gradeid = request.form.get("gradeid")
        slectedclubid = request.form.get("slectedclubid")
        teamname = request.form.get("teamname")
        cur = getCursor()
        cur.execute(
            "insert into teams values (null, %s, %s, %s); ",
            (slectedclubid, teamname, gradeid,))
        return(redirect(f"/admin?adminid={adminid}"))
    else:
        adminid = request.args.get("adminid")
        clubid = request.args.get("clubid")
        cur = getCursor()
        cur.execute(
            "select * from grades;")
        graderecord = cur.fetchall()
        cur.execute(
            "select * from clubs where ClubID<>%s;", (clubid,))
        clubrecord = cur.fetchall()
        return render_template('adminoppositionteamadd.html', graderecord=graderecord, clubrecord=clubrecord, adminid=adminid, clubid=clubid)


# route of admin assigning member team


@app.route("/admin/memberteam/assign", methods=['GET', 'POST'])
def adminmemberteamassign():
    if request.method == "POST":
        adminid = request.form.get("adminid")
        memberid = request.form.get("memberid")
        selectedteamid = request.form.get("selectedteamid")
        cur = getCursor()

        cur.execute(
            "update members set TeamID = %s where MemberID = %s;", (selectedteamid, memberid,))
        return (redirect(f"/admin?adminid={adminid}"))
    else:
        adminid = request.args.get("adminid")
        memberid = request.args.get("memberid")
        cur = getCursor()
        cur.execute(
            "select * from members where MemberID = %s;", (memberid,))
        memberrecord = cur.fetchall()[0]
        birthdate = memberrecord[10]
        today = date.today()
        yearsold = ((today - birthdate).days)/365
        clubid = memberrecord[1]
        cur.execute(
            "select * from teams \
            join grades on teams.TeamGrade = grades.GradeID \
            where ClubID = %s and GradeMinimumAge <= %s and GradeMaximumAge >= %s;", (clubid, yearsold, yearsold,))
        validteamrecord = cur.fetchall()
        return render_template('adminmemberteamassign.html', adminid=adminid, memberrecord=memberrecord, validteamrecord=validteamrecord)


# route of admin printing active members


@app.route("/admin/activemember/print", methods=['GET', 'POST'])
def adminactivememberprint():
    if request.method == "POST":
        adminid = 5643
        return(redirect(f"/admin?adminid={adminid}"))
    else:
        adminid = request.args.get("adminid")
        clubid = request.args.get("clubid")
        cur = getCursor()
        cur.execute(
            "select ClubName from clubs where ClubID = %s;", (clubid,))
        clubname = cur.fetchall()[0][0]
        cur.execute(
            "select * from members join teams on members.TeamID = teams.TeamID where members.ClubID = %s order by MemberFirstName, MemberLastName;", (clubid,))
        memberrecord = cur.fetchall()
        return render_template('adminactivememberprint.html', adminid=adminid, memberrecord=memberrecord, clubname=clubname)


# route of admin setting away team


@app.route("/admin/awayteam/set", methods=['GET', 'POST'])
def adminawayteamset():
    if request.method == "POST":
        adminid = request.form.get("adminid")
        teamid = request.form.get("teamid")
        datetime = request.form.get("datetime")
        selectedteamid = request.form.get("selectedteamid")
        cur = getCursor()
        cur.execute(
            "insert into fixtures values (null, %s, %s, %s, null, null);", (datetime, teamid, selectedteamid,))
        return(redirect(f"/admin?adminid={adminid}"))
    else:
        adminid = request.args.get("adminid")
        teamid = request.args.get("teamid")
        cur = getCursor()
        cur.execute(
            "select TeamName from teams where TeamID = %s;", (teamid,))
        teamname = cur.fetchall()[0][0]
        cur.execute(
            "select * from teams where \
            TeamGrade = (select TeamGrade from teams where TeamID = %s) and \
            ClubID <>(select ClubID from teams where TeamID = %s);", (teamid, teamid,))
        teamrecord = cur.fetchall()
        return render_template('adminawayteamset.html', adminid=adminid, teamrecord=teamrecord, teamname=teamname, teamid=teamid)


# route of admin setting home team


@app.route("/admin/hometeam/set", methods=['GET', 'POST'])
def adminhometeamset():
    if request.method == "POST":
        adminid = request.form.get("adminid")
        teamid = request.form.get("teamid")
        datetime = request.form.get("datetime")
        selectedteamid = request.form.get("selectedteamid")
        cur = getCursor()
        cur.execute(
            "insert into fixtures values (null, %s, %s, %s, null, null);", (datetime, selectedteamid, teamid,))
        return(redirect(f"/admin?adminid={adminid}"))
    else:
        adminid = request.args.get("adminid")
        teamid = request.args.get("teamid")
        cur = getCursor()
        cur.execute(
            "select TeamName from teams where TeamID = %s;", (teamid,))
        teamname = cur.fetchall()[0][0]
        cur.execute(
            "select * from teams where \
            TeamGrade = (select TeamGrade from teams where TeamID = %s) and \
            ClubID <>(select ClubID from teams where TeamID = %s);", (teamid, teamid,))
        teamrecord = cur.fetchall()
        return render_template('adminhometeamset.html', adminid=adminid, teamrecord=teamrecord, teamname=teamname, teamid=teamid)


# route of admin printting eligibility report


@app.route("/admin/eligibilityreport/print", methods=['GET', 'POST'])
def admineligibilityreportprint():
    if request.method == "POST":
        clubid = request.form.get("clubid")
        dateeligibility = request.form.get("dateeligibility")
        cur = getCursor()
        cur.execute(
            "select ClubName from clubs where ClubID = %s;", (clubid,))
        clubname = cur.fetchall()[0][0]
        cur.execute(
            "select * from members \
            join grades on DATEDIFF(%s, members.Birthdate)/365 \
            between grades.GradeMinimumAge and grades.GradeMaximumAge \
            where ClubID = %s and MembershipStatus = 1 order by GradeMinimumAge;", (dateeligibility, clubid,))
        eligibilityrecord = cur.fetchall()
        print(eligibilityrecord)
        return render_template('admineligibilityreportprint.html', eligibilityrecord=eligibilityrecord, clubname=clubname, dateeligibility=dateeligibility)
    else:
        adminid = request.args.get("adminid")
        clubid = request.args.get("clubid")
        return render_template('admineligibilityreportprint.html', adminid=adminid)
