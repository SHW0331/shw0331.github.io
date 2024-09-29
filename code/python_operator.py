# # # 덧셈 연산
# # x = 9
# # y = 8
# # result = x + y
# # print(f'X + Y = {result}')

# # # 뺄셈 연산
# # x = 9
# # y = 8
# # result = x - y
# # print(f'X - Y = {result}')

# # # 곱셈 연산
# # x = 9
# # y = 8
# # result = x * y
# # print(f'X * Y = {result}') # X * Y = 72

# # # 나눗셈 연산
# x = 9
# y = 8
# # result = x // y
# # print(f'X // Y = {result}') # X // Y = 1

# # # 나머지 연산
# # result = x % y
# # print(f'X % Y = {result}') # X % Y = 1

# # # 거듭제곱 연산
# # result = x ** y
# # print(f'X ** Y = {result}') # X ** Y = 430467213

# x = -9
# print(abs(x)) # 9
# print(abs(-x)) # 9

# y = -8.31
# print(abs(y)) # 8.31
# print(abs(-y)) # 8.31

# result = divmod(10, 3)
# print(result) # (3, 1)

# quotient, remainder = divmod(9.5, 2)
# print(f'quotient : {quotient}, remainder : {remainder}') # quotient : 4.0, remainder : 1.5

# result = pow(2, 3)
# print(result) # 8

# result = pow(2, 3, 5) # (2 ** 3) % 5
# print(result) # 3

# x = 3.141592
# y = round(x, 2) # 2(ndigits) : 2자리 소수점 이하 자릿수 반올림
# print(y) 
# z = round(y, 1)
# print(z) #  .3
# k = round(z) # ndigits 생략하면 소수점 아래를 없애고 가장 가까운 정수로 반올림
# print(k) # 

print(round(0.5))  # 출력: 0 (짝수인 0으로 반올림)
print(round(1.5))  # 출력: 2 (짝수인 2로 반올림)
print(round(2.5))  # 출력: 2 (짝수인 2로 반올림)
print(round(3.5))  # 출력: 4 (짝수인 4로 반올림)
print(round(4.5))  # 출력: 4 (짝수인 4로 반올림)
