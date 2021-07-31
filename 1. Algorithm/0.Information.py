
#  / : 나눗셈 (ex. 7/4 == 1/75)
#  // : 몫 구하기 (ex. 7//4 == 1)
#  % : 나머지 구하기 (ex. 7%4 == 3)
# : :전체 (ex. winner[2:] 3번째 부터 끝까지)



# end = '' : 아웃풋을 낼때 end의 형식에 맞춰서 결과가 나옴 (ex. print(sum, end = ', ') → 1, 3, 5, 7 이런 형식으로 나옴) 
# \t : 한 줄에 Tab만큼 떨어져서 결과값이 나온다. (ex. print(data[i], end = '\t')) 
# \n : 한줄 띄기
# f'' : print에서 출력에 변수가 포함되어있을때 사용 (ex. print(f'1부터 20까지 홀수의 합: {sum}') ※sum은 변수※)
# float() : 실수형 표현 (ex. float(2) -> 2.0)
# round() : 반올림
# round(실수, n) : 실수를 소숫점 n의자리까지 반올림하여 표현한다. 
# :.2f : 소수점 2번째 자리까지 표현 (ex. print(f'80점 이상 95점 이하인 점수의 평균 : {avg:.2f}') )
# :3  : 앞에 3칸을 잡는다(ex. print(f'{scores[i]:3}점 : {rankings[i]}등')
# $s : 문자열 출력 (ex. print('%s' %S1))
# %d : 정수 출력
# %f : 실수 출력
# .rjust(값) : 값만큼의 칸을 기본으로 잡고 오른쪽으로 들여쓰기 (ex. print(f'{g.name.rjust(6}'))
# .ljust(값) : 값만큼의 칸을 기본으로 잡고 왼쪽으로 들여쓰기 (ex. print(f'{g.name.ljust(6)}'))

# .append(값) : 괄호 안의 값을 리스트 맨 뒤에 추가한다. (ex. data = [1,2,3]   data.append(6) print(data) ->  [1,2,3,6])
# .reverse() : 괄호 안의 리스트를 역으로 취한다. (ex. data.reverse() -> [3,2,1])
# .inset(자리, 값) : 리스트의 '자리'번째에 '값' 넣는다. (ex. data.inset(1,10) -> [1,10,2,3])
# del : 원하는 위치의 값을 지운다. (ex. del data[2] -> [1,2], del data[:] -> [])
# .remove(값) : 괄호 안의 값을 없앤다. (ex. data.remove(1) -> [2,3])
# .pop() : 리스트의 맨 마지막 값을 없앤다. (ex. data.pop() -> [1,2])
# .extend(list2) : 리스트의 마지막에 list2의 값들을 더해준다. (ex. h = [6, 7, 8]  data.extend(h) -> [1,2,3,6,7,8])

# ** : 제곱의 표현 (ex. a = 3 ** 2 -> 9)
# math.pow(상수, 제곱근) : 제곱의 표현(이걸 사용하기 위해서는 import math를 시켜주어야 한다.) 상수^제곱근 (ex. math.pow(3, 2) -> 9)
# math.sqrt() : sqrt

# random.random() : 0.0에서 1.0까지의 실수(float)를 반환한다. (0.0 <= x < 1.0)
# random.uniform(a,b) : a~b사이의 실수(float)를 반환한다. (a <= x <= b)
# random.randint(a,b) : a~b사이의 정수(int)를 반환한다. (a <= x <= b)
# random.randrange(a, b) : a~b사이의 정수(int)를 반환한다. (a <= x < b, a를 입력하지 않는 경우 : 0 <= x < b)
# random.choice(seq) : 매개변수로 seq타입(문자열, 튜플, 리스트)을 받아서 무작위로 하나를 뽑는다. 비어있는 시퀀스 타입의 객체를 넣으면 indexError가 뜬다.  
# random.sample(seq or set, N) : 첫번째 매개변수로 시퀀스 데이터 타입(듀플, 문자열, range, 리스트) 또는 Set 타입을 받을 수 있다. 두번째 매개변수로는 랜덤하게 뽑을 인자의 갯수이다. 이때 뽑는 element가 겹치지 않는다. 
# random.shuffle(seq) : 데이터의 순서를 무작위로 바꾸어준다. 이때 리스트 형태만 가능하다. (문자열, 튜플, range(a,b) 불가능)

#with open("file.txt", 'w') as f:
#   f.write('hello world')
#  ----> sorce파일에 파일 생기고 실행하고 닫힘


