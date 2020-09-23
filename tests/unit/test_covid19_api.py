import json
import requests


def test_covid19_api():

    response = requests.get('https://api.covid19api.com/country/south-africa/status/confirmed')

    assert response.status_code == 200
    response_json = json.loads(response.content)
    most_recent_cases = response_json[-1]["Cases"]
    print(json.dumps(most_recent_cases, indent=4))

if __name__ == "__main__":
    test_covid19_api()