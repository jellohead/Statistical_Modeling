from __future__ import annotations

from pathlib import Path
import pyreadstat


def read_data(file_path: str | Path):
    file_path = str(Path(file_path).expanduser().resolve())
    df, meta = pyreadstat.read_sav(file_path)
    df_labeled = pyreadstat.set_value_labels(df, meta)
    return df, meta, df_labeled
