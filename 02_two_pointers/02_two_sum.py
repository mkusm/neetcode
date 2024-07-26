
def two_sum(numbers: list[int], target: int) -> list[int]:
    # assuming input is sorted in non-decreasing order
    i = 0
    j = len(numbers) - 1
    while i + 1 < j:
        while numbers[i] + numbers[j] > target:
            j -= 1
        while numbers[i] + numbers[j] < target:
            i += 1
        if numbers[i] + numbers[j] == target:
            return [i, j]
    return [i, j]
        

def test_two_sum():
    numbers = [1, 2, 3, 4]
    target = 3
    expected = [0, 1]
    assert(two_sum(numbers, target) == expected)

    numbers = [2, 3, 4]
    target = 6
    expected = [0, 2]
    assert(two_sum(numbers, target) == expected)

    numbers = [3, 3]
    target = 6
    expected = [0, 1]
    assert(two_sum(numbers, target) == expected)


if __name__ == "__main__":
    test_two_sum()
