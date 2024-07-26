def length_of_longest_substring_no_duplicates(s: str) -> int:
    substring = set()
    longest, l, r = 0, 0, 0

    while r < len(s):

        if s[r] in substring:
            while s[l] != s[r]:
                substring.remove(s[l])
                l += 1
            substring.remove(s[l])
            l += 1

        substring.add(s[r])
        r += 1
        longest = max(len(substring), longest)

    return longest
    

def test_length_of_longest_substring_no_duplicates():
    input = "zxyzxyz"
    assert length_of_longest_substring_no_duplicates(input) == 3

    input = "xxxx"
    assert length_of_longest_substring_no_duplicates(input) == 1

if __name__ == "__main__":
    test_length_of_longest_substring_no_duplicates()
