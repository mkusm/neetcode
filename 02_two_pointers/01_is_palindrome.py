def is_palindrome(s: str) -> bool:
    s = s.lower()
    i = 0
    j = len(s) - 1
    while i < j:
        if i >= len(s) or j < 0:
            return True
        if not s[i].isalnum():
            i += 1
            continue
        if not s[j].isalnum():
            j -= 1
            continue
        if not s[i] == s[j]:
            return False
        i += 1
        j -= 1
    return True


def test_is_palindrome():
    assert is_palindrome("racecar")
    assert not is_palindrome("hello")
    assert not is_palindrome("tab a cat")

if __name__ == "__main__":
    test_is_palindrome()
