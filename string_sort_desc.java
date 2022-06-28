class Solution {
    public String solution(String s) {
        String answer = "";
        int i = s.length()-1;
        while (i > -1) {
            answer += s.charAt(i);
            i--;
        }
        return answer;
    }
}

// 미완료. 테스트케이스 실패
