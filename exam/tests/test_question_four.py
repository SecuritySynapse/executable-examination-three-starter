"""Confirm the correctness of functions in question_four."""

import pytest

# ruff: noqa: PLR2004
from questions.question_four import (
    Daemon,
    SecurityEvent,
    SecurityVulnerability,
    calculate_average_cvss,
    calculate_confusion_matrix,
    calculate_security_metrics,
    check_duplicate_ports,
    check_non_running_services,
)


@pytest.mark.question_four_part_a
def test_check_duplicate_ports():
    """Test the check_duplicate_ports function with various inputs."""
    # Test case 1: No daemons
    daemons = []
    assert not check_duplicate_ports(daemons), "Failed: No daemons should return False"
    # Test case 2: Single daemon running
    daemon1 = Daemon(
        name="httpd",
        port=80,
        pid=1234,
        status="running",
        start_time="2023-10-01 12:00:00",
    )
    daemons = [daemon1]
    assert not check_duplicate_ports(
        daemons
    ), "Failed: Single daemon running should return False"
    # Test case 3: Multiple daemons running on different ports
    daemon2 = Daemon(
        name="sshd",
        port=22,
        pid=5678,
        status="running",
        start_time="2023-10-01 12:00:00",
    )
    daemons = [daemon1, daemon2]
    assert not check_duplicate_ports(
        daemons
    ), "Failed: Multiple daemons on different ports should return False"
    # Test case 4: Multiple daemons running on the same port
    daemon3 = Daemon(
        name="another_httpd",
        port=80,
        pid=9101,
        status="running",
        start_time="2023-10-01 12:00:00",
    )
    daemons = [daemon1, daemon2, daemon3]
    assert check_duplicate_ports(
        daemons
    ), "Failed: Multiple daemons on the same port should return True"
    # Test case 5: Multiple daemons, but only one running on a port
    daemon4 = Daemon(
        name="httpd",
        port=80,
        pid=1234,
        status="stopped",
        start_time="2023-10-01 12:00:00",
    )
    daemons = [daemon1, daemon2, daemon4]
    assert not check_duplicate_ports(
        daemons
    ), "Failed: Only one daemon running on a port should return False"
    # Test case 6: Multiple daemons, none running
    daemon5 = Daemon(
        name="sshd",
        port=22,
        pid=5678,
        status="stopped",
        start_time="2023-10-01 12:00:00",
    )
    daemons = [daemon4, daemon5]
    assert not check_duplicate_ports(
        daemons
    ), "Failed: No running daemons should return False"
    # Test case 7: Multiple daemons, mixed running and stopped, no duplicate ports
    daemon6 = Daemon(
        name="nginx",
        port=8080,
        pid=1111,
        status="running",
        start_time="2023-10-01 12:00:00",
    )
    daemons = [daemon1, daemon2, daemon4, daemon5, daemon6]
    assert not check_duplicate_ports(
        daemons
    ), "Failed: Mixed running and stopped daemons with no duplicate ports should return False"
    # Test case 8: Multiple daemons, mixed running and stopped, with duplicate ports
    daemon7 = Daemon(
        name="another_nginx",
        port=8080,
        pid=2222,
        status="running",
        start_time="2023-10-01 12:00:00",
    )
    daemons = [daemon1, daemon2, daemon4, daemon5, daemon6, daemon7]
    assert check_duplicate_ports(
        daemons
    ), "Failed: Mixed running and stopped daemons with duplicate ports should return True"


@pytest.mark.question_four_part_b
def test_check_non_running_services():
    """Confirm that the detection of non-running services is working."""
    httpd = Daemon(
        name="httpd",
        port=80,
        pid=1234,
        status="running",
        start_time="2023-10-01 12:00:00",
    )
    sshd = Daemon(
        name="sshd",
        port=22,
        pid=5678,
        status="running",
        start_time="2023-10-01 12:00:00",
    )
    nginx = Daemon(
        name="nginx",
        port=8080,
        pid=9101,
        status="stopped",
        start_time="2023-10-01 12:00:00",
    )
    # confirm that this is not a non-running service
    daemons = [httpd, sshd, nginx]
    service_names = ["httpd"]
    non_running_services_status = check_non_running_services(daemons, service_names)
    assert (
        not non_running_services_status
    ), "Failed to notice all services are running, one check service"
    # confirm that this is not a non-running service
    daemons = [httpd, sshd, nginx]
    service_names = ["httpd", "sshd"]
    non_running_services_status = check_non_running_services(daemons, service_names)
    assert (
        not non_running_services_status
    ), "Failed to notice all services are running, two check service"
    # confirm that there is a non-running service that should be running
    daemons = [httpd, sshd, nginx]
    service_names = ["httpd", "nginx"]
    non_running_services_status = check_non_running_services(daemons, service_names)
    assert non_running_services_status, "Failed to detect a non-running service"


@pytest.mark.question_four_part_c
def test_calculate_confusion_matrix_high_precision():
    """Test calculation of confusion matrix with high precision input labels."""
    events = [
        SecurityEvent(
            event_id=1, event_type="authentication", prediction=True, correct_label=True
        ),
        SecurityEvent(
            event_id=2, event_type="authorization", prediction=True, correct_label=True
        ),
        SecurityEvent(
            event_id=3, event_type="authentication", prediction=True, correct_label=True
        ),
        SecurityEvent(
            event_id=4, event_type="authorization", prediction=True, correct_label=False
        ),
    ]
    confusion_matrix = calculate_confusion_matrix(events)
    assert confusion_matrix["true_positive"] == 3, "True positives should be 3"
    assert confusion_matrix["true_negative"] == 0, "True negatives should be 0"
    assert confusion_matrix["false_positive"] == 1, "False positives should be 1"
    assert confusion_matrix["false_negative"] == 0, "False negatives should be 0"


@pytest.mark.question_four_part_c
def test_calculate_metrics_high_precision():
    """Test calculation of security metrics with high precision input labels."""
    events = [
        SecurityEvent(
            event_id=1, event_type="authentication", prediction=True, correct_label=True
        ),
        SecurityEvent(
            event_id=2, event_type="authorization", prediction=True, correct_label=True
        ),
        SecurityEvent(
            event_id=3, event_type="authentication", prediction=True, correct_label=True
        ),
        SecurityEvent(
            event_id=4, event_type="authorization", prediction=True, correct_label=False
        ),
    ]
    metrics = calculate_security_metrics(events)
    assert metrics["precision"] == 0.75, "Precision should be 0.75"
    assert metrics["recall"] == 1.0, "Recall should be 1.0"
    assert metrics["accuracy"] == 0.75, "Accuracy should be 0.75"
    assert metrics["f1_score"] == pytest.approx(
        0.8571428571428571, rel=1e-9
    ), "F1-score should be approximately 0.857"


@pytest.mark.question_four_part_c
def test_calculate_confusion_matrix_low_precision():
    """Test calculation of confusion matrix with low precision input labels."""
    events = [
        SecurityEvent(
            event_id=1,
            event_type="authentication",
            prediction=True,
            correct_label=False,
        ),
        SecurityEvent(
            event_id=2, event_type="authorization", prediction=True, correct_label=False
        ),
        SecurityEvent(
            event_id=3, event_type="authentication", prediction=True, correct_label=True
        ),
        SecurityEvent(
            event_id=4, event_type="authorization", prediction=True, correct_label=False
        ),
    ]
    confusion_matrix = calculate_confusion_matrix(events)
    assert confusion_matrix["true_positive"] == 1, "True positives should be 1"
    assert confusion_matrix["true_negative"] == 0, "True negatives should be 0"
    assert confusion_matrix["false_positive"] == 3, "False positives should be 3"
    assert confusion_matrix["false_negative"] == 0, "False negatives should be 0"


@pytest.mark.question_four_part_c
def test_calculate_metrics_low_precision():
    """Test calculation of security metrics with low precision input labels."""
    events = [
        SecurityEvent(
            event_id=1,
            event_type="authentication",
            prediction=True,
            correct_label=False,
        ),
        SecurityEvent(
            event_id=2, event_type="authorization", prediction=True, correct_label=False
        ),
        SecurityEvent(
            event_id=3, event_type="authentication", prediction=True, correct_label=True
        ),
        SecurityEvent(
            event_id=4, event_type="authorization", prediction=True, correct_label=False
        ),
    ]
    metrics = calculate_security_metrics(events)
    assert metrics["precision"] == 0.25, "Precision should be 0.25"
    assert metrics["recall"] == 1.0, "Recall should be 1.0"
    assert metrics["accuracy"] == 0.25, "Accuracy should be 0.25"
    assert metrics["f1_score"] == pytest.approx(
        0.4, rel=1e-9
    ), "F1-score should be approximately 0.4"


@pytest.mark.question_four_part_d
def test_calculate_average_cvss():
    """Test calculate_average_cvss function with various corner cases."""
    # assertion 1: Empty list of vulnerabilities
    vulnerabilities = []
    assert (
        calculate_average_cvss(vulnerabilities) == 0.0
    ), "Average CVSS score should be 0.0 for an empty list"
    # assertion 2: Single vulnerability with CVSS score 0.0
    vulnerabilities = [
        SecurityVulnerability(
            identifier="VULN-001", description="Test Vulnerability", cvss_score=0.0
        )
    ]
    assert (
        calculate_average_cvss(vulnerabilities) == 0.0
    ), "Average CVSS score should be 0.0 for a single vulnerability with CVSS score 0.0"
    # assertion 3: Single vulnerability with CVSS score 1.0
    vulnerabilities = [
        SecurityVulnerability(
            identifier="VULN-002", description="Test Vulnerability", cvss_score=1.0
        )
    ]
    assert (
        calculate_average_cvss(vulnerabilities) == 1.0
    ), "Average CVSS score should be 1.0 for a single vulnerability with CVSS score 1.0"
    # assertion 4: Multiple vulnerabilities with varying CVSS scores
    vulnerabilities = [
        SecurityVulnerability(
            identifier="VULN-003", description="Test Vulnerability 1", cvss_score=0.5
        ),
        SecurityVulnerability(
            identifier="VULN-004", description="Test Vulnerability 2", cvss_score=0.7
        ),
        SecurityVulnerability(
            identifier="VULN-005", description="Test Vulnerability 3", cvss_score=0.9
        ),
    ]
    assert (
        calculate_average_cvss(vulnerabilities) == pytest.approx(0.7, rel=1e-9)
    ), "Average CVSS score should be approximately 0.7 for multiple vulnerabilities with varying CVSS scores"
    # assertion 5: Multiple vulnerabilities with the same CVSS score
    vulnerabilities = [
        SecurityVulnerability(
            identifier="VULN-006", description="Test Vulnerability 1", cvss_score=0.8
        ),
        SecurityVulnerability(
            identifier="VULN-007", description="Test Vulnerability 2", cvss_score=0.8
        ),
        SecurityVulnerability(
            identifier="VULN-008", description="Test Vulnerability 3", cvss_score=0.8
        ),
    ]
    assert (
        calculate_average_cvss(vulnerabilities) == pytest.approx(0.8, rel=1e-9)
    ), "Average CVSS score should be 0.8 for multiple vulnerabilities with the same CVSS score"
