import coding_interview_solutions.*;

public class Main {

    public static void main(String[] args) {

        TwoSum solution = new TwoSum();

        int[] numbers = {1,2,3,4,5};
        int[] numbers2 = {-10,-10,1,2,3,4,5};

        solution.twoSumSolutions(numbers,9);

        TwoSum2 sol2 = new TwoSum2();
        sol2.twoSum2(numbers,9);
        MaxProductOfThreeNumber mul = new MaxProductOfThreeNumber();
        mul.maxProductNum(numbers);
        mul.maxProductNum(numbers2);
        ContainsDuplicate dup = new ContainsDuplicate();
        dup.duplicateWithDistanceK(numbers,2);

        Anagram ana = new Anagram();
        System.out.println(ana.anagramSolution("bolofinde","finbolode"));
       AnagramHashMap anagram2 = new AnagramHashMap();
       anagram2.isAnagram("bolofinde","bolofin");

       FirstNonDuplicateCharacter first = new FirstNonDuplicateCharacter();
       first.nonDuplicateChar("bolofinde");
       System.out.println(first.nonDuplicateChar("bbolofinde"));
    }
}
