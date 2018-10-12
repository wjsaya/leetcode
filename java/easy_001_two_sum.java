
class Solution2 {
    /**
     * 
     * @param nums 原数组
     * @param target 目标数字
     * @return 结果数组
     */
    public int[] twoSum(int[] nums, int target) {
        int[] re = new int[2];
        for(int i=0; i<nums.length; i++) {
            for(int j=i; j<nums.length; j++) {
                int temp = nums[i] + nums[j];
                if(temp == target) {
                	if(i == j)
                		continue;
                    re[0] = i;
                    re[1] = j;
                    // System.out.println(nums[i] + "+" + nums[j] + "=" + temp);
                }
            }
        }
        return re;
    }
}
/**   
        # 根据数组下标i(0-->n)遍历原数组，值放入valueNow
        # 找dict[valueNow]
        #   如果找到了
        #       说明valueNow是另一个数的互补数
        #       因此待返回的下标是 TOfind-valueNow 的下标与 valueNow 的下标
        #       即  dict[valueNow] 和 i ，构建一个 HashMap 直接返回即可。
        #       return [dict[valueNow], i]
        # 	如果没找到
        #       那么valueNow暂时没有互补数，将其存入 HashMap dict[TOfind-valueNow] , 值为 当前下标。

 */
class Solution {
    /**
     * 
     * @param nums 原数组
     * @param target 目标数字
     * @return 结果数组
     */
    public int[] twoSum(int[] nums, int target) {
        HashMap<Integer, Integer> tempDict = new HashMap<>();
        for(int i=0; i<nums.length; i++) {
            int valueNow = nums[i];
            
            if (tempDict.containsKey(valueNow)) {
            	return new int[] {tempDict.get(valueNow), i};
            }
            else
            	tempDict.put(target - valueNow, i);        	
        }
		return null;
    }
}

public class easy_001_two_sum {
    public static void main(String[] args) {
            int[] numlist = {3, 3};
            Solution test = new Solution();
            int[] result = {};
            result = test.twoSum(numlist, 6);
            System.out.println(result[0]);
            System.out.println(result[1]);            
    }
}