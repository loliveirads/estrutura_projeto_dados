import os
import glob
import pandas as pd
from typing import List

def extract_from_excel(path: str) -> List[pd.DataFrame]:
    """
    Lê todos os arquivos Excel (.xlsx) em um diretório e retorna uma lista de DataFrames.

    Esta função utiliza o módulo `glob` para encontrar todos os arquivos com extensão `.xlsx`
    no diretório especificado. Em seguida, cada arquivo é lido usando o `pandas.read_excel` 
    e armazenado em uma lista de DataFrames.

    Args:
        path (str): O caminho do diretório contendo os arquivos Excel.

    Returns:
        List[pd.DataFrame]: Uma lista de DataFrames, onde cada DataFrame representa 
        o conteúdo de um arquivo Excel encontrado no diretório.

    Example:
        >>> from app.pipeline.extract import extract_from_excel
        >>> data_frames = extract_from_excel("data/input")
        >>> len(data_frames)
        3  # Se houver três arquivos Excel no diretório

    Raises:
        FileNotFoundError: Se o diretório especificado não existir.
        ValueError: Se não houver arquivos Excel no diretório.

    """
    all_files = glob.glob(os.path.join(path, "*.xlsx"))

    data_frame_list = []
    for file in all_files:
        data_frame_list.append(pd.read_excel(file))

    return data_frame_list


if __name__ == "__main__":
    input_path = "data/input"
    data_frame_list = extract_from_excel(input_path)
    print(data_frame_list)
