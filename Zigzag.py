import unittest


def convert(s: str, k: int) -> str:
    Zigzag_matrix = [[] for _ in range(k)]
    row_pointer: int = 0
    row_direction: bool = True

    for char in s:
        Zigzag_matrix[row_pointer].append(char)
        if row_pointer == k - 1:
            row_direction = False
        elif row_pointer == 0:
            row_direction = True

        if row_direction and row_pointer < k:
            row_pointer += 1
        elif row_pointer > 0:
            row_pointer -= 1

    string = ""

    for i in Zigzag_matrix:
        for j in range(len(i)):
            string = string + i[j]

    return string


class TestZigzagConversion(unittest.TestCase):

    def test_zigzag_conversion_3_rows(self):
        result = convert("PAYPALISHIRING", 3)
        self.assertEqual(result, "PAHNAPLSIIGYIR")

    def test_zigzag_conversion_4_rows(self):
        result = convert("PAYPALISHIRING", 4)
        self.assertEqual(result, "PINALSIGYAHRPI")

    def test_single_char(self):
        result = convert("A", 1)
        self.assertEqual(result, "A")

    def test_single_row(self):
        result = convert("PAYPALISHIRING", 1)
        self.assertEqual(result, "PAYPALISHIRING")


if __name__ == '__main__':
    unittest.main()
