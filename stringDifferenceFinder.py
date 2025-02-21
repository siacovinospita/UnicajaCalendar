import difflib


def diff_two_string(string_1, string_2):
    # Get differences
    diff = difflib.ndiff(string_1.splitlines(), string_2.splitlines())

    # Print differences
    print("\n".join(diff))