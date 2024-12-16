import pandas as pd
from typing import List

def concat_data_frames(data_frame_list: List[pd.DataFrame]) -> pd.DataFrame:
    """
    Função para transformar uma lista de DataFrames em um único DataFrame.

    Args:
        data_frame_list (List[pd.DataFrame]): Lista de DataFrames a serem concatenados.

    Returns:
        pd.DataFrame: DataFrame resultante da concatenação.
    """
    if not data_frame_list:  # Verificação para lista vazia
        return pd.DataFrame()
    
    result = pd.concat(data_frame_list, ignore_index=True)
        # Força as colunas a int64, ignorando NaN para evitar erros
    for column in result.columns:
        if pd.api.types.is_numeric_dtype(result[column]):
            result[column] = result[column].fillna(0).astype("int64")
    return result
