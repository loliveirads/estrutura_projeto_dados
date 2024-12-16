import pandas as pd
import os

def load_excel(data_frame: pd.DataFrame, output_path: str, file_name: str) -> str:
    """
    Recebe um DataFrame e salva como Excel.

    Args:
        data_frame (pd.DataFrame): DataFrame a ser salvo como Excel.
        output_path (str): Caminho onde o arquivo será salvo.
        file_name (str): Nome do arquivo a ser salvo.

    Returns:
        str: Mensagem de sucesso.
    """
    # Garante que o diretório exista
    if not os.path.exists(output_path):
        os.makedirs(output_path)

    # Caminho do arquivo usando os.path.join
    file_path = os.path.join(output_path, f"{file_name}.xlsx")
    
    # Salva o DataFrame como Excel
    data_frame.to_excel(file_path, index=False)
    
    return "Arquivo salvo com sucesso"
