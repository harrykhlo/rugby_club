# Rugby Club Member Management System

## Introduction

This is an application for rugby clubs and their members managing their game activities which includes membership, team, game, club managements. The application pages and functions are given in the following sections.

## Login Page

- Functions of Login Page
  There is a drop-down list in which users can find all active member names for logging into the system. The login page can identify user class to be either general member or admin and bring the users to the right page. On this login page, the users can:

  - find and select their names on the drop-down list; and
  - click Sign in button to log into an user page which is either member or admin page.

- Route of Login Page
  The login page is at the root "/" of the site.

## Member page

- Functions of Member Page
  This member page is shown after a general user gets into the system via the login page. The users can update their personal details on this page. They can also find the following information on the page:

  - Latest 3 club news belong to user's club;
  - Upcoming games for user's team; and
  - User's personal details.

- Route of Member Page
  The member page is at /member of the site.

## Member Update Personal Detail Page

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
  The member page is at /member/update of the site.

## Admin page

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
  - Give a list of active members for printing purposes. - User's personal details.
