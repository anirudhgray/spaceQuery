# spaceQuery API
This is the repo containing the server-side code (Django) for the spaceQuery webapp. The client-side (Vue) code is at [this repository](https://github.com/anirudhgray/space-front).
# API

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

**/externals/actions/iss/data**
- GET

**/externals/actions/iss/loc**
- POST
  
# spaceQuery Frontend
This is the repo containing the clinet-side code (Vue) for the spaceQuery webapp. The server-side (Django) code is at [this repository](https://github.com/anirudhgray/space-api).

# spaceQuery
A webapp built for CS50Web.

**Live Site:** blah de blah blah

- [spaceQuery API](#spacequery-api)
- [API](#api)
    - [Prefix:](#prefix)
    - [Users](#users)
    - [Saves](#saves)
    - [Externals](#externals)
- [spaceQuery Frontend](#spacequery-frontend)
- [spaceQuery](#spacequery)
- [Project Overview](#project-overview)
  - [Distinctiveness and Complexity](#distinctiveness-and-complexity)
  - [Technologies Used](#technologies-used)
  - [Folder Structure and Files](#folder-structure-and-files)
  - [Running the Project Locally](#running-the-project-locally)
- [Objective and Features](#objective-and-features)
  - [Feature Overview](#feature-overview)
  - [API](#api-1)
  - [Frontend](#frontend)
- [Learnings and Experiences](#learnings-and-experiences)
- [Gallery](#gallery)

# Project Overview
At its core, this webapp (I've named it **spaceQuery**) acts as an app for querying a bunch of awesome space related APIs (more info below). It doesn't sound nearly as awesome now that I have written it down, but yeah. Why do I need to be logged in, you ask? Well, I've added some nifty functionality which allows you to save any query results that you particularly like to your user profile for later reference — can't do that without having you signed in. This also allows you to look up other users and look at their saved posts. I'm not entirely sure why I added this, and what purpose it serves, but it's there. Further explanation below.

## Distinctiveness and Complexity
I believe this project is **sufficiently distinct** from the others in the course, and is not based on the 2020 CS50W Pizza project.
- It is not, at it's core, a social media website (while it does incorporate features such as user profiles, they are more of a secondary thing).
- Nor is it an e-commerce based webapp in any way. In fact, it has nothing to do with commerce at all.
- It utilises a javascript frontend framework (Vue) alongside Django Rest Framework on the server side, which add to the projects distinctiveness.

It is also **more complex** than the other projects in the course.
- As said above, it utilises Vue and Django Rest Framework.
- It also incorporates heavy usage of multiple third party APIs (for maps and other data).

## Technologies Used
|                                                                                                                  |                                                                                                                                 |                                                                                                                                |                                                                                                                                       |
| ---------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------- |
| **Vue.js** <a href="https://v3.vuejs.org/"><img src="src/assets/readmeimgs/vue.svg" alt="vue" height="200"/></a> | **Django** <a href="https://www.djangoproject.com/"><img src="src/assets/readmeimgs/django.svg" alt="django" height="200"/></a> | **DRF** <a href="https://www.django-rest-framework.org/"><img src="src/assets/readmeimgs/drf.png" alt="drf" height="200"/></a> | **PostgreSQL** <a href="https://www.postgresql.org/"><img src="src/assets/readmeimgs/postgresql.svg" alt="pstgres" height="200"/></a> |


## Folder Structure and Files

## Running the Project Locally

# Objective and Features

## Feature Overview

## API

## Frontend

# Learnings and Experiences

# Gallery
