; hello.asm
section .data
    msg db 'Hello, World!', 0

section .text
global _start
_start:
    mov eax, 4  ; 시스템 호출 번호 (sys_write)
    mov ebx, 1  ; 파일 디스크립터 (stdout)
    mov ecx, msg    ; 메시지 포인터
    mov edx, 13 ; 메시지 길이
    int 0x80    ; 커널 호출

    mov eax, 1  ; 시스템 호출 번호 (sys_exit)
    xor ebx, ebx    ; 종료 코드 0
    int 0x80    ; 커널 호출