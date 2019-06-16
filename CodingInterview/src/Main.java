import coding_interview_solutions.MaxProductOfThreeNumber;
import coding_interview_solutions.TwoSum;
import coding_interview_solutions.TwoSum2;

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
    }
}
