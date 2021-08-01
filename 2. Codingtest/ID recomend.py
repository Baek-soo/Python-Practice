def solution(new_id):
    #1단계 소문자 치환
    new_id.lower()
    #2단계 '-', '_', '.'를 제외한 문자는 모두 지운다. 
    for char in new_id:
        if char not in 'abcdefgfijklmnopqrstuvwxyz0123456789-_.':
            new_id = new_id.replace(char, '')
    #3단계 '.'가 2번 이상 나올수 없다.
    for char in new_id:
        if char in new_id:
            new_id = new_id.replace('..' , '.')
    #4단계 '.'가 처음이나 끝에 위치하면 제거
    if new_id.startswith('.'):
        new_id = new_id[1:]
    if new_id.endswith('.'):
        new_id = new_id[:-1]
    #5단계 빈문자열이라면 'a'를 대입
    if len(new_id) == 0:
        new_id += 'a'
    #6단계 16개 이상이면 처음 15개를 제외하고 모두 제거 만약 제거하고 마침표가 마지막에 존재한다면 마침표도 제거
    if len(new_id) > 15:
        new_id = new_id[:15]
    if new_id.endswith('.'):
        new_id = new_id[:-1]   
    #7단계 길이가 2자 이하라면 new_id의 마지막 문자를 길이가 3이 될때까지 반복해서 끝에 붙인다. 
    if len(new_id) < 3:
        dummy = new_id[-1]
        while len(new_id) < 3:
            new_id += dummy

    return new_id


new_id = 'abaaasdf........asdf'
print(solution(new_id))

