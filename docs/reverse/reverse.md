---
layout: default
title: reverse
nav_order: 3
has_children: true
permalink: /docs/reverse
---

# Reverse Engineering
{: .no_toc }

게임 핵 분석을 위한 기술
{: .fs-6 .fw-300 }

---

## 기초 지식
{: .no_toc }

[Computer Science][Computer Basic]{: .btn .fs-5 .mb-4 .mb-md-0 }
[Binary Code][Binary Code]{: .btn .fs-5 .mb-4 .mb-md-0 }
[Program Language][Program Language]{: .btn .fs-5 .mb-4 .mb-md-0 }

1. TOC
{:toc}

---

## Reverse Engineering?
소프트웨어의 동작을 분석하여 원래의 소스 코드나 구조를 추론하는 과정

## Reversing Tools
- Debugging Tools : 바이너리 파일을 어셈블리어로 재구성
    - Ollydbg
    - IDA PRO
    - Immunity Debugger
    - Windbg

- Static Tools
    - Detour
    - Exeinfo, PEID
    - PEView, Stud_PE, loadPE
    - Strings, Bintext

- Dynamic Tools
    - Autoruns
    - ProcessMonitor
    - ProcessExplorer
    - HijackThis
    - Wireshark

- Other Useful Tools
    - Reflector
    - FFDec, Sothink, RABCD ASM
    - DeDe
    - 010 Editor, Notepad++
    - Cheat Engine

---

[Computer Basic]: https://shw0331.github.io/docs/reverse/computer.html
[Binary Code]: https://shw0331.github.io/docs/reverse/binary.html
[Program Language]: https://shw0331.github.io/docs/reverse/language.html