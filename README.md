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
1. In the dynamic programming version, I simply define subproblem<br>
        ![q7-eqn](https://github.com/Rui-Wang-813/blind_75_must_do_lc/blob/main/doc/img/q7-eqn.png?raw=true)

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

## Question 8: Merge Two Sorted Lists
[Question description](https://leetcode.com/problems/merge-two-sorted-lists/) here.

This is a very easy question. We simply create a new `ListNode` and two pointers each pointing to the current position in each list. In each iteration, we compare the pointed values in the two lists and insert the smaller one to the `result` and move that pointer. When one of the two pointers go to `None`, we simply inert every remaining value in the other list.

## Question 9: Merge K Sorted Lists
[Question description](https://leetcode.com/problems/merge-k-sorted-lists/) here.

This question is not conceptually hard, but requires relatively high coding technique. I have four solutions for this question.
1. Merge one by one. I use the `mergeTwoLists` function in [Question 8](https://github.com/Rui-Wang-813/blind_75_must_do_lc/blob/main/README.md#question-8-merge-two-sorted-lists) such that I merge the lists one by one (1 and 2 as 12, then 12 and 3 as 123, and so on...) But this is too slow and exceeds the time limit.
2. Use k pointers. Iterate until all pointers are `None`. For each iteration, insert the min of the k pointers into the `result` list. This is too slow and only beats 5% python3 submissions.
3. Use `queue.PriorityQueue`. Similar to approach 2, only using `PriorityQueue` to accomplish the comparing goal. The problem in this question is that I have to define an `__lt__` function for `ListNode` even if I put `(node.val, node)` in the priority queue, the reason is explained [here](https://stackoverflow.com/questions/53554199/heapq-push-typeerror-not-supported-between-instances). This solution has pretty satisfying complexity.
4. Insert all node values into one list, sort them, and then convert the list as a singly-linked list. This is the most stupid version, but thanks to the `sort` function built-in for python3 and other optimizations, this became the fastest of all my 4 versions. It beats about 67% python3 submissions.

## Question 10: Search in Rotated Sorted Array
[Question description](https://leetcode.com/problems/search-in-rotated-sorted-array/) here.

This question is very easy. We can simply find the pivot, and permute the array back. Then, we perform binary search in the permuted array. After we find the index of target in the permuted array, we use `(mi + i) % len(nums)` to get the index of target in the original array, where `mi` is the index of target in permuted array and `i` is the index of pivot.

## Question 11: Combination Sum
[Question description](https://leetcode.com/problems/combination-sum/) here.

This question is not very complex. I have two versions of solution.
1. Simply use dfs. If `target == 0`, then simply `return [[]]`. We need an inner list because we have found something, and we need an inner list such that previous calling frame can append something into it. If `target < 0 or len(candidates == 0)`, this means we cannot find anything, then we simply `return []`. Note that second case must come after first case. After handling these two base cases, we iterate through each candidate and recursively call with `candidates[i:]` and `target - candidates[i]` as we are handling with the case that the ith candidate is included in the combination.
2. Use a `stack` variable to record the current path we've gone through. Other process very similar to first version.

## Question 12: Rotate Image
[Question description](https://leetcode.com/problems/rotate-image/) here.

This question is also not conceptually complex, but very trivial in coding. My solution is to rotate layer by layer from outmost layer to inner most layer. Each layer is composed of 4 sides of the square. For example, in the following matrix:
<p align="center">
    <img src="doc/img/q11-mat-before-rotate.png">
</p>

, the most outer layer is `((1,2,3),(3,6,9),(9,8,7),(7,4,1))`. For each layer, we iterate through all items in one side. And in each iteration, we make swap operations to each of the 4 items in the corresponding position of each side. For example, after one iteration, the matrix becomes:
<p align="center">
    <img src="doc/img/q11-mat-after1-iter.png">
</p>

We do this for each of the item on one side, then we go to deeper layers.

## Question 13: Group Anagrams
[Question description](https://leetcode.com/problems/group-anagrams/) here.

This question is easy. We can simply first sort all strings in the list to make sure that each appearance of an anagram is the same. Then we make a dictionary `sdict` such that `sdict[str]` is a list of the indices of each appearance of this anagram. Then, we use these indices to take the strings from original list.

## Question 14: Maximum Subarray
[Question description](https://leetcode.com/problems/maximum-subarray/) here.

I use a moving window to solve this problem. I first set two variables `maxSum` and `curSum`. `maxSum` is the max sum of subarray I've seen, and `curSum` is the sum of the current window. In the loop, there are three cases:
1. `curSum < 0`: In this case, there is no way that the sum of window containing both current window and any following items will be larger than or equal to the sum of only the window of following items. So I set `maxSum = max(maxSum, curSum)` here and set `curSum = nums[i]`.
2. `curSum >= 0 and nums[i] < 0`: In this case, it is possible that the window containing current window and some following items to be larger, but I still need to record the current sum and then go on.
3. `curSum >= 0 and nums[i] >= 0`: This is the most simple case. I simply expand the window.

## Question 15: Spiral Matrix
[Question description](https://leetcode.com/problems/spiral-matrix/) here.

I use similar idea to [Qesution 12](https://github.com/Rui-Wang-813/blind_75_must_do_lc/blob/main/README.md#question-12-rotate-image). For each layer, I put every item clockwisely into the `result` array. Note that there is a special case in which there are only 1 row or 1 column left in a layer (as this is not a square, but a rectangle). In this special case, we can just return after we've processed the top side and the right side of the layer becuase there is nothing left in the rectangle.

## Question 16: Jump Game
[Question description](https://leetcode.com/problems/jump-game/) here.

I have two versions of solution for this question:
1. Use dynamic programming. We have `dp[i]` being whether we can jump to the last index from index `i`, and the base case is that `dp[len(nums)-1] = True`. We iterate from `i = len(nums) - 2` to `i = 0`, and for each `i`, we check `nums[i]` items in the array after it (which have been processed since our iteration is backward). If any of these items is True, then we set `dp[i] = True`, otherwise it is False.
Unfortunately it exceeded time limit.
2. The second version uses a `maxPos` to record the furthest index we can reach when the loop iterates to index `i`. Note that it does not necessarily jump from index `i`, but can be any index before it. In each iteration, we update `maxPos = max(nums[i], maxPos) - 1` because either `nums[i]` can help us reach to further index from `i`, or that we cannot and the `maxPos` should be one step smaller than `i - 1`.

## Question 17: Merge Intervals
[Question description](https://leetcode.com/problems/merge-intervals/) here.

To begin with, sort the list `intervals` by the $start_i$ of each interval. Then, in the loop traversing through the intervals, compare the $end_i$ with $end_{i+1}$. If $end_i \geq end_{i+1}$, then we know that the `i`th interval covers the `i+1`th interval, and we simply return the `i+1`th interval. If $ start_{i+1} \leq end_i \leq end{i+1}$, then we expand the `i`th interval and remove the `i+1`th interval. Finally, if neither of the cases is true, then we know that the two intervals do not overlap at all, we just take `i += 1`.

## Question 18: Insert Interval
[Question description](https://leetcode.com/problems/insert-interval/) here.

There are two parts in this solution.
1. Use binary search to find the index where we should insert the new interval into the intervals. The details of how I did it is in the code.
2. After insertion, as we are gauranteed that there are not overlapping intervals in the original `intervals` list, we only need to try to merge overlapping intervals in index from `max(0, idx-1)` to `min(len(intervals), idx+1)`.  The merging technique is same with that I used in [Question 17](https://github.com/Rui-Wang-813/blind_75_must_do_lc/blob/main/README.md#question-17-merge-intervals).

## Question 19: Unique Paths
[Question description](https://leetcode.com/problems/unique-paths/) here.

I use dynamic programming in this question. `dp[i][j]` is how many unique paths there are from the cell (i, j) to the bottom right corner. There are two base cases:
1. All cells on the right border has only one unique path toward the terminal because they can only go down. So `dp[1:m][-1] = 1`
2. All cells on the bottom border has only one unique path toward the terminal because they can only go right. So `dp[-1][1:n] = 1`.

And we have the relationship: `dp[i][j] = dp[i+1][j] + dp[i][j+1]`. Finally we return `dp[0][0]`.

## Question 20: Climbing Stairs
[Question description](https://leetcode.com/problems/climbing-stairs/) here.

This is a very easy question. I also use dynamic programming in this question. `dp[i]` represents how many ways there are to climb stairs after we've climbed i stairs. There are two base cases:
1. When we've reached the end, there is only one way.
2. When we've reached the `n-1`th stair, there is also only one way.

The relationship is `dp[i] = dp[i+1] + dp[i+2]`.

## Question 21: Set Matrix Zeroes
[Question description](https://leetcode.com/problems/set-matrix-zeroes/) here.

This is also a very easy question. I use a set to store the `(i, j)` of each 0 entry in the original matrix. Then, for each `(i, j)` in the set, I set the corresponding column and row to be 0.

## Question 22: Minimum Window Substring
[Question description](https://leetcode.com/problems/minimum-window-substring/) here.

For this question, unfortunately my own solution was flawed. I used the approach 1 of [official solution](https://leetcode.com/problems/minimum-window-substring/solution/).

The algorithm has the following 4 steps:
1. We first take two pointers `lt_ptr` and `rt_ptr` initially pointing at the start of the `s`.
2. We move `rt_ptr` to the right to expand the current window until our window contains all chars in `t`. 
3. Then, we move `lt_ptr` to the right to constrict the window so that we obtains a minimum possible window.
4. Go on and repeat from step 1.

## Question 23: Word Search
[Question description](https://leetcode.com/problems/word-search/) here.

My solution is to simply expand all possible paths from any cell. For a particular cell, if `board[i][j]` is not the same with `word[w_idx]`, then this path cannot constitute `word` and we abandon. Otherwise, we try to match `word[w_idx+1]` with the four neighbor cells and go on to expand.
The idea is very simple. But note that we need to mark `board[i][j]` as visited before the recursive call and mark it as unvisited after the recursive call.
The `helper(i, j, w_idx)` function I defined for this question returns whether we can expand a path originating from `board[i][j]` corresponding to `word[w_idx:]`.

## Question 24: Decode Ways
[Question description](https://leetcode.com/problems/decode-ways/) here.

My solution is dynamic programming. We have `dp[i]` represents how many ways are there to decode string `s[i:]`. There are two base cases:
1. If `s[-1] == '0'`, then `dp[-1] = 0`.
2. Otherwise, `dp[-1] = 1`.

The relationship is as follows:
1. `s[i] == '0'`, then we know that we cannot decode anything from `s[i:]` because this is an invalid string. So, we set `dp[i] = 0`.
2. `int(s[i:i+2]) <= 26`, then we know that we can either take `s[i]` to decode it as a char, or we can take `s[i:i+2]` to decode it as a char. So, we set `dp[i] = dp[i+1] + dp[i+2]`.
3. `int(s[i:i+2]) > 26`, then we know that we can only take `s[i]` and decode it as a char. So `dp[i] = dp[i+1]`.

Finally, we return `dp[0]`.

## Question 25: Validate Binary Search Tree
[Question description](https://leetcode.com/problems/validate-binary-search-tree/) here.

I simply used DFS for this question. At each node, I have a lower bound and upper bound for the value of this node. If the node value is not in the interval, then we know this tree is not a valid BST. Otherwise, if both the left and right child of current root is valid BST, then this tree is a valid BST. If not, then this tree is not a valid BST.


## Question 26: Same Tree
[Question description](https://leetcode.com/problems/same-tree/) here

This is a very easy question. Simply use DFS to check each value of both trees.

## Question 27: Binary Tree Level Order Traversal
[Question description](https://leetcode.com/problems/binary-tree-level-order-traversal/) here.

For this question, I use BFS. (this is actually very obvious) I use a `frontier` to store all nodes of current level. Each time, I traverse through all nodes in the current level, and push the nodes in the next level into `frontier` and also record the number of nodes in the next level. When the current level is finished, I push the list of all values of current level into `result`, and start a new loop.

## Question 28: Maximum Depth of Binary Tree
[Question description](https://leetcode.com/problems/maximum-depth-of-binary-tree/) here.

Basically I used the same idea as [Question 27](https://github.com/Rui-Wang-813/blind_75_must_do_lc/blob/main/README.md#question-27-binary-tree-level-order-traversal). Except that now I use `result` as an integer that records how many levels we've gone through. Each time I've traversed through 0 to `layer_size`, I add `result` by one.

## Question 29: Construct Binary Tree from Preorder and Inorder Traversal
[Question description](https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/) here.

The solution is ideally simple. We first find the root value from the `preorder` list as we know that in preorder, the root value is always the first. Then, we find the index of the root value in the `inorder` list. The length of `inorder` before that index is the number of nodes in the left child, and the length after that index is the number of nodes in the right child. We thus gain the `inorder` for both left and right child tree.
We know that in `preorder`, all tree nodes in left child comes before all tree nodes in right child. So, we can use the length we just gained to get the `preorder` for left and right child trees as well.
Now that we get all information for recursion, just use recursive call to construct the left and right children.

Here is one example:
> preoder = [3,9,20,15,7], inorder = [9,3,15,20,7]

We can see that `preorder[0]` is 3, so we know from `inorder` that the inorder traversal for the left child is `[9]`, and for the right child is `[15, 20, 7]`. By the lengths of these two lists, we know that the preorder traversal for the left child is `[9]`, and the preorder traversal for the right child is `[20, 15, 7]`.

Note that this solution only works when all the values in the tree are unique. This is gauranteed in the leetcode question description.

## Question 30: Best Time to Buy and Sell Stock
[Question description](https://leetcode.com/problems/best-time-to-buy-and-sell-stock/) here.

I used fast solution by [mageshyt](https://leetcode.com/problems/best-time-to-buy-and-sell-stock/discuss/1735550/Python-Javascript-Easy-solution-with-very-clear-Explanation). His explanation is very clean and neat.
I would like to provide a proof here: 
1. Assume that the best buy and sell dates are `i` and `j`. We know that `i < j`. 
2. We also know that `prices[i]` is the minimum of `prices[0:j]`. We can prove this by contradiction: if there is an `i1` in the interval [0:j], then `prices[j] - prices[i1] > prices[j] - prices[i1]` and thus `i` is not optimal.
3. Based on the fact from step 2, we know that our solution will always update our left pointer `lt` to be `i` when we reached `rt = i`. Because what every `lt` was, `prices[i] < prices[lt]`.
4. Based on the fact from step 2, we also know that `lt` will not be updated before our `rt` reach `j` as we know that `prices[j]` is minimum of `prices[0:j]`.
5. And so our solution will return `prices[j] - prices[i]`. And the result is correct.

## Question 31: Binary Tree Maximum Path Sum
[Question description](https://leetcode.com/problems/binary-tree-maximum-path-sum/) here.

I would use a postorder DFS to solve this question. I create a recursive helper function. Given a tree root, the helper function returns the max path sum ending at this root. In its body, it takes the max path sum ending at its left and right children, and use them to get the max path sum including the root itself.

## Question 32: Valid Palindrome
[Question description](https://leetcode.com/problems/valid-palindrome/) here.

This question is very easy. I simply have two pointers, `i` and `j`. `i` is the left pointer that starts from the start of the string, and `j` is the right pointer that starts from the end of the string. I move `i` from left to right and `j` from right to left, if `s[i]` is not alphanumeric, I simply have `i += 1`, and I do the same for `j`. Then, I compare `s[i]` and `s[j]`. If they are not equal, then I know that `s` is not palindrome.

## Question 33: Longest Consecutive Sequence
[Question description](https://leetcode.com/problems/longest-consecutive-sequence/) here.

This question is very easy. Initially I was trying to use an algorithm similar to what I used for Question 30 and use `rt - lt` to update `maxLen`, but it turns out that it did not work when there are duplicate elements in the middle of the longest subsequence.
So I used only one pointer `rt` and used `curLen` to record the length of the consecutive sequence ending at index `rt`. Note that we need to return `max(maxLen, curLen)` in case the last item is in the longest consecutive sequence and the loop did not update the `maxLen`.

## Question 34: Clone Graph
[Question description](https://leetcode.com/problems/clone-graph/) here.

This question is simple. I just used BFS to create a copied graph. I used a `val2Node` dictionary to store a mapping between node value to the node so that I won't create duplicate nodes. This only works when the graph nodes have unique values, which is gauranteed in the problem description.

## Question 35: Word Break
[Question description](https://leetcode.com/problems/word-break/) here.

This question is simple. At first I used tree recursion and it worked, but as I predicted, it was too slow and exceeded time limit.
Then I use dynamic programming and set `dp[i]` to be whether `s[i:]` can be segmented by the `wordDict`. I traverse from right to left of `s` and for every index i, I try to match every word in the `wordDict` with string start from `i` and if there is a match and that `dp[i+len(word)]` is True, I set `dp[i]` to be True. Finally I return `dp[0]`.