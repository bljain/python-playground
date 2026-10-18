from dataclasses import dataclass
from datetime import UTC, datetime
from enum import Enum


class CheckStatus(str, Enum): # noqa: UP042
    PASS = "pass"
    FAIL = "fail"
    ERROR = "error"


@dataclass(frozen=True)
class CheckResult:
    check_id: str
    check_type: str
    status: CheckStatus
    failed_count: int | None
    total_count: int | None
    message: str | None
    column: str | None
    run_id: str
    executed_at: datetime = datetime.now(UTC)

    def __post_init__(self):
        if self.failed_count is not None and self.total_count is None:
            raise ValueError(
                "total_count must be provided \
                    if failed_count is provided"
            )
        if self.failed_count is None and self.total_count is not None:
            raise ValueError(
                "failed_count must be provided if \
                    total_count is provided"
            )
        if self.failed_count is not None and self.total_count is not None:
            if self.failed_count > self.total_count:
                raise ValueError("failed_count cannot be greater than total_count")
        if self.status == CheckStatus.FAIL and (
            self.failed_count is None or self.total_count is None
        ):
            raise ValueError(
                "failed_count and total_count must be provided \
                    if status is FAIL"
            )
        if self.status == CheckStatus.PASS and self.failed_count != 0:
            raise ValueError("failed_count must be 0 if status is PASS")
        if self.status == CheckStatus.ERROR:
            return
        if self.check_type.strip() == "":
            raise ValueError("check_type must be a non-empty string")

    @property
    def percentage_failed(self) -> float | None:
        if self.failed_count is None or self.total_count is None:
            raise ValueError(
                "failed_count and total_count must be provided \
                    to calculate percentage_failed"
            )
        if self.total_count is None:
            return None

        return self.failed_count / self.total_count
