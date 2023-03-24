class Solution {
    public String solution(String my_string) {
        String answer = "";
        String[] Save = new String[my_string.length()];
        for (int i = 0; i < my_string.length(); i++) {
            Save[(my_string.length() - i) - 1] = my_string.substring(i, i + 1);
        }

        for (int j = 0; j < Save.length; j++) {
            answer += Save[j];
        }
        return answer;
    }
}