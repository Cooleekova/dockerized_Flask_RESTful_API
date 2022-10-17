## RESTful API for classifieds website

### Project functionality:

API provides acess to the database with users and ads.

**Users.** Implemented the ability to create new users and get user profile data by ID.

**Ads.** An ad can be created, viewed, and deleted.


#### Docker Instructions:

1. To build an image from a provided Dockerfile, change to the current directory and run the command:

    `docker build --tag flask_rest_api_image .`

2. The command to run the container based on the built image:

    `docker run -P -d --name rest_api_container flask_rest_api_image`


#### Used technologies:
- Python 3
- Flask
- PostgreSQL
- SQLAlchemy

