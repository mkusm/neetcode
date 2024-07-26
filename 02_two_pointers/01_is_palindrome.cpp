#include <cassert>
#include <iostream>
#include <string>
#include <cctype>

using std::string;

bool is_palindrome(string s)
{
	for (char& c : s) {
		c = std::tolower(c);;
	}

	int i = 0;
	int j = s.length() - 1;

	while (i < j) {
		if (i >= s.length() || j < 0) {
			return true;
		}

		while (!(s[i] >= 'a' && s[i] <= 'z') && i < j) i++;
		while (!(s[j] >= 'a' && s[j] <= 'z') && i < j) j--;

		if (!(s[i] == s[j])) {
			return false;
		}

		i++;
		j--;
	}

	return true;
}

void test_is_palindrome()
{
	assert(is_palindrome("racecar"));
	assert(!is_palindrome("hello"));
	assert(!is_palindrome("tab a cat"));

	std::cout << "All tests passed" << std::endl;
}

int main()
{
	test_is_palindrome();
	return 0;
}
