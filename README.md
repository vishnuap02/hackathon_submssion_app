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

APIs:
1) http://127.0.0.1:8000/admin : for admin controls.
2) http://127.0.0.1:8000/todo/api/v1/hackathons : for creating and viewing hackathons.
3) http://127.0.0.1:8000/todo/api/v1/listhackathons : GET list of ALL hackathons
4) http://127.0.0.1:8000/todo/api/v1/user : for creating and viewing users.
5) http://127.0.0.1:8000/todo/api/v1/register : for creating and viewing registrations.
6) http://127.0.0.1:8000/todo/api/v1/submission : for creating and viewing submissions.
7) http://127.0.0.1:8000/todo/api/v1/listsubmissions :  GET list of ALL submissions.

MODEL STRUCTURE:
User model : Has Name , email and password to register.

Hackathon model: Has all specified field with given PRIORITY to choose between image , file and link submission, has a field to mention which USER created it.

Register Model : Has Serial number of registration and which user(FK) has registered to which hackathon(FK).

Submission Model : Apart from mentioned field in docx , added the field "is_favouirte" , "sub_date" , github and other link. Here it can be submitted in image or file or link

<img width="905" alt="image" src="https://user-images.githubusercontent.com/85162998/231822801-01d1138f-25f9-4fd9-a06d-db4cf26bf81c.png">
<img width="946" alt="image" src="https://user-images.githubusercontent.com/85162998/231823160-f1a05b9d-923b-48ca-bd14-1cf50c48da4e.png">
<img width="955" alt="image" src="https://user-images.githubusercontent.com/85162998/231823340-4391d2c6-f003-4b3e-8f60-efe490addad6.png">
Tables in hackathon.
<img width="218" alt="image" src="https://user-images.githubusercontent.com/85162998/231823601-754368c3-0612-466e-b698-0ee0be527339.png">

