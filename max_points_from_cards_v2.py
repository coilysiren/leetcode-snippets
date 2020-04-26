# https://leetcode.com/contest/weekly-contest-186/problems/maximum-points-you-can-obtain-from-cards/
#
# source: https://leetcode.com/problems/maximum-points-you-can-obtain-from-cards/discuss/597763/Python3-Easy-Sliding-Window-O(n)%3A-Find-minimum-subarray
#
# time: O(TODO) - TODO
# space: O(TODO) - TODO


from typing import List


class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        size = len(cardPoints) - k
        minSubArraySum = float("inf")
        j = curr = 0

        for i, v in enumerate(cardPoints):
            curr += v
            if i - j + 1 > size:
                curr -= cardPoints[j]
                j += 1
            if i - j + 1 == size:
                minSubArraySum = min(minSubArraySum, curr)

        return sum(cardPoints) - minSubArraySum


if __name__ == "__main__":
    args = [
        ({"cardPoints": [1, 2, 3, 4, 5, 6, 1], "k": 3}, 12),
        ({"cardPoints": [2, 2, 2], "k": 2}, 4),
        ({"cardPoints": [9, 7, 7, 9, 7, 7, 9], "k": 7}, 55),
        ({"cardPoints": [1, 1000, 1], "k": 1}, 1),
        ({"cardPoints": [1, 79, 80, 1, 1, 1, 200, 1], "k": 3}, 202),
        ({"cardPoints": [2, 2, 2, 0, 100, 1, 1], "k": 3}, 102),
        ({"cardPoints": [1, 1, 1, 0, 100, 1, 1], "k": 3}, 102),
        ({"cardPoints": [1, 1, 0, 100, 1], "k": 2}, 101),
        ({"cardPoints": [2, 2, 2], "k": 20}, 6),
        (
            {
                "cardPoints": [
                    30,
                    88,
                    33,
                    37,
                    18,
                    77,
                    54,
                    73,
                    31,
                    88,
                    93,
                    25,
                    18,
                    31,
                    71,
                    8,
                    97,
                    20,
                    98,
                    16,
                    65,
                    40,
                    18,
                    25,
                    13,
                    51,
                    59,
                ],
                "k": 15,
            },
            0,
        ),
    ]

    for argset in args:
        inputs = argset[0]
        desiredOutput = argset[1]
        actualOutput = Solution().maxScore(**inputs)
        print(
            f"input \n\t{inputs}, \n\toutput (desired, actual) {desiredOutput}, {actualOutput}\n"
        )
