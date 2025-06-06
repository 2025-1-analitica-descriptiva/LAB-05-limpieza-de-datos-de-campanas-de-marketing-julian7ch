import zipfile
import pandas as pd

def leer_CSV_desde_ZIP(zip_path):
    with zipfile.ZipFile(zip_path, 'r') as z:
        csv_name = z.namelist()[0]
        with z.open(csv_name) as f:
            df = pd.read_csv(f)
    return df