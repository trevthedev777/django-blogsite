# Django Blog Site

## Table of Contents

🏠[Table of Contents](#table-of-contents)

### Technologies Used

- **Cloudinary** to store our images online
- **Django** for development
- **PostgreSQL** for database management
- **Dj Database** for Django database support

🏠[Table of Contents](#table-of-contents)

### App Production

1. Install `Django` and supporting libraries:

```
pip3 install 'django<4' gunicorn
```
```
pip3 install dj_database_url==0.5.0 psycopg2
```

2. Create an empty project and app
```
django-admin startproject <app_name> .
```

- Create our app:
```
python3 manage.py startapp <appname>
```

We then need to add this to our `installed apps` list in the `settings.py` file.

Then we should `migrate` our changes to the database using the `cli`, every time we add a new `app` to our workspace, we need to run this command 

```
python3 manage.py migrate
```

3. Set our project to use `Cloundinary` and `PostgreSQL`
```
pip3 install dj3-cloudinary-storage
```

4. Create our `requirements.txt` file
```
pip3 freeze --local > requirements.txt
```

5. Deploy our new, empty project to `Heroku`

🏠[Table of Contents](#table-of-contents)