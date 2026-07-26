import pytest

from palindrome import longest_palindromic_substring


def is_palindrome(s):
    return s == s[::-1]



# Basic cases


def test_odd_length_palindrome():
    # "babad" has two valid answers: "bab" and "aba"
    result = longest_palindromic_substring("babad")
    assert result in ("bab", "aba")


def test_even_length_palindrome():
    # "cbbd" -> "bb" is the only longest palindrome
    assert longest_palindromic_substring("cbbd") == "bb"


def test_whole_string_is_palindrome():
    assert longest_palindromic_substring("racecar") == "racecar"


def test_palindrome_at_start_of_string():
    assert longest_palindromic_substring("abaxyz") == "aba"


def test_palindrome_at_end_of_string():
    assert longest_palindromic_substring("xyzaba") == "aba"



# Edge cases


def test_empty_string_returns_empty_string():
    assert longest_palindromic_substring("") == ""


def test_single_character_string():
    assert longest_palindromic_substring("a") == "a"


def test_two_character_non_palindrome():
    result = longest_palindromic_substring("ab")
    assert result in ("a", "b")


def test_two_character_palindrome():
    assert longest_palindromic_substring("aa") == "aa"


def test_no_repeating_characters_returns_single_char():
    result = longest_palindromic_substring("abcde")
    assert len(result) == 1
    assert result in "abcde"


def test_all_same_characters():
    assert longest_palindromic_substring("aaaa") == "aaaa"


def test_long_string_with_known_palindrome():
    s = "a" * 50 + "b" + "a" * 50
    assert longest_palindromic_substring(s) == s


def test_result_is_actually_a_palindrome():
    for s in ["forgeeksskeegfor", "banana", "abcdefgfedcba"]:
        result = longest_palindromic_substring(s)
        assert is_palindrome(result)


def test_result_is_the_correct_length():
    # "forgeeksskeegfor" -> longest palindrome is "geeksskeeg" (length 10)
    assert longest_palindromic_substring("forgeeksskeegfor") == "geeksskeeg"




# Failure / invalid input cases


def test_non_string_input_raises_type_error():
    with pytest.raises(TypeError):
        longest_palindromic_substring(12321)


def test_none_input_raises_type_error():
    with pytest.raises(TypeError):
        longest_palindromic_substring(None)
