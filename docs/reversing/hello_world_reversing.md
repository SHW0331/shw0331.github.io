---
layout: default
title: Hello World!
nav_order: 1
parent: reversing
permalink: /docs/reversing
---

# Hello World! 리버싱
"Hello World!" 프로그램을 디버깅
{: .fs-6 .fw-300 }

---

## 1.0 Hello World! 프로그램
- Visual C++를 이용해 C 언어 HelloWorld.cpp를 빌드
- 소스코드는 Windows API를 사용하여 "Hello World!" 가 담긴 MessageBox 생성 프로그램
![](../../assets/images/reversing/HelloWorld/1.png)
```cpp
#include "windows.h"
#include "tchar.h"

int _tmain(int argc, TCHAR* argv[])
{
	MessageBox(NULL,
		L"Hello World!",
        L"Bite98",
		MB_OK)
		;
	return 0;
}
```

## 1.2 취약 대상
Apache OFBiz 버전 18.12.14 이전

## 1.3 공격 원리
- Apache OFBiz의 웹 애플리케이션에서 엔드포인트를 스캔하여 취약한 엔드포인트 식별
- 취약한 엔드포인트를 통해 접근한 공격자는 관련된 화면 정의 파일에 접근
- 화면 정의 파일에 포함된 화면 렌더링 코드를 악용하여 임의의 악성 코드를 실행
![](../../assets/images/cve-2024-27316/attack.png)
---
