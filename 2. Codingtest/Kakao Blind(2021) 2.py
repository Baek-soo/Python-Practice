# 1단계 소문자 치환
# 2단계 '-', '_', '.'를 제외한 문자는 모두 지운다
# 3단계 '.'가 2번 이상 나올수 없다
# 4단계 '.'가 처음이나 끝에 위치하면 제거
# 5단계 빈문자열이라면 'a'를 대입
# 6단계 16개 이상이면 처음 15개를 제외하고 모두 제거 만약 제거하고 마침표가 마지막에 존재한다면 마침표 제거
# 7단계 길이가 2자 이하라면 new_id의 마지막 문자를 길이가 3이 될때까지 반복해서 끝에 붙인다

import re
def solution(new_id):
    st = new_id
    st = st.lower() #소문자 구별
    st = re.sub('[^a-z0-9\-_.]','', st) #저거 이외에는 제거
    st = re.sub('\.+', '.', st) #.가 2개 이상있으면 한개로 변겅
    st = re.sub('^[.]|[.]$', '', st) #.으로 시작하거나 끝나면 없앤다
    st = 'a' if len(st) == 0 else st[:15] #빈문자열이라 'a'를 대입
    st = re.sub('^[.]|[.]$', '', st) #.으로 시작하거나 끝나면 없앤다
    st = st if len(st) > 2 else st + "".join([st[-1] for i in range(3-len(st))]) #길이가 2개 이하이면 [-1]에것을 붙여준다
    return st

string = ''
print(solution(string))
