class Solution {
    public int solution(int age) {
        int answer = 0;
        int minnum = 0;
        int maxnum = 120;
        if (minnum <= age || age <= maxnum) {
            answer = 2023 - age;
        }
        return answer;
    }
}