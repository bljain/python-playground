import pytest
import pandas as pd

from src.data_quality.checks import check_missing_values
from src.data_quality.exceptions import CheckExecutionError
from src.data_quality.models import CheckResult, CheckStatus


def test_missing_value_found():
    df = pd.DataFrame({"name": ["RIA", "NITIN", None, "AMAN"]})

    result = check_missing_values(df=df, column="name", run_id="check_missing")

    assert result.status == CheckStatus.FAIL
    assert result.failed_count == 1
    assert result.total_count == 4
    assert result.percentage_failed == 0.25


def test_with_no_missing_value():
    df = pd.DataFrame({"name": ["RIA", "NITIN"]})

    result = check_missing_values(df=df, column="name", run_id="check_missing")
    assert result.status == CheckStatus.PASS
    assert result.failed_count == 0
    assert result.total_count == 2
    assert result.percentage_failed == 0


def test_with_invalid_col():
    df = pd.DataFrame({"name": ["RIA", "AMAN"]})
    with pytest.raises(CheckExecutionError):
        result = check_missing_values(df=df, column="age", run_id="check_missing")


def test_with_no_input_value():
    with pytest.raises(TypeError):
        _ = check_missing_values(None, "", run_id="check_missing")

