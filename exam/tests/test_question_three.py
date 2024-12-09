"""Confirm the correctness of functions in question_three."""

import pytest

# ruff: noqa: PLR2004
from questions.question_three import (
    count_print_functions_malware_analysis,
    count_spaces_and_newlines_cryptanalysis,
    count_while_loops_malware_analysis,
    count_while_loops_malware_analysis_many_source_codes,
    count_words_cryptanalysis,
)

source_code_one_three_prints = """
def example_function():
    print("Hello, World!")
    print("This is a test.")
    x = 10
    if x > 5:
        print("x is greater than 5")
"""

source_code_one_three_prints_embedded_print = """
def example_function():
    print("Hello, World!")
    print("This is a test.")
    x = 10
    if x > 5:
        print("print x is greater than 5")
"""

source_code_one_zero_prints = """
def example_function():
    x = 10
    if x > 5:
        x = 5
"""

source_code_one_zero_prints_embedded_print = """
def example_function():
    x = 10
    if x > 5:
        x = 5
        example = "print x is greater than 5"
"""

source_code_two_one_while = """
def example_function():
    print("Hello, World!")
    print("This is a test.")
    x = 10
    while x > 5:
        print("x is greater than 5")
        x = x - 1
"""

source_code_two_one_while_embedded_while = """
def example_function():
    print("Hello, World!")
    print("This is a test.")
    x = 10
    while x > 5:
        print("while x is greater than 5")
        x = x - 1
"""

source_code_two_zero_while_embedded_while = """
def example_function():
    print("Hello, World!")
    print("This is a test.")
    x = 10
    print("while x is greater than 5")
    x = x - 1
"""


@pytest.mark.question_three_part_a
def test_extract_prints_from_source_code():
    """Test for a question part."""
    count = count_print_functions_malware_analysis(source_code_one_three_prints)
    assert (
        count == 3
    ), "Failed to count the number of print functions in the source code"


@pytest.mark.question_three_part_a
def test_extract_prints_from_source_code_embedded_print():
    """Test for a question part."""
    count = count_print_functions_malware_analysis(
        source_code_one_three_prints_embedded_print
    )
    assert (
        count == 3
    ), "Failed to count the number of print functions in the source code with a print string"


@pytest.mark.question_three_part_a
def test_zero_prints_in_source_code():
    """Test for a question part."""
    count = count_print_functions_malware_analysis(source_code_one_zero_prints)
    assert (
        count == 0
    ), "Failed to count the number of print functions in the source code with zero print statements"


@pytest.mark.question_three_part_a
def test_zero_prints_in_source_code_embedded():
    """Test for a question part."""
    count = count_print_functions_malware_analysis(
        source_code_one_zero_prints_embedded_print
    )
    assert (
        count == 0
    ), "Failed to count the number of print functions in the source code with zero print statements and embedded strings"


@pytest.mark.question_three_part_b
def test_count_words_cryptanalysis():
    """Test for a question part."""
    assert count_words_cryptanalysis("hello hello world") == {
        "hello": 2,
        "world": 1,
    }, "Word count failed for string with one duplicated word"
    assert count_words_cryptanalysis("Python Python Python") == {
        "Python": 3
    }, "Word count failed for string with the same word"
    assert count_words_cryptanalysis("") == {}, "Word count failed for an empty string"
    assert count_words_cryptanalysis("Hello % extraction point") == {
        "Hello": 1,
        "%": 1,
        "extraction": 1,
        "point": 1,
    }, "Word count failed for string with a percent sign symbol and single-count words"
    assert count_words_cryptanalysis("^ % & @") == {
        "^": 1,
        "%": 1,
        "&": 1,
        "@": 1,
    }, "Word count failed for string with a numerous symbols"


@pytest.mark.question_three_part_c
def test_count_spaces_and_newlines_cryptanalysis():
    """Test for a question part."""
    assert count_spaces_and_newlines_cryptanalysis("hello world") == {
        "spaces": 1,
        "newlines": 0,
    }, "Count failed for 'hello world'"
    assert count_spaces_and_newlines_cryptanalysis("hello\nworld") == {
        "spaces": 0,
        "newlines": 1,
    }, "Count failed for 'hello\\nworld'"
    assert count_spaces_and_newlines_cryptanalysis("hello world\nPython") == {
        "spaces": 1,
        "newlines": 1,
    }, "Count failed for 'hello world\\nPython'"
    assert count_spaces_and_newlines_cryptanalysis("") == {
        "spaces": 0,
        "newlines": 0,
    }, "Count failed for an empty string"


@pytest.mark.question_three_part_d
def test_extract_while_loops_from_source_code():
    """Test for a question part."""
    count = count_while_loops_malware_analysis(source_code_two_one_while)
    assert count == 1, "Failed to count the number of while loops in the source code"


@pytest.mark.question_three_part_d
def test_extract_while_loops_from_source_code_embedded_while():
    """Test for a question part."""
    count = count_while_loops_malware_analysis(source_code_two_one_while_embedded_while)
    assert (
        count == 1
    ), "Failed to count the number of while loops in the source code with embedded while loop"


@pytest.mark.question_three_part_d
def test_extract_no_while_loops_from_source_code_embedded_while():
    """Test for a question part."""
    count = count_while_loops_malware_analysis(
        source_code_two_zero_while_embedded_while
    )
    assert (
        count == 0
    ), "Failed to count zero while loops in the source code with embedded while loop"


@pytest.mark.question_three_part_d
def test_detect_while_loop_malware():
    """Test the function that detects while loop malware in multiple source code segments."""
    source_code_list = [
        source_code_two_one_while,
        source_code_two_one_while_embedded_while,
        source_code_two_zero_while_embedded_while,
    ]
    expected_result = {
        source_code_two_one_while: 1,
        source_code_two_one_while_embedded_while: 1,
        source_code_two_zero_while_embedded_while: 0,
    }
    result = count_while_loops_malware_analysis_many_source_codes(source_code_list)
    assert (
        result == expected_result
    ), "Failed to count while loops in multiple source code segments"
