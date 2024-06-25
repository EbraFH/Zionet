# tests/integration_test.py
import requests

def test_service_a():
    url = 'http://localhost:5000/service_a'
    response = requests.post(url, json={"value": 5})
    assert response.status_code == 200
    assert response.json() == {"processed_value": 10}

if __name__ == '__main__':
    test_service_a()
    print("Integration test passed!")
