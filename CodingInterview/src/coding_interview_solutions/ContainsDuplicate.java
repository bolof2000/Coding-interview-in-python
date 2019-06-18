package coding_interview_solutions;

import java.util.HashMap;

public class ContainsDuplicate {

    public boolean duplicateWithDistanceK(int[]nums,int k){

        int n = nums.length;
        HashMap<Integer,Integer> map = new HashMap<>();
        for(int i=0;i<n;i++){
            if(map.containsKey(nums[i]) && i-map.get(nums[i])<k){

                return true;


            }map.put(nums[i],i);
        }

        return false;
    }
}
