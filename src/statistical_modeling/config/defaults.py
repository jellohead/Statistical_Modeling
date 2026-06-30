from __future__ import annotations
from dataclasses import dataclass
from pathlib import Path
from statistical_modeling.config.paths import PATHS

EXCEL_FILE = PATHS.output_dir / "Statistical_Modeling_output.xlsx"
AUDIT_LOG_FILE = PATHS.output_dir / "Statistical_Modeling_audit.jsonl"


@dataclass(frozen=True)
class QuarterConfig:
    """Configuration for one data period's files.

    label : str
        Period identifier (e.g. "Q4_2025") stamped into the '_quarter' column.
    dir : Path
        Path to the directory holding this period's data files.
    """
    label: str
    dir: Path


QUARTERS: list[QuarterConfig] = [
    # QuarterConfig("Q1_2024", PATHS.data_store_curated_dir / "Q1_2024"),
]

NUMBER_OF_QUARTERS_REPORTING = 4
quarters_used_this_report = QUARTERS[-NUMBER_OF_QUARTERS_REPORTING:]
QUARTERS_LIST: list[str] = [q.label for q in quarters_used_this_report]
CURRENT_QUARTER = QUARTERS_LIST[-1] if QUARTERS_LIST else ""
