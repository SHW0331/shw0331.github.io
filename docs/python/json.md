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

## JSON 이란?
**"JSON(JavaScript Object Notation)"**은 데이터를 저장하고 전송하기 위한 경량의 데이터 형식으로, 텍스트 기반의 구조화된 데이터를 표현하는데 사용

## JSON 유형
- Object : Key-Value 쌍의 집합으로 표현
```json
{
    "name": "shw",
    "age": 27,
}
```

- Array : 값들의 목록으로 표현
```json
["Python","C++","Javascript"]
```

- String : 텍스트 데이터
```json
"Test JSON (String)"
```

- Number : 숫자를 나타냄
```json
1234567890
```

- Boolean : True 또는 False 값을 나타냄
```json
true
```

- null : 아무런 값도 나타내지 않음
```json
null
```

---
## Python JSON
{: .no_toc }

2. TOC
{:toc}

# import
- JSON 모듈을 사용하기 위해 json 내장 모듈을 import
```py
import json
```
# 



---

[python json docs]: https://docs.python.org/ko/3/library/json.html