def solution(price, money, count):
    using_time = 1
    new_price = 0
    for using_time in range(using_time, count+1):
        if using_time < count:
            new_price += price
            money = money - new_price
            using_time += 1
    return count*price - money

# 미친 문제 풀이 
# def solution(price, money, count):
#     return max(0, price*(count+1)*count // 2-money)