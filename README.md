# API

**/api/v1/users/auths**
- POST (account creation)

**/api-token-auth**
- POST (will return token for storage)

**/api-auth**
- For logging into the browseable API.

### Prefix:
/api/v1

**/users**
Root API for the users app.

**NOTE: You must be logged in.**

**/users/auths**
- GET
  
**/users/auths/:id**
- GET
- PATCH (only for that user and admins)
- DELETE (only for admins)

**/users/profiles**
- GET

**/users/profiles/:id**
- GET
- PATCH (only for that user and admins)
