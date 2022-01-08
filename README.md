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
  
