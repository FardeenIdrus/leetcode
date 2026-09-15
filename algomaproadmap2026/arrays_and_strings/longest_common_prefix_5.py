from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        # Start by assuming the first word is the entire common prefix.
        # We will shrink this down as we compare it against each subsequent word.
        running_prefix = strs[0]

        # Tracks how many characters of running_prefix have matched the current
        # word so far. Reset to 0 before comparing against each new word.
        pointer = 0

        for i in range(1, len(strs)):
            if not strs[i]:
                running_prefix = ""
            for char in strs[i]:
    
                # running_prefix has already been fully matched/exhausted by this word
                # (i.e. this word is at least as long as running_prefix, and every
                # character checked so far has matched). There is nothing left in
                # running_prefix to compare against, so stop checking this word.
                # running_prefix does NOT need to shrink here, because everything
                # in it has matched so far.
                if pointer >= len(running_prefix):
                    break

                # Compare the character at position `pointer` in running_prefix
                # against the current character in strs[i].
                if char != running_prefix[pointer]:
                    # Mismatch found. The common prefix can only be as long as the
                    # characters that matched before this point, so truncate
                    # running_prefix to length `pointer`.
                    running_prefix = running_prefix[0:pointer]
                    # No need to check the rest of this word's characters — the
                    # prefix has already been decided for this comparison.
                    break

                else:
                    # Characters matched. Move to the next position to compare.
                    pointer += 1

                    # The current word ended exactly here, with every character
                    # matching so far, and no mismatch was found. This means the
                    # word itself is shorter than (or equal to) running_prefix,
                    # so the common prefix can't be longer than this word.
                    # Truncate running_prefix to this word's length.
                    if len(strs[i]) == pointer:
                        running_prefix = running_prefix[0:pointer]

            # Reset pointer before comparing running_prefix against the next word.
            pointer = 0

        return running_prefix


if __name__ == "__main__":
    sol = Solution()

    print(sol.longestCommonPrefix(["flower", "flow", "flight"]))
    print(sol.longestCommonPrefix(["dog", "racecar", "car"]))
    print(sol.longestCommonPrefix(["abab", "aba", ""]))


# Time complexity: O(n * m), where n is the number of words in strs, and m is
# the length of the longest word. In the worst case (e.g. all words identical
# or all sharing a long common prefix), we compare up to m characters for each
# of the n words.

# Space complexity: O(1) auxiliary space — pointer is a single integer that
# does not grow with input size. running_prefix is not counted as extra space
# because it holds the function's return value (the output itself), not
# additional working memory. Note: if you count the output, running_prefix's
# size is bounded by the length of the longest word, i.e. O(m) — but this is
# excluded under the standard convention of measuring only auxiliary space.