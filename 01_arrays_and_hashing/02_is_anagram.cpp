#include <cassert>
#include <string>
#include <unordered_map>

using std::string;

bool is_anagram(string s, string t)
{
	if (s.length() != t.length())
		return false;

	std::unordered_map<char, int> s_chars, t_chars;

	for (char c : s) s_chars[c]++;
	for (char c : t) t_chars[c]++;

	return s_chars == t_chars;
}

void test_is_anagram()
{
	assert(is_anagram("anagram", "nagaram"));
	assert(!is_anagram("anagram", "nagaramm"));
	assert(!is_anagram("rat", "car"));
	assert(is_anagram("listen", "silent"));
	assert(is_anagram("triangle", "integral"));
	assert(!is_anagram("hello", "world"));

	printf("All tests passed for is_anagram.\n");
}

int main()
{
	test_is_anagram();
	return 0;
}
