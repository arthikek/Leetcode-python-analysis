import unittest


def lengthOfLongestSubstring(s: str) -> int:
    charSet = set()
    l = 0
    res = 0

    for r in range(len(s)):
        while s[r] in charSet:
            charSet.remove(s[l])
            l += 1
        charSet.add(s[r])
        res = max(res, r - l + 1)

    return res


class TestLongestSubstring(unittest.TestCase):
    def test_longest_substring_with_repeated_chars(self):
        """Test case for a string with repeated characters and a mix of unique characters."""
        result = lengthOfLongestSubstring("pwwkew")
        self.assertEqual(result, 3)

    def test_longest_substring_unique_chars(self):
        """Test case for a string with a mix of repeating and non-repeating characters."""
        result = lengthOfLongestSubstring("abcabcbb")
        self.assertEqual(result, 3)

    def test_longest_substring_single_char(self):
        """Test case for a string with all characters being the same."""
        result = lengthOfLongestSubstring("bbbbb")
        self.assertEqual(result, 1)

    # You can add more test cases here


# This allows running the tests from the command line
if __name__ == '__main__':
    unittest.main()
