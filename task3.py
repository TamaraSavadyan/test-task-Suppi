def task3(df):
    df['income'] = df['price'] * df['quantity']
    df['expenses'] = df['highway_cost'] * df['quantity']
    df['profit'] = df['income'] + df['expenses']

    order_profit_df = df.groupby('order_id')['profit'].sum().reset_index()

    order_profit_df.rename(columns={'profit': 'order_profit'}, inplace=True)

    average_order_profit = order_profit_df['order_profit'].mean()

    return order_profit_df, f'\nAverage order profit: {average_order_profit}'
