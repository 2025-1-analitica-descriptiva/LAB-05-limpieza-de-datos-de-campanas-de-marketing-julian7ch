import pandas as pd

def limpiar_datos_cliente(df_completo: pd.DataFrame) -> pd.DataFrame:
    # Seleccionar columnas relevantes
    cliente_df = df_completo[['client_id', 'age', 'job', 'marital', 'education', 'credit_default', 'mortgage']].copy()

    # Limpiar columna job
    cliente_df['job'] = cliente_df['job'].str.replace('.', '', regex=False).str.replace('-', '_')

    # Limpiar columna education
    cliente_df['education'] = cliente_df['education'].str.replace('.', '_', regex=False)
    cliente_df['education'] = cliente_df['education'].replace('unknown', pd.NA)

    # Convertir credit_default y mortgage a 0/1
    cliente_df['credit_default'] = cliente_df['credit_default'].apply(lambda x: 1 if x.strip().lower() == 'yes' else 0)
    cliente_df['mortgage'] = cliente_df['mortgage'].apply(lambda x: 1 if x.strip().lower() == 'yes' else 0)

    return cliente_df
