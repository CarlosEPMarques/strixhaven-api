from __future__ import annotations

from dataclasses import dataclass
from datetime import UTC, datetime


@dataclass(frozen=True)
class DateTime:
    value: datetime

    @staticmethod
    def now() -> DateTime:
        return DateTime(datetime.now(tz=UTC))

    def __str__(self) -> str:
        return self.value.strftime('%Y-%m-%d %H:%M:%S+00:00')
