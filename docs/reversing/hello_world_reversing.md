---
layout: default
title: Hello World!
nav_order: 1
parent: reversing
---

# Hello World! 리버싱
"Hello World!" 프로그램을 디버깅
{: .fs-6 .fw-300 }

---

## 1.0 Hello World! 프로그램
- Visual C++를 이용해 C 언어 HelloWorld.cpp를 빌드
- 소스코드는 Windows API를 사용하여 "Hello World!"가 담긴 MessageBox 출력
- HelloWorld.cpp 빌드 후, 실행 파일(HelloWorld.exe) 생성

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

## 1.1 HelloWorld.exe 디버깅
- HelloWorld.exe 파일을 OllyDbg로 열기

{: .note-title }
> **OllyDbg**는 Windows 환경에서 동작하는 **디버거(Debugger)**로, 주로 어셈블리 언어 수준에서 프로그램의 실행을 분석하는 데 사용
> [OllyDbg](https://www.ollydbg.de/)

- 실행 파일을 디버깅(Debugging)하여 어셈블리 언어로 변환 된 main() 함수 찾기


## 1.3 공격 원리
- Apache OFBiz의 웹 애플리케이션에서 엔드포인트를 스캔하여 취약한 엔드포인트 식별
- 취약한 엔드포인트를 통해 접근한 공격자는 관련된 화면 정의 파일에 접근
- 화면 정의 파일에 포함된 화면 렌더링 코드를 악용하여 임의의 악성 코드를 실행
![](../../assets/images/cve-2024-27316/attack.png)
---
