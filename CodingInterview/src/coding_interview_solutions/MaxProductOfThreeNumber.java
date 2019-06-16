package coding_interview_solutions;

import java.util.Arrays;

public class MaxProductOfThreeNumber {

    public int maxProductNum(int[]nums){

        int n = nums.length;
        // sort the arrays
        Arrays.sort(nums);

        //calculate two maximum possible results

        // for all positive numbers in the array

        int p1 = nums[n-1]*nums[n-2]*nums[n-3];

        //for negative numbers in a sorted array - the first two numbers are smallest negative numbers

        int p2 = nums[0]*nums[1]*nums[n-1];

        return Math.max(p1,p2);
    }


}
