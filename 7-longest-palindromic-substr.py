# solution by Rui Wang
# problem description link: https://leetcode.com/problems/longest-palindromic-substring/

class Solution:
    # dynamic programming version, but too slow.
    def longestPalindrome_dp(self, s: str) -> str:
        dp = [[False] * len(s) for _ in range(len(s))]
        for i in range(len(s)):
            dp[i][i] = True
        
        # first, take s[0] as longest.
        max_str = s[0]
        for i in range(len(s)-1, -1, -1):
            for j in range(i+1, len(s)):
                if s[i] == s[j]:
                    if j == i+1 or dp[i+1][j-1]:
                        dp[i][j] = True
                        if len(max_str) < j - i + 1:
                            max_str = s[i:j+1]
        
        return max_str
    
    # window expansion version, much faster.
    def longestPalindrome(self, s: str) -> str:
        if len(s) <= 1:
            return s
        
        # I want to use centers, but sometimes center is between two chars, so I plug in '|' between each
        # char.
        s1 = '|'
        for c in s:
            s1 += c + '|'
        
        # longest radius of palindrome centered at i.
        longestRadius = [0] * len(s1)
        
        center = 0
        radius = 0
        while center < len(s1):
            # first, expand the window to max radius.
            while (center - radius - 1) >= 0 and (center + radius + 1) < len(s1):
                if s1[center-radius-1] != s1[center+radius+1]:
                    break
                radius += 1
            
            longestRadius[center] = radius
            
            # now we should try to expand window for following centers. The loop goes to the leftmost
            # position of current palindrome window.
            old_center, old_radius = center, radius
            center, radius = center + 1, 0
            while center < old_center + old_radius:
                # the mirrored center of current center w.r.t the old center (the one we expanded in
                # the previous inner loop.)
                mirrored_center = old_center - (center - old_center)
                # this is the max possible mirrored radius of current center.
                max_mirrored_rad = old_center + old_radius - center

                if longestRadius[mirrored_center] < max_mirrored_rad:
                    # in this case, we know that the palindrome window of mirrored center is within the
                    # palindrome center of old center. And we know that the radius of current center 
                    # must be the same with mirrored center. We can prove this by contradiction.
                    longestRadius[center] = longestRadius[mirrored_center]
                elif longestRadius[mirrored_center] > max_mirrored_rad:
                    # in this case, the radius of current center is exactly the max_mirrored_rad because
                    # s1[mirrored_center - max_mirrored_rad - 1] == s1[mirrored_center + max_mirrored_rad + 1]
                    # == s1[center - max_mirrored_rad - 1] != s1[center + max_mirrored_rad + 1]
                    longestRadius[center] = max_mirrored_rad
                else:
                    # in this case, the radius of current center is to be determined.
                    radius = max_mirrored_rad
                    break
                center += 1
        
        max_center = max(range(len(s1)), key=lambda i: longestRadius[i])
        max_radius = longestRadius[max_center]

        if max_radius % 2 == 0:
            lt_bd = (max_center - max_radius + 1) // 2
            rt_bd = (max_center + max_radius - 1) // 2
            return s[lt_bd:rt_bd+1]
        else:
            max_center //= 2
            max_radius //= 2
            return s[max_center-max_radius:max_center+max_radius+1]

sol = Solution()
print(sol.longestPalindrome('cbbd'))