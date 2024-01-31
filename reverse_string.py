def reverse_string(s):
    reverse_string = ""
    length_string = len(s)

    for i in reversed(range(length_string)):
        print(i)
        reverse_string += s[i]

    return reverse_string


if __name__ == "__main__":
    # Test case 1
    s1 = "hallo"
    print("Test Case 1:", reverse_string(s1))  # Expected output: ["o", "l", "l", "e", "h"]

    # Test case 2
    s2 = "Mijn naam is Arthike"
    print("Test Case 2:", reverse_string(s2))  # Expected output: ["h", "a", "n", "n", "a", "H"]
