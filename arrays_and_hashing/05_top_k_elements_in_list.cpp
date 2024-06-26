#include <cassert>
#include <cstdio>
#include <stdexcept>
#include <unordered_map>
#include <vector>

using std::vector;

vector<int> top_k_frequent(vector<int>& nums, int k) {
	std::unordered_map<int, int> num_count;
	for (const auto& num : nums) {
		num_count[num]++;
	}

	vector<vector<int>> count_to_nums(nums.size() + 1, vector<int>{}); 
	for (auto& pair : num_count) {
		count_to_nums[pair.second].push_back(pair.first);
	}

	vector<int> result;
	for (int i = count_to_nums.size() - 1; i > 0; i--) {
		for (auto& num : count_to_nums[i]) {
			result.push_back(num);
			if (result.size() == k) {
				return result;
			}
		}
	}
	throw std::invalid_argument("no matching values");
}

void test_top_k_frequent()
{
	vector<int> nums = {1, 1, 1, 2, 2, 3};
	int k = 2;
	vector<int> result = top_k_frequent(nums, k);
	vector<int> expected = {1, 2};
	assert(result == expected);

	nums = {1};
	k = 1;
	result = top_k_frequent(nums, k);
	expected = {1};
	assert(result == expected);

	nums = {7, 7};
	k = 1;
	result = top_k_frequent(nums, k);
	expected = {7};
	assert(result == expected);

	nums = {1, 2, 2, 3, 3, 3};
	k = 2;
	result = top_k_frequent(nums, k);
	expected = {3, 2};
	assert(result == expected);

	printf("All tests passed for make_hashable.\n");
}

int main()
{
	test_top_k_frequent();
	return 0;
}
