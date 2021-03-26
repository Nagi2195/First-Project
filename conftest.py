import slack  # import slack integration file
import pytest


# Command line options:
def pytest_addoption(parser):
    "add parser options"
    parser.addoption("--api", action="store")


# pytest plugin hook
def pytest_sessionfinish(session, exitstatus):
    slack.post_reports_to_slack()
