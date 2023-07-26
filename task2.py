def task2(df):
    df['income'] = df['price'] * df['quantity']
    df['expenses'] = df['highway_cost'] * df['quantity']
    df['profit'] = df['income'] - df['expenses']

    result_df = df.groupby('product').agg(
        quantity=('quantity', 'sum'),
        income=('income', 'sum'),
        expenses=('expenses', 'sum'),
        profit=('profit', 'sum')
    ).reset_index()

    return result_df
