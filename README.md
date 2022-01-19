## LCD ISS TRACKER

Well, this is a simple project to display the location where the iss is on a lcd

The project use a python script to get the location via an api (http://api.open-notify.org/iss-now.json) and it sends it to the arduino via the Serial. The arduino parse the location and print them on the lcd

*The arduino must be connected to a pc with internet connection*
*Requires LiquidCrystal library for arduino code*

###Installation (python):
`pip install -r requirements.txt`

### Circuit
![circuit](https://user-images.githubusercontent.com/56369290/150192689-cc61816d-5d20-4677-bbe1-f750c3c492a0.png)

