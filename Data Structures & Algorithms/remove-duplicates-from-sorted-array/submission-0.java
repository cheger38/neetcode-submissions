class Solution {
    public int removeDuplicates(int[] nums) {
        if (nums.length == 0) return 0;

        int i = 0;
        int r = 1;

        while (r < nums.length) {
            if (nums[r] != nums[i]) {
                i++;
                nums[i] = nums[r];
            }
            r++;
        }

        return i + 1;
    }
}
