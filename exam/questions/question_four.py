"""Question Four: Executable Examination."""

# Note: The imports in the following source code block may no longer
# adhere to the industry best practices for Python source code.
# You must reorganize and/or add the imports so that they adhere
# to the industry best practices for Python source code.

from typing import Dict, List

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

# Function specification for check_duplicate_ports:
# The function check_duplicate_ports should:
# --> Take as input the parameter daemons that is a list of Daemon instances
#     representing daemon processes running on a network-accessible server.
# --> Produce as output a boolean that indicates whether or not there are
#     two or more daemons running on the same port.
# --> If there are two or more daemons running on the same port, the function
#     should return True. Otherwise, it should return False.
# Note that it would be a security risk if a network-accessible server had
# two daemon processes running on the same port.

# Note: This function may not not have all of the correct type annotations for
# certain variables. You must add all of any needed type annotations
# so that the function and any code that uses it passes the type checker.

# Note: This function may not have a docstring and thus it may not adhere
# to industry best practices for Python source code. You may need to add a docstring
# so that this function is correctly documented by an software engineer using it.

# Note: You do not need to modify the Daemon class to answer any part of this
# question. To be clear, modifying the Daemon class may result in other checks
# for the required functions to not pass correctly.


class Daemon:
    """A class representing a daemon process."""

    def __init__(self, name: str, port: int, pid: int, status: str, start_time: str):
        """Initialize an instance of the Daemon class."""
        self.name = name
        self.port = port
        self.pid = pid
        self.status = status
        self.start_time = start_time

    def __repr__(self) -> str:
        """Return a string representation of the Daemon instance."""
        return (
            f"Daemon(name={self.name}, port={self.port}, pid={self.pid}, "
            f"status={self.status}, start_time={self.start_time})"
        )

    def is_running(self) -> bool:
        """Check if the daemon is running."""
        return self.status.lower() == "running"


def check_duplicate_ports(daemons: list[Daemon]) -> bool:
    """Check if there are two daemons running on the same port."""
    port_map = {}
    for daemon in daemons:
        if daemon.is_running():
            if daemon.port in port_map:
                return True
            port_map[daemon.port] = daemon
    return False


# }}}

# Part (b) {{{

# Instructions: Implement the following function so that it adheres to all
# aspects of the following specification.

# Function specification for check_non_running_services:
# The function check_non_running_services should:
# --> Take as input the parameters:
#     daemons: a list of Daemon instances representing daemon processes running on a
#     network-accessible server
#     service_names: a list of strings representing the names of the services to check
#     for non-running instances (i.e., instances with a status other than "running")
# --> Produce as output a boolean that indicates whether or not there are any
#     services in the list of daemon names that have an instance that is not running.
# --> Note that a service is considered to be running if its status is "running".
#     If any service in the list of daemon names has an instance that is not running,
#     the function should return True. Otherwise, it should return False.
# --> Importantly, if a service is not running when it should be running this may
#     indicate a security risk and is a limitation to the system's availability.

# Note: This function may not not have all of the correct type annotations for
# certain variables. You must add all of any needed type annotations
# so that the function and any code that uses it passes the type checker.

# Note: This function may not have a docstring and thus it may not adhere
# to industry best practices for Python source code. You may need to add a docstring
# so that this function is correctly documented by an software engineer using it.


def check_non_running_services(daemons: list[Daemon], service_names: list[str]) -> bool:
    """Check if any services in the list of daemon names have an instance that is not running."""
    for daemon in daemons:
        if daemon.name in service_names and not daemon.is_running():
            return True
    return False


# }}}


# Part (c) {{{

# Instructions: Implement and/or debug the following functions so that they
# adhere to all aspects of the following specification.

# Function specification for calculate_confusion_matrix:
# The function calculate_confusion_matrix should:
# --> Take as input the parameter events that is a list of SecurityEvent instances
#     representing security events.
#   Each SecurityEvent instance has the following attributes:
#    - event_id: an integer representing the unique identifier
#    - event_type: a string representing the type of event ('authentication' or 'authorization')
#    - prediction: a boolean representing the prediction about whether or not the event should be allowed
#    - correct_label: a boolean representing the correct label about whether or not the event should be allowed
# --> Produce as output a dictionary that contains the following key value pairs:
#    - The key is "true_positive" and the value is the number of true positives
#    - The key is "true_negative" and the value is the number of true negatives
#    - The key is "false_positive" and the value is the number of false positives
#    - The key is "false_negative" and the value is the number of false negatives

# Function specification for calculate_security_metrics:
# The function calculate_security_metrics should:
# --> Take as input the parameter events that is a list of SecurityEvent instances
#     representing security events.
#   Each SecurityEvent instance has the following attributes:
#    - event_id: an integer representing the unique identifier
#    - event_type: a string representing the type of event ('authentication' or 'authorization')
#    - prediction: a boolean representing the prediction about whether or not the event should be allowed
#    - correct_label: a boolean representing the correct label about whether or not the event should be allowed
# --> Produce as output a dictionary that contains the following key value pairs:
#    - The key is "precision" and the value is the precision of the security events
#    - The key is "recall" and the value is the recall of the security events
#    - The key is "accuracy" and the value is the accuracy of the security events
#    - The key is "f1_score" and the value is the F1-score of the security events

# Note: This function may not not have all of the correct type annotations for
# certain variables. You must add all of any needed type annotations
# so that the function and any code that uses it passes the type checker.

# Note: This function may not have a docstring and thus it may not adhere
# to industry best practices for Python source code. You may need to add a docstring
# so that this function is correctly documented by an software engineer using it.

# Note: You do not need to modify the SecurityEvent class to answer any part of this
# question. To be clear, modifying the SecurityEvent class may result in other checks
# for the required functions to not pass correctly.


class SecurityEvent:
    """A class representing a security event."""

    def __init__(
        self, event_id: int, event_type: str, prediction: bool, correct_label: bool
    ):
        """Construct an instance of the SecurityEvent class."""
        self.event_id = event_id
        self.event_type = event_type  # 'authentication' or 'authorization'
        self.prediction = prediction  # True if allowed, False if denied
        self.correct_label = correct_label  # True if allowed, False if denied


def calculate_confusion_matrix(events: List[SecurityEvent]) -> Dict[str, int]:
    """Calculate the confusion matrix based on the provided list of security events and their classification."""
    true_positive = sum(
        1 for event in events if event.prediction and event.correct_label
    )
    true_negative = sum(
        1 for event in events if not event.prediction and not event.correct_label
    )
    false_positive = sum(
        1 for event in events if event.prediction and not event.correct_label
    )
    false_negative = sum(
        1 for event in events if not event.prediction and event.correct_label
    )
    return {
        "true_positive": true_positive,
        "true_negative": true_negative,
        "false_positive": false_positive,
        "false_negative": false_negative,
    }


def calculate_security_metrics(events: List[SecurityEvent]) -> Dict[str, float]:
    """Calculate security metrics based on the provided list of security events and their classification."""
    true_positive = sum(
        1 for event in events if event.prediction and event.correct_label
    )
    true_negative = sum(
        1 for event in events if not event.prediction and not event.correct_label
    )
    false_positive = sum(
        1 for event in events if event.prediction and not event.correct_label
    )
    false_negative = sum(
        1 for event in events if not event.prediction and event.correct_label
    )
    precision = (
        true_positive / (true_positive + false_positive)
        if (true_positive + false_positive) > 0
        else 0
    )
    recall = (
        true_positive / (true_positive + false_negative)
        if (true_positive + false_negative) > 0
        else 0
    )
    accuracy = (true_positive + true_negative) / len(events) if len(events) > 0 else 0
    f1_score = (
        (2 * precision * recall) / (precision + recall)
        if (precision + recall) > 0
        else 0
    )
    return {
        "precision": precision,
        "recall": recall,
        "accuracy": accuracy,
        "f1_score": f1_score,
    }


# }}}

# Part (d) {{{

# Instructions: Implement and/or debug the following functions so that they
# adhere to all aspects of the following specification.

# Function specification for calculate_average_cvss:
# The function calculate_average_cvss should:
# --> Take as input the parameter vulnerabilities that is a list of SecurityVulnerability instances
#    representing security vulnerabilities.
# --> Produce as output a float that represents the average CVSS score
# --> If the input list is empty, the function should return 0.0
# --> The CVSS score must be a number between 0.0 and 1.0
#     that represents the severity of a security vulnerability.
#     Please note that 0.0 represents the lowest severity and
#     1.0 represents the highest severity. Also, please note that,
#     while some sources uses a CVSS score that can go up to a value
#     of 10.0, this is not a valid CVSS score for the purposes of
#     this question and this should be avoided.
# --> Note that many CVSS scores are connected to security vulnerabilities
#     that are connected to networking on web-based platforms.

# Note: This function may not not have all of the correct type annotations for
# certain variables. You must add all of any needed type annotations
# so that the function and any code that uses it passes the type checker.

# Note: This function may not have a docstring and thus it may not adhere
# to industry best practices for Python source code. You may need to add a docstring
# so that this function is correctly documented by an software engineer using it.

# Note: You do not need to modify the SecurityVulnerability class to answer any
# part of this question. In fact, any modification to the SecurityVulnerability
# class may lead to other checks not passing correctly.


class SecurityVulnerability:
    """A class representing a security vulnerability."""

    def __init__(self, identifier: str, description: str, cvss_score: float):
        """Initialize the SecurityVulnerability instance."""
        if not (0.0 <= cvss_score <= 1.0):
            raise ValueError("CVSS score must be between 0.0 and 1.0")
        self.identifier = identifier
        self.description = description
        self.cvss_score = cvss_score

    def __repr__(self):
        """Return a string representation of the SecurityVulnerability instance."""
        return (
            f"SecurityVulnerability(identifier={self.identifier}, "
            f"description={self.description}, cvss_score={self.cvss_score})"
        )


def calculate_average_cvss(vulnerabilities: list[SecurityVulnerability]) -> float:
    """Calculate the average CVSS score from a list of SecurityVulnerability instances."""
    if not vulnerabilities:
        return 0.0
    total_score = sum(vul.cvss_score for vul in vulnerabilities)
    return total_score / len(vulnerabilities)


# }}}
