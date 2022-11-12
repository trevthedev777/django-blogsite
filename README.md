# Django Blog Site

[Django Blog Live Site]()

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

### Deployment

#### Deployments Steps

1. Create the `Heroku` app
    - Open `Heroku`
    - Select `NEW APP` on the `Heroku Dashboard`
    - Once the app is provisioned:
        - Select the `Rescources` tab
        - In the `Add-ons` tab, search for `Postgres`
        - Then proceed to our `Settings` tab
            - The click on `Reveal Config Vars`
            - Cope the provided `DATABASE_URL` key
        - Return to the project workspace
        - Create a `env.py` in the `home directory`
        - Create `SECRET_KEY` 
            - Link to `CONFIG VARS` in Heroku

2. Attach the PostrgreSQL database
    - in `settings.py`, scroll down to `DATABASES`, paste the provided key from `Heroku` (check source code for variable declaration)
    - Perform `Migration`
    ```
    python3 manage.py migrate
    ```
    **Please check using the resources tab that the database is connected in `heroku`**

    __Please add PORT 8000__ to the config vars in Heroku

3. Prepare our environment and `settings.py` files
4. Get our static and media files stored on `Cloudinary`

    #### Creat Cloudinary Account
    - Visit the [Cloudinary Website](https://cloudinary.com/)
    - Click on the **Sign up For Free** button
    - Provide your details and choose a password
    - For **Primary interest" you can choose **Programmable Media for image and video API**
    - __Optional__: edit your assigned cloud name to somethjign more memorable
    - Click **Create Account**
    - Verify your email and you will be redirected to the dashboard

    - Copy the API key from the Dashboard and create a new `environment variable`
    - Then import that into `Heroku`
    - __while here create a temp config var of `DISABLE_COLLECTSTATIC` and set it to `1` and we will remove at the end of development

    Add these to the `Installed Apps` in our `settings.py`

    Then we need to tell Django to use `cloudinary` to store our `static files`

```
heroku logs --app codestar2022-trevor --tail
```