def longest_consecutive(nums: list[int]) -> int:
    counter = {}
    longest = 0

    for n in nums:
        if n in counter:
            continue

        if n - 1 in counter and n + 1 in counter:
            if len(counter[n - 1]) > len(counter[n + 1]):
                s = counter[n - 1]
                s |= counter[n + 1]
                for e in counter[n + 1]:
                    counter[e] = s
            else:
                s = counter[n + 1]
                s |= counter[n - 1]
                for e in counter[n - 1]:
                    counter[e] = s


        elif n - 1 in counter:
            s = counter[n - 1]
        elif n + 1 in counter:
            s = counter[n + 1]
        else:
            s = set()

        s.add(n)
        counter[n] = s
        longest = max(longest, len(s))
    return longest

def test_longest_consecutive():
    nums = [2, 20, 4, 10, 3, 4, 5]
    assert(longest_consecutive(nums) == 4)

    nums = [0, 3, 2, 5, 4, 6, 1, 1]
    assert(longest_consecutive(nums) == 7)


if __name__ == "__main__":
    test_longest_consecutive()
