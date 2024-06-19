### Quickstart
- from vscode install these extensions
  - Python
  - Python Debugger
  - Black Formatter
  - autopep8
- Set up black or autopep8 in .vscode/settings.json
- python3 -m venv venv
- source venv/bin/activate
- pip install -U pip setuptools wheel
- python3 -m pip install Django

### Admin Project
- django-admin startproject [<myproject>]
- cd [<myproject>]
- python manage.py runserver 8000 #8000 is the default port

### Scaffold a site
- in the [<myproject>]/[<myproject>]/urls.py folder add your pages to urlpatterns
- now create in same folder a views.py to hold your views (these are controllers)
- back up one folder create a templates folder in same dir as manage.py to hold your html templates
- go down one directory again to settings.py. Find "TEMPLATES" array, and in the "DIRS" array spcify your templates directory as "templates:
- now open the views.py to connect up our templates
  
### CSS
- opening settings and in the top "import os"
- Under STATIC_URL add a "STATICFILES_DIRS" array varible and add to it the location of the static folder you created.
- now in your html templates you can add your style sheets
