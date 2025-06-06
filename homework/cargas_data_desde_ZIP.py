import os
import pandas as pd
from homework.leer_CSV_desde_ZIP import leer_CSV_desde_ZIP

def carga_data_desde_ZIP(input_dir):
    zip_files = [f for f in os.listdir(input_dir) if f.endswith('.zip')]
    all_dataframes = []

    for zip_name in zip_files:
        zip_path = os.path.join(input_dir, zip_name)
        df = leer_CSV_desde_ZIP(zip_path)
        all_dataframes.append(df)

    full_df = pd.concat(all_dataframes, ignore_index=True)
    return full_df