# 2 Pointer Solution

class Solution: 
    def trap(self, height:list[int]) -> int:

        # Main idea: the water above a block = min(tallest block to its left, tallest block to its right) - height of the block,
        # or 0 if this is negative. The brute force stored both tallest values for every block in two lists.
        # Here we only keep a running maximum for each side, and process one block per step,
        # always from the side with the smaller maximum
        
        n = len(height)
        # Left and right pointers, standing on the first and last blocks.
        # These two blocks are already "seen": they hold no water (nothing is on one side of them),
        # so we skip them and only use them as walls
        left_wall = 0
        right_wall = n-1
        # The tallest block seen so far on each side. At the start, that is the block each pointer stands on
        left_max = height[left_wall]
        right_max = height[right_wall]
        # Initialise total
        total = 0
        
        # Each iteration processes one new block, from the left or the right, and moves that pointer inwards.
        # When the pointers meet, every block has been processed
        while left_wall < right_wall:
            # The water level above a block is set by the lower of its two walls.
            # smaller_wall is the lower of the two running maximums, so it tells us which side to process
            smaller_wall = min(left_max, right_max)
            # If left_max is the smaller one (or they are equal), process the left side.
            # Why this is safe: the next block on the left is at index left_wall + 1.
            # Its left wall is exactly left_max, because left_max is the tallest of the blocks at indexes 0 to left_wall,
            # which are all the blocks to its left.
            # If left_max is the smaller one (or they are equal), process the left side.
            # The next block's left wall is exactly left_max (every block to its left has been seen).
            # Its right wall is the tallest block to its right. One of those blocks is already known to be right_max tall,
            # so the right wall is at least right_max, which is at least left_max. So the lower wall is left_max
            if smaller_wall == left_max:
                # Move the left pointer to the next block. left_wall is already seen (the start, or the block just processed),
                # so the next block still to process is left_wall + 1
                left_wall +=1
                
                # The water above this block is the tallest wall to its left (left_max) minus the height of the block itself.
                # Imagine left_max = 3, and the current block has height = 1, so we can store (3-1=2) blocks of water here.
                # However, if the current block is taller than any wall to its left, then no water can be stored here.
                # Imagine left_max = 3, and the current block has height 4, so 3-4 is negative, and max(0, ...) makes it 0
                pot = max(0, left_max - height[left_wall])
                # Add the water above this block to the running total
                total += pot
                # Now include this block in left_max, ready for the next block. This is done AFTER computing the water,
                # so the block is not compared with itself
                left_max = max(left_max, height[left_wall])
            
            # Otherwise right_max is the smaller one, so process the right side. This is the same as the left side, mirrored
            else:
                right_wall -=1
                pot = max(0, right_max - height[right_wall])
                total += pot
                right_max = max(right_max, height[right_wall])
        
        return total


if __name__ == "__main__":
    sol = Solution()
    print(sol.trap([0,1,0,2,1,0,1,3,2,1,2,1]))
    print(sol.trap([3,0,2,0,4]))
    