def max_area(heights: list[int]) -> int:
    l = 0
    r = len(heights) - 1
    max_area = 0

    while (l < r):
        area = min(heights[l], heights[r]) * (r - l)
        max_area = max(max_area, area)
        if heights[l] <= heights[r]:
            l += 1
        else:
            r -= 1

    return max_area


def test_max_area():
    height = [1,7,2,5,4,7,3,6]
    assert max_area(height) == 36

    height = [2, 2, 2]
    assert max_area(height) == 4


if __name__ == "__main__":
    test_max_area()
