class Solution(object):
    def maxActiveSectionsAfterTrade(self, s, queries):
        """
        :type s: str
        :type queries: List[List[int]]
        :rtype: List[int]
        """

        n = len(s)

        total_ones = 0
        for ch in s:
            if ch == '1':
                total_ones += 1

       
        zero_starts = []
        zero_lengths = []

        zero_group_index = [-1] * n

        group = -1

        for i in range(n):
            if s[i] == '0':
                if i == 0 or s[i - 1] == '1':
                    zero_starts.append(i)
                    zero_lengths.append(1)
                    group += 1
                else:
                    zero_lengths[group] += 1

            zero_group_index[i] = group

        
        if not zero_lengths:
            return [total_ones] * len(queries)

        merge_gain = []

        for i in range(len(zero_lengths) - 1):
            merge_gain.append(zero_lengths[i] + zero_lengths[i + 1])

        sparse = []

        if merge_gain:
            sparse.append(merge_gain[:])
            length = 2

            while length <= len(merge_gain):
                previous = sparse[-1]
                current = [0] * (len(merge_gain) - length + 1)
                half = length // 2

                for i in range(len(current)):
                    left_value = previous[i]
                    right_value = previous[i + half]

                    if left_value > right_value:
                        current[i] = left_value
                    else:
                        current[i] = right_value

                sparse.append(current)
                length *= 2

        def range_max(left, right):
            """Return maximum merge_gain value from left to right."""
            length = right - left + 1
            power = length.bit_length() - 1
            block_size = 1 << power

            first = sparse[power][left]
            second = sparse[power][right - block_size + 1]

            if first > second:
                return first
            return second

        answer = []

        for left_index, right_index in queries:
            best = total_ones

            left_group = zero_group_index[left_index]
            right_group = zero_group_index[right_index]

            left_zero_part = -1

            if s[left_index] == '0':
                start = zero_starts[left_group]
                full_length = zero_lengths[left_group]
                left_zero_part = full_length - (left_index - start)

            right_zero_part = -1

            if s[right_index] == '0':
                start = zero_starts[right_group]
                right_zero_part = right_index - start + 1

            
            first_complete_group = left_group + 1

            if s[right_index] == '1':
                last_complete_group = right_group
            else:
                last_complete_group = right_group - 1

            if (
                s[left_index] == '0'
                and s[right_index] == '0'
                and left_group + 1 == right_group
            ):
                candidate = total_ones + left_zero_part + right_zero_part

                if candidate > best:
                    best = candidate

            else:

                first_pair = first_complete_group
                last_pair = last_complete_group - 1

                if first_pair <= last_pair:
                    candidate = total_ones + range_max(first_pair, last_pair)

                    if candidate > best:
                        best = candidate

            if s[left_index] == '0':
                next_group = left_group + 1

                if next_group <= last_complete_group:
                    candidate = (
                        total_ones
                        + left_zero_part
                        + zero_lengths[next_group]
                    )

                    if candidate > best:
                        best = candidate

            if s[right_index] == '0':
                previous_group = right_group - 1

                if left_group < previous_group:
                    candidate = (
                        total_ones
                        + zero_lengths[previous_group]
                        + right_zero_part
                    )

                    if candidate > best:
                        best = candidate

            answer.append(best)

        return answer