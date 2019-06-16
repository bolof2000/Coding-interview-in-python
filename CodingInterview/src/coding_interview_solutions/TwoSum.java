package coding_interview_solutions;

import java.util.HashMap;

public class TwoSum {


    public int[] twoSumSolutions(int[]nums,int target){

        int[] result = new int[2];

        for(int i =0;i<nums.length;i++){
            for(int j=0;j<i+1;j++){

                if(nums[i]+nums[j]==target){

                    result[0] =i;
                    result[1] = j;
                    return result;
                }

            }

        }
        return result;

        // time complexity N*2 - not efficient
        // efficient solution is to use hashmap


    }

    }

