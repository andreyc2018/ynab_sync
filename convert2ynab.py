#!/usr/bin/env python

"""
Convert a bank or YNAB staement to YNAB view sorted by YNAB rules.
"""

import argparse
import pandas as pd


def convert_money(input):
    negative = input[0] == '-'
    return pd.to_numeric(input[1:]) if not negative else pd.to_numeric(input[2:])


def convert_balance(input):
    # type: (str) -> str
    """Withouy this function, an empty CURRENT BALANCE is converted to float nan
    """
    return input


def convert_date(input):
    return pd.to_datetime(input)


def calculate_running_balance(df, initial_balance):
    # type: (pd.DataFrame, float) -> None
    df.at[len(df)-1, 'Balance'] = initial_balance
    for i in range(len(df)-2, -1, -1):
        df.at[i, 'Balance']  = df.at[i+1, 'Balance'] - df.at[i, 'Outflow'] + df.at[i, 'Inflow']
    df.index.name = 'Index'


def convert_ynab(filename, initial_balance):
    # type: (str, float) -> pd.DataFrame
    """Convert transactions csv file
    """
    df = pd.read_csv(filename, sep=',', header=0,
                     usecols=['Date', 'Outflow', 'Inflow'],
                     converters={'Date': convert_date,
                                 'Outflow': convert_money,
                                 'Inflow': convert_money})
    df['Balance'] = 0.0
    df.at[len(df)-1, 'Balance'] = initial_balance
    calculate_running_balance(df, initial_balance)
    return df


def convert_bank(filename, initial_balance):
    # type: (str, float) -> pd.DataFrame
    """Convert transactions csv file
    """
    bank_df = pd.read_csv(filename, sep=',', header=0,
                          converters={'DATE': convert_date,
                                      'AMOUNT': convert_money,
                                      'CURRENT BALANCE': convert_balance})
    data = []
    for _, row in bank_df.iterrows():
        if len(row['CURRENT BALANCE']) < 1 or row['AMOUNT'] == 0.0:
            continue
        line = [row['DATE']]
        if row['TRANSACTION TYPE'] == 'DEBIT':
            line.append(0.0)
            line.append(row['AMOUNT'])
        else:
            line.append(row['AMOUNT'])
            line.append(0.0)
        line.append(0.0)
        data.append(line)
    df = pd.DataFrame(data, columns=['Date', 'Outflow', 'Inflow', 'Balance'])
    df.sort_values(['Date', 'Outflow', 'Inflow'], ascending=[False, False, True], inplace=True)
    df.reset_index(drop=True, inplace=True)
    calculate_running_balance(df, initial_balance)
    return df


def print_csv(df):
    # type: (pd.DataFrame) -> None
    print(df.to_csv(float_format=lambda x: f"{x:.2f}"))


def print_text(df):
    # type: (pd.DataFrame) -> None
    print(df.to_string(float_format=lambda x: f"{x:.2f}"))


def print_excel(df):
    # type: (pd.DataFrame) -> None
    print(df.to_excel('transactions.xlsx'))


PARSERS = {'bank': convert_bank,
           'ynab': convert_ynab}

OUTPUTS = {'csv': print_csv,
           'text': print_text,
           'excel': print_excel}

if __name__ == '__main__':
    parser = argparse.ArgumentParser(prog = 'convert2ynab',
                                     description = 'Convert bank or ynab csv to ynab view. By default it prints CSV to stdout.')
    parser.add_argument('filename', help='CSV filename')
    parser.add_argument('-t', '--type', default='bank',
                        help='parser type. Available parsers: bank, ynab')
    parser.add_argument('-b', '--balance', type=float, default=0.0,
                        help='initial balance for the csv time period. Zero if not specified.')
    parser.add_argument('-o', '--output', default='csv',
                        help='output type. Available: csv (default), text, excel')

    args = parser.parse_args()

    df = PARSERS[args.type](args.filename, args.balance)

    OUTPUTS[args.output](df)
