import pandas as pd


def read_csv(file_path):
    """Чтение CSV файла с разделителем ';'."""
    return pd.read_csv(file_path, sep=';')


def write_csv(dataframe, file_path):
    """Запись DataFrame в CSV файл с разделителем ';'."""
    dataframe.to_csv(file_path, sep=';', index=False)


def handle_error(error_message):
    """Обработка ошибок."""
    print(f"Ошибка: {error_message}")
