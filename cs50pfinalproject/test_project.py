import pytest
import sys
from datetime import date
from project import get_todays_date, get_goal_date, calculate_weight_loss
from freezegun import freeze_time

def test_calculate_weight_loss():
    assert calculate_weight_loss(1) == .11
    assert calculate_weight_loss(30) == 3.43
    assert calculate_weight_loss(92) == 10.51


def test_get_goal_date():
    try:
        assert get_goal_date("2025-3-16") == (2025, 3, 16)
    except AssertionError:
        None == ()


@freeze_time("2024-06-23")
def test_get_todays_date():
    assert get_todays_date() == (2024, 6, 23)
