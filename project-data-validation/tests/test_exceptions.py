from data_quality.exceptions import (
    CheckExecutionError,
    ConfigurationError,
    DataValidationError,
)


def test_data_validation_error():
    try:
        raise DataValidationError("This is a data validation error.")
    except DataValidationError as e:
        assert str(e) == "This is a data validation error."


def test_configuration_error():
    try:
        raise ConfigurationError("This is a configuration error.")
    except ConfigurationError as e:
        assert str(e) == "This is a configuration error."


def test_check_execution_error():
    try:
        raise CheckExecutionError("This is a check execution error.")
    except CheckExecutionError as e:
        assert str(e) == "This is a check execution error."