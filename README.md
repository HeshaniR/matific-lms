# League Management System
#### how to setup the project
1. Clone the project
2. Create the mysql database ```lms```
3. Change mysql configurations in ```lms/settings.py``` as shown below

```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'USER': 'mysqluser',
        'PASSWORD': 'passowrd',
        'HOST': 'host',
        'PORT': 'port',
        'NAME': 'lms',
    }
}
```

4. Enter this command to install the required libraries

```
pip install -r requirements.txt
```

5.Migrate the database using following command.

```
py manage.py migrate
```

6. To Generate fake data run the following manage commands

```
py manage.py teamfaker
py manage.py userfaker
py manage.py gamefaker
```
This will create an admin user as 

```
username = sadmin
password = sadmin@123
```
and 16 coaches and 160 players and 10 teams.

username and password for each generated user will be visible at terminal

7. run ```py manage.py runserver``` to start the server.

8. Following APIs are available and use ```api/postman.json``` to test the APIs

- /users/login (POST)

Login

- /users/logout (GET)

Logout

- /users/create (POST)

Create a user

- /team (GET)

List all the teams

- /team/<team_id> (GET)

View team details by team id

- /users/players (GET)

List all the players based on the requested user type

- /users/player/<player_id> (GET)

Get details of a selected player by id

- /users/players/<avg_score>

Get player who are above the given average score

- /users/stats (GET)

Get login stats of users

#### Additional info
 python version - 3.9
