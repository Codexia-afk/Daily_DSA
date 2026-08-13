class Solution(object):

    def longestRepeating(self, s, queryCharacters, queryIndices):
        """
        :type s: str
        :type queryCharacters: str
        :type queryIndices: List[int]
        :rtype: List[int]
        """
        n = len(s)
        tree_max = [0] * (4 * n)
        tree_pref = [0] * (4 * n)
        tree_suff = [0] * (4 * n)
        tree_first = [""] * (4 * n)
        tree_last = [""] * (4 * n)

        def merge(tree_idx, l, mid, r):
            left_child = 2 * tree_idx
            right_child = 2 * tree_idx + 1

            left_len = mid - l + 1
            right_len = r - mid

            tree_first[tree_idx] = tree_first[left_child]
            tree_last[tree_idx] = tree_last[right_child]

            tree_pref[tree_idx] = tree_pref[left_child]
            if (
                tree_pref[left_child] == left_len
                and tree_last[left_child] == tree_first[right_child]
            ):
                tree_pref[tree_idx] += tree_pref[right_child]

            tree_suff[tree_idx] = tree_suff[right_child]
            if (
                tree_suff[right_child] == right_len
                and tree_last[left_child] == tree_first[right_child]
            ):
                tree_suff[tree_idx] += tree_suff[left_child]

            m = max(tree_max[left_child], tree_max[right_child])
            if tree_last[left_child] == tree_first[right_child]:
                m = max(m, tree_suff[left_child] + tree_pref[right_child])
            tree_max[tree_idx] = m

        def build(tree_idx, l, r):
            if l == r:
                tree_max[tree_idx] = 1
                tree_pref[tree_idx] = 1
                tree_suff[tree_idx] = 1
                tree_first[tree_idx] = s[l]
                tree_last[tree_idx] = s[l]
                return

            mid = (l + r) // 2
            build(2 * tree_idx, l, mid)
            build(2 * tree_idx + 1, mid + 1, r)
            merge(tree_idx, l, mid, r)

        def update(tree_idx, l, r, pos, ch):
            if l == r:
                tree_first[tree_idx] = ch
                tree_last[tree_idx] = ch
                return

            mid = (l + r) // 2
            if pos <= mid:
                update(2 * tree_idx, l, mid, pos, ch)
            else:
                update(2 * tree_idx + 1, mid + 1, r, pos, ch)
            merge(tree_idx, l, mid, r)

        build(1, 0, n - 1)

        ans = []
        for i in range(len(queryIndices)):
            idx = queryIndices[i]
            ch = queryCharacters[i]
            update(1, 0, n - 1, idx, ch)
            ans.append(tree_max[1])

        return ans