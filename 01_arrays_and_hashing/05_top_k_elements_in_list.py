from collections import defaultdict
from collections import Counter


def test_top_k_frequent():
    assert set(top_k_frequent([1, 1, 1, 2, 2, 3], 2)) == set([1, 2])
    assert set(top_k_frequent([1], 1)) == set([1])
    assert set(top_k_frequent([1,2,2,3,3,3], 2)) == set([3, 2])


# solution 1
def top_k_frequent(nums: list[int], k: int) -> list[int]:
    num_count = defaultdict(int)
    for num in nums:
        num_count[num] += 1

    counts_and_values = sorted(num_count.items(), key=lambda x: x[1], reverse=True)
    counts = [pair[0] for pair in counts_and_values[:k]]
    return counts


# solution 2
def top_k_frequent(nums: list[int], k: int) -> list[int]:
    return [most_common for most_common, count in Counter(nums).most_common(k)]


# solution 3
def top_k_frequent(nums: list[int], k: int) -> list[int]:
    num_count = defaultdict(int)
    for num in nums:
        num_count[num] += 1
    count_to_nums = [[] for i in range(len(nums) + 1)]

    for key, value in num_count.items():
        count_to_nums[value].append(key)

    res = []
    for counted_nums in reversed(count_to_nums):
        for num in counted_nums:
            res.append(num)
            if len(res) == k:
                return res


if __name__ == "__main__":
    test_top_k_frequent()
