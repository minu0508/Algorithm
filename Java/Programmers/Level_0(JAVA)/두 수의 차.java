class Solution {
    public int solution(int num1, int num2) {
        int answer = 0;
        int minnum = -50000;
        int maxnum = 50000;
        if (minnum <= num1 || minnum <= num1 && maxnum <= num2 || num2 <= minnum) {
            answer = num1 - num2;
        }
        return answer;
    }
}