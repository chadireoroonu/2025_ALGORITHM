# 두 개 뽑아서 더하기
# https://school.programmers.co.kr/learn/courses/30/lessons/68644

# set 중복 관리
def solution(numbers):
    answer = set()
    for i in range(len(numbers) - 1):
        for j in range(i + 1, len(numbers)):
            answer.add(numbers[i] + numbers[j])

    return sorted(list(answer))


# list 중복 조건문 확인
# def solution(numbers):
#     answer = []
#     for i in range(len(numbers) - 1):
#         for j in range(i + 1, len(numbers)):
#             num = numbers[i] + numbers[j]
#             if num not in answer:
#                 answer.append(num)
                
#     answer.sort()

#     return answer
