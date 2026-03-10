from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any
import pandas as pd


@dataclass(slots=True)
class Metric:
    """Single rendered metric."""

    name: str
    value: str
    raw_value: float | int | None = None
    unit: str | None = None

    def to_dict(self) -> dict[str, Any]:
        """Convert metric to a serializable dictionary."""
        return {
            "name": self.name,
            "value": self.value,
            "raw_value": self.raw_value,
            "unit": self.unit,
        }


@dataclass(slots=True)
class Section:
    """Logical report section."""

    title: str
    metrics: list[Metric] = field(default_factory=list)

    def to_dict(self) -> dict[str, Any]:
        """Convert section to a serializable dictionary."""
        return {
            "title": self.title,
            "metrics": [metric.to_dict() for metric in self.metrics],
        }


@dataclass(slots=True)
class PortfolioReport:
    """Structured portfolio report with ASCII rendering helpers."""

    title: str
    strategy_name: str
    sample_size: int
    date: str
    annualization: int
    sections: list[Section]
    width: int = 66

    def __repr__(self) -> str:
        """Return the ASCII representation of the report."""
        return self.render()

    def __str__(self) -> str:
        """Return the ASCII representation of the report."""
        return self.render()

    def render(self) -> str:
        """Render the report as an ASCII table."""
        lines: list[str] = [
            "=" * self.width,
            self.title.center(self.width),
            "=" * self.width,
            (
                f"Strategy: {self.strategy_name} | "
                f"Sample size: {self.sample_size} | "
                f"Date: {self.date}"
            ),
            f"Annualization: {self.annualization} periods per year",
            "",
        ]

        for section in self.sections:
            lines.append(section.title)
            lines.append("-" * self.width)

            for metric in section.metrics:
                lines.append(
                    self._format_metric_row(
                        label=metric.name,
                        value=metric.value,
                    )
                )

            lines.append("")

        return "\n".join(lines).rstrip()

    def to_dict(self) -> dict[str, Any]:
        """Convert the full report to a serializable dictionary."""
        return {
            "title": self.title,
            "strategy_name": self.strategy_name,
            "sample_size": self.sample_size,
            "date": self.date,
            "annualization": self.annualization,
            "width": self.width,
            "sections": [section.to_dict() for section in self.sections],
        }

    def to_dataframe(self) -> pd.DataFrame:
        """Convert the report to a flat pandas DataFrame."""
        rows: list[dict[str, Any]] = []

        for section in self.sections:
            for metric in section.metrics:
                rows.append(
                    {
                        "section": section.title,
                        "metric": metric.name,
                        "display_value": metric.value,
                        "raw_value": metric.raw_value,
                        "unit": metric.unit,
                    }
                )

        return pd.DataFrame(rows)

    def _format_metric_row(
        self,
        label: str,
        value: str
    ) -> str:
        """Format a single metric row."""
        spaces = max(self.width - len(label) - len(value), 2)
        return f"{label}{' ' * spaces}{value}"
