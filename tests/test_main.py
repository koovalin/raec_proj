import unittest
import os
import pandas as pd
from src.data_processing import load_data, process_sellout, process_stock, match_city, match_city_code
from src.report_generator import generate_sales_report, generate_stock_report
from src.utils import get_stock_file_name, get_sellout_file_name


class TestProject(unittest.TestCase):

    def setUp(self):
        self.sellout_file = get_sellout_file_name()
        self.stock_file = get_stock_file_name()
        # Загрузка тестовых данных
        self.sellout_df = load_data('../data/sellout/' + self.sellout_file)
        self.stock_df = load_data('../data/stock/' + self.stock_file)
        self.reg_city_db = load_data('../data/reg_city_db.xlsx')
        self.city = 'Москва'

    def test_load_data(self):
        df = load_data('../data/sellout/' + self.sellout_file)
        self.assertFalse(df.empty)

    def test_process_sellout(self):
        processed = process_sellout(self.sellout_df, self.reg_city_db)
        self.assertGreater(len(processed), 0)

    def test_process_stock(self):
        processed = process_stock(self.stock_df)
        self.assertGreater(len(processed), 0)

    def test_generate_sales_report(self):
        report = process_sellout(self.sellout_df, self.reg_city_db)
        partner_id = '12345'
        generate_sales_report(report, partner_id)
        self.assertTrue(os.path.exists(f'reports/sales/{partner_id}_sales.csv'))

    # def test_generate_stock_report(self):
    #     processed_stock = process_stock(self.stock_df)
    #     partner_id = '12345'
    #     generate_stock_report(processed_stock, partner_id)
    #     self.assertTrue(os.path.exists(f'reports/stock/{partner_id}_stock.csv'))

    def test_match_city(self):
        result = match_city(self.city, self.reg_city_db)
        print(result)
        self.assertIsNotNone(result)

    def test_match_city_code(self):
        result = match_city_code(self.city, self.reg_city_db)
        print(result)
        self.assertIsNotNone(result)


if __name__ == '__main__':
    unittest.main()
