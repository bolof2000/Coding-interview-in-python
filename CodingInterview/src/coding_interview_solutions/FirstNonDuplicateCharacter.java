package coding_interview_solutions;

public class FirstNonDuplicateCharacter {

    public int nonDuplicateChar(String s){

        //edge case check

        if (s == null || s.length() == 0) {

            return -1;
        }
        int[] charArr = new int[26];
        for(int i=0;i<s.length();i++){
            charArr[s.charAt(i)-'a']++;

            //System.out.println(charArr);

        }

        for(int i=0;i<s.length();i++){
            if(charArr[s.charAt(i)-'a']==1){
                return i;
            }
        }

        return -1;
    }
}
