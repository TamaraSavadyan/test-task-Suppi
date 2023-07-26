def task1(df):
    df['total_delivery_cost'] = df['highway_cost'] * df['quantity']

    result_df = df.groupby('warehouse_name')[
        'total_delivery_cost'].sum().reset_index()

    return result_df
