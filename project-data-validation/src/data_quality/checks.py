import pandas as pd

from src.data_quality.exceptions import CheckExecutionError
from src.data_quality.models import CheckResult, CheckStatus


def check_missing_values(
    df: pd.DataFrame, column: str, run_id: str, check_id="missing_value_check"
) -> CheckResult:
    """Check a dataframe column for missing values.

    Args:
        df (pd.DataFrame): Input dataframe to check
        column (str): Column to check for
        check_id (str, optional): Name of check type. Defaults to "missing_value_check".
        run_id (str): Unique run id.

    Returns:
        CheckResult: Returns object for result.
    """
    if not isinstance(df, pd.DataFrame):
        raise TypeError("Input df type must be a pandas dataframe.")

    if column not in df.columns:
        raise CheckExecutionError(f"Column: '{column}' not present in the dataframe.")
    total_count = len(df)
    missing_count = df[column].isna().sum()

    if total_count == 0:
        status = CheckStatus.ERROR
        message = f"Can not check '{column}' for an empty dataframe."
    elif missing_count > 0:
        status = CheckStatus.FAIL
        message = (
            f"Found {missing_count} values in column: '{column}' "
            f"out of total {total_count}."
        )
    else:
        status = CheckStatus.PASS
        message = f"Found no missing values in the column: '{column}'."
    return CheckResult(
        check_id=check_id,
        check_type="missing_values",
        status=status,
        failed_count=missing_count,
        total_count=total_count,
        message=message,
        column=column,
        run_id=run_id,
    )
