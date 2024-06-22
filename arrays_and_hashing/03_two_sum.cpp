#include <cassert>
#include <cstdio>
#include <unordered_map>
#include <vector>
#include <stdexcept>

using std::vector, std::unordered_map;


vector<int> two_sum(vector<int>& nums, int target) {
	unordered_map<int, int> seen_nums;
	for (int i = 0; i < nums.size(); i++) {
		int missing = target - nums[i];
		if (seen_nums.contains(missing))
			return vector<int>{seen_nums[missing], i};
		seen_nums[nums[i]] = i;
	}
	throw std::invalid_argument("no matching values");
}

void test_two_sum()
{
	vector<int> nums = {2, 7, 11, 15};
	int target = 9;
	vector<int> expected = {0, 1};
	assert(two_sum(nums, target) == expected);

	nums = {3, 2, 4};
	target = 6;
	expected = {1, 2};
	assert(two_sum(nums, target) == expected);

	nums = {3, 3};
	target = 6;
	expected = {0, 1};
	assert(two_sum(nums, target) == expected);

	printf("All tests passed for two_sum.\n");
}

int main()
{
	test_two_sum();
	return 0;
}
