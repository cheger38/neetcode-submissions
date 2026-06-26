class Solution {
    public int search(int[] nums, int target) {
        return binarySearch(nums, 0, nums.length-1, target);
    }

    public int binarySearch(int[] nums, int start, int end, int target) {
        if (start > end) return -1;

        int middle = start + (end - start) / 2;

        if (nums[middle] == target) {
            return middle;
        } else if (nums[middle] > target) {
            return binarySearch(nums, start, middle - 1, target);
        } else {
            return binarySearch(nums, middle + 1, end, target);
        }
        
    }
}
