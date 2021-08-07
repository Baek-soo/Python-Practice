#마라톤 참여선수 participant
#완주 선수 이름 completion
#와주하지 못한 선수 return

def solution(participant, completion):
    participant.sort()
    completion.sort()
    for i in range(len(participant)):
        if participant[i] != completion[i]:
            return participant[i]

# 미친 문제 풀이
# import collections 
# def solution(participant, completion):
#     answer = collections.Counter(participant) - collections.Counter(completion)
#     return list(answer.keys())[0]
#         #ex. member = {'ID' : 102, 'Name' : 'fofofofo', 'Address' : 'seoul'} 
#         #print(member.keys())
#         #---> deic_keys(['ID', 'Name', 'Address'])
#         #print(list(member.keys()))
#         #---> ['ID', 'Name', 'Address']