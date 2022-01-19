import time
import serial
import requests
import json

url_iss = "http://api.open-notify.org/iss-now.json" # Api to get location


ser = serial.Serial("replace-with-your-com-port", 9600, timeout=0.050) # replace "replace-with-your-com-port" with your com port 

def get_iss_location(): # getting and parsing data
    response = requests.get(url=url_iss)
    obj = json.loads(response.content)
    lat = f"{float(obj['iss_position']['latitude'])}" 
    lon = f"{float(obj['iss_position']['longitude'])}"

    while len(lat) < 7:
        lat = lat + " "

    while len(lon) < 7:
        lon = lon + " "

    final_location = f"{lon[:7]}{lat}"
    return final_location.encode()


if __name__ == "__main__":
    while True:
        location = get_iss_location()
        ser.write(location)
        print("Data sent")
        time.sleep(1) #Update the location every 1 second
