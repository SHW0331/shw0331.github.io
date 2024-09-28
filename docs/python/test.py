import sys
import argparse

# # input() 함수
# # 가장 기본적인 사용자 입력 함수로, 사용자로부터 한 줄의 입력을 받을 때 사용
# # 입력된 값은 항상 문자열로 반환
# user_input = input("input : ")
# print(f'input() : {user_input}')
# # 출력 값 : input() : shw98

# # sys.stdin.read()
# # sys.stdin.read()는 여러 줄의 데이터를 받을 때 유용, 일반적으로 EOF(End of File)를 통해 입력을 종료
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
# parser = argparse.ArgumentParser(description='argparse : ')
# parser.add_argument('--name', type=str, help='user name')
# args = parser.parse_args()
# print(f'argparser() : {args}')
# # 출력 값 : argparser() : Namespace(name='shw98')




