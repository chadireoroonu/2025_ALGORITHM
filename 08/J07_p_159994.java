// 카드 뭉치
// https://school.programmers.co.kr/learn/courses/30/lessons/159994

class Solution {
    public String solution(String[] cards1, String[] cards2, String[] goal) {
        int i = 0, j = 0, g = 0;
        
        while (g < goal.length) {
            if (i < cards1.length && goal[g].equals(cards1[i])) {
                g++;
                i++;              
            }
            else if (j < cards2.length && goal[g].equals(cards2[j])) {
                g++;
                j++;
            }
            else {
                return "No";
            }
        }

        return "Yes";
    }
}