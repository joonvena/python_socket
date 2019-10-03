from client import get_sensordata
import time
import json

for i in range(0, 10):
    convert_to_json = json.loads(get_sensordata())
    print(convert_to_json['coordY'])
    i += 1
    time.sleep(5)