import pandas as pd

def limpiar_datos_campana(df_completo: pd.DataFrame) -> pd.DataFrame:
    # Seleccionar columnas relevantes
    campana_df = df_completo[['client_id', 'number_contacts', 'contact_duration', 'previous_campaign_contacts', 'previous_outcome', 'campaign_outcome', 'day', 'month']].copy()

    # Cambiar valores de previous_outcome
    campana_df['previous_outcome'] = campana_df['previous_outcome'].apply(lambda x: 1 if x.strip().lower() == 'success' else 0)

    # Cambiar valores de campaign_outcome
    campana_df['campaign_outcome'] = campana_df['campaign_outcome'].apply(lambda x: 1 if x.strip().lower() == 'yes' else 0)

    # Crear columna last_contact_date con formato YYYY-MM-DD
    def crear_fecha(row):
        mapa_meses = {
            'jan': '01', 'feb': '02', 'mar': '03', 'apr': '04',
            'may': '05', 'jun': '06', 'jul': '07', 'aug': '08',
            'sep': '09', 'oct': '10', 'nov': '11', 'dec': '12'
        }
        mes_num = mapa_meses.get(row['month'].strip().lower(), '01')
        dia = str(row['day']).zfill(2)
        return f'2022-{mes_num}-{dia}'

    campana_df['last_contact_date'] = campana_df.apply(crear_fecha, axis=1)

    # Eliminar columnas day y month
    campana_df = campana_df.drop(columns=['day', 'month'])

    return campana_df
