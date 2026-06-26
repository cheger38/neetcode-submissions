class Solution {
    public int minEatingSpeed(int[] piles, int h) {
        int max = Integer.MIN_VALUE;
        for (int i : piles) {
            if (i > max) max = i;
        }
        int min = 1;

        int middle = -1;
        while (min < max) {
            middle = min + (max - min) / 2;
            if (validRate(piles, h, middle)) {
                max = middle;
            } else {
                min = middle + 1;
            }
        }

        return min;
        
    }


    public boolean validRate(int[] piles, int h, int k) {
        int timeNeeded = 0;

        for (int i : piles) {
            timeNeeded += (i + k - 1) / k;
        }

        return timeNeeded <= h;
    }
}
