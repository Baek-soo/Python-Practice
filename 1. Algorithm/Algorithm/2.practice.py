str1 = '''
1. add
2. sub
3. quit
'''
while True:
    print(str1)
    number = int(input('번호를 입력하세요 : '))
    if number == 1:
        print('\n덧셈')
        num1 = int(input('첫번째 숫자 : '))
        num2 = int(input('두번째 숫자 : '))
        result = num1 + num2
        print(f'{num1}과 {num2}의 합은 {result}입니다.')
        break
    elif number == 2:
        print('뺄셈')
        num1 = int(input('첫번째 숫자 : '))
        num2 = int(input('두번째 숫자 : '))
        result = num1 - num2
        print(f'{num1}에서 {num2}을 빼면 {result}입니다. ')
        break
    elif number == 3:
        print('종료')
        break
    else:
        print('잘못 입력됬습니다.')

    