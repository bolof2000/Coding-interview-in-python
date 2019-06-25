package coding_interview_solutions;

import java.util.Arrays;
import java.util.HashMap;

public class Anagram {

    public boolean anagramSolution(String s1,String s2){

        char[] ch = s1.toCharArray();
        char[] ch2 = s2.toCharArray();

        Arrays.sort(ch);
        Arrays.sort(ch2);
        return Arrays.equals(ch,ch2);



    }


        }






