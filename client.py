import sys
import json
import requests

URL = "http://localhost:5000/"
PREDICTION_URL = 'http://localhost:5000/predict'


if __name__ == '__main__':
    argument_length = len(sys.argv)

    if argument_length == 1:
        r = requests.get(URL)
        print(r.text)
    else:

        image_file = sys.argv[1]
        payload = {'data': str(image_file)}
        headers = {
            'Content-Type': 'application/json'
        }

        response = requests.post(PREDICTION_URL, headers=headers, data = json.dumps(payload))
        print(response.text, "Status Code: ", response.status_code)