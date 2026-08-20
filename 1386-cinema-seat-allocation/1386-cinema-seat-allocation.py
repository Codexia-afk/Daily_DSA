from collections import defaultdict

class Solution(object):
    def maxNumberOfFamilies(self, n, reservedSeats):
        reserved_map = defaultdict(int)
        
        for r, c in reservedSeats:
            if 2 <= c <= 9:
                reserved_map[r] |= (1 << c)
        
        ans = (n - len(reserved_map)) * 2
        
        left_mask = (1 << 2) | (1 << 3) | (1 << 4) | (1 << 5)
        right_mask = (1 << 6) | (1 << 7) | (1 << 8) | (1 << 9)
        mid_mask = (1 << 4) | (1 << 5) | (1 << 6) | (1 << 7)
        
        for mask in reserved_map.values():
            left = (mask & left_mask) == 0
            right = (mask & right_mask) == 0
            mid = (mask & mid_mask) == 0
            
            if left and right:
                ans += 2
            elif left or right or mid:
                ans += 1
                
        return ans