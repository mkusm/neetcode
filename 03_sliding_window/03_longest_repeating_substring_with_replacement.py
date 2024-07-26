from collections import defaultdict


def character_replacement(s: str, k: int) -> int:
    l, r = 0, 0
    chars = defaultdict(int)
    longest = 0

    while r < len(s):
        chars[s[r]] += 1
        r += 1

        window_length = r - l
        is_legit = window_length <= max(chars.values()) + k

        if is_legit:
            longest = max(longest, window_length)
        else:
            chars[s[l]] -= 1
            l += 1

    return longest



def test_character_replacement():
    s = "XYYX"
    k = 2
    assert character_replacement(s, k) == 4

    s = "AAABABB"
    k = 1
    assert character_replacement(s, k) == 5

    s = "AAAA"
    k = 2
    assert character_replacement(s, k) == 4

    s = "AABABBA"
    k = 1
    assert character_replacement(s, k) == 4

    s = "ABBB"
    k = 2
    assert character_replacement(s, k) == 4


if __name__ == "__main__":
    test_character_replacement()
