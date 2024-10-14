목표
- 이 문제는 사용자에게 문자열 입력을 받아 정해진 방법으로 입력값을 검증하여 correct 또는 wrong을 출력하는 프로그램이 주어집니다.
- 해당 바이너리를 분석하여 correct를 출력하는 입력값을 찾으세요!

- RDX 값에 "Compar3_the_str1ng" 저장



함수 정리
- RDI : 데이터의 주소를 가리키는 포인터로 사용됩니다. 주로 문자열이나 배열의 주소를 처리할 때 사용
- SUB : 빼기 연산을 수행하는 명령어입니다. 예를 들어 SUB RSP, 0x10은 RSP 레지스터에서 0x10을 뺍니다.
- RSP : RSP는 스택 포인터를 가리키는 레지스터로, 스택에서 현재 위치를 추적합니다. 함수 호출, 로컬 변수 할당
- MOV : 데이터를 이동시키는 명령어
- RAX : 64비트 레지스터로, 함수 호출의 반환값을 저장하거나 연산의 결과를 저장
- QWORD : 64비트(8바이트) 크기의 데이터를 의미
- PTR :  메모리 참조를 나타낼 때 사용
- REL : 상대 주소를 의미합니다. 즉, 현재 위치에서 상대적으로 얼마나 떨어진 주소를 참조
- LEA : LEA는 계산된 주소를 로드하는 명령어
- XOR : XOR는 비트 연산 중 하나로, 두 값의 각 비트를 비교하여 서로 다르면 1을, 같으면 0을 반환
- EAX : AX는 32비트 레지스터로, 64비트 환경에서는 RAX의 하위 32비트 부분
- CALL : 함수를 호출하는 명령어
- JMP : 무조건적으로 지정된 주소로 점프
- ADD : ADD는 더하기 연산을 수행
- POP : POP은 스택에서 값을 꺼내 레지스터나 메모리에 저장하는 명령어


```c
CPU Disasm
Address        Hex dump             Command                                  Comments
7FF6_94371100    40:57              PUSH RDI                                 ; correct, wrong function
7FF6_94371102    48:81EC 30010000   SUB RSP,130
7FF6_94371109    48:8B05 F81E0000   MOV RAX,QWORD PTR [REL 7FF6_94373008]
7FF6_94371110    48:33C4            XOR RAX,RSP
7FF6_94371113    48:898424 20010000 MOV QWORD PTR [RSP+120],RAX
7FF6_9437111B    48:8D4424 20       LEA RAX,[RSP+20]
7FF6_94371120    48:8BF8            MOV RDI,RAX
7FF6_94371123    33C0               XOR EAX,EAX
7FF6_94371125    B9 00010000        MOV ECX,100
7FF6_9437112A    F3:AA              REP STOS BYTE PTR [RDI]
7FF6_9437112C    48:8D0D 05110000   LEA RCX,[REL 7FF6_94372238]              ; ASCII "Input : "
7FF6_94371133    E8 58000000        CALL 00007FF6_94371190
7FF6_94371138    48:8D5424 20       LEA RDX,[RSP+20]
7FF6_9437113D    48:8D0D 00110000   LEA RCX,[REL 7FF6_94372244]              ; ASCII "%256s"
7FF6_94371144    E8 A7000000        CALL 00007FF6_943711F0
7FF6_94371149    48:8D4C24 20       LEA RCX,[RSP+20]
7FF6_9437114E    E8 ADFEFFFF        CALL 00007FF6_94371000
7FF6_94371153    85C0               TEST EAX,EAX
7FF6_94371155    74 0F              JE SHORT 7FF6_94371166
7FF6_94371157    48:8D0D F2100000   LEA RCX,[REL 7FF6_94372250]              ; ASCII "Correct"
7FF6_9437115E    FF15 0C100000      CALL QWORD PTR [REL <&api-ms-win-crt-std
7FF6_94371164    EB 0D              JMP SHORT 7FF6_94371173
7FF6_94371166    48:8D0D EB100000   LEA RCX,[REL 7FF6_94372258]              ; ASCII "Wrong"
7FF6_9437116D    FF15 FD0F0000      CALL QWORD PTR [REL <&api-ms-win-crt-std
7FF6_94371173    33C0               XOR EAX,EAX
7FF6_94371175    48:8B8C24 20010000 MOV RCX,QWORD PTR [RSP+120]
7FF6_9437117D    48:33CC            XOR RCX,RSP
7FF6_94371180    E8 5B010000        CALL 00007FF6_943712E0
7FF6_94371185    48:81C4 30010000   ADD RSP,130
7FF6_9437118C    5F                 POP RDI
7FF6_9437118D    C3                 RETN
```