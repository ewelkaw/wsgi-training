# WSGI training repository. 
How to run:
  - make run

# WSGI -> Web Server Gateway Interface
WSGI is not a server it is just an interface specification by which server and application communicate (PEP 3333). 

WSGI apps need to implement: 
`server <-> WSGI interface <-> application`

1. Client make a request.
2. Request is passed to application.
3. Response is send back to the client.
