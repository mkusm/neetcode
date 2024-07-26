from collections import defaultdict


def character_replacement(s: str, k: int) -> int:
    def most_common_char_count(chars: dict[str, int]) -> str:
        # max_ = 0
        # max_char = ""
        # for c in chars.keys():
        #     if chars[c] > max_:
        #         max_ = chars[c]
        #         max_char = c
        # return max_char
        max_ = 0
        for v in chars.values():
            max_ = max(max_, v)
        return max_

    l, r = 0, 0
    chars = defaultdict(int)
    longest = 0

    while r < len(s):
        chars[s[r]] += 1
        r += 1

        window_length = r - l
        is_legit = window_length <= most_common_char_count(chars) + k

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
