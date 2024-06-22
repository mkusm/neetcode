def test_two_sum():
    assert two_sum([2, 7, 11, 15], 9) == [0, 1]
    assert two_sum([3, 2, 4], 6) == [1, 2]
    assert two_sum([3, 3], 6) == [0, 1]


def two_sum(nums: list[int], target: int) -> list[int]:
    seen_nums = {}
    for i, e in enumerate(nums):
        missing = target - e
        if missing in seen_nums:
            return [seen_nums[missing], i]
        seen_nums[e] = i
    raise ValueError


if __name__ == "__main__":
    test_two_sum()
        
