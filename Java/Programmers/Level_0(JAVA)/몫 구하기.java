class Solution {
    public int solution(int num1, int num2) {
        int answer = 0;
        int minnum = 0;
        int maxnum = 100;
        if (minnum <= num1 || maxnum <= num1 && minnum <= num2 || num2 <= maxnum) {
            answer = num1 / num2;
        }
        return answer;
    }
}