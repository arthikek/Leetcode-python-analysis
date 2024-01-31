import unittest


def longest_palindromic_substring(s: str) -> str:
    longest_palindrome_answer = ""

    for index, character in enumerate(s):
        palin = expander(s, index)
        if len(palin) > len(longest_palindrome_answer):
            longest_palindrome_answer = palin

    return longest_palindrome_answer


def expander(array, index):
    palin_start_location = " "
    last_index = len(array) - 1
    lower_bound = index
    upper_bound = last_index - index
    allowed_steps = lower_bound if lower_bound < upper_bound else upper_bound

    if index == 0:
        for i in range(len(array)):
            palin = palindrome_checker(array[0:i])
            if palin:
                palin_start_location = array[0:i]

                continue
            else:
                break

    if index == last_index:
        for i in range(len(array)):
            palin = palindrome_checker(array[-i])
            if palin:
                palin_start_location = array[-i]
                continue
            else:
                break


    else:
        for i in range(allowed_steps):
            window = array[index - i - 1:index + i + 2]
            palin = palindrome_checker(window)
            if palin:
                if len(palin_start_location) < len(window):
                    palin_start_location = window
            else:
                break

    return palin_start_location


def palindrome_checker(palindrome):
    if palindrome == palindrome[::-1]:
        return True
    else:
        return False


class TestLongestPalindromicSubstring(unittest.TestCase):

    def test_basic_cases(self):
        self.assertEqual(longest_palindromic_substring("babad"), "bab")
        self.assertEqual(longest_palindromic_substring("cbbd"), "bb")

    def test_edge_cases(self):
        self.assertEqual(longest_palindromic_substring(""), "")
        self.assertEqual(longest_palindromic_substring("a"), "a")
        self.assertEqual(longest_palindromic_substring("aa"), "aa")

    def test_complex_cases(self):
        self.assertEqual(longest_palindromic_substring("abacdfgdcaba"), "aba")
        self.assertEqual(longest_palindromic_substring("abacdfgdcabba"), "abba")

    def test_single_character_repeated(self):
        self.assertEqual(longest_palindromic_substring("aaaa"), "aaaa")


# Make sure to add this block to allow running the tests
if __name__ == '__main__':
    unittest.main()
