"""Question Three: Executable Examination."""

# Note: The imports in the following source code block may no longer
# adhere to the industry best practices for Python source code.
# You must reorganize and/or add the imports so that they adhere
# to the industry best practices for Python source code.

from typing import Dict
import ast

# Introduction: Read This First! {{{

# Keep in mind these considerations as you implement the required functions:

# --> You must implement Python functions to complete each of these steps,
# bearing in mind that one defective function may break other function(s).

# --> Your source code must adhere to industry best practices in, for instance,
# source code formatting, variable naming, and documentation.

# --> You may refer to the checks that are specified in the exam/gatorgrade.yml file
# in this GitHub repository for the configuration and name of each tool used
# to analyze the code inside of this file.

# }}}

# Question (a) {{{

# Instructions: Implement and/or debug the following functions so that they
# adhere to all aspects of the following specification.

# Function specification for count_print_functions_malware_analysis:
# The function count_print_functions_malware_analysis should:
# --> Take as input the parameter source_code that is a string
#     consisting of valid Python source code that can be parsed and run.
# --> Produce as output an integer that represents the number of times
#     that the print function call is found inside of the source code.
# --> If the source code does not contain the print function call, then
#     the function should return 0.
# --> If the source code contains the word "print" but it is not a function
#     call, then it should not be counted.

# The overall purpose of the count_print_functions_malware_analysis function
# is that it could be used during malware analysis to find debugging statements
# inside of a malware sample. This could perhaps help the malware analyst to
# determine if the malware is being debugged or not. The final question part
# in this file will further develop and explore this idea of malware analysis.

# Note: This function may not not have all of the correct type annotations for
# certain variables. You must add all of any needed type annotations
# so that the function and any code that uses it passes the type checker.

# Note: This function may not have a docstring and thus it may not adhere
# to industry best practices for Python source code. You may need to add a docstring
# so that this function is correctly documented by an software engineer using it.


def count_print_functions_malware_analysis(source_code):
    print_count = 0
    return print_count


# }}}

# Part (b) {{{

# Instructions: Implement the following function so that it adheres to all
# aspects of the following specification.

# Function specification:
# The function count_words_cryptanalysis should:
# --> Take as input the parameter called text that is a string
#     consisting of any valid words represented by ASCII or Unicode characters.
# --> Produce as output a dictionary of key value pairs such that:
#     - The key is the word found in the text
#     - The value is the number of times that the specific word was found in the text

# The content in the dictionary could be used as one of the data points that
# would support the cryptanalysis of a text that was encrypted. You can think of
# this function as performing a type of "frequency analysis" on the text.

# Note: This function may not not have all of the correct type annotations for
# certain variables. You must add all of any needed type annotations
# so that the function and any code that uses it passes the type checker.

# Note: This function may not have a docstring and thus it may not adhere
# to industry best practices for Python source code. You may need to add a docstring
# so that this function is correctly documented by an software engineer using it.


def count_words_cryptanalysis(text):
    analysis_dictionary: Dict[str, int] = {}
    return analysis_dictionary


# }}}


# Part (c) {{{

# Instructions: Implement and/or debug the following functions so that they
# adheres to all aspects of the following specification.

# Function specification for count_spaces_and_newlines_cryptanalysis:
# The function count_spaces_and_newlines_cryptanalysis should:
# --> Take as input the parameter:
#     text: a string that represents the text to be analyzed
# --> Produce as output a dictionary that contains the following key value pairs:
#    - The key is "spaces" and the value is the number of spaces found in the text
#    - The key is "newlines" and the value is the number of newlines found in the text

# The content of the dictionary could be used as one of the data points that
# would support the cryptanalysis of a text that was encrypted. You can think of
# this function as performing another type of "frequency analysis" on the text.

# Note: This function may not not have all of the correct type annotations for
# certain variables. You must add all of any needed type annotations
# so that the function and any code that uses it passes the type checker.

# Note: This function may not have a docstring and thus it may not adhere
# to industry best practices for Python source code. You may need to add a docstring
# so that this function is correctly documented by an software engineer using it.


def count_spaces_and_newlines_cryptanalysis(text):
    count_dict = {}
    return count_dict


# }}}

# Part (d) {{{

# Instructions: Implement and/or debug the following functions so that they
# adheres to all aspects of the following specification.

# Function specification for count_while_loops_malware_analysis:
# The function count_while_loops_malware_analysis should:
# --> Take as input the parameter source_code that is a string
#     consisting of valid Python source code that can be parsed and run.
# --> Produce as output an integer that represents the number of times
#     that a while loop is found inside of the source code.
# --> If the source code does not contain any while loops, then
#     the function should return 0.
# --> If the source code contains the word "while" but it is not a while loop
#     then it should not be counted.

# Function specification for count_while_loops_malware_analysis_many_source_codes:
# The function count_while_loops_malware_analysis_many_source_codes should:
# --> Take as input the parameter source_code_list that is a list of strings
#     consisting of valid Python source code that can be parsed and run.
# --> Produce as output a dictionary that contains the following key value pairs:
#     - The key is the source code string
#     - The value is the count of the while loops in the source code
# --> This function should call the count_while_loops_malware_analysis function
#     for each source code string in the list and return a dictionary that
#     contains the source code string and its count of while loops.

# The overall purpose of the count_while_loops_malware_analysis function is
# that it could be used during malware analysis to find iteration constructs
# inside of a malware sample. This could perhaps help the malware analyst to
# determine if the malware matches a signature of how a known malware iterates.

# Note: This function may not not have all of the correct type annotations for
# certain variables. You must add all of any needed type annotations
# so that the function and any code that uses it passes the type checker.

# Note: This function may not have a docstring and thus it may not adhere
# to industry best practices for Python source code. You may need to add a docstring
# so that this function is correctly documented by an software engineer using it.


def count_while_loops_malware_analysis(source_code):
    while_count = 0
    return while_count


def count_while_loops_malware_analysis_many_source_codes(
    source_code_list,
):
    """Count the number of while loops in a list of source code segments."""
    result = {}
    return result


# }}}
