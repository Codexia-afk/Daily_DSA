class Solution(object):

    def smallestNumber(self, num, t):
        """
        :type num: str
        :type t: int
        :rtype: str
        """
       
        temp = t
        c2 = c3 = c5 = c7 = 0

        while temp % 2 == 0:
            c2 += 1
            temp //= 2
        while temp % 3 == 0:
            c3 += 1
            temp //= 3
        while temp % 5 == 0:
            c5 += 1
            temp //= 5
        while temp % 7 == 0:
            c7 += 1
            temp //= 7

        if temp > 1:
            return "-1"

        DIGIT_FACTORS = {
            1: (0, 0, 0, 0),
            2: (1, 0, 0, 0),
            3: (0, 1, 0, 0),
            4: (2, 0, 0, 0),
            5: (0, 0, 1, 0),
            6: (1, 1, 0, 0),
            7: (0, 0, 0, 1),
            8: (3, 0, 0, 0),
            9: (0, 2, 0, 0),
        }

        def get_min_suffix_str(r2, r3, r5, r7):
            
            r2 = max(0, r2)
            r3 = max(0, r3)
            r5 = max(0, r5)
            r7 = max(0, r7)

            best_str = None
            best_len = float("inf")

            max_c6 = min(r2, r3)
            for c6 in range(max_c6 + 1):
                rem3 = r3 - c6
                rem2 = r2 - c6

                c9 = rem3 // 2
                c3_count = rem3 % 2

                c8 = rem2 // 3
                rem2_mod = rem2 % 3
                c4 = 1 if rem2_mod == 2 else 0
                c2_count = 1 if rem2_mod == 1 else 0

                digits = (
                    "2" * c2_count
                    + "3" * c3_count
                    + "4" * c4
                    + "5" * r5
                    + "6" * c6
                    + "7" * r7
                    + "8" * c8
                    + "9" * c9
                )
                curr_len = len(digits)

                if curr_len < best_len:
                    best_len = curr_len
                    best_str = digits
                elif curr_len == best_len:
                    if digits < best_str:
                        best_str = digits

            return best_str

        N = len(num)

        pref_2 = [0] * (N + 1)
        pref_3 = [0] * (N + 1)
        pref_5 = [0] * (N + 1)
        pref_7 = [0] * (N + 1)

        first_zero = N
        for idx, ch in enumerate(num):
            if ch == "0":
                first_zero = idx
                break
            d = int(ch)
            f2, f3, f5, f7 = DIGIT_FACTORS[d]
            pref_2[idx + 1] = pref_2[idx] + f2
            pref_3[idx + 1] = pref_3[idx] + f3
            pref_5[idx + 1] = pref_5[idx] + f5
            pref_7[idx + 1] = pref_7[idx] + f7

        if first_zero == N:
            if (
                pref_2[N] >= c2
                and pref_3[N] >= c3
                and pref_5[N] >= c5
                and pref_7[N] >= c7
            ):
                return num


        for i in range(min(N - 1, first_zero), -1, -1):
            d_start = 1 if i == first_zero else int(num[i]) + 1

            for d in range(d_start, 10):
                f2, f3, f5, f7 = DIGIT_FACTORS[d]
                r2 = c2 - pref_2[i] - f2
                r3 = c3 - pref_3[i] - f3
                r5 = c5 - pref_5[i] - f5
                r7 = c7 - pref_7[i] - f7

                rem_len = N - 1 - i
                min_suf = get_min_suffix_str(r2, r3, r5, r7)

                if len(min_suf) <= rem_len:
                    suf = "1" * (rem_len - len(min_suf)) + min_suf
                    return num[:i] + str(d) + suf

        min_suf = get_min_suffix_str(c2, c3, c5, c7)
        target_len = max(N + 1, len(min_suf))
        return "1" * (target_len - len(min_suf)) + min_suf