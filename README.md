# hackathon_submssion_app

The hackathon can be posted by anyone and they will be authorized before they are allowed to post hackathons. Users should be able to come and submit some code or files as hackathon submissions. 

Setup:
1) setup virtual environment using "python -m venv venv_name".
2) Install all dependencies using "pip install -r requirements.txt".
3) Go to django_rest/settings.py and in "DATABASES" , add your username , password and DB name.
4) Open MYsqldb and enter command , "CREATE DATABASE IF NOT EXISTS DB_name;"
5) use "cd djnago_rest" in terminal to navigate to that directory.
6) Now enter "python manage.py makemigrations"
7) Then enter "python manage.py migrate"
8) Create superuser by "python manage.py createsuperuser" , this helps in using / adding data using admin controls.
9) enter "python manage.py runserver" , to bring server live on localhost.
