import requests


def random():
    req_Data = {
        "jsonrpc": "2.0",
        "method": "generateIntegers",
        "params": {
            "apiKey": "bd4e7f16-4777-494f-8c30-b1f05b765ace",
            "n": 2,
            "min": 1,
            "max": 6,
            "replacement": True,
            "base": 10
        },
        "id": 26657
    }

    response = requests.post('https://api.random.org/json-rpc/1/invoke', json=req_Data)
    response.raise_for_status()
    json = response.json()
    data = json['result']['random']['data']
    return data
