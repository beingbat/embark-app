## DJANGO BACKEND

To run the project, you will need to setup a server on which backend would run.

Django related packages are all in the virtual environment included in this folder.

Steps to run this:

- Open terminal in current folder
- run: source venv/bin/activate
- run: cd embark_django
- run: python3 manage.py runserver

This will start server on the port number 8000 on the local host.

The backend has JWT authentication implemented.

**Important links:**

For generating access and refresh token: i.e. login [by passing username and password in POST]
`localhost:8000/api/token/` 

For creating new access token by passing refresh token in POST
`localhost:8000/api/token/refresh/`

After signing in, user specific data can be found at:
`localhost:8000/info/`
using GET, but access token must be passed in header

example: `header: {"Content-Type":"application/json", 'Authorization':'Bearer '  access_token}`

Then in response you will get the information.


Username and passwords:

1:
username: malek
pass: a

2:
username: ahmad
pass: alsi123!