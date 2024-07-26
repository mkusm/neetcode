def test_has_duplicate():
    assert has_duplicate([1, 2, 3, 3])
    assert has_duplicate([1, 1])
    assert has_duplicate([-1, -1])
    assert not has_duplicate([1, 2, 3, 4])
    assert not has_duplicate([1])
    assert not has_duplicate([])


def has_duplicate(nums: list[int]) -> bool:
    return len(set(nums)) < len(nums)


if __name__ == "__main__":
    test_has_duplicate()
