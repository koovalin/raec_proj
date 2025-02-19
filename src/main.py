import os
from src.data_processing import load_data, process_sellout, process_stock
from src.report_generator import generate_sales_report, generate_stock_report
from src.utils import get_stock_file_name, get_sellout_file_name


def main():
    sellout_file = get_sellout_file_name()
    stock_file = get_stock_file_name()

    sellout_df = load_data('../data/sellout/' + sellout_file)
    stock_df = load_data('../data/stock/' + stock_file)
    reg_city_db = load_data('../data/reg_city_db.xlsx')  # Загрузка базы данных городов

    # Обработка данных
    processed_sellout = process_sellout(sellout_df, reg_city_db)
    # processed_stock = process_stock(stock_df)

    print(processed_sellout)
    # print(processed_stock)

    # # Генерация отчетов
    # partner_id = '12345'  # Укажите идентификатор партнера
    # generate_sales_report(processed_sellout, partner_id)
    # generate_stock_report(processed_stock, partner_id)


if __name__ == "__main__":
    main()
