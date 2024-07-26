#include <unordered_set>
#include <vector>
#include <cassert>
#include <iostream>

using std::vector, std::unordered_set;

int longest_consecutive(vector<int>& nums) 
{
	unordered_set<int> set;
	int longest = 0;

	for (int n : nums) {
		set.insert(n);
	}

	for (int n : set) {
		if (set.find(n - 1) != set.end()) {
			continue;
		}

		int len = 1;
		while (set.find(n + len) != set.end()) {
			len++;
		}

		if (len > longest) {
			longest = len;
		}
	}
	
	return longest;
}

void test_longest_consecutive()
{
	vector<int> nums;

	nums = {2, 20, 4, 10, 3, 4, 5};
	assert(longest_consecutive(nums) == 4);

	nums = {0, 3, 2, 5, 4, 6, 1, 1};
	assert(longest_consecutive(nums) == 7);

	std::cout << "All tests passed" << std::endl;
}

int main()
{
	test_longest_consecutive();
	return 0;
}
