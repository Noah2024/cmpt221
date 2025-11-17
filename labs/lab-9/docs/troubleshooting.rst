.. _`Troubleshooting`:

Troubleshooting
===============
This section describes some common issues that can arise and possible solutions.

Issue #1
--------
In Postgres SQL tables and records you use double quotes
and text you use single quotes ''
MAKE SURE YOU USE THESE, because things don't work unless you do

Issue #2
--------
If there are issues with form data not showing up on the flask backed
Make sure your using the correct action set for the form and the correct
HTTP method (such as POST and GET)

Issue #3
--------
If there is a problem with permissions and HTTPS methods
Like you get redirected to a page that says that method is not allowed or something like that 
Make sure you've put both POST and GET methods in the sqlAlchemy decorator around endpoints
Becuase you need to have permissions for both GET and POST, even if your just using POST
<Solution>