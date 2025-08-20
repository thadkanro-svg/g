def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "오류! 0으로 나눌 수 없습니다."
    return x / y

print("원하는 연산을 선택하세요.")
print("1. 더하기")
print("2. 빼기")
print("3. 곱하기")
print("4. 나누기")

while True:
    choice = input("연산을 입력하세요(1/2/3/4): ")

    if choice in ('1', '2', '3', '4'):
        try:
            num1 = float(input("첫 번째 숫자를 입력하세요: "))
            num2 = float(input("두 번째 숫자를 입력하세요: "))
        except ValueError:
            print("잘못된 입력입니다. 숫자를 입력해주세요.")
            continue
        
        if choice == '1':
            print(f"결과: {add(num1, num2)}")
        elif choice == '2':
            print(f"결과: {subtract(num1, num2)}")
        elif choice == '3':
            print(f"결과: {multiply(num1, num2)}")
        elif choice == '4':
            print(f"결과: {divide(num1, num2)}")
        
    else:
        print("잘못된 입력입니다.")
