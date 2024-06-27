import requests

# ActiveMQ 웹 콘솔 URL
url = "http://192.168.56.1:61616/admin"

# 기본 인증 정보
auth = ('admin', 'admin')

try:
    response = requests.get(url, auth=auth)
    if response.status_code == 200:
        print("접속 성공!")
    else:
        print(f"접속 실패, 상태 코드: {response.status_code}")
except requests.exceptions.RequestException as e:
    print(f"접속 오류: {e}")
