import pandas as pd
from json import load
from task1 import task1
from task2 import task2
from task3 import task3
from task4_task5_task6 import task4_task5_task6


def write_dataframe_to_file(df, output_file_path):
    df.to_csv(output_file_path, index=False, sep=',', encoding='utf-8')


def get_result_and_write_to_file(df, function):
    task_result = function(df)
    output_file = f'{function.__name__}_output.csv'
    write_dataframe_to_file(task_result, output_file)
    print(task_result)


def main():
    file = 'trial_task.json'
    with open(file, 'rb') as f:
        data = load(f)

    df = pd.json_normalize(data, record_path='products', meta=[
                           'order_id', 'warehouse_name', 'highway_cost'])

    get_result_and_write_to_file(df, task1)
    get_result_and_write_to_file(df, task2)
    get_result_and_write_to_file(df, task4_task5_task6)

    task3(df)


if __name__ == '__main__':
    main()
