# F1_project

install docker
download and unzip the contents repository
cd into the root folder(F1_Project) and run:    docker-compose build
                                                docker compose up
give everything a minute or to to come up and then test the API at: http://localhost:5000/
to connect to the db you can use the following informations:

    ServerHost: localhost
    Database: ergastdb
    Username: root
    Passwort: f1

    Remember to use SSL and allow public key retrieval.

At the moment the DB data is updated to 28/03/2017

run the file "position_comparer HAM-VET.py" to retrieve data from the DB