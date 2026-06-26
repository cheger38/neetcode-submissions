class Solution {
    public int removeElement(int[] nums, int val) {
        int base = 0;
        int out = 0;

        while (out < nums.length) {
            if (nums[out] != val) {
                nums[base] = nums[out];
                out++;
                base++;
            } else {
                out++;
            }
        }

        return base;
    }
}