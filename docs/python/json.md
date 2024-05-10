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
- 
{: .no_toc}

```py
# Object : Key-Value 쌍의 집합으로 표현
{
    "name": "shw",
    "age": 27,
}

# Array : 값들의 목록으로 표현
["Python","C++","Javascript"]

# String : 텍스트 데이터 
"Test JSON (String)"

# Number : 숫자를 나타냄
1234567890

# Boolean : True 또는 False 값을 나타냄
True
False

# null : 아무런 값도 나타내지 않음
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
    return data_loads
```

## json_dump
- Python 객체를 JSON 파일로 직렬화

```py
def json_dump(data, path):
    with open(path, "w") as json_file:
        json.dump(data, json_file)
        return
```

## json_load
- JSON 파일을 Python 객체로 역직렬화

```py 
def json_load(path):
    with open(path, "r") as json_file:
        data_load = json.load(json_file)
        return data_load
```

## json_indent
- JSON 데이터 들여쓰기 --> 가독성

```py
def json_indent(data):
    data_indent = json.dumps(data, indent=4)
    return data_indent
```

## json_sort_keys
- JSON 데이터 Key 정렬
```py
def json_sort_keys(data):
    data_sort = json.dumps(data, sort_keys=True) # Key sort True
    data_sort = json.dumps(data, sort_keys=False) # Key sort False
    return data_sort

# key sort True : {"a": 1, "b": 2, "c": 3}
# key sort False : {"b": 2, "a": 1, "c": 3}
```

## json_skipkeys
- JSON 데이터의 key가 문자열이 아닌 경우, 무시처리
```py
def json_skipkeys(data):
    data_skipkeys = json.dumps(data, skipkeys=True)
    try:
        data_skipkeys = json.dumps(data, skipkeys=False)
        print("skipkeys False " + data_skipkeys)
    except Exception as e:
        print("skipkeys False : ", e)
    return data_skipkeys

# skipkeys True {"key2": "value"}
# skipkeys False :  keys must be str, int, float, bool or None, not tuple 
```

## json_ensure_ascii
- JSON 데이터에서 ASCII 문자 이외의 문자들을 모두 이스케이프(escape) 처리할지 여부를 결정
```py
def json_ensure_ascii(data):
    data_ascii = json.dumps(data, ensure_ascii=True)
    data_ascii = json.dumps(data, ensure_ascii=False)
    return data_ascii

# ensure ascii True : {"name": "\uc11c\u314e\u3150\uc6d0", "age": 27}
# ensure ascii False : {"name": "서ㅎㅐ원", "age": 27}
```

## json_check_circular
- JSON 데이이터의 순환 참조를 확인하여 데이터를 반환
- 순환 참조는 객체 간에 서로를 참조
```py
def json_check_circular(data):
    data_circular = json.dumps(data, check_circular=True)
    data_circular = json.dumps(data, check_circular=False)
    return data_circular

# check circular True :  Circular reference detected
# check circular False:  maximum recursion depth exceeded while encoding a JSON object
```

## json_allow_nan
- JSON 데이터의 NaN(Not a Number) 값을 허용할지 여부를 설정
```py
def json_allow_nan(data):
    data_nan = json.dumps(data, allow_nan=True)
    data_nan = json.dumps(data, allow_nan=False)
    return data_nan

# allow nan True : {"value": NaN}
# allow nan False :  Out of range float values are not JSON compliant
```

## json_separators
- JSON 데이터의 기본 구분자를 변경
```py
def json_separators(data):
    data_separators = json.dumps(data, separators=(" \ ", "="))
    return data_separators

# {"name"="shw" \ "age"=27}
```
---
[python json docs]: https://docs.python.org/ko/3/library/json.html