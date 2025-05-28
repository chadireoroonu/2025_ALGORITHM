# 숫자 문자열과 영단어
# https://school.programmers.co.kr/learn/courses/30/lessons/81301

# 1
# def solution(s):
#     nums = {0: 'zero', 1: 'one', 2: 'two', 3: 'three', 4: 'four',
#     	    5: 'five', 6: 'six', 7: 'seven', 8: 'eight', 9: 'nine'}
    
#     for i in range(10):
#         if nums[i] in s:
#             s = s.replace(nums[i], str(i))
    
#     return int(s)

# 2
def solution(s):
    nums = {'zero': '0', 'one': '1', 'two': '2', 'three': '3', 'four': '4',
            'five' : '5', 'six': '6', 'seven': '7', 'eight': '8', 'nine': '9'}
    
    for word, num in nums.items():
        s = s.replace(word, num)

    return int(s)