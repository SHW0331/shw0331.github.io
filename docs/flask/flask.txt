---
layout: default
<<<<<<< HEAD
title: python
nav_order: 5
has_children: true
permalink: /docs/flask
---

# Flask
본 문서는 Flask 공식 문서를 참고하여 작성되었습니다.
{: .fs-6 .fw-300 }

- Flask Version

- link : https://flask.palletsprojects.com/en/3.0.x/installation/#python-version
- link : https://pypi.org/project/python-steam-api/
- link : 

# 폴더 구조
steamproject/
│
├── app.py                # Flask 애플리케이션 파일
├── templates/            # HTML 파일을 저장할 폴더
│   └── main.html         # main 페이지 HTML 파일
├── static/               # CSS, JavaScript 파일을 저장할 폴더
│   ├── css/
│   │   └── style.css     # CSS 파일
│   └── js/
│       └── script.js     # JavaScript 파일


1. 게임 뉴스 포털
사용 API: ISteamNews
아이디어: Steam 게임들의 최신 뉴스를 제공하는 웹사이트를 만들 수 있습니다. 이 사이트에서는 특정 게임에 대한 업데이트, 패치 노트, 이벤트 정보 등을 사용자에게 실시간으로 보여줄 수 있습니다. 뉴스 피드를 모아서 사용자들이 관심 있는 게임의 최신 소식을 쉽게 확인할 수 있는 대시보드 형태로 제공할 수 있습니다.
추가 기능: 뉴스에 대한 사용자 댓글 또는 좋아요 기능을 추가하면 소통의 장이 될 수 있습니다.
2. 게임 통계 및 리더보드 사이트
사용 API: ISteamUserStats
아이디어: 각 게임의 전 세계 플레이어들의 통계 데이터를 실시간으로 보여주는 리더보드 웹사이트를 만들 수 있습니다. 예를 들어, 게임 내에서 가장 많이 사용된 무기, 가장 높은 점수를 기록한 플레이어, 각국의 통계 등을 시각화하여 보여줄 수 있습니다.
추가 기능: 실시간 업데이트, 특정 게임 또는 기간에 따른 통계 필터링 기능을 제공하면 더 유용할 것입니다.
3. Steam 사용자 프로필 조회 사이트
사용 API: ISteamUser
아이디어: Steam 사용자들의 프로필을 조회하고, 게임 활동, 친구 목록, 최근 플레이한 게임 등의 정보를 제공하는 사이트를 만들 수 있습니다. 이를 통해 사용자가 자신의 친구들 또는 유명 플레이어의 게임 플레이 시간을 확인하거나 비교할 수 있습니다.
추가 기능: 커뮤니티 기능을 추가하여 서로 친구 추가나 메시지 주고받기가 가능하도록 할 수 있습니다.
4. Team Fortress 2 아이템 마켓
사용 API: ITFItems_440
아이디어: Team Fortress 2에서 사용되는 아이템 데이터를 제공하는 마켓 웹사이트를 만들 수 있습니다. 이를 통해 특정 플레이어의 아이템을 조회하거나, 시장 가격 변동, 희귀 아이템 트래킹 등을 제공할 수 있습니다. 아이템 거래 플랫폼과도 연동하여 실제 거래 정보를 제공하면 흥미로운 마켓 사이트가 될 수 있습니다.
추가 기능: 사용자 간의 거래 알림 및 추천 시스템을 구축할 수 있습니다.

- pip install
pip install python-steam-api

## venv : Virtual Environment

- fast memo
mkdir steamproject
cd steamproject
py -3 -m venv .venv

- venv exec
.\.venv\Scripts\activate

- flask
python app.py

```py
from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello, Steam API Project"

if __name__ == '__main__':
    app.run(debug=True)
```
# app = Flask(__name__)
app : 객체는 애플리케이션의 루트 객체로서 라우팅, 설정 및 요청 처리 등의 역할
Flask(__name__) : 현재 실행 중인 모듈의 이름을 나타내며, Flask는 이 정보를 통해 현재 파일이 애플리케이션의 시작점인지 판단

# @app.route('/')
데코레이터 : @app.route('/')는 Flask에게 '/'라는 URL 경로(루트 경로)가 요청되었을 때, 어떤 함수를 실행해야 하는지 지정, 즉 이 URL이 호출될 때 아래 정의된 home() 함수가 실행

# if __name__ == '__main__':
이 코드는 파이썬 스크립트가 직접 실행될 때만 특정 코드를 실행하도록 하는 구문이다. 파이썬에서는 각 파일이 실행될 때마다 __name__이라는 특별한 변수가 설정되는데, 그 값이 '__'main__' 이면 해당 파일이 현재 직접 실행되고 있다는 의미이다.

# 왜 사용하나요?
이 구조는 모듈화를 지원하기 위해 사용됩니다. 특정 파일이 직접 실행될 때는 app.run() 같은 서버 실행 코드를 돌리고, 다른 파일에서 이 파일을 임포트해서 사용할 때는 그런 코드를 실행하지 않도록 할 수 있습니다.

직접 실행: 해당 파일이 메인 프로그램처럼 동작하게 하고 싶을 때.
임포트: 다른 파일에서 재사용할 수 있는 모듈로 활용하고 싶을 때.

# app.run(debug=True)
app.run()은 Flask 애플리케이션을 실행하는 함수
debug=True --> Flask 개발 모드


# link 태그 차이
<link rel="stylesheet" href="../static/css/style.css">

--> url 주소를 이용한 파일 추가
Flask 프레임워크에서 사용되는 구문입니다. url_for 함수는 Flask 앱의 정적(static) 디렉터리 안에서 filename에 지정된 파일을 찾아 URL을 동적으로 생성합니다.
<link rel="stylesheet" href="{{ url_for('static', filename='css/style.css') }}">

# 폴더구조
app/: 애플리케이션 코드가 들어가는 폴더입니다.
__init__.py: Flask 애플리케이션을 초기화하는 파일입니다.
routes.py: 라우팅을 정의하는 파일입니다.
models.py: 데이터베이스 모델을 정의하는 파일입니다.
forms.py: WTForms를 사용하여 폼을 정의하는 파일입니다.
templates/: HTML 템플릿 파일을 저장하는 폴더입니다.
static/: CSS, JS, 이미지 파일과 같은 정적 파일을 저장하는 폴더입니다.
config.py: 애플리케이션 설정을 담는 파일입니다.
run.py: 애플리케이션을 실행하는 파일입니다.

# from steam_web_api import Steam
=======
title: flask
nav_order: 2
has_children: true
permalink: /docs/splunk
---

# Flask

본 문서는 Flask 공식 문서 참고
{: .fs-6 .fw-300 }

Version: Flask 3.0.3


>>>>>>> 96edf119d221332068e4ae8306d4e7ced90af90c
