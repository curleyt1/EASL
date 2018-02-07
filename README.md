# EASL
eASL is here to bridge the communication gap that exists between students with
a hearing disability and their educators. We allow the student to simply select
an image of what matches what they are trying to tell their teacher and store
the data creating a personalized action log for each student.


#### Dev Instructions
First configure your virtual-env or IDE and install python3, django, and
python-bootstrap3.

###### When you update the model:
- run `python manage.py migrate`.
- run `python manage.py makemigration`.

###### To start the Server
- run `python manage.py runserver` to start server.

###### To access /admin pages
- run `python manage.py createsuperuser`
- set username and password (email optional).
- run the server and navigate to `localhost:8000/admin`.
- log in with credentials that you set.
