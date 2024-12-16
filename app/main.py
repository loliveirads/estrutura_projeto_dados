from pipeline.extract import extract_from_excel
from pipeline.transform import concat_data_frames
from pipeline.load import load_excel
import os

if __name__ == "__main__":
    try:
        input_path = "data/input"
        output_path = "data/output"
        file_name = "output"

        # Verifica diretório de entrada
        if not os.path.exists(input_path):
            raise FileNotFoundError(f"Diretório de entrada '{input_path}' não encontrado.")

        # Extrai e transforma os dados
        data_frame_list = extract_from_excel(input_path)
        print(f"Arquivos carregados: {len(data_frame_list)}")
        print(type(data_frame_list))  # Lista de DataFrames

        data_frame = concat_data_frames(data_frame_list)
        print(f"DataFrame final com {len(data_frame)} linhas e {len(data_frame.columns)} colunas.")
        print(type(data_frame))  # DataFrame único

        # Salva o resultado
        load_excel(data_frame, output_path, file_name)
        print(f"Arquivo salvo com sucesso em '{output_path}/{file_name}.xlsx'.")

    except Exception as e:
        print(f"Ocorreu um erro: {e}")
