#include <cassert>
#include <cstdio>
#include <unordered_set>
#include <vector>

using std::vector, std::printf;

bool has_duplicate(vector<int>& nums) {
	std::unordered_set<int> set;
	for (int num : nums) {
		if (set.find(num) == set.end()) {
			set.insert(num);
		} else {
			return true;
		}
	}

	return false;
}

void test_has_duplicate()
{
	std::vector<int> vec1 = {1, 2, 3, 4, 5};
	assert(!has_duplicate(vec1));

	std::vector<int> vec2 = {1, 2, 3, 4, 5, 1};
	assert(has_duplicate(vec2));

	std::vector<int> vec3 = {1, 1, 1, 1, 1};
	assert(has_duplicate(vec3));

	std::vector<int> vec4 = {1};
	assert(!has_duplicate(vec4));

	printf("All tests passed for has_duplicate.\n");
}

int main()
{
	test_has_duplicate();
	return 0;
}
