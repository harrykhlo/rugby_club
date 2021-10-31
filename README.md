# Rugby Club Member Management System

## Introduction

This is an application for rugby clubs and their members managing their game activities which includes membership, team, game, club managements. The application pages and functions are given in the following sections.

## Design

This application consists of three pages which are login, member and admin. The login page is the entry point of the application for both admins and members. A user selects their name and login into their own page. The system can distinguish between members and admins, bringing the users to a right page according to their identity after login. The member and admin pages show corresponding user information and provide corresponding functions according to their identity. The functions are given via a button click on the pages accordingly.

## Assumptions

This application assumes user always enter the date in yyyy-mm-dd format, and time in hh:mm:ss format.

## Login Page

- Functions of Login Page
  There is a drop-down list in which users can find all active member names for logging into the system. The login page can identify user class to be either general member or admin and bring the users to the right page. On this login page, the users can:

  - find and select their names on the drop-down list; and
  - click Sign in button to log into an user page which is either member or admin page.

- Route of Login Page
  The login page is at the root "/" of the site.

## Member page

This page is brought after a member logged in.

- Functions of Member Page
  This member page is shown after a general user gets into the system via the login page. The users can:

  - Update their personal details vai a button click bringing the user to a Member Update Personal Detail Page as mentioned in next Section below for entering new details.

  They can also find the following information on the page:

  - Latest 3 club news belong to user's club;
  - Upcoming games for user's team; and
  - User's personal details.

- Route of Member Page
  The member page is at /member?memberid=`<member id>` of the site. The member id from the login page is required to be given in the form of a GET request.

## Member Update Personal Detail Page (is entered from member page)

This page is brought by a button click on member page.

- Functions of Member Update Personal Detail Page
  This member update personal detail page is shown after the user click the “Update Personal Detail” button on the member page. The following details can be updated.

  - First Name;
  - Last Name;
  - Address 1;
  - Address 2;
  - City;
  - Email;
  - Phone; and
  - Birthday.

- Route of Member Update Personal Detail Page
  The member page is at /member/update?memberid=`<member id>` of the site. The member id from the member page is required to be given in the form of a GET request.

## Admin page

This page is brought after an admin logged in.

- Functions of Admin Page
  This Admin page is shown after an admin user gets into the system via the login page. The admin can find the following information on the page:

  - All news belong to admin's club;
  - All member details belong to admin's club;
  - All team details belong to admin's club;
  - All team detials belong to other clubs; and
  - All fixtures.

- The admin can also initiate the following actions on the page:

  - Add new news belonging to admin's club;
  - Add members with details belonging to admin's club;
  - Edit existing member details belonging to admin's club;
  - Edit member status (i.e. de-activate or re-activate members) belonging to admin's club;
  - Give a list of active members for printing purposes;
  - Add new teams with details belonging to admin's club;
  - Join members to a team belonging to admin's club;
  - Add new opposition teams with details belonging to other clubs;
  - Create either home or away fixtures with a team belonging to admin's club and another team in the same grade; and
  - Give a list of all active members eligible to play in a specific grade on a given date.

- Route of Admin Page
  The admin page is at /admin?adminid=`<admin id>` of the site. The admin id from the login page is required to be given in the form of a GET request.

## Add News Page (is entered from admin page)

This page is brought by a button click on admin page.

- Functions of Add News Page
  This Add News Page allows the admin to added a new news. The following information should be included in a news:

  - News Header;
  - News Byline;
  - News Date (yyyy-mm-dd); and
  - News Content.

- Route of Member Update Personal Detail Page
  The admin page is at /admin/news/add?clubid=`<club id>`&adminid=`<admin id>` of the site. The club id and the admin id from the admin page are required to be given in the form of a GET request.

## Add New Member Page (is entered from admin page)

This page is brought by a button click on admin page.

- Functions of Add New Member Page
  This Add New Member allows the admin to added a new member in the admin's club. The following information should be included in a new member:

  - First Name;
  - Last Name;
  - Address 1;
  - Address 2;
  - City;
  - Email;
  - Phone;
  - Birthday; and
  - Team.

- Route of Add New Member Page
  The admin page is at admin/member/add?adminid=`<admin id>` of the site. The admin id from admin page is required to be given in the form of a GET request.
