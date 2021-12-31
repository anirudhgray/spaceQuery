After login, send a get request to the profiles endpoint. Filter for the logged in user.
Return user id and "new" field value. If "new" is True, ask for Profile information. Otherwise continue directly to the profile.

NOTES: Should have just used djoser...
Had some issues with token in browser cache.
Add docstrings
Make it possible to handle large number of results in the user query.

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
