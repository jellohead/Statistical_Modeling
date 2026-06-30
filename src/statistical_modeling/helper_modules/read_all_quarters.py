import pandas as pd
from pathlib import Path
from statistical_modeling.config.defaults import (
    QUARTERS,
    CURRENT_QUARTER,
    QuarterConfig,
)
from statistical_modeling.config.paths import PATHS


def _find_parquet(directory: Path, pattern: str) -> Path:
    """Return the single parquet file matching *pattern* in *directory*.

    Raises FileNotFoundError if the match count is not exactly one.
    """
    matches = list(directory.glob(pattern))
    if len(matches) != 1:
        raise FileNotFoundError(
            f"Expected exactly 1 file matching '{pattern}' in {directory}, "
            f"found {len(matches)}: {[m.name for m in matches]}"
        )
    return matches[0]


def _load_quarter(qc: QuarterConfig):
    df = pd.read_parquet(_find_parquet(qc.dir, "responses.parquet"))
    df_labeled = pd.read_parquet(_find_parquet(qc.dir, "responses_labeled.parquet"))
    df["_quarter"] = qc.label
    df_labeled["_quarter"] = qc.label
    return df, df_labeled


def read_all_quarters():
    """Load and combine all quarters defined in QUARTERS.

    Returns (df, df_labeled) where every row is tagged with a '_quarter' column.
    """
    dfs, dfs_labeled = [], []
    for qc in QUARTERS:
        df_q, df_labeled_q = _load_quarter(qc)
        dfs.append(df_q)
        dfs_labeled.append(df_labeled_q)

    df = pd.concat(dfs, ignore_index=True)
    df_labeled = pd.concat(dfs_labeled, ignore_index=True)
    return df, df_labeled
