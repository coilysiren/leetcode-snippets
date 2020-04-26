# https://leetcode.com/contest/weekly-contest-186/problems/maximum-score-after-splitting-a-string/
#
# time: O(3n) - iterate through the list 3 times
# space: O(n) - store a key value list the same size as the input list


class Solution:
    def maxScore(self, scoreString: str) -> int:
        print(scoreString)

        # this data structure keys on the split position on provides the combined score
        splitScore = {index: 0 for index in range(1, len(scoreString))}

        # iterate forwards, counting zeros
        zeroesSeen = 0
        for index, char in enumerate(scoreString[:-1]):
            if char == "0":
                zeroesSeen += 1
            splitScore[index + 1] = zeroesSeen
        print(splitScore)

        # iterate backwards, counting ones
        onesSeen = 0
        for index, char in reversed(list(enumerate(scoreString))[1:]):
            if char == "1":
                onesSeen += 1
            splitScore[index] = splitScore[index] + onesSeen
        print(splitScore)

        # iterate the split score, to find the max
        maxScore = 0
        for _, score in splitScore.items():
            maxScore = max(maxScore, score)

        # done!
        return maxScore


if __name__ == "__main__":
    args = [
        ("011101", 5),
        ("00111", 5),
        ("1000", 2),
        ("0001", 4),
        ("0000", 3),
        ("1111", 3),
    ]

    for argset in args:
        inputArg = argset[0]
        desiredOutput = argset[1]
        actualOutput = Solution().maxScore(inputArg)
        print(
            f"input {inputArg}, \toutput (desired, actual) {desiredOutput}, {actualOutput}"
        )
