package coding_interview_solutions;

import java.util.HashMap;

public class TwoSum2 {

    public int[] twoSum2(int[]nums,int target){

        int[] result2 = new int[2];
        if(nums==null || nums.length==0){
            return result2;
        }

        HashMap<Integer,Integer> dic = new HashMap<>();
        for(int i=0;i<nums.length;i++){

            dic.put(nums[i],i);
            System.out.println(dic);
            int k = target-nums[i];
            if(dic.containsKey(k)){
                result2[0] =dic.get(k);
                result2[1] = i;
                return result2;
            }dic.put(nums[i],i);

            //System.out.println(dic);


        }return result2;

    }
}
