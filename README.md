## RESTful API for classifieds website

### Project functionality:

API provides acess to the database with users and ads.

**Users.** Implemented the ability to create new users and get user profile data by ID.

**Ads.** An ad can be created, viewed, and deleted.


#### Docker Instructions:

The command to run the database service locally:

`docker compose up -d db`

Then to run your Flask application, type:

`docker compose up --build dockerized_flask_api`

If you get an error related to port 5432, try to check if this port is locally occupied by PostgreSQL:

`sudo ss -lptn 'sport = :5432'`

And if so, local PostgreSQL can be temporarily disabled this way:

`sudo service postgresql stop`

#### Testing Instructions:

After you recieved a message like:

**Running on http://HOST:PORT/ (Press CTRL+C to quit)**

you can try to add new user to the app by running command:
    
`curl HOST:PORT/users/ -d '{"username": "Name", "email": "example@example.com", "password": "abc12536"}' -H 'Content-Type: application/json'`


#### Used technologies:
- Python 3
- Flask
- PostgreSQL
- SQLAlchemy
- Docker
