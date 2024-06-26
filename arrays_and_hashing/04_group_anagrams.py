def test_group_anagrams():
    assert (
        sort(group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
        == sort([["bat"], ["nat", "tan"], ["ate", "eat", "tea"]])
    )
    assert (
        sort(group_anagrams(["anagram", "nagaram", "margana"]))
        == sort([["anagram", "nagaram", "margana"]])
    )
    assert sort(group_anagrams([""])) == sort([[""]])
    assert sort(group_anagrams(["a"])) == sort([["a"]])
    assert sort(group_anagrams(["", ""])) == sort([["", ""]])
    assert sort(group_anagrams(["a", "a"])) == sort([["a", "a"]])
    assert sort(group_anagrams(["a", "b"])) == sort([["a"], ["b"]])
    assert sort(group_anagrams(["ab", "ba"])) == sort([["ab", "ba"]])


def sort(group):
    if len(group) < 2:
        return sorted(group)
    return sorted([sorted(words) for words in group])
    
    
# solution 1
from collections import defaultdict
def group_anagrams(strs: list[str]) -> list[list[str]]:
    grouped_anagrams = []
    for word in strs:
        chars = defaultdict(int)
        for char in word:
            chars[char] += 1
        for group in grouped_anagrams:
            if group[0] == chars:
                group[1].append(word)
                break
        else:
            grouped_anagrams.append([chars, [word]])
    groups = [group[1] for group in grouped_anagrams]
    return groups


# solution 2
from collections import defaultdict
def group_anagrams(strs: list[str]) -> list[list[str]]:
    grouped_anagrams = defaultdict(list)
    for word in strs:
        chars = defaultdict(int)
        for char in word:
            chars[char] += 1
        hashable_chars = tuple(sorted(chars.items()))
        grouped_anagrams[hashable_chars].append(word)
    return grouped_anagrams.values()

# solution 3
from collections import defaultdict
def group_anagrams(strs: list[str]) -> list[list[str]]:
    grouped_anagrams = defaultdict(list)
    for word in strs:
        chars = [0] * 26
        for char in word:
            chars[ord(char) - ord("a")] += 1
        grouped_anagrams[tuple(chars)].append(word)
    return grouped_anagrams.values()


if __name__ == "__main__":
    test_group_anagrams()
