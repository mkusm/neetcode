def test_is_anagram():
    assert is_anagram('racecar', 'carrace')
    assert not is_anagram('racecar', 'carraco')
    assert not is_anagram('jar', 'jam')
    assert is_anagram('anagram', 'garanam')
    assert not is_anagram('anagram', 'garanamm')
    assert is_anagram('a', 'a')
    assert not is_anagram('a', 'aa')
    assert not is_anagram('a', 'b')


# first solution, O(n*log(n))
def is_anagram(s: str, t: str) -> bool:
    l = list(t)
    for e in s:
        try:
            l.pop(l.index(e))
        except ValueError:
            return False
    return not bool(l)


# second solution, O(n)
from collections import defaultdict
def is_anagram(s: str, t: str) -> bool:
    s_dict = defaultdict(int)
    t_dict = defaultdict(int)

    for e in s: s_dict[e] += 1
    for e in t: t_dict[e] += 1

    return s_dict == t_dict


if __name__ == "__main__":
    test_is_anagram()
