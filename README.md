# UWB---Indoor-navigation-
Front-end demo app of UWB indoor navigation


*step1* : open the folder " python app " on your vs code.

*step2* : run the Flask server to listen for incoming requests on the terminal :-    python3 flask_server.py

*step3* : send a POST Request via Postman 

 URL    : http://localhost:5000/update_coordinates
 Method : POST
 Body (raw -> json)
 {
    "x":400,
    "y":300
  }
                    
*step4* : run the pygame frontend :-     python3 pygame_frontend.py

*step5* : now hit send on the postman app and anticipate the change in iphone marker on the map.
