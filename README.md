# Blind 75 Must Do Leetcode
A list of leetcode questions by Dequan Zhang. Here is the [link](https://leetcode.com/list/945gkup7/)

## Question 1: Two Sum
[Question description](https://leetcode.com/problems/two-sum/) here.

This question is very easy. My main idea was to use a dictionary to store a mapping between a number to its index in the list. So, for a number, we check if (target - num) is already met before. If yes, then we can directly return the result. Otherwise, we simply put pair(num, i) into dictionary.

## Question 2: Longest Substring Without Repeating Characters
[Question description](https://leetcode.com/problems/longest-substring-without-repeating-characters/) here.

This question is not very easy. My main idea is to use dynamic programming. **dp[i]** stores the length of the longest substring ending in ith character. There is also a **charDict** such that **charDict[c]** stores the last index that character c appeared before index i (in the loop).
In the loop, when we meet a character c, we check if we already met it. If we have not met it before, we simply take **dp[i] = dp[i-1] + 1**. Otherwise, we check if the last index we met c can be reached by the longest substring ending in (i-1)th character. If no, we take the same **dp[i]** value as the previous case, otherwise we take **dp[i] = i - charDict[c]** as we are assured that there are no other repeating characters between them.

## Question 3: Container with Most Water
[Question description](https://leetcode.com/problems/container-with-most-water/) here.

This question is a little bit conceptually complex. What I did is to simply set two pointers, i and j. i is the left most building, and j is the right most building. For each pair of (i, j), I calculate the area of them, and if height[i] $<$ height[j], I use i += 1, otherwise j -= 1.
But we need a proof on why this solution is optimal. Here I quote a comment under the official solution for this question by **davidhuangdw**:
1. case height[i] $<$ height[j]: we can prove that j is the best choice here. For any k such that $i \le k \le j$, we have area(i, j) $\ge$ area(i, k). So, area(i, j) is the max area involving i. This means that max_area_in_range(i, j) = max(max_area_in_range(i+1, j), area(i, j)). By this, we can see that i += 1 is the best choice here.
2. case height[i] $\ge$ height[j]: we can prove similarly that j -= 1 is the best choice here.