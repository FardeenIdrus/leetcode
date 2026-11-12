class Solution:

    def maxArea(self, height: list[int]) -> int:

        # Initialise the left and right walls at the two ends, the widest possible pair
        left_wall = 0
        right_wall = len(height)-1

        # The height of the container is the height of the shorter wall, because water
        # spills over the shorter wall, so it cannot rise any higher than that
        shorter_wall = min(height[left_wall], height[right_wall])

        # The width is the difference between the indexes of the two walls
        width = right_wall - left_wall

        max_area = width * shorter_wall

        # Check one pair of walls per iteration. Not every pair is checked: dropping the
        # shorter wall each time skips pairs that cannot beat the area already recorded
        while left_wall < right_wall:

            shorter_wall = min(height[left_wall],height[right_wall])
            width = right_wall - left_wall
            max_area = max(max_area, shorter_wall*width)

            # If the left wall is shorter than the right wall, discard the left wall.
            # Any other pair that keeps the left wall has a height of at most the left wall's
            # height and a smaller width than the current pair, so its area is smaller than
            # the current pair's area. Keeping the shorter wall cannot give a better area,
            # so move the left wall inwards to try a different pair
            if height[left_wall] < height[right_wall]:

                # If moving the left wall inwards would make it meet the right wall,
                # no valid pair of walls is left, so return the maximum area
                if left_wall + 1 < right_wall:
                    left_wall +=1
                else:
                    return max_area

            # If the right wall is shorter, discard it for the same reason
            elif height[left_wall] > height[right_wall]:
                if right_wall -1 >left_wall:
                    right_wall -=1
                else:
                    return max_area

            # If both walls are the same height, dropping either one is safe.
            # Any other pair that keeps the left wall has a smaller width and a height of at most
            # that wall's height, so it cannot beat the recorded area. The same is true of the
            # right wall, so neither is needed and either can be dropped.
            else:
                if right_wall-1 > left_wall:
                    right_wall -=1
                else:
                    return max_area

        return max_area
    
    

if __name__ == "__main__":
    sol = Solution()
    print(sol.maxArea([1,8,6,2,5,4,8,3,7]))
    print(sol.maxArea([1,1]))
    
# Time Complexity: O(n), where n is the number of elements in height
    # The while loop runs at most n times, because every iteration moves one wall inwards, 
    # so the gap between the walls shrinks by 1 each time
    # Each iteration of the while loop does O(1) work
    # Total : O(n)
    
# Space Complexity: O(1)
    # All variables used take constant space -> O(1)

    