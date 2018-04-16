# eASL
eASL is here to bridge the communication gap that exists between students with
a hearing disability and their educators. We allow the student to simply select
an image that matches what they are trying to tell their teacher and store
the data creating a personalized action log for each student.

## Try it out!
eASL is currently hosted at http://curleyt.pythonanywhere.com/

#### Dev Instructions
Setting-up your own instance of eASL for development or testing purposes is easiest on a machine running Linux or Mac OS

###### Set-Up
- Clone this repository
- Install python 3, which comes with its own package manager, pip.
- Install virtualenv with the command `pip install virtualenv`
- Create a python 3 virtual env by pointing it to your python 3 installation, example: `virtualenv -p /usr/local/bin/python3 env`
- Activate the environment: `source env/bin/activate`
- Install the packages necessary to run eASL: `pip install django django-bootstrap3 django-extensions python-dotenv`

###### When you update the model:
- Navigate to the project directory.
- Run `python manage.py migrate`.
- Run `python manage.py makemigration`.

###### To start the Server
- Navigate to the project directory.
- Run `python manage.py runserver` to start a server locally.
- Navigate to `localhost:8000` in a web browser to test the site.

###### To create super-users and access /admin pages
- Navigate to the project directory.
- Run `python manage.py createsuperuser`.
- Set username and password (email optional).
- Run the server and navigate to `localhost:8000/admin`.
- Sign in with new superuser account.

###### A note on password reset emails
On the production server, the account password of our easl no-reply address is retrieved from the environment to avoid storing it in the source code. This means that emails cannot be sent from a localhost server with the current settings. There are two ways to configure it locally:
- Change the SMTP configuration in `settings.py` to use a private account.
- Remove the SMTP configuration and log emails to console with the line `EMAIL_BACKEND='django.core.mail.backends.smtp.EmailBackend'` in `settings.py`
