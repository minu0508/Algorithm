class Solution {
    public int[] solution(String[] strlist) {
        int[] answer = new int[strlist.length];
        for (int i = 0; i < strlist.length; i++) {
            int word_len = strlist[i].length();
            answer[i] = word_len;
        }
        return answer;
    }
}