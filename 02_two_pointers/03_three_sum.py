def three_sum(nums: list[int]) -> list[list[int]]:
    res = []
    nums.sort()

    for i, n in enumerate(nums):
        if n > 0:
            break

        if i > 0 and nums[i - 1] == n:
            continue

        l = i + 1
        r = len(nums) - 1

        while (l < r):
            if n + nums[l] + nums[r] > 0: r -= 1
            elif n + nums[l] + nums[r] < 0: l += 1
            else:
                res.append([n, nums[l], nums[r]])
                r -= 1
                l += 1
                while (l != len(nums) and nums[l] == nums[l - 1]):
                    l += 1

    return res



def test_three_sum():
    nums = [-1,0,1,2,-1,-4]
    expected = [[-1,-1,2],[-1,0,1]]
    assert three_sum(nums) == expected

    nums = [0, 0, 0]
    expected = [[0, 0, 0]]
    assert three_sum(nums) == expected

    nums=[-2, 0, 0, 2, 2]
    expected = [[-2, 0, 2]]
    assert three_sum(nums) == expected


if __name__ == "__main__":
    test_three_sum()
