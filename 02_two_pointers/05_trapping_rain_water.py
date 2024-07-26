# find heighest first solution
def trap(height: list[int]) -> int:
    highest_val = 0
    highest_index = 0
    for i, val in enumerate(height):
        if val > highest_val:
            highest_val = val
            highest_index = i

    total_water = 0

    l = 0
    r = highest_index
    beginning = True
    left_max = 0

    while (l < r):
        if beginning:
            if height[l] == 0:
                l += 1
                continue
            else:
                beginning = False

        left_max = max(left_max, height[l])
        total_water += left_max - height[l]
        l += 1

    l = highest_index
    r = len(height) - 1
    beginning = True
    right_max = 0

    while (l < r):
        if beginning:
            if height[r] == 0:
                r -= 1
                continue
            else:
                beginning = False

        right_max = max(right_max, height[r])
        total_water += right_max - height[r]
        r -= 1

    return total_water


# simpler solution
def trap(height):

    total_water = 0

    l = 0
    r = len(height) - 1
    left_max = height[l]
    right_max = height[r]

    while (l < r):
        while left_max == 0:
            l += 1
            left_max = max(left_max, height[l])
        while right_max == 0:
            r -= 1
            right_max = max(right_max, height[r])

        if left_max < right_max:
            total_water += left_max - height[l]
            l += 1
            left_max = max(left_max, height[l])
        else:
            total_water += right_max - height[r]
            r -= 1
            right_max = max(right_max, height[r])

    return total_water



def test_trap():
    height = [0, 2, 0, 3, 1, 0, 1, 3, 2, 1]
    assert trap(height) == 9


if __name__ == "__main__":
    test_trap()
