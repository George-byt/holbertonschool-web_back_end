# 0x07-Session_authentication
The main objective of this project is to implement a Session Authentication.
# Learning Objectives
* What authentication means
* What session authentication means
* What Cookies are
* How to send Cookies
* How to parse Cookies

## Authentication
Authentication is the verification of the credentials of the connection attempt. This process consist of sending the credentials from the remote access client to the remote access server in an either plaintext or encrypted form by using an authentication protocol.
## Session Authentication
A session is a small file, most likely in JSON format, that stores information about the user, such as a unique ID, time of login and expirations, and so on. It is generated and stored on the server so that the server can keep track of the user requests. The user receives some of these details, especially the ID, as cookies that will be sent with every new request, so that the server can recognize the ID and authorize the user’s requests. 