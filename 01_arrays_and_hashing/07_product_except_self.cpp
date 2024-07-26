#include <iostream>
#include <vector>
#include <cassert>

using std::vector;

vector<int> product_except_self(const vector<int>& nums)
{
	vector<int> prefixes(nums.size(), 1), postfixes(nums.size(), 1), res(nums.size(), 0);
	for (int i = 1; i < nums.size(); i++) {
		prefixes[i] = prefixes[i-1] * nums[i-1];
	}
	for (int i = nums.size() - 2; i >= 0; i--) {
		postfixes[i] = postfixes[i+1] * nums[i+1];
	}
	for (int i = 0; i < nums.size(); i++) {
		res[i] = prefixes[i] * postfixes[i];
	}

	return res;
}

void test_product_except_self()
{
	vector<int> v, expected;

	v = {1,2,3,4};
	v = product_except_self(v);
	expected = {24,12,8,6};
	assert(v == expected);

	v = {-1,1,0,-3,3};
	v = product_except_self(v);
	expected = {0,0,9,0,0};
	assert(v == expected);

	std::cout << "All tests passed." << std::endl;
}

int main()
{
	test_product_except_self();
	return 0;
}
