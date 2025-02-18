import os
from src.data_processing import load_data, process_sellout, process_stock
from src.report_generator import generate_sales_report, generate_stock_report


def main():
    # Загрузка данных
    sellout_file = 'data/sellout/sellout_file.csv'  # Укажите путь к файлу
    stock_file = 'data/stock/stock_file.csv'  # Укажите путь к файлу

    sellout_df = load_data(sellout_file)
    stock_df = load_data(stock_file)

    # Обработка данных
    reg_city_db = load_data('data/reg_city_db.xlsx')  # Загрузка базы данных городов
    processed_sellout = process_sellout(sellout_df, reg_city_db)
    processed_stock = process_stock(stock_df)

    # Генерация отчетов
    partner_id = '12345'  # Укажите идентификатор партнера
    generate_sales_report(processed_sellout, partner_id)
    generate_stock_report(processed_stock, partner_id)


if __name__ == "__main__":
    main()
