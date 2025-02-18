def generate_sales_report(report, partner_id):
    report['Date_sale'] = report['date'].str.replace('-', '')
    report['Article'] = report['vendor_article']
    report['Sale_qty'] = report['sellout']
    report['Total_sum'] = report['sales_amount_with_VAT_in_the_purchase_price']

    final_report = report[['Date_sale', 'Region_code', 'City_code', 'Article', 'Sale_qty', 'Total_sum']]
    final_report.to_csv(f'reports/sales/{partner_id}_sales.csv', sep=';', index=False)


def generate_stock_report(stock_df, partner_id):
    stock_df['Period'] = stock_df['date'].str.replace('-', '')
    stock_df['Article'] = stock_df['vendor_article']
    stock_df['Stock_qty'] = stock_df['available']

    final_report = stock_df[['Period', 'Article', 'Stock_qty']]
    final_report.to_csv(f'reports/stock/{partner_id}_stock.csv', sep=';', index=False)
