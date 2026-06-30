# write_meta_data_to_excel.py
import pandas as pd


def write_meta_data_to_excel(meta, writer):
    pd.Series(meta.column_names_to_labels, name='Label').rename_axis('Variable').reset_index().to_excel(
        writer, sheet_name='meta.column_names_to_labels', index=False
    )

    rows = [
        {'Variable': var, 'Code': code, 'Label': label}
        for var, mapping in meta.variable_value_labels.items()
        for code, label in sorted(mapping.items())
    ]
    value_labels_df = pd.DataFrame(rows, columns=['Variable', 'Code', 'Label'])
    value_labels_df.to_excel(writer, sheet_name='meta.variable_value_labels', index=False)

