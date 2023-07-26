import pandas as pd

def task4_task5_task6(df):
    df['income'] = df['price'] * df['quantity']
    df['expenses'] = df['highway_cost'] * df['quantity']
    df['profit'] = df['income'] + df['expenses']

    warehouse_product_df = df.groupby(['warehouse_name', 'product']).agg(
        quantity=('quantity', 'sum'),
        profit=('profit', 'sum')
    ).reset_index()

    warehouse_profit_df = warehouse_product_df.groupby(
        'warehouse_name')['profit'].sum().reset_index()

    result_df = pd.merge(warehouse_product_df, warehouse_profit_df,
                         on='warehouse_name', suffixes=('', '_total'))

    result_df['percent_profit_product_of_warehouse'] = (
        result_df['profit'] / result_df['profit_total']) * 100
    result_df.drop('profit_total', axis=1, inplace=True)

    result_df.sort_values(
        by='percent_profit_product_of_warehouse', ascending=False, inplace=True)

    result_df['accumulated_percent_profit_product_of_warehouse'] = result_df['percent_profit_product_of_warehouse'].cumsum()

    result_df['category'] = pd.cut(
        result_df['accumulated_percent_profit_product_of_warehouse'],
        bins=[-float('inf'), 70, 90, float('inf')],
        labels=['A', 'B', 'C'],
        right=False
    )

    return result_df
