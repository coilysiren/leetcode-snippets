# https://leetcode.com/contest/weekly-contest-186/problems/maximum-points-you-can-obtain-from-cards/
#
# time: O(TODO) - TODO
# space: O(TODO) - TODO


from typing import List


class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        maxScore = 0

        # this is a recursive decision tree where you have to find the highest value path
        _, _, maxScore = self.findBestPath(cardPoints, k + 1, maxScore)

        # done!
        return maxScore

    def findBestPath(
        self, path: List[int], steps: int, score: int,
    ) -> (List[int], int, int):
        steps = steps - 1

        if steps == 0:
            return [], 0, score

        leftPath = path[1:]
        rightPath = path[:-1]

        leftScore = path[0]
        rightScore = path[-1]

        _, _, leftTreeScore = self.findBestPath(leftPath, steps, leftScore)
        _, _, rightTreeScore = self.findBestPath(rightPath, steps, rightScore)

        if leftTreeScore > rightTreeScore:
            score = score + leftTreeScore
            path = leftPath

        else:
            score = score + rightTreeScore
            path = rightPath

        # print(f"\t path {path}")
        # print(f"\t steps {steps}")
        # print(f"\t score {score}")

        return path, steps, score


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
    ]

    for argset in args:
        inputs = argset[0]
        desiredOutput = argset[1]
        actualOutput = Solution().maxScore(**inputs)
        print(
            f"\ninput \n\t{inputs}, \n\toutput (desired, actual) {desiredOutput}, {actualOutput}"
        )
