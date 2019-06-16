

/*
given an array of integers , return indices of the two number such that they add up to a specific target
for example
given numbers [1,3,4,5]  target 9.  find two elements that return the target
 */

public class TwoSum {

    public int[] twoSumSolution(int[]nums, int target){

        int n = nums.length;

        int[] result = new int[2];

        for(int i=0;i<n;i++){

            for(int j=0;j<i+n;j++){
                if(nums[i]+nums[j]==target){

                   result[0] =i;
                    result[1] =j;
                }
            }
        }
        return result;


    }
}

