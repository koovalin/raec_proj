import unittest
import os
import pandas as pd
from src.data_processing import load_data, process_sellout, process_stock
from src.report_generator import generate_sales_report, generate_stock_report


class TestProject(unittest.TestCase):

    def setUp(self):
        # Загрузка тестовых данных
        self.sellout_df = load_data('data/sellout/sellout_file.csv')
        self.stock_df = load_data('data/stock/stock_file.csv')
        self.reg_city_db = load_data('data/reg_city_db.xlsx')

    def test_load_data(self):
        df = load_data('data/sellout/sellout_file.csv')
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

    def test_generate_stock_report(self):
        processed_stock = process_stock(self.stock_df)
        partner_id = '12345'
        generate_stock_report(processed_stock, partner_id)
        self.assertTrue(os.path.exists(f'reports/stock/{partner_id}_stock.csv'))


if __name__ == '__main__':
    unittest.main()
