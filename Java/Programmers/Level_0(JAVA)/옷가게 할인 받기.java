class Solution {
    public double solution(int price) {
        double answer = 0;
        if (10 <= price && price< 100000) {
            answer = price;
        } else if (100000 <= price && price < 300000) {
            answer = price * 0.95;
        } else if (300000 <= price && price < 500000) {
            answer =  price * 0.9;
        } else if (500000 <= price) {
            answer = price * 0.8;
        }
        answer = (int) answer;
        return answer;
    }
}