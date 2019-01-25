from collections import defaultdict


class Solution(object):

    def pickFruits(self, fruits):
        """Pick fruits
        Args:
          fruits: A list of fruits, each digit
            represents a type of fruit
        Returns:
          Maximum number of fruits that can
            be picked.
        """

        # Assign two pointers.
        slow = 0
        fast = 0

        # Preparations.
        # The memo stores the occurrence of a
        # particular kind of fruits
        memo = defaultdict(int)
        ans = 0
        num_fruit_types = 0

        # Start loop
        while fast < len(fruits):

            # Update the memo and num_fruit_types
            if memo[fruits[fast]] == 0:
                num_fruit_types += 1
            memo[fruits[fast]] += 1
            fast += 1

            # When num_fruit_types >= 3, we need to dump
            # some fruits picked previously
            while num_fruit_types >= 3:
                if memo[fruits[slow]] == 1:
                    num_fruit_types -= 1
                memo[fruits[slow]] -= 1
                slow += 1

            # Update the answer
            ans = max(ans, fast - slow)

        # Return the correct answer
        return ans



input1 = [1, 2, 1, 3, 4, 3, 5, 1, 2] #3
input2 = [1, 2, 1, 2, 1, 2, 1] #7
input3 = [1, 1, 1, 2, 2, 3, 3, 3, 3] #6
input4 = [2, 1, 2, 1, 2, 3, 3, 3, 3] #5
mySolution = Solution()
ans = mySolution.pickFruits(input4)
print(ans)
# earilier