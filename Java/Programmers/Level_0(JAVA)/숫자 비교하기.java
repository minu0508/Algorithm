class Solution {
    public int solution(int num1, int num2) {
        int answer = 0;
        int minnum = 0;
        int maxnum = 10000;
        if (minnum <= num1 || num1 <= maxnum && minnum <= num2 || num2 <= maxnum) {
            if (num1 == num2) {
                answer = 1;
            } else {
                answer = -1;
            }
        }
        return answer;
    }
}