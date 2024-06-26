def test_encode_decode():
    cases = [
        ["we","say",":","yes","!@#$%^&*()"],
        ["a", "b", "c"],
        ["a"],
        ["test", "test", "test"],
        ["python", "java", "c++"],
        ["", "test", "test"],
        ["", "", ""],
        [""],
        ["1num", "num1", ";;", ";1;3"]
    ]
    for string_l in cases:
        assert decode(encode(string_l)) == string_l, string_l


def encode(strs: list[str]) -> str:
    res = []
    for s in strs:
        res.append(str(len(s)) + ';' + s)
    return "".join(res)


def decode(s: str) -> list[str]:
    res = []
    i = 0
    while i < len(s):
        digits = []
        j = 0
        while (digit := s[i + j]) != ';':
            digits.append(digit)
            j += 1
        assert s[i + len(digits)] == ';'
        string_length = int("".join(digits))
        current_string_position = len(digits) + 1 + i
        next_string_position = current_string_position + string_length
        string_content = s[current_string_position:next_string_position]
        res.append(string_content)
        i = next_string_position
    return res


if __name__ == "__main__":
    test_encode_decode()
