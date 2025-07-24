// 없는 숫자 더하기
// https://school.programmers.co.kr/learn/courses/30/lessons/86051

#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

int solution(int numbers[], size_t numbers_len) {
    int answer = 0;
    bool check[10] = {};
    
    for (int i = 0; i < numbers_len; i++) {
        check[numbers[i]] = true;
    }
    
    for (int i = 1; i < 10; i++) {
        if (!check[i]) {
            answer += i;
        }
    }
    
    return answer;
}