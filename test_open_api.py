import requests
import pytest
import json


@pytest.fixture()
def api(pytestconfig):
    return pytestconfig.getoption("api")

def test_open_api(api):
    URI = "http://api.openweathermap.org/data/2.5/weather?q=bangalore&appid=" + str(api)
    print(URI)
    response = requests.get(URI)
    response_body = response.json()
    assert response.status_code == 200
    assert response_body["name"] == "Bengaluru"
    # print(json.dumps(response.json(), indent=4, sort_keys=True))


def test_open_api_error(api):
    URI = "http://api.openweathermap.org/data/2.5/weather?q=bangalore&appid=" + str(api)
    print(URI)
    response = requests.get(URI)
    response_body = response.json()
    assert response.status_code == 200
    assert response_body["name"] == "Bengaluru"


