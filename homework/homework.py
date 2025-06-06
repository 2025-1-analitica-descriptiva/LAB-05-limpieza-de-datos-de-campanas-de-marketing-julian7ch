"""
Escriba el codigo que ejecute la accion solicitada.
"""

# pylint: disable=import-outside-toplevel
from homework.cargas_data_desde_ZIP import carga_data_desde_ZIP
from homework.limpiar_datos_cliente import limpiar_datos_cliente
from homework.limpiar_datos_campana import limpiar_datos_campana
from homework.limpiar_datos_economicos import limpiar_datos_economicos


def clean_campaign_data():
    input_dir = 'files/input/'
    output_dir = 'files/output/'

    full_df = carga_data_desde_ZIP(input_dir)

    client_df = limpiar_datos_cliente(full_df)   
    campaign_df =  limpiar_datos_campana(full_df)
    economics_df = limpiar_datos_economicos(full_df)    

    client_df.to_csv(f'{output_dir}client.csv', index=False)
    campaign_df.to_csv(f'{output_dir}campaign.csv', index=False)
    economics_df.to_csv(f'{output_dir}economics.csv', index=False)


    """
    En esta tarea se le pide que limpie los datos de una campaña de
    marketing realizada por un banco, la cual tiene como fin la
    recolección de datos de clientes para ofrecerls un préstamo.

    La información recolectada se encuentra en la carpeta
    files/input/ en varios archivos csv.zip comprimidos para ahorrar
    espacio en disco.

    Usted debe procesar directamente los archivos comprimidos (sin
    descomprimirlos). Se desea partir la data en tres archivos csv
    (sin comprimir): client.csv, campaign.csv y economics.csv.
    Cada archivo debe tener las columnas indicadas.

    Los tres archivos generados se almacenarán en la carpeta files/output/.

    client.csv:
    - client_id
    - age
    - job: se debe cambiar el "." por "" y el "-" por "_"
    - marital
    - education: se debe cambiar "." por "_" y "unknown" por pd.NA
    - credit_default: convertir a "yes" a 1 y cualquier otro valor a 0
    - mortage: convertir a "yes" a 1 y cualquier otro valor a 0

    campaign.csv:
    - client_id
    - number_contacts
    - contact_duration
    - previous_campaing_contacts
    - previous_outcome: cmabiar "success" por 1, y cualquier otro valor a 0
    - campaign_outcome: cambiar "yes" por 1 y cualquier otro valor a 0
    - last_contact_day: crear un valor con el formato "YYYY-MM-DD",
        combinando los campos "day" y "month" con el año 2022.

    economics.csv:
    - client_id
    - const_price_idx
    - eurobor_three_months



    """

    return


if __name__ == "__main__":
    clean_campaign_data()
