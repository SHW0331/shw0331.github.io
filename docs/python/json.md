---
layout: default
title: json
parent: python
nav_order: 1
---

# JSON
{: .no_toc}

본 문서는 python docs 공식 문서를 참고하여 작성되었습니다.
{: .fs-6 .fw-300 }

[json Docs][python json docs]{: .btn .fs-5 .mb-4. mb-md-0 }

1. TOC
{:toc}
---

## JSON 정의
**"JSON(JavaScript Object Notation)"**은 데이터를 저장하고 전송하기 위한 경량의 데이터 형식으로, 텍스트 기반의 구조화된 데이터를 표현하는데 사용

## JSON 유형
- Object : Key-Value 쌍의 집합으로 표현
{: .no_toc}

```json
{
    "name": "shw",
    "age": 27,
}
```

<br>
- Array : 값들의 목록으로 표현
{: .no_toc}

```json
["Python","C++","Javascript"]
```

<br>
- String : 텍스트 데이터 
{: .no_toc}

```json
"Test JSON (String)"
``` 

<br>
- Number : 숫자를 나타냄
{: .no_toc}

```json
1234567890
```

<br>
- Boolean : True 또는 False 값을 나타냄
{: .no_toc}

```json
true
```

<br>
- null : 아무런 값도 나타내지 않음
{: .no_toc}

```json
null
```

---

## import
- JSON 모듈을 사용하기 위해 json 내장 모듈을 import

```py
import json
```

## json_dumps
- Python 객체를 JSON 형식의 문자열로 변환

```py
def json_dumps(data):
    data_dumps = json.dumps(data)
    return data_dumps
```

## json_loads
- JSON 형식의 문자열을 Python 객체로 변환
{: .warning }
> Python에서 정의된 json 형식 데이터는 json.loads 사용 불가   
> json.dumps 함수를 사용하여 json 데이터 객체로 변환 후 사용 가능   

```py
def json_loads(data):
    data_loads = json.loads(data)
    data_loads['content'] = "json loads Test"
```

## json_dump
- Python 객체를 JSON 파일로 직렬화

```py
def json_dump(data, path):
    with open(path, "w") as json_file:
        json.dumps(data, json_file)
```





---

[python json docs]: https://docs.python.org/ko/3/library/json.html