#include <cassert>
#include <cstdio>
#include <sstream>
#include <string>
#include <unordered_map>
#include <vector>
#include <iterator>
#include <algorithm>

using std::vector, std::string;

string make_hashable(const vector<int>& vec) {
	std::ostringstream oss;
	std::copy(vec.begin(), vec.end(), std::ostream_iterator<int>(oss, " "));
	return oss.str();
}

vector<vector<string>> group_anagrams(vector<string>& strs) {
	std::unordered_map<string, vector<string>> grouped_anagrams;
	for (const string& word : strs) {
		vector<int> chars(26, 0);
		for (const char& c : word) {
			chars[c - 'a']++;
		}
		grouped_anagrams[make_hashable(chars)].push_back(word);
	}

	vector<vector<string>> result;
	for (const auto& [key, value] : grouped_anagrams) {
		result.push_back(value);
	}
	return result;
}

void test_make_hashable()
{
	vector<int> v = {2, 4, 6};
	assert(make_hashable(v) == "2 4 6 ");

	printf("All tests passed for make_hashable.\n");
}

        
void test_group_anagrams()
{
	vector<string> strs = {"eat", "tea", "tan", "ate", "nat", "bat"};
	vector<vector<string>> result = group_anagrams(strs);
	vector<vector<string>> expected = {{"bat"}, {"nat", "tan"}, {"ate", "eat", "tea"}};
	for (auto &v : result) {
		std::sort(v.begin(), v.end());
	}
	std::sort(result.begin(), result.end());
	for (auto &v : expected) {
		std::sort(v.begin(), v.end());
	}
	std::sort(expected.begin(), expected.end());

	assert(result == expected);

	strs = {""};
	expected = {{""}};
	assert(group_anagrams(strs) == expected);

	strs = {"a"};
	expected = {{"a"}};
	assert(group_anagrams(strs) == expected);

	strs = {"bdddddddddd","bbbbbbbbbbc"};
	expected = {{"bbbbbbbbbbc"},{"bdddddddddd"}};
	result = group_anagrams(strs);
	std::sort(result.begin(), result.end());
	assert(group_anagrams(strs) == expected);

	printf("All tests passed for group_anagrams.\n");
}

int main()
{
	test_make_hashable();
	test_group_anagrams();
	return 0;
}
