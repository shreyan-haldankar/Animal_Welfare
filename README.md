# Animal_Welfare

## Setup

The first thing to do is to clone the repository:

```sh
$ git clone https://github.com/shreyan-haldankar/Animal_Welfare.git
```

Install requirements using:

```sh
$ pip install -r requirements.txt
```

Once `pip` has finished installing the requirements:
```sh      
$ python manage.py runserver
```
And navigate to `http://127.0.0.1:8000/`.


<br>
<h3> To check the whether user has been added in the database. </h3>

First, Create a superuser using 
```sh
python manage.py createsuperuser
```

Go to http://127.0.0.1:8000/admin
and Login using your superuser credentials.

Check if the user has been added by clicking on Users.
