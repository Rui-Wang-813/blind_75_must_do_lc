# Blind 75 Must Do Leetcode
A list of leetcode questions. The list is given by **Dequan Zhang (张德权)** @Dezhang1999. The solution is given by **Rui Wang (王锐)** @Rui-Wang-813. Here is the [link to the list](https://leetcode.com/list/945gkup7/).

## Question 1: Two Sum
[Question description](https://leetcode.com/problems/two-sum/) here.

This question is very easy. My main idea was to use a dictionary to store a mapping between a number to its index in the list. So, for a number, we check if ```target - num``` is already met before. If yes, then we can directly return the result. Otherwise, we simply put pair(num, i) into dictionary.

## Question 2: Longest Substring Without Repeating Characters
[Question description](https://leetcode.com/problems/longest-substring-without-repeating-characters/) here.

This question is not very easy. My main idea is to use dynamic programming. ```dp[i]``` stores the length of the longest substring ending in ith character. There is also a ```charDict``` such that ```charDict[c]``` stores the last index that character c appeared before index i (in the loop).
In the loop, when we meet a character c, we check if we already met it. If we have not met it before, we simply take ```dp[i] = dp[i-1] + 1```. Otherwise, we check if the last index we met c can be reached by the longest substring ending in (i-1)th character. If no, we take the same ```dp[i]``` value as the previous case, otherwise we take ```dp[i] = i - charDict[c]``` as we are assured that there are no other repeating characters between them.

## Question 3: Container with Most Water
[Question description](https://leetcode.com/problems/container-with-most-water/) here.

This question is a little bit conceptually complex. What I did is to simply set two pointers, i and j. i is the left most building, and j is the right most building. For each pair of (i, j), I calculate the area of them, and if ```height[i] < height[j]```, I use ```i += 1```, otherwise ```j -= 1```.
But we need a proof on why this solution is optimal. Here I quote a comment under the official solution for this question by **davidhuangdw**:
1. case ```height[i] < height[j]```: we can prove that j is the best choice here. For any k such that $i \le k \le j$, we have ```area(i, j) <= area(i, k)```. So, ```area(i, j)``` is the max area involving i. This means that ```max_area_in_range(i, j) = max(max_area_in_range(i+1, j), area(i, j))```. By this, we can see that ```i += 1``` is the best choice here.
2. case ```height[i] >= height[j]```: we can prove similarly that ```j -= 1``` is the best choice here.

## Question 4: 3 Sum
[Question description](https://leetcode.com/problems/3sum/) here.

I have two solutions for this question. The first is my own, dfs, but exceeded time limit when the ```nums``` list became too large. The second is from discussion of the problem on leetcode website, and here is the [link](https://www.code-recipe.com/post/three-sum).
1. My solution uses dfs tree version and limited depth of 3. If the depth limit is exceeded or that there are no more numbers (no branches to go), it returns. If the depth limit is reached, we check if the path to the current leaf has a sum of 0. If yes, we append the path to the result. If depth limit is not reached, we simply dfs throughout each of the child nodes.
2. The solution from online source uses three pointers (i, j, k) and two loops. The first loop traverse i from 0 to ```len(nums) - 1``` and in each outer loop, we set ```j, k = i + 1, len(nums) - 1``` and the condition of inner loop is that ```j < k```. In each inner loop, we check if ```nums[j] + nums[k] == -nums[i]```. If yes, we append the triplet to result and move k such that ```nums[k]``` is not what we used in this triplet. If ```nums[j] + nums[k] < -nums[i]```, we move j to right. Otherwise, we move k to left. (note that this array is sorted at the beginning).

## Question 5: Remove Nth Node From End of List
[Question description](https://leetcode.com/problems/remove-nth-node-from-end-of-list/) here.

I use double pointer again for this question. The first pointer ```t_head1``` aims to point to the node ```n``` nodes after the second pointer ```t_head2```. After moving ```t_head1``` to the desired position, I check if ```t_head1 is None```. If yes, then we know that ```n``` is the size of the list, and the first node will be removed. Thus we simply return ```head.next```. Otherwise, we use a loop to make ```t_head1``` reach the last node, and now ```t_head2``` points to the node just before the node to be removed from list, and now we remove this node and return ```head```.

## Question 6: Valid Parenthesis
[Question description](https://leetcode.com/problems/valid-parentheses/) here.

I use a stack structure and its First-In-First-Out to solve this question. When I see one of ```'([{'```, I push this char onto stack. When I see one of ```')]}'```, I check if the top item of the stack is the corresponding parenthesis. If the stack is empty, then this close parenthesis is redundant, and thus return false. If not corresponding, then return false as well. At the end, check if there are unclosed left parenthesis on stack.
The stack is actually a similar process to recursion.

## Question 7: Longest Palindromic Substring
[Question description](https://leetcode.com/problems/longest-palindromic-substring/) here.

I used two approaches for this question again. My first approach is dynamic programming, and my second approach is window expansion. Dynamic programming is too slow, while window expansion is much faster.
1. In the dynamic programming version, I simply define subproblem
        $$
            P(i, j)=
            \begin{cases}
            True\text{ if }P(i+1, j-1)\text{ and }s[i] == s[j],\\
            False\text{ otherwise}\\
            \end{cases}
        $$
    and the base cases are that:
    - $P(i, i) = True$
    - $P(i, i+1) = (s[i] == s[i+1])$
    Unfortunately this method is pretty slow and could only beat 11% of python submissions.
2. For the second approach I use a much more conceptually complex approach. It is a window expansion. Each palindrome has a center. Even if the length of this palindrome is even, there is a center between the two most middle chars. I want to try to expand from every possible center. So, I first plug in a ```'|'``` between each pair of chars (and the two ends). Call this string ```s1``` Then, for each center, I first find its max palindrome radius. Afther this, I use this center to find the max palindrome radius of each center to the right of this old center but in the palindrome window of it. For each center, I find its mirrored center about the old center. There are three cases:
    1. The palindrome radius of mirrored center is smaller than the distance between the current center to the rightmost of palindrome window. In this case we can easily determine that the radius of the current center is same as the radius of mirrored center.
    2. The palindrome radius of mirrored center is larger than the distance between the current center to the rightmost of palindrome window. In this case, we can see that the char just left to the leftmost of palindrome window (call it ```a```) is same as its mirrored char ```b``` about the mirrored center, and this ```b``` is same as its mirrored char ```c``` about the old center, while this ```c``` is different from the char ```d``` just right to the rightmost of palindrome window. So, the radius of current center is its distance to the rightmost of palindrom window.
    3. The radius is same as the distance. In this case, we know no more info, and the radius of current center is to be determined (have to continue to the next iteration of outer loop).

After this, we just get the substring from ```s``` by the ```center``` and ```radius``` we just determined from ```s1```. If ```radius``` is even, we know that the length of the substring in ```s``` is also even. Otherwise the substring is odd. When it is even, we use
```
lt_bd = (max_center - max_radius + 1) // 2
rt_bd = (max_center + max_radius - 1) // 2
return s[lt_bd:rt_bd+1]
```
Otherwise, we use
```
max_center //= 2
max_radius //= 2
return s[max_center-max_radius:max_center+max_radius+1]
```