package coding_interview_solutions;

public class AnagramHashMap{

    public boolean isAnagram(String s1,String s2){

        //edge check

        if(s1.length() != s2.length()){
            return false;

        }

        int[] map = new int[128];
       int l1 = s1.length();
       int l2 = s2.length();
       for(int i=0;i<l1;i++){
           map[s1.charAt(i)]++;
       }

       for(int j=0;j<l2;j++){
           map[s2.charAt(j)]--;
       }

       for(int i=0;i<map.length;i++){
           if(map[i] != 0) return false;
       }

       return true;
    }


}
