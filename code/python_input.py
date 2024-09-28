# # input() 함수
# # 가장 기본적인 사용자 입력 함수로, 사용자로부터 한 줄의 입력을 받을 때 사용
# # 입력된 값은 항상 문자열로 반환
# user_input = input("input : ")
# print(f'input() : {user_input}')
# # 출력 값 : input() : shw98

# # sys.stdin.read()
# # sys.stdin.read()는 여러 줄의 데이터를 받을 때 유용, 일반적으로 EOF(End of File)를 통해 입력을 종료
# import sys
# print("여러 줄의 텍스트를 입력하고, Ctrl+D(Unix) 또는 Ctrl+Z(Windows)로 종료")
# multi_line_input = sys.stdin.read()
# print(f"Sys stdin read() : \n{multi_line_input}")
# # 출력 값 : Sys stdin read() :
# # s
# # h
# # w
# # 9
# # 8

# # argparse
# # 명령행 인자를 통해 입력을 받을 수 있는 모듈. 스크립트를 실행할 때 명령행 옵션을 지정 가능
# # python test.py --name 'shw98'
# import argparse
# parser = argparse.ArgumentParser(description='argparse : ')
# parser.add_argument('--name', type=str, help='user name')
# args = parser.parse_args()
# print(f'argparser() : {args}')
# # 출력 값 : argparser() : Namespace(name='shw98')

# # fileinput.input()
# # 파일이나 표준 입력에서 여러 줄을 입력받을 때 사용. 주로 파일에서 데이터를 읽어올 때 유용
# # python test.py test.txt
# import fileinput
# for line in fileinput.input():
#     print(f"line : {line.strip()}")
# # 출력 값 : 
# # line : file input Test
# # line : 1. python
# # line : 2. shw98
# # line : 3. test

# getpass
# 비밀번호와 같은 민감한 데이터를 입력받을 때 사용, 이 함수는 비밀번호를 입력받는 상황에서 유용하며, 사용자가 입력하는 내용을 보이지 않도록 보호
import getpass
password = getpass.getpass('Password : ')
print(f'Password : {'*' * len(password)}')
print(f'실제 값 : 1998')
