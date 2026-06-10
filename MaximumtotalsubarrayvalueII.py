from collections import deque

class Solution:
    def maxTotalValue(self, nums, k):
        n = len(nums)

        def sum_all():
            
            SM = [0] * n; Sm = [0] * n
            stk, sm = [], 0
            for r in range(n):
                c = 1
                while stk and stk[-1][0] <= nums[r]:
                    ov, oc = stk.pop(); sm -= ov * oc; c += oc
                stk.append((nums[r], c)); sm += nums[r] * c; SM[r] = sm
            stk, sm = [], 0
            for r in range(n):
                c = 1
                while stk and stk[-1][0] >= nums[r]:
                    ov, oc = stk.pop(); sm -= ov * oc; c += oc
                stk.append((nums[r], c)); sm += nums[r] * c; Sm[r] = sm
            return SM, Sm

        if max(nums) == min(nums):
            return 0

        SM, Sm = sum_all()

        def compute(x):
            
            if x == 0:
                return n * (n + 1) // 2, sum(SM[r] - Sm[r] for r in range(n))

            lo_arr = [0] * n
            max_dq = deque(); min_dq = deque()
            lo = 0
            for r in range(n):
                v = nums[r]
                while max_dq and nums[max_dq[-1]] <= v: max_dq.pop()
                max_dq.append(r)
                while min_dq and nums[min_dq[-1]] >= v: min_dq.pop()
                min_dq.append(r)
                
                while nums[max_dq[0]] - nums[min_dq[0]] >= x:
                    lo += 1
                    if max_dq[0] < lo: max_dq.popleft()
                    if min_dq[0] < lo: min_dq.popleft()
                lo_arr[r] = lo  

            cnt = sum(lo_arr)

            
            inv_max = deque(); inv_min = deque()
            inv_s_max = 0; inv_s_min = 0
            cur_lo = 0
            total = 0

            for r in range(n):
                v = nums[r]
                
                c = 1
                while inv_max and inv_max[-1][0] <= v:
                    ov, oc = inv_max.pop(); inv_s_max -= ov * oc; c += oc
                inv_max.append((v, c)); inv_s_max += v * c

                c = 1
                while inv_min and inv_min[-1][0] >= v:
                    ov, oc = inv_min.pop(); inv_s_min -= ov * oc; c += oc
                inv_min.append((v, c)); inv_s_min += v * c

                
                while cur_lo < lo_arr[r]:
                    ov, oc = inv_max[0]
                    inv_s_max -= ov
                    if oc == 1: inv_max.popleft()
                    else: inv_max[0] = (ov, oc - 1)

                    ov, oc = inv_min[0]
                    inv_s_min -= ov
                    if oc == 1: inv_min.popleft()
                    else: inv_min[0] = (ov, oc - 1)

                    cur_lo += 1

                total += (SM[r] - inv_s_max) - (Sm[r] - inv_s_min)

            return cnt, total

        lo, hi = 0, max(nums) - min(nums)
        while lo < hi:
            mid = (lo + hi + 1) // 2
            if compute(mid)[0] >= k:
                lo = mid
            else:
                hi = mid - 1

        x = lo
        cnt_gt, sum_gt = compute(x + 1)
        return sum_gt + x * (k - cnt_gt)
