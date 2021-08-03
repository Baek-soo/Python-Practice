#마라톤 참여선수 participant
#완주 선수 이름 completion
#와주하지 못한 선수 return

def solution(participant, completion):
    participant.sort()
    completion.sort()
    for i in range(len(participant)):
        if participant[i] != completion[i]:
            return participant[i]

