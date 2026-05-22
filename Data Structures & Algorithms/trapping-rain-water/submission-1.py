class Solution:
    def trap(self, height: List[int]) -> int:
        l_max = [0]
        max = -1
        for i in range(1, len(height)):
            if height[i-1] > max:
                max = height[i-1]
                
            l_max.append(max)
        
        r_max = [0]
        max = -1
        for i in range((len(height)-2), -1, -1):
            if height[i+1] > max:
                max = height[i+1]
            r_max.append(max)
        
        r_max = r_max[::-1]
        r_max

        water = 0
        for i in range(1, len(height)-1):
            if (min(l_max[i], r_max[i]) - height[i]) <= 0:
                continue
            else:
                water += min(l_max[i], r_max[i]) - height[i]
                print(water)
        return water