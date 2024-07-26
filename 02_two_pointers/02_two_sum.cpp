#include <cassert>
#include <vector>
#include <iostream>

using std::vector;

vector<int> two_sum(vector<int>& numbers, int target)
{
	int i = 0;
	int j = numbers.size() - 1;

	while (i < j) {
		int sum = numbers[i] + numbers[j];

		if (sum > target) j--;
		else if (sum < target) i++;
		else return vector<int>{i++, j++};
	}

	return vector<int>{i, j};
}

void test_two_sum()
{
	vector<int> numbers, expected;
	int target;

	numbers = {1, 2, 3, 4};
	target = 3;
	expected = {0, 1};
	assert(two_sum(numbers, target) == expected);

	numbers = {2, 3, 4};
	target = 6;
	expected = {0, 2};
	assert(two_sum(numbers, target) == expected);

	numbers = {3, 3};
	target = 6;
	expected = {0, 1};
	assert(two_sum(numbers, target) == expected);

	std::cout << "All tests passed" << std::endl;
}

int main()
{
	test_two_sum();
	return 0;
}
