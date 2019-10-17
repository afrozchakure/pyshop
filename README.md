# pyshop
Django app for shopping


Commands for setting up 
python3 -m venv venv

Press Ctrl + L to clean up the terminal 

#### Activating the virtual Environment
source venv/bin/activate

#### Installing Django 2.1
pip install django==2.1

#### Creating the admin page for our project (creates a project pyshop in current folder (.))
django-admin startproject pyshop .

#### To run our server
python3 manage.py runserver

#### To create an app products
python3 manage.py startapp products

### View functions gets called when a user goes to a particular page (/products, /offer)
### to map a url to a function make a urls.py file in your app folder
### views.py -> urls.py  (maps to)

