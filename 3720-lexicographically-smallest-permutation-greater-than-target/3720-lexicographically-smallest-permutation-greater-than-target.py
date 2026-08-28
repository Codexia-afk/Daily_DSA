from collections import Counter


class Solution(object):

    def lexGreaterPermutation(self, s, target):
        n = len(s)
        total_counts = Counter(s)

        for i in range(n - 1, -1, -1):
            cur_counts = dict(total_counts)
            valid_prefix = True

            for j in range(i):
                ch = target[j]
                if cur_counts.get(ch, 0) > 0:
                    cur_counts[ch] -= 1
                else:
                    valid_prefix = False
                    break

            if not valid_prefix:
                continue

            for code in range(ord(target[i]) + 1, ord("z") + 1):
                ch = chr(code)
                if cur_counts.get(ch, 0) > 0:
                    cur_counts[ch] -= 1
                    res = list(target[:i]) + [ch]
                    for rem_ch in sorted(cur_counts.keys()):
                        res.extend([rem_ch] * cur_counts[rem_ch])
                    return "".join(res)

        return ""