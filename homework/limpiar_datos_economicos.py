import pandas as pd 
def limpiar_datos_economicos(df_completo: pd.DataFrame) -> pd.DataFrame:
    economics_df = df_completo[['client_id', 'cons_price_idx', 'euribor_three_months']].copy()
    return economics_df
