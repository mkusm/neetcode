#include <vector>
#include <string>
#include <cassert>
#include <cstdio>
#include <iostream>

using std::vector, std::string;

string encode(const vector<string>& strs) {
	string result;
	for (const auto& s : strs) {
		result += std::to_string(s.size()) + ";" + s;
	}
	return result;
}

vector<string> decode(const string s) {
	vector<string> result;

	int i = 0;
	while (i < s.size()) {
		int j = i;
		while (s[j] != ';') {
			j++;
		}
		int length = std::stoi(s.substr(i, j - i));
		result.push_back(s.substr(j+1, length));
		i = j+1+length;
	}
	return result;
}

void test_encode_decode()
{
	vector<vector<string>> str_cases = {
		vector<string>{"test", "test", "test"},
		vector<string>{"1num", "num1", ";;", ";1;3"},
		vector<string>{"test", "longassstring"},
		vector<string>{"test"},
	};
	for (const auto& str_case : str_cases) {
		assert(decode(encode(str_case)) == str_case);
	}

	printf("All tests passed for encode and decode.\n");
}

int main()
{
	test_encode_decode();
	return 0;
}
