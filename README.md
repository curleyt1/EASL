# eASL
eASL is here to bridge the communication gap that exists between students with
a hearing disability and their educators. We allow the student to simply select
an image that matches what they are trying to tell their teacher and store
the data creating a personalized action log for each student.

## Try it out!
eASL is currently hosted at http://curleyt.pythonanywhere.com/.
This instance of eASL can be used to try out the application without hosting a local server.

## Dev Instructions
Setting-up your own instance of eASL for development or testing purposes is easiest on a machine running Linux or Mac OS.

#### Set-Up
- Clone this repository
- Install python 3 and its package manager, pip
  - Depending on your operating system and package manager, pip may be bundled with your python installation, or it may need to be installed separately from the `python-pip` package.
- Install virtualenv to create a virtual python environment.
  - Some operating systems / Linux distributions include a `virtualenv` package in their package manager.
  - It can also be installed via pip with the command `pip install virtualenv` in a terminal.
- Create a python 3 virtual env by pointing it to your python 3 installation.
  - Example: `virtualenv -p /usr/bin/python3 env` creates a python 3 virtual environment with the name `env`.
  - Enter `which python3` into a terminal to see the path to your python 3 installation.
- Activate the environment: `source env/bin/activate`
  - When the environment has been activated the terminal prompt will show the environment name in parentheses.
- Install the packages necessary to run eASL:
  - `pip install django django-bootstrap3 django-extensions python-dotenv`

#### When you update the model:
- Activate your virtual environment
- Navigate to the project directory.
- Run `python manage.py migrate`.
- Run `python manage.py makemigration`.

#### To start the Server
- Activate your virtual environment
- Navigate to the project directory.
- Run `python manage.py runserver` to start a server locally.
- Navigate to `localhost:8000` in a web browser to test the site.

###### To create super-users and access /admin pages
- Activate your virtual environment
- Navigate to the project directory.
- Run `python manage.py createsuperuser`.
- Set username and password (email optional).
- Run the server and navigate to `localhost:8000/admin`.
- Sign in with new superuser account.

#### A note on password reset emails
On the production server, the account password of our easl no-reply address is retrieved from the environment to avoid storing it in the source code. This means that emails cannot be sent from a localhost server with the current settings. There are two ways to configure it locally:
- Change the SMTP configuration in `settings.py` to use a private account.
- Remove the SMTP configuration and log emails to console with the line `EMAIL_BACKEND='django.core.mail.backends.smtp.EmailBackend'` in `settings.py`
