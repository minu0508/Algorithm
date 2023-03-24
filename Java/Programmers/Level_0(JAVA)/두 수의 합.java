class Solution {
    public int solution(int num1, int num2) {
        int answer = -1;
        int minnum = -50000;
        int maxnum = 50000;
        if (minnum <= num1 || num1 <= maxnum && minnum <= num2 || num2 <= maxnum) {
            answer = num1 + num2;
        }
        return answer;
    }
}