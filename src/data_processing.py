import pandas as pd
from fuzzywuzzy import process


def load_data(file_path):
    if file_path.endswith('.csv'):
        return pd.read_csv(file_path, sep=';', low_memory=False)
    elif file_path.endswith('.xlsx'):
        return pd.read_excel(file_path)
    else:
        raise ValueError("Unsupported file format")


def process_sellout(sellout_df, reg_city_db):
    # Извлечение необходимых столбцов
    sellout_df = sellout_df[['date', 'member_name', 'vendor_article', 'rf_subject', 'city', 'sellout',
                             'sales_amount_with_VAT_in_the_purchase_price']]

    # Логика сопоставления городов и регионов
    sellout_df['Region_code'] = sellout_df['city'].apply(lambda x: match_city(x, reg_city_db))
    sellout_df['City_code'] = sellout_df['city'].apply(lambda x: match_city_code(x, reg_city_db))

    # Группировка данных
    report = sellout_df.groupby(['member_name', 'Region_code', 'City_code', 'vendor_article']).sum([
        'sellout', 'sales_amount_with_VAT_in_the_purchase_price'])

    return report
    # return sellout_df


def match_city(city, reg_city_db):
    match = process.extractOne(city, reg_city_db['city'], score_cutoff=70)
    return reg_city_db.loc[reg_city_db['city'] == match[0], 'region_code'].values[0] if match else 99


def match_city_code(city, reg_city_db):
    match = process.extractOne(city, reg_city_db['city'], score_cutoff=70)
    return reg_city_db.loc[reg_city_db['city'] == match[0], 'city_code'].values[0] if match else 0


def process_stock(stock_df):
    # Извлечение необходимых столбцов
    stock_df = stock_df[['date', 'raec_member_name', 'vendor_article', 'available']]

    # Группировка данных
    report = stock_df.groupby(['raec_member_name', 'vendor_article']).sum(['available']).reset_index()
    report.rename(columns={'available': 'Stock_qty'}, inplace=True)
    return report
