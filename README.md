# spaceQuery
A webapp built for CS50Web using Vue.js and Django.

**Live Site:** blah de blah blah

- [spaceQuery](#spacequery)
- [Project Overview](#project-overview)
  - [Distinctiveness and Complexity](#distinctiveness-and-complexity)
  - [Technologies Used](#technologies-used)
  - [Folder Structure and Files](#folder-structure-and-files)
    - [space-api](#space-api)
    - [space-front](#space-front)
  - [Running the Project Locally](#running-the-project-locally)
    - [Setting up the Django Rest Framework API](#setting-up-the-django-rest-framework-api)
    - [Setting up the Vue.js front end](#setting-up-the-vuejs-front-end)
- [Objective and Features](#objective-and-features)
  - [Feature Overview](#feature-overview)
  - [API Documentation](#api-documentation)
    - [Prefix:](#prefix)
    - [Users](#users)
    - [Saves](#saves)
    - [Externals](#externals)
  - [Frontend](#frontend)
    - [Third-Party APIs used](#third-party-apis-used)
- [Learnings and Experiences](#learnings-and-experiences)
- [Gallery](#gallery)

# Project Overview
At its core, this webapp (I've named it **spaceQuery**) acts as an app for querying a bunch of awesome space related APIs (more info below). It doesn't sound nearly as awesome now that I have written it down, but yeah. Why do I need to be logged in, you ask? Well, I've added some nifty functionality which allows you to save any query results that you particularly like to your user profile for later reference — can't do that without having you signed in. This also allows you to look up other users and look at their saved posts. I'm not entirely sure why I added this, and what purpose it serves, but it's there. Further explanation [below](#objective-and-features).

## Distinctiveness and Complexity
I believe this project is **sufficiently distinct** from the others in the course, and is not based on the 2020 CS50W Pizza project.
- It is not, at it's core, a social media website (while it does incorporate features such as user profiles, they are more of a secondary thing).
- Nor is it an e-commerce based webapp in any way. In fact, it has nothing to do with commerce at all.
- It utilises a javascript frontend framework (Vue) alongside Django Rest Framework on the server side, which add to the projects distinctiveness.

It is also **more complex** than the other projects in the course.
- As said above, it utilises Vue and Django Rest Framework.
- It also incorporates heavy usage of multiple third party APIs (for maps and other data).

## Technologies Used
|                                                                                                                              |                                                                                                                                             |                                                                                                                                            |                                                                                                                                                   |
| ---------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Vue.js** <a href="https://v3.vuejs.org/"><img src="space-front/src/assets/readmeimgs/vue.svg" alt="vue" height="200"/></a> | **Django** <a href="https://www.djangoproject.com/"><img src="space-front/src/assets/readmeimgs/django.svg" alt="django" height="200"/></a> | **DRF** <a href="https://www.django-rest-framework.org/"><img src="space-front/src/assets/readmeimgs/drf.png" alt="drf" height="200"/></a> | **PostgreSQL** <a href="https://www.postgresql.org/"><img src="space-front/src/assets/readmeimgs/postgresql.svg" alt="pstgres" height="200"/></a> |


## Folder Structure and Files

### space-api
The server-side Django code lives here.

***manage.py:*** This file does the same thing as django-admin (i.e., Django's command line utility for administrative tasks), and also points to the project settings. It is a standard file created for every project.

***requirements.txt:*** The python modules and libraries necessary for the app.

**config:** Main python package for the project contains overall project settings and project-level urls.\
- ***config/settings.py:*** Project settings (installed apps, middleware, databases, etc)
- ***config/urls.py:*** Project level URLs. Creates the root API view.

**apps:** Contains the various custom apps involved in the project.

- **apps/users:** Contains code related to the handling and storage of user data (auth and profile information). Also contains the logic for various actions such as password reset, forgot password, etc.
  - ***apps/users/models.py:*** Defines the database models for the app. Each model maps to a single table in the database, and contains information about the fields and how information is stored. The Users app has models for User data, User profiles and Forgot Password requests, along with the logic for the custom user manager.
  - ***apps/users/permissions.py:*** Defines the custom permission classes used in the views to block/allow access to anonymous/authenticated/admin users.
  - ***apps/users/serialzers.py:*** Serializers allow for querysets and model instances to be converted into easy to handle datatypes, which can be rendered as JSON — this makes them useful in an API, since data returned must be understandable by javascript. They also provide deserialisation (allowing validated incoming data to be converted into the complex datatypes for storage). The Users app has serialisers for User data and User Profiles.
  - ***apps/users/urls.py:*** App level urls (reset password, forgot password, etc) and API endpoints (users, profiles, etc).
  - ***apps/users/views.py:*** Functions which recieve a web request and return a web response, and also contain the business logic for that particular "page". The Users app has views which return viewsets for auth and profile data, along with views for actions such as resetting passwords.

- **apps/externals:** Contains code (models, views, serialisers, etc) related to the storage and handling of external API data and urls.

- **apps/saves:** Contains code related to saving API results to the user's profile, the search history feature, and the storage of the same.

### space-front
The front-end Vue.js code lives here.

**public:** Static files for the project (which don't go through webpack).

- ***public/index.html:*** The main entry point for the frontend (it provides an element for vue to load into).

**src:** Contains the main content and files for the project.

- **src/assets:** Images and other assets.

- ***src/router/index.js:*** Code for the vue router. Contains all routes and navigation guards.

- ***src/store/index.js:*** Code for the vuex store. Contains data and actions (functions) which should be globally accessible for ease.

- ***src/main.js:*** Initialises the main vue component into index.html, and sets up plugins, third party components, UI libraries, etc.

- ***src/App.vue:***  Root component of the application. Defines the page template, and all the router views (via the router) load into this.

- **src/views:** Contains single-file Vue components. These function as page views, and are accessed by at least one route.
  - **src/views/Externals:** Vue files for the external API Query pages (ISS, Asteroids, Mars Rovers and Exoplanets).
  - Authentication related pages (***src/views/LogIn.vue***, ***src/views/Register.vue***, ***src/views/ResetPassword.vue***, ***src/views/ForgotPassword.vue***, ***src/views/ForgotReset.vue***).
  - ***src/views/Profile.vue:*** User profile page.
  - ***src/views/UserSearch.vue:*** Searching users by email.
  - ***src/views/Explore.vue:*** Navigation page for external API Queries.
  - ***src/views/Feedback.vue:*** Feedback form for logged in users.
  - ***src/views/Home.vue:*** The landing page for the site.
  - ***src/views/NotFound404.vue*** Utlity page for invalid routes.

- **src/components:** Also contains single-file Vue components. However, these aren't page views, and are used inside other vue components. These aren't accessed directly by a route.
  - ***src/components/Footer.vue***, ***src/components/Navbar.vue*** and ***src/components/Skeleload.vue*** (skeleton shown while content is loading).
## Running the Project Locally

### Setting up the Django Rest Framework API
1. Must have Python 3 running.
2. Clone the repo and cd into the `space-api` directory.
3. Create `virtualenv venv` and activate `.\venv\scripts\activate` a virtual environment. 
4. Install dependencies: `pip install -r requirements.txt`
5. Create an admin user for logging into the Django admin interface and accessing the API otherwise: `python manage.py createsuperuser`
6. Make migrations. `python manage.py makemigrations`
7. Run migrations: `python manage.py migrate`
8. Generate a `SECRET_KEY` and add it to an `.env` file in the root directory in the format `SECRET_KEY: your-secret-key`. You can use this method to quickly generate one: `python -c "import secrets; print(secrets.token_urlsafe())"`
9. Create a PostgreSQL database (name it `space_db`), and add `DB_USER` (username which can access the databse) and `DB_PWD` (password for the same user) to the `.env` file. Alternatively, change the database settings to use sqlite/other database.
10. Add `EMAIL` and `EMAIL_PWD` for the email you would like to use to send forgot password links, and receive feedback on.
11. Generate a google maps API key from [this link](https://developers.google.com/maps/documentation/embed/map-generator), and add it to `.env` in the `MAP_KEY` environment variable.
12. Run the app: `python manage.py runserver`

### Setting up the Vue.js front end
1. Cd into the `space-front` directory.
2. Run `npm install`.
3. Run `npm run serve` to create a development build of the web app.

# Objective and Features

## Feature Overview
- A CRUD (Create, Read, Update, Delete) app at its core, coupled with moderate usage of third party APIs.
- Browseable REST API.
- Token-based authentication.
- Forgot/Reset password functionality.
- (TODO) Social Auth.

- Access multiple space-related APIs via an easy to use interface.
- Save results to your profile.
- Social Features: Public profiles.
- Fully responsive for mobiles and tablets.
- Dark Mode.
- (TODO) Progressive Web App.

## API Documentation

**/api-token-auth**
- POST (will return token for storage)

**/api-auth**
- For logging into the browseable API.

### Prefix:
/api/v1

**NOTE: You must be logged in.**

### Users

**/users/auths**
- GET
- POST (account creation)
  
**/users/auths/:id**
- GET
- PATCH (only for that user and admins)
- DELETE (only for admins)

**/users/profiles** - User Profile
- GET

**/users/profiles/:id**
- GET
- PATCH (only for that user and admins)

**/users/me** - Current logged in User
- GET

**/users/actions/logout**

**/users/actions/reset** - Password Reset

**/users/actions/forgot** - Forgot Password

**/users/actions/token-check** - Post-Forgot Password Reset

**/users/actions/feedback**

### Saves

**/saves** - Saved Posts
- GET
- POST
- DELETE (that user and admins)

**/history** - User history
- GET (that user and admins)
- POST
  
### Externals

**/externals** - External APIs available.
- GET (everyone, rest for admins only)
- POST
- DELETE
- PATCH
- PUT

**/externals/actions/iss/data** - Current position of the ISS.
- GET

**/externals/actions/iss/loc** - Country code, timezone and map url.
- POST

## Frontend
The app is designed to be easy to use. The user can login by creating an account (or using their GitHub account), and head to the Explore page, which details all the APIs currently available. On selection of any of the available APIs, the user can then enter the query parameters (if applicable) in an easy to use form, and wait for the response on submission. Once the response has arrived, the user will have an option to save the response to their public profile (which can be viewed by other users) for future reference. These saved posts can also be deleted later on. Their profile will also house their search history for any API that involves user-entered search paramters (this history will not be visible to other users). Further, the user will have the option to reset their password, and to submit a Forgot Password request if needed.
### Third-Party APIs used
- Not an API, but the collection at [NASA Open APIs](https://api.nasa.gov/) is what gave me the original idea for the web app.
- [Google Maps API](https://developers.google.com/maps/apis-by-platform)
- [NASA Exoplanet Archive](https://exoplanetarchive.ipac.caltech.edu/docs/program_interfaces.html)
- [Where the ISS at?](https://wheretheiss.at/)
- [Mars Photo API](https://github.com/chrisccerami/mars-photo-api)
- [Asteroids - Near Earth Objects Web Service](https://github.com/SpaceRocks/)

I also used [PrimeVue](https://primefaces.org/primevue/) for the UI Library.

# Learnings and Experiences

# Gallery
