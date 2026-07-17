class Solution {
    public int[] gcdValues(int[] nums, long[] queries) {
        int maximum = 0;

        for (int num : nums) {
            if (num > maximum) {
                maximum = num;
            }
        }

        long[] frequency = new long[maximum + 1];

        for (int num : nums) {
            frequency[num]++;
        }

        
        long[] exactGcd = new long[maximum + 1];

        for (int g = maximum; g >= 1; g--) {
            long divisibleCount = 0;

            
            for (int multiple = g;
                 multiple <= maximum;
                 multiple += g) {
                divisibleCount += frequency[multiple];
            }

            
            long pairCount =
                divisibleCount * (divisibleCount - 1) / 2;

            
            for (int multiple = g * 2;
                 multiple <= maximum;
                 multiple += g) {
                pairCount -= exactGcd[multiple];
            }

            exactGcd[g] = pairCount;
        }

        
        long[] prefixPairs = new long[maximum + 1];

        for (int g = 1; g <= maximum; g++) {
            prefixPairs[g] =
                prefixPairs[g - 1] + exactGcd[g];
        }

        int[] answer = new int[queries.length];

        for (int i = 0; i < queries.length; i++) {
            long query = queries[i];

            int left = 1;
            int right = maximum;

            while (left < right) {
                int middle = left + (right - left) / 2;

                if (prefixPairs[middle] > query) {
                    right = middle;
                } else {
                    left = middle + 1;
                }
            }

            answer[i] = left;
        }

        return answer;
    }
}