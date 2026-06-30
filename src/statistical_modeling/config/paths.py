# src/statistical_modeling/config/paths.py
"""Centralized path management for Statistical_Modeling.

Design goals:
- Never hard-code relative paths like ../../..
- Work whether invoked from CLI, IDE, or notebooks
- Keep non-code directories (data_store, resources, output, logs) outside src/
"""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import Optional


def _find_project_root(start: Optional[Path] = None) -> Path:
    """Walk upward from `start` until a directory containing pyproject.toml is found."""
    start_path = (start or Path(__file__)).resolve()
    for candidate in [start_path, *start_path.parents]:
        if (candidate / "pyproject.toml").exists():
            return candidate
    raise RuntimeError(
        "Could not locate project root (pyproject.toml not found in parent chain). "
        f"Start path was: {start_path}"
    )


@dataclass(frozen=True)
class ProjectPaths:
    """Canonical project paths. Import PATHS and use these properties."""
    root: Path

    @property
    def src_dir(self) -> Path:
        return self.root / "src"

    @property
    def package_dir(self) -> Path:
        return self.src_dir / "statistical_modeling"

    @property
    def data_store_dir(self) -> Path:
        return self.root / "data_store"

    @property
    def data_store_raw_dir(self) -> Path:
        return self.data_store_dir / "raw"

    @property
    def data_store_curated_dir(self) -> Path:
        return self.data_store_dir / "curated"

    @property
    def data_store_runs_dir(self) -> Path:
        return self.data_store_dir / "runs"

    @property
    def resources_dir(self) -> Path:
        return self.root / "resources"

    @property
    def templates_dir(self) -> Path:
        return self.resources_dir / "templates"

    @property
    def images_dir(self) -> Path:
        return self.resources_dir / "images"

    @property
    def output_dir(self) -> Path:
        return self.root / "output"

    @property
    def logs_dir(self) -> Path:
        return self.root / "logs"

    @property
    def notebooks_dir(self) -> Path:
        return self.root / "notebooks"

    def raw_period_dir(self, period: str) -> Path:
        return self.data_store_raw_dir / period

    def curated_period_dir(self, period: str) -> Path:
        return self.data_store_curated_dir / period

    def curated_raw_parquet_path(self, period: str) -> Path:
        return self.curated_period_dir(period) / "responses.parquet"

    def curated_labeled_parquet_path(self, period: str) -> Path:
        return self.curated_period_dir(period) / "responses_labeled.parquet"

    def template_path(self, filename: str) -> Path:
        return self.templates_dir / filename

    def output_path(self, filename: str) -> Path:
        return self.output_dir / filename

    def ensure_runtime_dirs(self) -> None:
        """Create directories that must exist at runtime (safe to call repeatedly)."""
        for d in [
            self.data_store_dir,
            self.data_store_raw_dir,
            self.data_store_curated_dir,
            self.data_store_runs_dir,
            self.resources_dir,
            self.templates_dir,
            self.images_dir,
            self.output_dir,
            self.logs_dir,
            self.notebooks_dir,
        ]:
            d.mkdir(parents=True, exist_ok=True)


PATHS = ProjectPaths(root=_find_project_root())
