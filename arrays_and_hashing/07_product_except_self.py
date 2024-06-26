from functools import reduce

def test_product_except_self():
    assert product_except_self([1, 2, 3, 4]) == [24, 12, 8, 6]
    assert product_except_self([-1, 1, 0, -3, 3]) == [0, 0, 9, 0, 0]


# solution 1 using division
def product_except_self(nums: list[int]) -> list[int]:
    zeros = nums.count(0) 
    if zeros > 1:
        return [0] * len(nums)
    elif zeros == 1:
        product_without_zero = reduce(lambda a,b: a*b if b!=0 else a, nums)
        return [0 if e != 0 else product_without_zero for e in nums]
    product = reduce(lambda a,b: a*b, nums)
    return [product/e if e != 0 else product for e in nums]


# solution 2 without division
def product_except_self(nums: list[int]) -> list[int]:
    prefixes = [1] * len(nums)
    postfixes = [1] * len(nums)
    for i in range(len(nums)):
        if i == 0:
            continue
        prefixes[i] = prefixes[i - 1] * nums[i - 1]
    for i in reversed(range(len(nums))):
        if i == len(nums) - 1:
            continue
        postfixes[i] = postfixes[i + 1] * nums[i + 1]
    res = [0] * len(nums)
    for i in range(len(nums)):
        res[i] = prefixes[i] * postfixes[i]
    return res
        

if __name__ == "__main__":
    test_product_except_self()

