# audit_log.py
# Helper for writing per-slide audit records to a JSONL file.
import json
import numpy as np
from datetime import datetime
from pathlib import Path


class _NumpyEncoder(json.JSONEncoder):
    """Serialize numpy scalar and array types to native Python types."""
    def default(self, obj):
        if isinstance(obj, np.integer):
            return int(obj)
        if isinstance(obj, np.floating):
            return float(obj)
        if isinstance(obj, np.ndarray):
            return obj.tolist()
        return super().default(obj)


class AuditLog:
    """Appends one JSON record per slide to a .jsonl audit file.

    The current_quarter is stamped on every record automatically so slide
    updaters do not need to import it themselves.
    """

    def __init__(self, file_path: Path, current_quarter: str):
        self._file = open(file_path, 'w', encoding='utf-8')
        self.current_quarter = current_quarter

    def write(self, record: dict) -> None:
        """Stamp quarter and generated_at, then append the record as a JSON line."""
        record.setdefault('quarter', self.current_quarter)
        record['generated_at'] = datetime.now().isoformat(timespec='seconds')
        self._file.write(json.dumps(record, cls=_NumpyEncoder) + '\n')
        self._file.flush()

    def close(self) -> None:
        self._file.close()


def create_audit_log(file_path: Path, current_quarter: str) -> AuditLog:
    """Open a new audit log at file_path, overwriting any existing file."""
    return AuditLog(file_path, current_quarter)
