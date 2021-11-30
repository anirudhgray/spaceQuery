# API

### Prefix:
/api/v1

**/users**
Root API for the users app.

**NOTE: You must be logged in.**

**/users/auths**
- GET
- POST
  
**/users/auths/:id**
- GET
- PATCH (only for that user and admins)
- DELETE (only for admins)

**/users/profiles**
- GET

**/users/profiles/:id**
- GET
- PATCH (only for that user and admins)
