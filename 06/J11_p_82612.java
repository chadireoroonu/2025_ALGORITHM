// 부족한 금액 계산하기
// https://school.programmers.co.kr/learn/courses/30/lessons/82612

class Solution {
    public long solution(int price, int money, int count) {
        long answer = - money; // 가지고 있는 돈 음수로 저장
        
        // 총 필요한 금액을 계산
        for (int i = 1; i <= count; i++){
            answer += i * price;
        }

        // 부족한 금액 출력 or 부족하지 않으면 0 출력
        return (answer > 0) ? answer : 0;
    }
}