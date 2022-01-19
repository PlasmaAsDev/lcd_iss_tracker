import time
import serial
import requests
import json

url_iss = "http://api.open-notify.org/iss-now.json" # Api to get location


ser = serial.Serial('replace-with-your-com-port', 9600, timeout=0.050) # replace "replace-with-your-com-port" with your com port 

def get_iss_location(): # getting and parsing data
    response = requests.get(url=url_iss)
    obj = json.loads(response.content)
    lat = f"lat = {float(obj['iss_position']['latitude'])}" 
    lon = f"lon = {float(obj['iss_position']['longitude'])}"

    while len(lat) < 16:
        lat = lat + " "

    while len(lon) < 16:
        lon = lon + " "

    final_location = f"{lon}{lat}"
    return final_location.encode()


if __name__ == "__main__":
    while True:
        location = get_iss_location()
        ser.write(location)
        print("Data sent")
        time.sleep(5) #Update the location every 5 seconds

