# Blind 75 Must Do Leetcode
A list of leetcode questions by Dequan Zhang. Here is the [link](https://leetcode.com/list/945gkup7/)

## Question 1: Two Sum
[Question description](https://leetcode.com/problems/two-sum/) here.

This question is very easy. My main idea was to use a dictionary to store a mapping between a number to its index in the list. So, for a number, we check if (target - num) is already met before. If yes, then we can directly return the result. Otherwise, we simply put pair(num, i) into dictionary.