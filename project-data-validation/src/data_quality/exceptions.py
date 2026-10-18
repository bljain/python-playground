class DataValidationError(Exception):
    """Base class for data validation errors."""

    pass


class ConfigurationError(DataValidationError):
    """Raised when there is a configuration error."""

    pass


class CheckExecutionError(DataValidationError):
    """Raised when there is an error during the execution of a check."""

    pass
