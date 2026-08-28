from collections import Counter


class Solution(object):

    def lexPalindromicPermutation(self, s, target):
        n = len(s)
        m = n // 2
        counts = Counter(s)

        odd_chars = [ch for ch, cnt in counts.items() if cnt % 2 != 0]
        if len(odd_chars) > (1 if n % 2 != 0 else 0):
            return ""

        mid_char = odd_chars[0] if odd_chars else ""
        half_counts = {ch: cnt // 2 for ch, cnt in counts.items()}

        def can_form(sub):
            c = Counter(sub)
            return all(half_counts.get(ch, 0) >= cnt for ch, cnt in c.items())

        if can_form(target[:m]):
            p0 = target[:m] + (mid_char if n % 2 != 0 else "") + target[:m][::-1]
            if p0 > target:
                return p0

        pref_counts = Counter()
        for i in range(m):
            ch = target[i]
            if pref_counts[ch] + 1 <= half_counts.get(ch, 0):
                pref_counts[ch] += 1
            else:
                valid_prefix_len = i
                break
        else:
            valid_prefix_len = m

        for i in range(valid_prefix_len, -1, -1):
            cur_used = Counter(target[:i])
            rem_counts = {
                ch: half_counts[ch] - cur_used[ch]
                for ch in half_counts
                if half_counts[ch] > cur_used[ch]
            }

            if i < m:
                target_char = target[i]
                candidates = sorted([ch for ch in rem_counts if ch > target_char])
                if candidates:
                    chosen = candidates[0]
                    rem_counts[chosen] -= 1
                    if rem_counts[chosen] == 0:
                        del rem_counts[chosen]

                    suffix_chars = []
                    for ch in sorted(rem_counts.keys()):
                        suffix_chars.append(ch * rem_counts[ch])

                    first_half = target[:i] + chosen + "".join(suffix_chars)
                    return (
                        first_half
                        + (mid_char if n % 2 != 0 else "")
                        + first_half[::-1]
                    )

        return ""