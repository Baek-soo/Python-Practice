# 스코빌 지수 k 이상
# 스코빌 지수가 가장 낮은 두개의 음식을 섞는다
# 섞은 음식 = 가장 맵지 않은 음식의 스코빌 지수 + (두번재로 맵지 않은 음식 스코빌 지수 * 2)
# 스코빌 지수가 k 이상이 될 때 까지 반복한다. 

import heapq

def solution(scoville, k):
    count = 0
    h = []
    for i in scoville:
        heapq.heappush(h, i)
    while h[0] < k:
        try:
            heapq.heappush(h, heapq.heappop(h) + (heapq.heappop(h)*2))
        except IndexError:
            return -1
        count += 1

    return count


#미친 문제 풀이
# import heapq as hq

# def solution(scoville, K):
#     hq.heapify(scoville)
#     count = 0
#     while True:
#         first = hq.heappop(scoville)
#         if first >= K:
#             break
#         if len(scoville) == 0:
#             return -1
#         second = hq.heappop(scoville)
#         hq.heappush(scoville, first + second*2)
#         count += 1  
#     return count