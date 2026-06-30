# excel_output.py
# Helpers for writing DataFrames to a shared Excel workbook
import pandas as pd


def create_excel_writer(file_path: str) -> pd.ExcelWriter:
    """Create and return an ExcelWriter. Call save_excel_writer() when done."""
    return pd.ExcelWriter(file_path, engine="openpyxl")


def write_sheet(writer: pd.ExcelWriter, df: pd.DataFrame, sheet_name: str, startrow: int = 0, index=True) -> int:
    """Write a DataFrame to a named sheet at the given row offset.

    Returns the next available row (startrow + len(df) + header + 1 blank row),
    so you can pass it as startrow for the next call to the same sheet.
    """
    sheet_name = sheet_name.replace(":", "")[:31]  # Excel sheet names cannot contain ":" and are limited to 31 chars
    df.to_excel(writer, sheet_name=sheet_name, startrow=startrow, index=index)
    return startrow + len(df) + 2  # +1 for header row, +1 blank gap


def save_excel_writer(writer: pd.ExcelWriter) -> None:
    """Save and close the workbook. No-op if no sheets were written."""
    if writer.sheets:
        writer.close()