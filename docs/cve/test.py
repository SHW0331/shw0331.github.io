user_input = input("입력 값: ")
num = int(user_input)
print(f"사용자 입력 값: {num}")

# 

for index in range(num):
    if (index % 10) % 3 == 0:
        if index == 0:
            print(f"값 : 0")
        else:
            print(f"값: 짝")
    else:
        print(f"값 : {index}")
