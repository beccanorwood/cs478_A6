# cs478_A6
Author: Rebecca Norwood

Section A: ML Web Server Description

    Overview: This application uses Python Flask, Tensorflow, Keras, 
            and more machine learning libraries/modules to classify
            an image that a user enters via the command line. The image
            is classifed and predicted as either 'rock', 'paper', or 'scissors' 
            using a trained model. 

    Server: The server is created with Python Flask. It has various methods
            and endpoints that take in information from the client (user) and
            process it depending upon the specified HTTP request. These methods
            include the '/' endpoint which displays the server information to the
            client and the '/predict' endpoint predicting the image the client submits. 

Section B: Testing the Web Server and Clients

    Testing the web server relies on making sure that the information is being
    property read from the client and is also being properly returned. This includes
    setting the proper HTTP protocols for each server endpoint. These include GET, POST,
    PUT, and DELETE. When a client makes a get or post request, there needs to be 
    specified parameters for the endpoint that allow for those requests to be made and
    if an endpoint can accept multiple methods, there needs to be conditional statements
    that account for each possibility. This also is true for the client. Just as the server
    needs to accomodate the clients requests, the client needs to send proper requests
    to the server. 


Section C: Screen Captures of Test Run

![Server Command](/screenshots/server_cmd_1.png?raw=true)
![Flask Server](/screenshots/server_cmd_2.png?raw=true)

![Client Command](/screenshots/client_cmd.png?raw=true)
![Client Command with Image (1)](/screenshots/client_cmd_with_img.png?raw=true)
![Client Command with image (2)](/screenshots/client_cmd_with_img2.png?raw=true)