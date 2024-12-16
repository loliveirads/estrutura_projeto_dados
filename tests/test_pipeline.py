import pandas as pd
import pytest
from app.pipeline.transform import concat_data_frames

def test_concat_data_frames():
    """
    Testa a função concat_data_frames para combinar uma lista de DataFrames.
    """
    # Dados simulados
    df1 = pd.DataFrame({"col1": [1, 2], "col2": [3, 4]})
    df2 = pd.DataFrame({"col1": [5, 6], "col2": [7, 8]})
    df3 = pd.DataFrame({"col1": [], "col2": []})  # DataFrame vazio

    # Teste com lista de DataFrames
    result = concat_data_frames([df1, df2])
    expected = pd.DataFrame({"col1": [1, 2, 5, 6], "col2": [3, 4, 7, 8]})

    pd.testing.assert_frame_equal(result, expected)

    # Teste com DataFrame vazio na lista
    result_with_empty = concat_data_frames([df1, df3])
    expected_with_empty = pd.DataFrame({"col1": [1, 2], "col2": [3, 4]})
    pd.testing.assert_frame_equal(result_with_empty, expected_with_empty)

    # Teste com lista vazia
    result_empty_list = concat_data_frames([])
    expected_empty_list = pd.DataFrame()
    pd.testing.assert_frame_equal(result_empty_list, expected_empty_list)

