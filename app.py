from client import get_sensordata
import time
import json
import threading


def get_data():
    while True:
        convert_to_json = json.loads(get_sensordata())
        return convert_to_json['coordY']
        time.sleep(5)


data_thread = threading.Thread(target=get_data)
data_thread.daemon = True
data_thread.start()


while True:
    if(get_data() == "test"):
        print("Yes it is test")